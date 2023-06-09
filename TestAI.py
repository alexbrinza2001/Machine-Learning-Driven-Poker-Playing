import random

from PokerEvaluator import PokerEvaluator
from PokerGame import PokerGame
from AveragePokerPlayer import AveragePokerPlayer

class TestAI:

    def __init__(self):
        self.evaluator = PokerEvaluator()
        self.equityPreFlop = dict()
        self.prob = dict()

        file = open("pokerOddsPreflop", "r+")

        for line in file.readlines():
            line = line.split()
            cards = [line[0]] + [line[1]]
            cards = sorted(cards)
            self.equityPreFlop[cards[0] + " " + cards[1]] = float(line[2])

        file = open("input_cfr", "r+")

        for line in file.readlines():
            line = line.split(",")
            field1 = line[0]
            field2 = line[1]
            field3 = line[2]
            field4 = line[3]
            pb = float(line[4])

            if field1 not in self.prob.keys():
                self.prob[field1] = dict()

            if field2 not in self.prob[field1].keys():
                self.prob[field1][field2] = dict()

            if field3 not in self.prob[field1][field2].keys():
                self.prob[field1][field2][field3] = dict()

            self.prob[field1][field2][field3][field4] = pb

    def getHandName(self, hand):

        while hand[-1] in ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]:
            hand = hand[:-2]

        hand = hand.strip()

        return hand

    def playerChooseAction(self, cards, board, stage, lastAction, money, pot):
        probs = dict()

        if stage == "PreFlop":
            stringHand = cards[0] + " " + cards[1]
            eq = self.equityPreFlop[stringHand]
            eqGroup = ""

            if eq <= 40:
                eqGroup = "40 and lower"
            elif 40 < eq <= 45:
                eqGroup = "40-45"
            elif 45 < eq <= 50:
                eqGroup = "45-50"
            elif 50 < eq <= 60:
                eqGroup = "50-60"
            elif eq > 60:
                eqGroup = "60+"

            probs = self.prob[stage][eqGroup][lastAction]

        elif stage == "Flop":
            hand = self.evaluator.handEvaluation(cards, board[:3])
            hand = self.getHandName(hand[0])
            probs = self.prob[stage][hand][lastAction]
        elif stage == "Turn":
            hand = self.evaluator.handEvaluation(cards, board[:4])
            hand = self.getHandName(hand[0])
            probs = self.prob[stage][hand][lastAction]
        elif stage == "River":
            hand = self.evaluator.handEvaluation(cards, board)
            hand = self.getHandName(hand[0])
            probs = self.prob[stage][hand][lastAction]

        actions = list(probs.keys())

        print("Possible Actions: ", end="")
        for action in actions:
            print(action, end=" ")
        print()
        print("You have " + str(money) + " left")
        print("Pot: " + str(pot))

        print("Please write your action:")

        ok = 0
        act = ""

        while ok == 0:
            act = input()

            if act in actions:
                ok = 1
            else:
                print("Action is not valid! Please choose another one!")

        return act


    def playAction(self, cards, board, stage, lastAction):

        probs = dict()

        if stage == "PreFlop":
            stringHand = cards[0] + " " + cards[1]
            eq = self.equityPreFlop[stringHand]
            eqGroup = ""

            if eq <= 40:
                eqGroup = "40 and lower"
            elif 40 < eq <= 45:
                eqGroup = "40-45"
            elif 45 < eq <= 50:
                eqGroup = "45-50"
            elif 50 < eq <= 60:
                eqGroup = "50-60"
            elif eq > 60:
                eqGroup = "60+"

            probs = self.prob[stage][eqGroup][lastAction]

        elif stage == "Flop":
            hand = self.evaluator.handEvaluation(cards, board[:3])
            hand = self.getHandName(hand[0])
            probs = self.prob[stage][hand][lastAction]
        elif stage == "Turn":
            hand = self.evaluator.handEvaluation(cards, board[:4])
            hand = self.getHandName(hand[0])
            probs = self.prob[stage][hand][lastAction]
        elif stage == "River":
            hand = self.evaluator.handEvaluation(cards, board)
            hand = self.getHandName(hand[0])
            probs = self.prob[stage][hand][lastAction]

        actions = []
        probList = []

        for act in probs.keys():
            actions.append(act)
            probList.append(probs[act])

        action = random.choices(actions, weights=probList, k=1)

        return action[0]

    def getNextGameStage(self, currentStage):
        if currentStage == "River":
            return -1
        elif currentStage == "PreFlop":
            return "Flop"
        elif currentStage == "Flop":
            return "Turn"
        elif currentStage == "Turn":
            return "River"

    def getBetSize(self, action, pot, money):
        if action == "Bet 1/3":
            return pot // 3
        elif action == "Bet 2/3":
            return 2 * (pot // 3)
        elif action == "Bet Pot":
            return pot
        else:
            return money

    def playAgainstAverage(self):
        average = AveragePokerPlayer()

        game = PokerGame()
        ownHand = sorted(game.getHand())
        avgHand = sorted(game.getHand())

        board = game.getFlop()
        board = board + game.getNextCard()
        board = board + game.getNextCard()

        winnerIfShowdown = self.evaluator.compareHands(ownHand, avgHand, board)

        turn = random.randint(1, 2)

        ok = 0
        history = "PreFlop action: "
        actionCounter = 0
        gameStage = "PreFlop"
        ownMoney = 497
        avgMoney = 497
        pot = 6
        lastAction = "Check"
        profit = 0

        while ok == 0:
            if turn == 1:
                lastAction = self.playAction(ownHand, board, gameStage, lastAction)
                actionCounter += 1

                if lastAction == "Fold":
                    history = history + "Player Folded"
                    profit -= 500 - max(ownMoney, avgMoney)
                    ok = 1
                elif lastAction == "Call":
                    if self.getNextGameStage(gameStage) == -1 or avgMoney == 0:
                        ok = 1
                        history = history + "Player Called Showdown: "
                        pot += ownMoney - avgMoney
                        ownMoney = avgMoney
                        if winnerIfShowdown == 1:
                            history = history + "Player Wins"
                            profit += 500 - max(ownMoney, avgMoney)
                        elif winnerIfShowdown == -1:
                            history = history + "Average Wins"
                            profit -= 500 - max(ownMoney, avgMoney)
                        else:
                            history = history + "Draw"
                    else:
                        gameStage = self.getNextGameStage(gameStage)
                        history = history + "Player Called "
                        history = history + gameStage + " action "
                        actionCounter = 0
                        pot += ownMoney - avgMoney
                        ownMoney = avgMoney
                        lastAction = "Check"
                elif lastAction == "Check":
                    if actionCounter == 2:
                        if self.getNextGameStage(gameStage) == -1:
                            ok = 1
                            history = history + "Player Checked Showdown: "
                            if winnerIfShowdown == 1:
                                history = history + "Player Wins"
                                profit += 500 - max(ownMoney, avgMoney)
                            elif winnerIfShowdown == -1:
                                history = history + "Average Wins"
                                profit -= 500 - max(ownMoney, avgMoney)
                            else:
                                history = history + "Draw"
                        else:
                            gameStage = self.getNextGameStage(gameStage)
                            history = history + "Player Checked "
                            history = history + gameStage + " action "
                            actionCounter = 0
                            lastAction = "Check"
                    else:
                        history = history + "Player Checked "
                else:
                    bet = self.getBetSize(lastAction, pot, ownMoney)
                    ownMoney -= bet

                    pot += bet

                    history = history + "Player Bet " + str(bet) + " "

                turn = 3 - turn

            else:

                lastAction = average.playAction(avgHand, board, gameStage, lastAction)

                actionCounter += 1

                if lastAction == "Fold":

                    history = history + "Average Folded"
                    profit += 500 - max(ownMoney, avgMoney)

                    ok = 1

                elif lastAction == "Call":

                    if self.getNextGameStage(gameStage) == -1 or ownMoney == 0:

                        ok = 1
                        pot += avgMoney - ownMoney
                        avgMoney = ownMoney
                        history = history + "Average Called Showdown: "

                        if winnerIfShowdown == 1:
                            history = history + "Player Wins"
                            profit += 500 - max(ownMoney, avgMoney)
                        elif winnerIfShowdown == -1:
                            history = history + "Average Wins"
                            profit -= 500 - max(ownMoney, avgMoney)
                        else:
                            history = history + "Draw"

                    else:

                        gameStage = self.getNextGameStage(gameStage)
                        pot += avgMoney - ownMoney
                        avgMoney = ownMoney
                        history = history + "Average Called "
                        history = history + gameStage + " action "
                        actionCounter = 0
                        lastAction = "Check"

                elif lastAction == "Check":

                    if actionCounter == 2:

                        if self.getNextGameStage(gameStage) == -1:

                            ok = 1
                            history = history + "Average Checked Showdown: "

                            if winnerIfShowdown == 1:
                                history = history + "Player Wins"
                                profit += 500 - max(ownMoney, avgMoney)
                            elif winnerIfShowdown == -1:
                                history = history + "Average Wins"
                                profit -= 500 - max(ownMoney, avgMoney)
                            else:
                                history = history + "Draw"

                        else:

                            gameStage = self.getNextGameStage(gameStage)
                            history = history + "Average Checked "
                            history = history + gameStage + " action "
                            actionCounter = 0
                            lastAction = "Check"

                    else:
                        history = history + "Average Checked "

                else:

                    bet = self.getBetSize(lastAction, pot, avgMoney)

                    avgMoney -= bet

                    pot += bet

                    history = history + "Average Bet " + str(bet) + " "

                turn = 3 - turn

        # print(history)
        # print(profit)
        return profit

    def playAgainstHuman(self):
        game = PokerGame()
        ownHand = sorted(game.getHand())
        playerHand = sorted(game.getHand())

        board = game.getFlop()
        board = board + game.getNextCard()
        board = board + game.getNextCard()

        winnerIfShowdown = self.evaluator.compareHands(ownHand, playerHand, board)

        ownFinalHand, draws = self.evaluator.handEvaluation(ownHand, board)
        ownFinalHand = self.getHandName(ownFinalHand)

        playerFinalHand, draws = self.evaluator.handEvaluation(playerHand, board)
        playerFinalHand = self.getHandName(playerFinalHand)

        turn = random.randint(1, 2)

        print("Your Cards Are: " + playerHand[0] + " " + playerHand[1])

        ok = 0
        history = "PreFlop action: "
        actionCounter = 0
        gameStage = "PreFlop"
        ownMoney = 497
        avgMoney = 497
        pot = 6
        lastAction = "Check"
        profit = 0

        print("Preflop:")

        while ok == 0:
            if turn == 1:
                lastAction = self.playAction(ownHand, board, gameStage, lastAction)
                actionCounter += 1

                if lastAction == "Fold":
                    print("Bot Folded")
                    print("You win")
                    print("Bot had " + ownHand[0] + " " + ownHand[1])
                    profit -= 500 - max(ownMoney, avgMoney)
                    ok = 1
                elif lastAction == "Call":
                    if self.getNextGameStage(gameStage) == -1 or avgMoney == 0:
                        ok = 1
                        print("Bot Called Showdown: ")
                        print("Bot had " + ownHand[0] + " " + ownHand[1])
                        pot += ownMoney - avgMoney
                        ownMoney = avgMoney
                        if winnerIfShowdown == 1:
                            print("Bot Wins With " + ownFinalHand)
                            profit += 500 - max(ownMoney, avgMoney)
                        elif winnerIfShowdown == -1:
                            print("You Win")
                            profit -= 500 - max(ownMoney, avgMoney)
                        else:
                            print("Draw")
                    else:
                        gameStage = self.getNextGameStage(gameStage)
                        print("Bot Called ")
                        print(gameStage)
                        if gameStage == "Flop":
                            print("Board:  " + board[0] + " " + board[1] + " " + board[2])
                        elif gameStage == "Turn":
                            print("Board:  " + board[0] + " " + board[1] + " " + board[2] + " " + board[3])
                        elif gameStage == "River":
                            print("Board:  " + board[0] + " " + board[1] + " " + board[2] + " " + board[3] + " " + board[4])
                        actionCounter = 0
                        pot += ownMoney - avgMoney
                        ownMoney = avgMoney
                        lastAction = "Check"

                        print("Pot: " + str(pot))

                elif lastAction == "Check":
                    if actionCounter == 2:
                        if self.getNextGameStage(gameStage) == -1:
                            ok = 1
                            print("Bot Checked Showdown: ")
                            print("Bot had " + ownHand[0] + " " + ownHand[1])
                            if winnerIfShowdown == 1:
                                print("Bot Wins With " + ownFinalHand)
                                profit += 500 - max(ownMoney, avgMoney)
                            elif winnerIfShowdown == -1:
                                print("You Win")
                                profit -= 500 - max(ownMoney, avgMoney)
                            else:
                                print("Draw")
                        else:
                            gameStage = self.getNextGameStage(gameStage)

                            print("Bot Checked ")
                            print(gameStage)
                            if gameStage == "Flop":
                                print("Board:  " + board[0] + " " + board[1] + " " + board[2])
                            elif gameStage == "Turn":
                                print("Board:  " + board[0] + " " + board[1] + " " + board[2] + " " + board[3])
                            elif gameStage == "River":
                                print("Board:  " + board[0] + " " + board[1] + " " + board[2] + " " + board[3] + " " + board[4])
                            actionCounter = 0
                            lastAction = "Check"

                            print("Pot: " + str(pot))

                    else:
                        print("Bot Checked ")
                else:
                    bet = self.getBetSize(lastAction, pot, ownMoney)
                    ownMoney -= bet

                    pot += bet

                    print("Bot Bet " + str(bet) + " ")

                turn = 3 - turn

            else:

                lastAction = self.playerChooseAction(playerHand, board, gameStage, lastAction, avgMoney, pot)

                actionCounter += 1

                if lastAction == "Fold":

                    print("You folded")
                    print("Bot Wins")
                    print("Bot had " + ownHand[0] + " " + ownHand[1])
                    profit += 500 - max(ownMoney, avgMoney)

                    ok = 1

                elif lastAction == "Call":

                    if self.getNextGameStage(gameStage) == -1 or ownMoney == 0:

                        ok = 1
                        pot += avgMoney - ownMoney
                        avgMoney = ownMoney
                        print("Showdown")
                        print("Bot had " + ownHand[0] + " " + ownHand[1])

                        if winnerIfShowdown == 1:
                            print("Bot Wins With " + ownFinalHand)
                            profit += 500 - max(ownMoney, avgMoney)
                        elif winnerIfShowdown == -1:
                            print("You Win")
                            profit -= 500 - max(ownMoney, avgMoney)
                        else:
                            print("Draw")

                    else:

                        gameStage = self.getNextGameStage(gameStage)

                        print("You Called ")
                        print(gameStage)
                        if gameStage == "Flop":
                            print("Board:  " + board[0] + " " + board[1] + " " + board[2])
                        elif gameStage == "Turn":
                            print("Board:  " + board[0] + " " + board[1] + " " + board[2] + " " + board[3])
                        elif gameStage == "River":
                            print(
                                "Board:  " + board[0] + " " + board[1] + " " + board[2] + " " + board[3] + " " + board[
                                    4])

                        pot += avgMoney - ownMoney
                        avgMoney = ownMoney
                        actionCounter = 0
                        lastAction = "Check"

                        print("Pot: " + str(pot))

                elif lastAction == "Check":

                    if actionCounter == 2:

                        if self.getNextGameStage(gameStage) == -1:

                            ok = 1
                            print("You checked")
                            print("Showdown")
                            print("Bot had " + ownHand[0] + " " + ownHand[1])

                            if winnerIfShowdown == 1:
                                print("Bot Wins With " + ownFinalHand)
                                profit += 500 - max(ownMoney, avgMoney)
                            elif winnerIfShowdown == -1:
                                print("You Win")
                                profit -= 500 - max(ownMoney, avgMoney)
                            else:
                                print("Draw")

                        else:

                            gameStage = self.getNextGameStage(gameStage)

                            print("You Checked ")
                            print(gameStage)
                            if gameStage == "Flop":
                                print("Board:  " + board[0] + " " + board[1] + " " + board[2])
                            elif gameStage == "Turn":
                                print("Board:  " + board[0] + " " + board[1] + " " + board[2] + " " + board[3])
                            elif gameStage == "River":
                                print(
                                    "Board:  " + board[0] + " " + board[1] + " " + board[2] + " " + board[3] + " " +
                                    board[
                                        4])

                            actionCounter = 0
                            lastAction = "Check"

                            print("Pot: " + str(pot))

                    else:
                        print("You checked")

                else:

                    bet = self.getBetSize(lastAction, pot, avgMoney)

                    avgMoney -= bet

                    pot += bet

                    print("You bet " + str(bet))

                turn = 3 - turn

        # print(history)
        # print(profit)
        return profit

test = TestAI()
total = 0
iterationCount = 10
for ind in range(1000):

    profit = 0

    for index in range(iterationCount):
        profit += test.playAgainstAverage()

    total += profit

    print(ind)

print("Total profit: " + str(total))
print("Average profit " + str(total / 1000))

'''profit = 0

for index in range(iterationCount):
    profit += test.playAgainstAverage()
    print(index)

print("Total profit: " + str(profit))
print("Average profit " + str(profit / iterationCount))'''

# test.playAgainstHuman()



