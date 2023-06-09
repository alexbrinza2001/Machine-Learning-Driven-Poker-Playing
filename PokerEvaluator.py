import re


class PokerEvaluator:
    def __init__(self):
        self.cardToValue = dict()

        for index in range(10):
            self.cardToValue[str(index)] = index
        self.cardToValue['T'] = 10
        self.cardToValue['J'] = 11
        self.cardToValue['Q'] = 12
        self.cardToValue['K'] = 13
        self.cardToValue['A'] = 14

        self.valueToCard = dict()

        for index in range(10):
            self.valueToCard[index] = str(index)
        self.valueToCard[10] = 'T'
        self.valueToCard[11] = 'J'
        self.valueToCard[12] = 'Q'
        self.valueToCard[13] = 'K'
        self.valueToCard[14] = 'A'

    def handEvaluation(self, playerCards, board):
        hand = ""
        draws = []

        allCards = playerCards + board

        sz = len(allCards)

        values = [self.cardToValue[allCards[i][0]] for i in range(sz)]
        suits = [allCards[i][1] for i in range(sz)]

        values.sort(reverse=True)

        # CHECK ROYAL FLUSH
        if "AH" in allCards and "KH" in allCards and "QH" in allCards and "JH" in allCards and "TH" in allCards:
            hand = "Royal Flush"
        elif "AC" in allCards and "KC" in allCards and "QC" in allCards and "JC" in allCards and "TC" in allCards:
            hand = "Royal Flush"
        elif "AD" in allCards and "KD" in allCards and "QD" in allCards and "JD" in allCards and "TD" in allCards:
            hand = "Royal Flush"
        elif "AS" in allCards and "KS" in allCards and "QS" in allCards and "JS" in allCards and "TS" in allCards:
            hand = "Royal Flush"
        else:
            # CHECK STRAIGHT FLUSH
            for cardValue in values:
                if (cardValue - 1) in values and (cardValue - 2) in values and (cardValue - 3) in values and (
                        cardValue - 4) in values:
                    if self.valueToCard[cardValue] + "H" in allCards and self.valueToCard[cardValue - 1] + "H" in allCards and \
                            self.valueToCard[cardValue - 2] + "H" in allCards and self.valueToCard[
                        cardValue - 3] + "H" in allCards and self.valueToCard[cardValue - 4] + "H" in allCards:
                        hand = "Straight Flush " + self.valueToCard[cardValue]
                    elif self.valueToCard[cardValue] + "C" in allCards and self.valueToCard[cardValue - 1] + "C" in allCards and \
                            self.valueToCard[cardValue - 2] + "C" in allCards and self.valueToCard[
                        cardValue - 3] + "C" in allCards and self.valueToCard[cardValue - 4] + "C" in allCards:
                        hand = "Straight Flush " + self.valueToCard[cardValue]
                    elif self.valueToCard[cardValue] + "D" in allCards and self.valueToCard[cardValue - 1] + "D" in allCards and \
                            self.valueToCard[cardValue - 2] + "D" in allCards and self.valueToCard[
                        cardValue - 3] + "D" in allCards and self.valueToCard[cardValue - 4] + "D" in allCards:
                        hand = "Straight Flush " + self.valueToCard[cardValue]
                    elif self.valueToCard[cardValue] + "S" in allCards and self.valueToCard[cardValue - 1] + "S" in allCards and \
                            self.valueToCard[cardValue - 2] + "S" in allCards and self.valueToCard[
                        cardValue - 3] + "S" in allCards and self.valueToCard[cardValue - 4] + "S" in allCards:
                        hand = "Straight Flush " + self.valueToCard[cardValue]
            if hand == "":
                # CHECK FOUR OF A KIND
                for cardValue in values:
                    if values.count(cardValue) == 4:
                        hand = "Four Of A Kind " + self.valueToCard[cardValue]
                        for cardValue2 in values:
                            if cardValue2 != cardValue:
                                hand = hand + " " + self.valueToCard[cardValue2]
                                break
                        break

                if hand == "":
                    # CHECK HIGH FULL HOUSE HIGH PAIR
                    maxValue = values[0]
                    secondMax = 0
                    for cardValue in values:
                        if cardValue != maxValue:
                            secondMax = cardValue
                            break
                    if values.count(maxValue) == 3 and values.count(secondMax) >= 2:
                        hand = "High Full House High Pair " + self.valueToCard[maxValue] + " " + self.valueToCard[secondMax]

                    if hand == "":
                        # CHECK HIGH FULL HOUSE LOW PAIR
                        if values.count(maxValue) == 3:
                            for cardValue in values:
                                if cardValue != maxValue and cardValue != secondMax:
                                    if values.count(cardValue) >= 2:
                                        hand = "High Full House Low Pair " + self.valueToCard[maxValue] + " " + self.valueToCard[
                                            cardValue]
                                        break

                        if hand == "":
                            # CHECK LOW FULL HOUSE HIGH PAIR
                            for cardValue in values:
                                if values.count(cardValue) == 3 and values.count(maxValue) == 2:
                                    hand = "Low Full House High Pair " + self.valueToCard[cardValue] + " " + self.valueToCard[
                                        maxValue]
                                    break

                            if hand == "":
                                # CHECK LOW FULL HOUSE LOW PAIR
                                for cardValue1 in values:
                                    for cardValue2 in values:
                                        if values.count(cardValue1) == 3 and values.count(cardValue2) == 2:
                                            hand = "Low Full House Low Pair " + self.valueToCard[cardValue1] + " " + \
                                                   self.valueToCard[cardValue2]
                                            break

                                if hand == "":
                                    # CHECK FLUSHES
                                    if suits.count('H') >= 5:
                                        if self.valueToCard[maxValue] + 'H' in playerCards and self.valueToCard[
                                            secondMax] + 'H' in playerCards:
                                            hand = "Flush With 2 Overs " + self.valueToCard[maxValue] + " " + self.valueToCard[
                                                secondMax]
                                            for cardValue in values:
                                                if cardValue != maxValue and cardValue != secondMax and self.valueToCard[
                                                    cardValue] + "H" in allCards and self.valueToCard[cardValue] not in hand:
                                                    hand = hand + " " + self.valueToCard[cardValue]

                                        elif self.valueToCard[maxValue] + 'H' in playerCards:
                                            hand = "Flush With 1 Over " + self.valueToCard[maxValue]
                                            for cardValue in values:
                                                if cardValue != maxValue and self.valueToCard[
                                                    cardValue] + "H" in allCards and self.valueToCard[cardValue] not in hand:
                                                    hand = hand + " " + self.valueToCard[cardValue]

                                        elif self.valueToCard[secondMax] + 'H' in playerCards:
                                            hand = "Flush With 1 Over " + self.valueToCard[secondMax]
                                            for cardValue in values:
                                                if self.valueToCard[cardValue] + "H" in allCards and self.valueToCard[
                                                    cardValue] not in hand:
                                                    hand = hand + " " + self.valueToCard[cardValue]

                                        else:
                                            hand = "Flush "
                                            for cardValue in values:
                                                if self.valueToCard[cardValue] + "H" in allCards and self.valueToCard[
                                                    cardValue] not in hand:
                                                    hand = hand + " " + self.valueToCard[cardValue]

                                    if suits.count('C') >= 5:
                                        if self.valueToCard[maxValue] + 'C' in playerCards and self.valueToCard[
                                            secondMax] + 'C' in playerCards:
                                            hand = "Flush With 2 Overs " + self.valueToCard[maxValue] + " " + self.valueToCard[
                                                secondMax]
                                            for cardValue in values:
                                                if cardValue != maxValue and cardValue != secondMax and self.valueToCard[
                                                    cardValue] + "C" in allCards and self.valueToCard[cardValue] not in hand:
                                                    hand = hand + " " + self.valueToCard[cardValue]

                                        elif self.valueToCard[maxValue] + 'C' in playerCards:
                                            hand = "Flush With 1 Over " + self.valueToCard[maxValue]
                                            for cardValue in values:
                                                if cardValue != maxValue and self.valueToCard[
                                                    cardValue] + "C" in allCards and self.valueToCard[cardValue] not in hand:
                                                    hand = hand + " " + self.valueToCard[cardValue]

                                        elif self.valueToCard[secondMax] + 'C' in playerCards:
                                            hand = "Flush With 1 Over " + self.valueToCard[secondMax]
                                            for cardValue in values:
                                                if self.valueToCard[cardValue] + "C" in allCards and self.valueToCard[
                                                    cardValue] not in hand:
                                                    hand = hand + " " + self.valueToCard[cardValue]

                                        else:
                                            hand = "Flush "
                                            for cardValue in values:
                                                if self.valueToCard[cardValue] + "C" in allCards and self.valueToCard[
                                                    cardValue] not in hand:
                                                    hand = hand + " " + self.valueToCard[cardValue]

                                    if suits.count('D') >= 5:
                                        if self.valueToCard[maxValue] + 'D' in playerCards and self.valueToCard[
                                            secondMax] + 'D' in playerCards:
                                            hand = "Flush With 2 Overs " + self.valueToCard[maxValue] + " " + self.valueToCard[
                                                secondMax]
                                            for cardValue in values:
                                                if cardValue != maxValue and cardValue != secondMax and self.valueToCard[
                                                    cardValue] + "D" in allCards and self.valueToCard[cardValue] not in hand:
                                                    hand = hand + " " + self.valueToCard[cardValue]

                                        elif self.valueToCard[maxValue] + 'D' in playerCards:
                                            hand = "Flush With 1 Over " + self.valueToCard[maxValue]
                                            for cardValue in values:
                                                if cardValue != maxValue and self.valueToCard[
                                                    cardValue] + "D" in allCards and self.valueToCard[cardValue] not in hand:
                                                    hand = hand + " " + self.valueToCard[cardValue]

                                        elif self.valueToCard[secondMax] + 'D' in playerCards:
                                            hand = "Flush With 1 Over " + self.valueToCard[secondMax]
                                            for cardValue in values:
                                                if self.valueToCard[cardValue] + "D" in allCards and self.valueToCard[
                                                    cardValue] not in hand:
                                                    hand = hand + " " + self.valueToCard[cardValue]

                                        else:
                                            hand = "Flush "
                                            for cardValue in values:
                                                if self.valueToCard[cardValue] + "D" in allCards and self.valueToCard[
                                                    cardValue] not in hand:
                                                    hand = hand + " " + self.valueToCard[cardValue]

                                    if suits.count('S') >= 5:
                                        if self.valueToCard[maxValue] + 'S' in playerCards and self.valueToCard[
                                            secondMax] + 'S' in playerCards:
                                            hand = "Flush With 2 Overs " + self.valueToCard[maxValue] + " " + self.valueToCard[
                                                secondMax]
                                            for cardValue in values:
                                                if cardValue != maxValue and cardValue != secondMax and self.valueToCard[
                                                    cardValue] + "S" in allCards and self.valueToCard[cardValue] not in hand:
                                                    hand = hand + " " + self.valueToCard[cardValue]

                                        elif self.valueToCard[maxValue] + 'S' in playerCards:
                                            hand = "Flush With 1 Over " + self.valueToCard[maxValue]
                                            for cardValue in values:
                                                if cardValue != maxValue and self.valueToCard[
                                                    cardValue] + "S" in allCards and self.valueToCard[cardValue] not in hand:
                                                    hand = hand + " " + self.valueToCard[cardValue]

                                        elif self.valueToCard[secondMax] + 'S' in playerCards:
                                            hand = "Flush With 1 Over " + self.valueToCard[secondMax]
                                            for cardValue in values:
                                                if self.valueToCard[cardValue] + "S" in allCards and self.valueToCard[
                                                    cardValue] not in hand:
                                                    hand = hand + " " + self.valueToCard[cardValue]

                                        else:
                                            hand = "Flush"
                                            for cardValue in values:
                                                if self.valueToCard[cardValue] + "S" in allCards and self.valueToCard[
                                                    cardValue] not in hand:
                                                    hand = hand + " " + self.valueToCard[cardValue]

                                    if hand == "":
                                        # CHECK STRAIGHTS
                                        for cardValue in values:
                                            if (cardValue - 1) in values and (cardValue - 2) in values and (
                                                    cardValue - 3) in values and (cardValue - 4) in values:
                                                if self.valueToCard[cardValue] + "H" in playerCards or self.valueToCard[
                                                    cardValue] + "S" in playerCards or self.valueToCard[
                                                    cardValue] + "D" in playerCards or self.valueToCard[
                                                    cardValue] + "C" in playerCards:
                                                    hand = "Straight OverCard " + self.valueToCard[cardValue] + " " + \
                                                           self.valueToCard[cardValue - 1] + " " + self.valueToCard[
                                                               cardValue - 2] + " " + self.valueToCard[cardValue - 3] + " " + \
                                                           self.valueToCard[cardValue - 4]
                                                elif self.valueToCard[cardValue - 4] + "H" in playerCards or self.valueToCard[
                                                    cardValue - 4] + "S" in playerCards or self.valueToCard[
                                                    cardValue - 4] + "D" in playerCards or self.valueToCard[
                                                    cardValue - 4] + "C" in playerCards:
                                                    hand = "Straight Lower Card " + self.valueToCard[cardValue] + " " + \
                                                           self.valueToCard[cardValue - 1] + " " + self.valueToCard[
                                                               cardValue - 2] + " " + self.valueToCard[cardValue - 3] + " " + \
                                                           self.valueToCard[cardValue - 4]
                                                else:
                                                    hand = "Straight Middle Card " + self.valueToCard[cardValue] + " " + \
                                                           self.valueToCard[cardValue - 1] + " " + self.valueToCard[
                                                               cardValue - 2] + " " + self.valueToCard[cardValue - 3] + " " + \
                                                           self.valueToCard[cardValue - 4]

                                                break

                                        lowestValue = values[len(values) - 1]

                                        if hand == "":
                                            # CHECK SET
                                            if values.count(maxValue) == 3:
                                                hand = "Top Set " + self.valueToCard[maxValue]
                                                ct = 0
                                                for cardValue in values:
                                                    if cardValue != maxValue:
                                                        hand = hand + " " + self.valueToCard[cardValue]
                                                        ct += 1

                                                        if ct == 2:
                                                            break
                                            elif values.count(lowestValue) == 3:
                                                hand = "Low Set " + self.valueToCard[lowestValue]
                                                ct = 0
                                                for cardValue in values:
                                                    if cardValue != lowestValue:
                                                        hand = hand + " " + self.valueToCard[cardValue]
                                                        ct += 1

                                                        if ct == 2:
                                                            break
                                            else:
                                                ct = 0
                                                for cardValue in values:
                                                    if values.count(cardValue) == 3:
                                                        hand = "Middle Set " + self.valueToCard[cardValue]

                                                        for cardValue2 in values:
                                                            if cardValue2 != cardValue:
                                                                hand = hand + " " + self.valueToCard[cardValue2]
                                                                ct += 1

                                                                if ct == 2:
                                                                    break
                                                        break

                                            if hand == "":
                                                # CHECK PAIRS

                                                pair1 = 0
                                                pair2 = 0

                                                for cardValue in values:
                                                    if values.count(cardValue) == 2 and pair1 == 0:
                                                        pair1 = cardValue
                                                    elif values.count(cardValue) == 2 and cardValue != pair1:
                                                        pair2 = cardValue
                                                        break

                                                if pair1 != 0 and pair2 != 0:

                                                    lastCard = 0
                                                    for cardValue in values:
                                                        if cardValue != pair1 and cardValue != pair2:
                                                            lastCard = cardValue
                                                            break

                                                    if pair1 == maxValue and pair2 == secondMax:
                                                        hand = "Two Pair Top Two " + self.valueToCard[pair1] + " " + \
                                                               self.valueToCard[pair2] + " " + self.valueToCard[lastCard]
                                                    elif pair1 == maxValue:
                                                        hand = "Two Pair Top One " + self.valueToCard[pair1] + " " + \
                                                               self.valueToCard[pair2] + " " + self.valueToCard[lastCard]
                                                    else:
                                                        hand = "Two Pair Two Low " + self.valueToCard[pair1] + " " + \
                                                               self.valueToCard[pair2] + " " + self.valueToCard[lastCard]
                                                elif pair1 != 0:
                                                    if playerCards[0][0] == playerCards[1][0] and self.cardToValue[
                                                        playerCards[0][0]] == maxValue:
                                                        hand = "OverPair " + self.valueToCard[maxValue]
                                                        for cardValue in values:
                                                            if cardValue != pair1:
                                                                hand = hand + " " + self.valueToCard[cardValue]

                                                    elif playerCards[0][0] == playerCards[1][0]:
                                                        hand = "Pocket Pair " + playerCards[0][0]
                                                        for cardValue in values:
                                                            if cardValue != playerCards[0][0]:
                                                                hand = hand + " " + self.valueToCard[cardValue]

                                                    elif pair1 == maxValue:
                                                        handCard1 = self.cardToValue[playerCards[0][0]]
                                                        handCard2 = self.cardToValue[playerCards[1][0]]
                                                        if handCard1 == secondMax or handCard2 == secondMax:
                                                            hand = "Top Pair Top Kicker " + self.valueToCard[maxValue]
                                                        else:
                                                            hand = "Top Pair Low Kicker " + self.valueToCard[maxValue]

                                                        for cardValue in values:
                                                            if cardValue != maxValue:
                                                                hand = hand + " " + self.valueToCard[cardValue]

                                                    elif pair1 == lowestValue:
                                                        handCard1 = self.cardToValue[playerCards[0][0]]
                                                        handCard2 = self.cardToValue[playerCards[1][0]]

                                                        if handCard1 == maxValue or handCard2 == maxValue:
                                                            hand = "Low Pair Top Kicker " + self.valueToCard[lowestValue]
                                                        else:
                                                            hand = "Low Pair Low Kicker " + self.valueToCard[lowestValue]

                                                        for cardValue in values:
                                                            if cardValue != lowestValue:
                                                                hand = hand + " " + self.valueToCard[cardValue]
                                                    else:
                                                        handCard1 = self.cardToValue[playerCards[0][0]]
                                                        handCard2 = self.cardToValue[playerCards[1][0]]

                                                        if handCard1 == maxValue or handCard2 == maxValue:
                                                            hand = "Middle Pair Top Kicker " + self.valueToCard[pair1]
                                                        else:
                                                            hand = "Middle Pair Low Kicker " + self.valueToCard[pair1]

                                                        for cardValue in values:
                                                            if cardValue != pair1:
                                                                hand = hand + " " + self.valueToCard[cardValue]
                                                else:
                                                    hand = "High Card"
                                                    for cardValue in values:
                                                        if cardValue != pair1:
                                                            hand = hand + " " + self.valueToCard[cardValue]

        # CHECK FOR DRAWS

        if suits.count('H') == 4:

            maxValue = 0

            for card in allCards:
                if card[1] == 'H':
                    if self.cardToValue[card[0]] > maxValue:
                        maxValue = self.cardToValue[card[0]]

            if self.valueToCard[maxValue] + "H" in playerCards:
                draws.append("Flush Draw Overcard")
            else:
                draws.append("Flush Draw No Overcard")

        if suits.count('D') == 4:

            maxValue = 0

            for card in allCards:
                if card[1] == 'D':
                    if self.cardToValue[card[0]] > maxValue:
                        maxValue = self.cardToValue[card[0]]

            if self.valueToCard[maxValue] + "D" in playerCards:
                draws.append("Flush Draw Overcard")
            else:
                draws.append("Flush Draw No Overcard")

        if suits.count('C') == 4:

            maxValue = 0

            for card in allCards:
                if card[1] == 'C':
                    if self.cardToValue[card[0]] > maxValue:
                        maxValue = self.cardToValue[card[0]]

            if self.valueToCard[maxValue] + "C" in playerCards:
                draws.append("Flush Draw Overcard")
            else:
                draws.append("Flush Draw No Overcard")

        if suits.count('S') == 4:

            maxValue = 0

            for card in allCards:
                if card[1] == 'S':
                    if self.cardToValue[card[0]] > maxValue:
                        maxValue = self.cardToValue[card[0]]

            if self.valueToCard[maxValue] + "S" in playerCards:
                draws.append("Flush Draw Overcard")
            else:
                draws.append("Flush Draw No Overcard")

        for cardValue in values:
            if (cardValue - 1) in values and (cardValue - 2) in values and (cardValue - 3):
                draws.append("Straight Draw")
                break

        return hand, draws

    def compareHands(self, cards1, cards2, board):
        hand1, draws1 = self.handEvaluation(cards1, board)
        hand2, draws2 = self.handEvaluation(cards2, board)

        val1 = 0
        val2 = 0

        if "Royal" in hand1:
            val1 = 10
        elif "Straight" in hand1 and "Flush" in hand1:
            val1 = 9
        elif "Four" in hand1:
            val1 = 8
        elif "House" in hand1:
            val1 = 7
        elif "Flush" in hand1:
            val1 = 6
        elif "Straight" in hand1:
            val1 = 5
        elif "Set" in hand1:
            val1 = 4
        elif "Two" in hand1:
            val1 = 3
        elif "Pair" in hand1:
            val1 = 2
        else:
            val1 = 1

        if "Royal" in hand2:
            val2 = 10
        elif "Straight" in hand2 and "Flush" in hand2:
            val2 = 9
        elif "Four" in hand2:
            val2 = 8
        elif "House" in hand2:
            val2 = 7
        elif "Flush" in hand2:
            val2 = 6
        elif "Straight" in hand2:
            val2 = 5
        elif "Set" in hand2:
            val2 = 4
        elif "Two" in hand2:
            val2 = 3
        elif "Pair" in hand2:
            val2 = 2
        else:
            val2 = 1

        if val1 < val2:
            return -1
        elif val1 > val2:
            return 1
        else:

            hand1 = hand1 + " "
            hand2 = hand2 + " "

            newNumbers1 = []

            for index in range(1,  len(hand1) - 1):
                if hand1[index - 1] == " " and hand1[index] == "2" and hand1[index + 1] == " ":
                    newNumbers1.append(2)
                elif hand1[index - 1] == " " and hand1[index] == "3" and hand1[index + 1] == " ":
                    newNumbers1.append(3)
                elif hand1[index - 1] == " " and hand1[index] == "4" and hand1[index + 1] == " ":
                    newNumbers1.append(4)
                elif hand1[index - 1] == " " and hand1[index] == "5" and hand1[index + 1] == " ":
                    newNumbers1.append(5)
                elif hand1[index - 1] == " " and hand1[index] == "6" and hand1[index + 1] == " ":
                    newNumbers1.append(6)
                elif hand1[index - 1] == " " and hand1[index] == "7" and hand1[index + 1] == " ":
                    newNumbers1.append(7)
                elif hand1[index - 1] == " " and hand1[index] == "8" and hand1[index + 1] == " ":
                    newNumbers1.append(8)
                elif hand1[index - 1] == " " and hand1[index] == "9" and hand1[index + 1] == " ":
                    newNumbers1.append(9)
                elif hand1[index - 1] == " " and hand1[index] == "T" and hand1[index + 1] == " ":
                    newNumbers1.append(10)
                elif hand1[index - 1] == " " and hand1[index] == "J" and hand1[index + 1] == " ":
                    newNumbers1.append(11)
                elif hand1[index - 1] == " " and hand1[index] == "Q" and hand1[index + 1] == " ":
                    newNumbers1.append(12)
                elif hand1[index - 1] == " " and hand1[index] == "K" and hand1[index + 1] == " ":
                    newNumbers1.append(13)
                elif hand1[index - 1] == " " and hand1[index] == "A" and hand1[index + 1] == " ":
                    newNumbers1.append(14)

            newNumbers2 = []

            for index in range(1, len(hand2) - 1):
                if hand2[index - 1] == " " and hand2[index] == "2" and hand2[index + 1] == " ":
                    newNumbers2.append(2)
                elif hand2[index - 1] == " " and hand2[index] == "3" and hand2[index + 1] == " ":
                    newNumbers2.append(3)
                elif hand2[index - 1] == " " and hand2[index] == "4" and hand2[index + 1] == " ":
                    newNumbers2.append(4)
                elif hand2[index - 1] == " " and hand2[index] == "5" and hand2[index + 1] == " ":
                    newNumbers2.append(5)
                elif hand2[index - 1] == " " and hand2[index] == "6" and hand2[index + 1] == " ":
                    newNumbers2.append(6)
                elif hand2[index - 1] == " " and hand2[index] == "7" and hand2[index + 1] == " ":
                    newNumbers2.append(7)
                elif hand2[index - 1] == " " and hand2[index] == "8" and hand2[index + 1] == " ":
                    newNumbers2.append(8)
                elif hand2[index - 1] == " " and hand2[index] == "9" and hand2[index + 1] == " ":
                    newNumbers2.append(9)
                elif hand2[index - 1] == " " and hand2[index] == "T" and hand2[index + 1] == " ":
                    newNumbers2.append(10)
                elif hand2[index - 1] == " " and hand2[index] == "J" and hand2[index + 1] == " ":
                    newNumbers2.append(11)
                elif hand2[index - 1] == " " and hand2[index] == "Q" and hand2[index + 1] == " ":
                    newNumbers2.append(12)
                elif hand2[index - 1] == " " and hand2[index] == "K" and hand2[index + 1] == " ":
                    newNumbers2.append(13)
                elif hand2[index - 1] == " " and hand2[index] == "A" and hand2[index + 1] == " ":
                    newNumbers2.append(14)

            val = min(min(len(newNumbers1), len(newNumbers2)), 5)

            for index in range(val):
                if newNumbers1[index] < newNumbers2[index]:
                    return -1

                if newNumbers1[index] > newNumbers2[index]:
                    return 1

            return 0


'''hand1 = ["2H", "TD"]
hand2 = ["8H", "2D"]
brd = ["8D", "TC", "QC", "KC", "AH"]

evall = PokerEvaluator()
print(evall.compareHands(hand1, hand2, brd))'''