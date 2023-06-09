import random
import pygame

from PokerEvaluator import PokerEvaluator
from PokerGame import PokerGame

class Play:

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

        file = open("input_play", "r+")

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

        pygame.init()

        self.width = 1200
        self.height = 800

        # startScreen = pygame.display.set_mode((width, height))
        self.gameScreen = pygame.display.set_mode((self.width, self.height))

        self.background_image = pygame.image.load("background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (1200, 800))

        self.buttonImage = pygame.image.load("button.png")
        self.buttonImage = pygame.transform.scale(self.buttonImage, (150, 75))

        self.potImage = pygame.image.load("pot.png")
        self.potImage = pygame.transform.scale(self.potImage, (150, 70))

        self.actionImage = pygame.transform.scale(self.potImage, (400, 100))

        self.textImage = pygame.image.load("text.png")
        self.textImage = pygame.transform.scale(self.textImage, (250, 75))

        self.tableColor = (28, 60, 13)
        self.tableRect = pygame.Rect((200, 200, 800, 400))

        self.font = pygame.font.Font(None, 35)

        self.stackColor = (1, 100, 32)
        self.playerStackRect = pygame.Rect((50, 600, 200, 100))
        self.text = "Your stack: 1000"
        self.playerStackText = self.font.render(self.text, True, (0, 0, 0))
        self.playerStackTextRect = self.playerStackText.get_rect()
        self.playerStackTextRect.center = self.playerStackRect.center

        self.botStackRect = pygame.Rect((50, 70, 200, 100))
        self.text = "Bot stack: 1000"
        self.botStackText = self.font.render(self.text, True, (0, 0, 0))
        self.botStackTextRect = self.botStackText.get_rect()
        self.botStackTextRect.center = self.botStackRect.center

        self.botActionRect = pygame.Rect((400, 70, 450, 100))
        self.text = "Bot Action! Showdown: Player wins"
        self.botActionText = self.font.render(self.text, True, (0, 0, 0))
        self.botActionTextRect = self.botActionText.get_rect()
        self.botActionTextRect.center = self.botActionRect.center

        self.buttonNextHandRect = pygame.Rect((1000, 70, 150, 100))
        self.text = "Next Hand"
        self.buttonNextHandText = self.font.render(self.text, True, (0, 0, 0))
        self.buttonNextHandTextRect = self.buttonNextHandText.get_rect()
        self.buttonNextHandTextRect.center = self.buttonNextHandRect.center

        self.potColor = (138, 43, 226)
        self.potRect = pygame.Rect((755, 365, 125, 100))
        self.text = "Pot: 500"
        self.potText = self.font.render(self.text, True, (0, 0, 0))
        self.potTextRect = self.potText.get_rect()
        self.potTextRect.center = self.potRect.center

        self.cardImage = pygame.image.load("cards/2_of_clubs.png")
        self.cardImage = pygame.transform.scale(self.cardImage, (70, 90))
        self.playerCardRect = self.cardImage.get_rect()
        self.playerCardRect.center = (555, 505)

        self.backImage = pygame.image.load("cards/back_of_card.png")
        self.backImage = pygame.transform.scale(self.backImage, (70, 95))

        self.playerCardRect2 = self.cardImage.get_rect()
        self.playerCardRect2.center = (645, 505)

        self.flopCard1 = self.cardImage.get_rect()
        self.flopCard1.center = (340, 400)

        self.flopCard2 = self.cardImage.get_rect()
        self.flopCard2.center = (430, 400)

        self.flopCard3 = self.cardImage.get_rect()
        self.flopCard3.center = (520, 400)

        self.turnCard = self.cardImage.get_rect()
        self.turnCard.center = (610, 400)

        self.riverCard = self.cardImage.get_rect()
        self.riverCard.center = (700, 400)

        self.botCardRect = self.cardImage.get_rect()
        self.botCardRect.center = (555, 290)

        self.botCardRect2 = self.cardImage.get_rect()
        self.botCardRect2.center = (645, 290)

        self.buttonSurface = pygame.Surface((150, 75), pygame.SRCALPHA)
        self.buttonSurface.fill((0, 0, 0, 0))

        self.bet1ButtonColor = (1, 100, 32)
        self.bet1ButtonRect = self.buttonSurface.get_rect()
        self.bet1ButtonRect.center = (1075, 527)
        self.text = "Bet 1/3 Pot"
        self.bet1ButtonText = self.font.render(self.text, True, (0, 0, 0))
        self.bet1ButtonTextRect = self.bet1ButtonText.get_rect()
        self.bet1ButtonTextRect.center = self.bet1ButtonRect.center

        self.bet2ButtonColor = (1, 100, 32)
        self.bet2ButtonRect = self.buttonSurface.get_rect()
        self.bet2ButtonRect.center = (1075, 633)
        self.text = "Bet 2/3 Pot"
        self.bet2ButtonText = self.font.render(self.text, True, (0, 0, 0))
        self.bet2ButtonTextRect = self.bet2ButtonText.get_rect()
        self.bet2ButtonTextRect.center = self.bet2ButtonRect.center

        self.bet3ButtonColor = (1, 100, 32)
        self.bet3ButtonRect = self.buttonSurface.get_rect()
        self.bet3ButtonRect.center = (1075, 738)
        self.text = "Bet Pot"
        self.bet3ButtonText = self.font.render(self.text, True, (0, 0, 0))
        self.bet3ButtonTextRect = self.bet3ButtonText.get_rect()
        self.bet3ButtonTextRect.center = self.bet3ButtonRect.center

        self.checkButtonColor = (1, 100, 32)
        self.checkButtonRect = self.buttonSurface.get_rect()
        self.checkButtonRect.center = (905, 633)
        self.text = "Check"
        self.checkButtonText = self.font.render(self.text, True, (0, 0, 0))
        self.checkButtonTextRect = self.checkButtonText.get_rect()
        self.checkButtonTextRect.center = self.checkButtonRect.center

        self.allButtonColor = (1, 100, 32)
        self.allButtonRect = self.buttonSurface.get_rect()
        self.allButtonRect.center = (905, 738)
        self.text = "All In"
        self.allButtonText = self.font.render(self.text, True, (0, 0, 0))
        self.allButtonTextRect = self.allButtonText.get_rect()
        self.allButtonTextRect.center = self.allButtonRect.center

        self.callButtonColor = (1, 100, 32)
        self.callButtonRect = self.buttonSurface.get_rect()
        self.callButtonRect.center = (905, 633)
        self.text = "Call"
        self.callButtonText = self.font.render(self.text, True, (0, 0, 0))
        self.callButtonTextRect = self.callButtonText.get_rect()
        self.callButtonTextRect.center = self.callButtonRect.center

        self.foldButtonColor = (1, 100, 32)
        self.foldButtonRect = self.buttonSurface.get_rect()
        self.foldButtonRect.center = (1075, 633)
        self.text = "Fold"
        self.foldButtonText = self.font.render(self.text, True, (0, 0, 0))
        self.foldButtonTextRect = self.foldButtonText.get_rect()
        self.foldButtonTextRect.center = self.foldButtonRect.center

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

        if "Call" in actions:
            self.gameScreen.blit(self.buttonImage, self.callButtonRect)
            self.gameScreen.blit(self.buttonImage, self.foldButtonRect)
            self.gameScreen.blit(self.font.render("Fold", True, (0, 0, 0)), (1050, 623))
            self.gameScreen.blit(self.font.render("Call", True, (0, 0, 0)), (882, 623))
            pygame.display.update()

            ans = 0

            while ans == 0:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()

                        if self.callButtonRect.collidepoint(mouse_pos):
                            return "Call"

                        if self.foldButtonRect.collidepoint(mouse_pos):
                            return "Fold"


        else:
            self.gameScreen.blit(self.buttonImage, self.bet1ButtonRect)
            self.gameScreen.blit(self.buttonImage, self.bet2ButtonRect)
            self.gameScreen.blit(self.buttonImage, self.bet3ButtonRect)
            self.gameScreen.blit(self.buttonImage, self.checkButtonRect)
            self.gameScreen.blit(self.buttonImage, self.allButtonRect)
            self.gameScreen.blit(self.font.render("Bet 1/3", True, (0, 0, 0)), (1036, 518))
            self.gameScreen.blit(self.font.render("Bet 2/3", True, (0, 0, 0)), (1036, 623))
            self.gameScreen.blit(self.font.render("Bet Pot", True, (0, 0, 0)), (1036, 728))
            self.gameScreen.blit(self.font.render("Check", True, (0, 0, 0)), (870, 623))
            self.gameScreen.blit(self.font.render("All In", True, (0, 0, 0)), (878, 728))
            pygame.display.update()

            ans = 0

            while ans == 0:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()

                        if self.bet1ButtonRect.collidepoint(mouse_pos):
                            return "Bet 1/3"

                        if self.bet2ButtonRect.collidepoint(mouse_pos):
                            return "Bet 2/3"

                        if self.bet3ButtonRect.collidepoint(mouse_pos):
                            return "Bet Pot"

                        if self.checkButtonRect.collidepoint(mouse_pos):
                            return "Check"

                        if self.allButtonRect.collidepoint(mouse_pos):
                            return "All In"



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

    def getFileFromCard(self, card):
        file = ""
        value = card[0]
        suit = card[1]

        if value == "T":
            file = "10"
        elif value == "J":
            file = "jack"
        elif value == "Q":
            file = "queen"
        elif value == "K":
            file = "king"
        elif value == "A":
            file = "ace"
        else:
            file = value

        file = file + "_of_"

        if suit == "C":
            file = file + "clubs.png"
        elif suit == "D":
            file = file + "diamonds.png"
        elif suit == "H":
            file = file + "hearts.png"
        elif suit == "S":
            file = file + "spades.png"

        return file

    def waitForNext(self):
        pygame.draw.rect(self.gameScreen, self.stackColor, self.buttonNextHandRect)
        pygame.draw.rect(self.gameScreen, self.stackColor, self.buttonNextHandTextRect)
        self.gameScreen.blit(self.buttonNextHandText, self.buttonNextHandTextRect)
        pygame.display.update()
        next = 0

        while next == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()

                    if self.buttonNextHandRect.collidepoint(mouse_pos):
                        return


    def playAgainstHuman(self, startingAmount1, startingAmount2):

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
        ownMoney = startingAmount1 - 3
        avgMoney = startingAmount2 - 3
        pot = 6

        if ownMoney < 0:
            ownMoney = 0
            avgMoney = startingAmount2
            pot = 0

        if avgMoney < 0:
            avgMoney = 0
            ownMoney = startingAmount1
            pot = 0

        lastAction = "Check"
        profit = 0
        amountBet = 0

        playerCard1 = pygame.image.load("cards/" + self.getFileFromCard(playerHand[0]))
        playerCard1 = pygame.transform.scale(playerCard1, (70, 95))

        playerCard2 = pygame.image.load("cards/" + self.getFileFromCard(playerHand[1]))
        playerCard2 = pygame.transform.scale(playerCard2, (70, 95))

        botCard1 = pygame.image.load("cards/" + self.getFileFromCard(ownHand[0]))
        botCard1 = pygame.transform.scale(botCard1, (70, 95))

        botCard2 = pygame.image.load("cards/" + self.getFileFromCard(ownHand[1]))
        botCard2 = pygame.transform.scale(botCard2, (70, 95))

        flopCard1 = pygame.image.load("cards/" + self.getFileFromCard(board[0]))
        flopCard1 = pygame.transform.scale(flopCard1, (70, 95))

        flopCard2 = pygame.image.load("cards/" + self.getFileFromCard(board[1]))
        flopCard2 = pygame.transform.scale(flopCard2, (70, 95))

        flopCard3 = pygame.image.load("cards/" + self.getFileFromCard(board[2]))
        flopCard3 = pygame.transform.scale(flopCard3, (70, 95))

        turnCard = pygame.image.load("cards/" + self.getFileFromCard(board[3]))
        turnCard = pygame.transform.scale(turnCard, (70, 95))

        riverCard = pygame.image.load("cards/" + self.getFileFromCard(board[4]))
        riverCard = pygame.transform.scale(riverCard, (70, 95))

        botLastAct = ""

        print("Preflop:")

        running = True

        while running:

            self.gameScreen.blit(self.background_image, (0, 0))
            self.gameScreen.blit(self.textImage, self.playerStackRect)
            self.gameScreen.blit(self.textImage, self.botStackRect)
            self.gameScreen.blit(self.potImage, self.potRect)
            self.gameScreen.blit(playerCard1, self.playerCardRect)
            self.gameScreen.blit(playerCard2, self.playerCardRect2)

            if gameStage == "Flop" or gameStage == "Turn" or gameStage == "River":
                self.gameScreen.blit(flopCard1, self.flopCard1)
                self.gameScreen.blit(flopCard2, self.flopCard2)
                self.gameScreen.blit(flopCard3, self.flopCard3)

                if gameStage == "Turn" or gameStage == "River":
                    self.gameScreen.blit(turnCard, self.turnCard)

                    if gameStage == "River":
                        self.gameScreen.blit(riverCard, self.riverCard)

            self.gameScreen.blit(self.backImage, self.botCardRect)
            self.gameScreen.blit(self.backImage, self.botCardRect2)

            self.gameScreen.blit(self.font.render("Your stack: " + str(avgMoney), True, (0, 0, 0)), (80, 625))
            self.gameScreen.blit(self.font.render("Bot stack: " + str(ownMoney), True, (0, 0, 0)), (90, 95))
            self.gameScreen.blit(self.font.render("Pot: " + str(pot), True, (0, 0, 0)), (780, 390))

            if startingAmount1 == 0 or startingAmount2 == 0:
                if startingAmount1 == 0:
                    self.gameScreen.blit(self.font.render("Game Over! You Win!", True, (255, 255, 255)),
                                         self.botActionTextRect)
                    pygame.display.update()
                else:
                    self.gameScreen.blit(self.font.render("Game Over! Bot Wins!", True, (255, 255, 255)),
                                         self.botActionTextRect)
                    pygame.display.update()

                end = 0

                while end == 0:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()

                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            mouse_pos = pygame.mouse.get_pos()

                            if self.buttonNextHandRect.collidepoint(mouse_pos):
                                return

            if turn == 1:
                lastAction = self.playAction(ownHand, board, gameStage, lastAction)
                actionCounter += 1

                if lastAction == "Fold":
                    print("Bot Folded")
                    self.gameScreen.blit(self.font.render("Bot Folded! You Win!", True, (255, 255, 255)), self.botActionTextRect)
                    pygame.display.update()
                    print("You win")
                    print("Bot had " + ownHand[0] + " " + ownHand[1])
                    ok = 1

                    self.gameScreen.blit(botCard1, self.botCardRect)
                    self.gameScreen.blit(botCard2, self.botCardRect2)
                    self.waitForNext()
                    self.playAgainstHuman(ownMoney, avgMoney + pot)

                elif lastAction == "Call":
                    if self.getNextGameStage(gameStage) == -1 or avgMoney == 0:

                        print("Bot Called Showdown: ")
                        print("Bot had " + ownHand[0] + " " + ownHand[1])

                        self.gameScreen.blit(botCard1, self.botCardRect)
                        self.gameScreen.blit(botCard2, self.botCardRect2)

                        self.gameScreen.blit(flopCard1, self.flopCard1)
                        self.gameScreen.blit(flopCard2, self.flopCard2)
                        self.gameScreen.blit(flopCard3, self.flopCard3)
                        self.gameScreen.blit(turnCard, self.turnCard)
                        self.gameScreen.blit(riverCard, self.riverCard)

                        amount = min(amountBet, ownMoney)

                        pot += amount
                        ownMoney = ownMoney - amount
                        if winnerIfShowdown == 1:
                            print("Bot Wins With " + ownFinalHand)
                            self.gameScreen.blit(self.font.render("Bot Called! Showdown: Bot Wins!", True, (255, 255, 255)),
                                                 self.botActionTextRect)
                            self.waitForNext()
                            self.playAgainstHuman(ownMoney + pot, avgMoney)
                        elif winnerIfShowdown == -1:
                            print("You Win")
                            self.gameScreen.blit(self.font.render("Bot Called! Showdown: You Win!", True, (255, 255, 255)), self.botActionTextRect)
                            self.waitForNext()
                            self.playAgainstHuman(ownMoney, avgMoney + pot)
                        else:
                            print("Draw")
                            self.gameScreen.blit(self.font.render("Bot Called! Showdown: Draw!", True, (255, 255, 255)), self.botActionTextRect)
                            self.waitForNext()
                            self.playAgainstHuman(startingAmount1, startingAmount2)

                    else:
                        gameStage = self.getNextGameStage(gameStage)
                        print("Bot Called ")
                        botLastAct = "Call"
                        print(gameStage)
                        if gameStage == "Flop":
                            print("Board:  " + board[0] + " " + board[1] + " " + board[2])
                        elif gameStage == "Turn":
                            print("Board:  " + board[0] + " " + board[1] + " " + board[2] + " " + board[3])
                        elif gameStage == "River":
                            print("Board:  " + board[0] + " " + board[1] + " " + board[2] + " " + board[3] + " " + board[4])
                        actionCounter = 0

                        if amountBet >= ownMoney:

                            pot += min(ownMoney, avgMoney)
                            ownMoney = max(0, ownMoney - avgMoney)

                            self.gameScreen.blit(botCard1, self.botCardRect)
                            self.gameScreen.blit(botCard2, self.botCardRect2)

                            self.gameScreen.blit(flopCard1, self.flopCard1)
                            self.gameScreen.blit(flopCard2, self.flopCard2)
                            self.gameScreen.blit(flopCard3, self.flopCard3)
                            self.gameScreen.blit(turnCard, self.turnCard)
                            self.gameScreen.blit(riverCard, self.riverCard)

                            if winnerIfShowdown == 1:
                                print("Bot Wins With " + ownFinalHand)
                                self.gameScreen.blit(
                                    self.font.render("Bot Called! Showdown: Bot Wins!", True, (255, 255, 255)),
                                    self.botActionTextRect)
                                self.waitForNext()
                                self.playAgainstHuman(ownMoney + pot, avgMoney)
                            elif winnerIfShowdown == -1:
                                print("You Win")
                                self.gameScreen.blit(
                                    self.font.render("Bot Called! Showdown: You Win!", True, (255, 255, 255)),
                                    self.botActionTextRect)
                                self.waitForNext()
                                self.playAgainstHuman(ownMoney, avgMoney + pot)
                            else:
                                print("Draw")
                                self.gameScreen.blit(self.font.render("Bot Called! Showdown: Draw!", True, (255, 255, 255)),
                                                     self.botActionTextRect)
                                self.waitForNext()
                                self.playAgainstHuman(startingAmount1, startingAmount2)
                        else:
                            pot += amountBet
                            ownMoney -= amountBet
                            lastAction = "Check"
                            botLastAct = "Call"

                            print("Pot: " + str(pot))

                elif lastAction == "Check":
                    if actionCounter == 2:
                        if self.getNextGameStage(gameStage) == -1:
                            ok = 1
                            print("Bot Checked Showdown: ")
                            print("Bot had " + ownHand[0] + " " + ownHand[1])

                            self.gameScreen.blit(botCard1, self.botCardRect)
                            self.gameScreen.blit(botCard2, self.botCardRect2)

                            self.gameScreen.blit(flopCard1, self.flopCard1)
                            self.gameScreen.blit(flopCard2, self.flopCard2)
                            self.gameScreen.blit(flopCard3, self.flopCard3)
                            self.gameScreen.blit(turnCard, self.turnCard)
                            self.gameScreen.blit(riverCard, self.riverCard)

                            if winnerIfShowdown == 1:
                                print("Bot Wins With " + ownFinalHand)
                                self.gameScreen.blit(self.font.render("Bot Checked! Showdown: Bot Wins!", True, (255, 255, 255)),
                                                     self.botActionTextRect)
                                self.waitForNext()
                                self.playAgainstHuman(ownMoney + pot, avgMoney)
                            elif winnerIfShowdown == -1:
                                print("You Win")
                                self.gameScreen.blit(
                                    self.font.render("Bot Checked! Showdown: You Win!", True, (255, 255, 255)),
                                    self.botActionTextRect)
                                self.waitForNext()
                                self.playAgainstHuman(ownMoney, avgMoney + pot)
                            else:
                                print("Draw")
                                self.gameScreen.blit(
                                    self.font.render("Bot Checked! Showdown: Draw!", True, (255, 255, 255)),
                                    self.botActionTextRect)
                                self.waitForNext()
                                self.playAgainstHuman(startingAmount1, startingAmount2)
                        else:
                            gameStage = self.getNextGameStage(gameStage)

                            print("Bot Checked ")
                            botLastAct = "Check"

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
                        botLastAct = "Check"
                else:
                    bet = self.getBetSize(lastAction, pot, ownMoney)

                    amountBet = bet

                    if bet < ownMoney:
                        ownMoney -= bet
                        pot += bet
                    else:
                        pot += min(ownMoney, avgMoney)
                        ownMoney = max(0, ownMoney - avgMoney)
                        lastAction = "All In"

                    botLastAct = "Bet"

                    print("Bot Bet " + str(bet) + " ")

                turn = 3 - turn

            else:
                if botLastAct == "Call":
                    self.gameScreen.blit(self.font.render("Bot Called!", True, (255, 255, 255)),
                                     self.botActionTextRect)
                    pygame.display.update()
                elif botLastAct == "Check":
                    self.gameScreen.blit(self.font.render("Bot Checked!", True, (255, 255, 255)),
                                     self.botActionTextRect)
                    pygame.display.update()
                else:

                    if amountBet == 0:
                        self.gameScreen.blit(self.font.render("You are the first to act!", True, (255, 255, 255)),
                                             self.botActionTextRect)
                        pygame.display.update()
                    else:
                        self.gameScreen.blit(self.font.render("Bot Bet " + str(amountBet), True, (255, 255, 255)),
                                         self.botActionTextRect)
                        pygame.display.update()
                lastAction = self.playerChooseAction(playerHand, board, gameStage, lastAction, avgMoney, pot)

                actionCounter += 1

                if lastAction == "Fold":

                    print("You folded")
                    print("Bot Wins")
                    print("Bot had " + ownHand[0] + " " + ownHand[1])

                    self.gameScreen.blit(botCard1, self.botCardRect)
                    self.gameScreen.blit(botCard2, self.botCardRect2)
                    self.gameScreen.blit(self.font.render("Bot Bet " + str(amountBet) + " Bot Wins!", True, (255, 255, 255)),
                                         self.botActionTextRect)
                    pygame.display.update()
                    self.waitForNext()
                    self.playAgainstHuman(ownMoney + pot, avgMoney)

                elif lastAction == "Call":

                    if self.getNextGameStage(gameStage) == -1 or ownMoney == 0:

                        pot += amountBet
                        avgMoney -= amountBet
                        print("Showdown")
                        print("Bot had " + ownHand[0] + " " + ownHand[1])

                        self.gameScreen.blit(botCard1, self.botCardRect)
                        self.gameScreen.blit(botCard2, self.botCardRect2)

                        self.gameScreen.blit(flopCard1, self.flopCard1)
                        self.gameScreen.blit(flopCard2, self.flopCard2)
                        self.gameScreen.blit(flopCard3, self.flopCard3)
                        self.gameScreen.blit(turnCard, self.turnCard)
                        self.gameScreen.blit(riverCard, self.riverCard)

                        if winnerIfShowdown == 1:
                            print("Bot Wins With " + ownFinalHand)

                            self.gameScreen.blit(self.font.render("Bot Bet " + str(amountBet) + " Bot Wins!", True, (255, 255, 255)),
                                         self.botActionTextRect)
                            self.waitForNext()
                            self.playAgainstHuman(ownMoney + pot, avgMoney)

                        elif winnerIfShowdown == -1:
                            print("You Win")
                            self.gameScreen.blit(self.font.render("Bot Bet " + str(amountBet) + " You Win!", True, (255, 255, 255)),
                                                 self.botActionTextRect)
                            self.waitForNext()
                            self.playAgainstHuman(ownMoney, avgMoney + pot)
                        else:
                            print("Draw")
                            self.gameScreen.blit(self.font.render("Bot Bet " + str(amountBet) + " Draw!", True, (255, 255, 255)),
                                                 self.botActionTextRect)
                            self.waitForNext()
                            self.playAgainstHuman(startingAmount1, startingAmount2)

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

                        if amountBet >= avgMoney:
                            pot += min(ownMoney, avgMoney)
                            avgMoney = max(0, avgMoney - ownMoney)

                            self.gameScreen.blit(botCard1, self.botCardRect)
                            self.gameScreen.blit(botCard2, self.botCardRect2)

                            self.gameScreen.blit(flopCard1, self.flopCard1)
                            self.gameScreen.blit(flopCard2, self.flopCard2)
                            self.gameScreen.blit(flopCard3, self.flopCard3)
                            self.gameScreen.blit(turnCard, self.turnCard)
                            self.gameScreen.blit(riverCard, self.riverCard)

                            if winnerIfShowdown == 1:
                                print("Bot Wins With " + ownFinalHand)
                                self.gameScreen.blit(self.font.render("Bot Bet " + str(amountBet) + " Bot Wins!", True, (255, 255, 255)),
                                                     self.botActionTextRect)
                                self.waitForNext()
                                self.playAgainstHuman(ownMoney + pot, avgMoney)

                            elif winnerIfShowdown == -1:
                                print("You Win")
                                self.gameScreen.blit(self.font.render("Bot Bet " + str(amountBet) + " You Win!", True, (255, 255, 255)),
                                                     self.botActionTextRect)
                                self.waitForNext()
                                self.playAgainstHuman(ownMoney, avgMoney + pot)
                            else:
                                print("Draw")
                                self.gameScreen.blit(self.font.render("Bot Bet " + str(amountBet) + " Draw!", True, (255, 255, 255)),
                                                     self.botActionTextRect)
                                self.waitForNext()
                                self.playAgainstHuman(startingAmount1, startingAmount2)

                        else:
                            pot += amountBet
                            avgMoney -= amountBet
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

                            self.gameScreen.blit(botCard1, self.botCardRect)
                            self.gameScreen.blit(botCard2, self.botCardRect2)

                            self.gameScreen.blit(flopCard1, self.flopCard1)
                            self.gameScreen.blit(flopCard2, self.flopCard2)
                            self.gameScreen.blit(flopCard3, self.flopCard3)
                            self.gameScreen.blit(turnCard, self.turnCard)
                            self.gameScreen.blit(riverCard, self.riverCard)

                            if winnerIfShowdown == 1:
                                print("Bot Wins With " + ownFinalHand)
                                self.gameScreen.blit(self.font.render("Bot Wins!", True, (255, 255, 255)),
                                                     self.botActionTextRect)
                                self.waitForNext()
                                self.playAgainstHuman(ownMoney + pot, avgMoney)
                            elif winnerIfShowdown == -1:
                                print("You Win")
                                self.gameScreen.blit(self.font.render("You Win!", True, (255, 255, 255)),
                                                     self.botActionTextRect)
                                self.waitForNext()
                                self.playAgainstHuman(ownMoney, avgMoney + pot)
                            else:
                                print("Draw")
                                self.gameScreen.blit(self.font.render("Draw!", True, (255, 255, 255)),
                                                     self.botActionTextRect)
                                self.waitForNext()
                                self.playAgainstHuman(startingAmount1, startingAmount2)

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

                    amountBet = bet

                    if bet < avgMoney:
                        avgMoney -= bet
                        pot += bet
                    else:
                        pot += min(ownMoney, avgMoney)
                        avgMoney = max(0, avgMoney - ownMoney)
                        lastAction = "All In"

                    print("You bet " + str(bet))

                turn = 3 - turn

            pygame.display.update()

        pygame.quit()

        # print(history)
        # print(profit)
        return profit

game = Play()

game.playAgainstHuman(1000, 1000)