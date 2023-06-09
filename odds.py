import copy
import functools
import random

d = dict()
for index in range(10):
    d[str(index)] = index
d['T'] = 10
d['J'] = 11
d['Q'] = 12
d['K'] = 13
d['A'] = 14


def compare(x, y):
    valX = d[x[0]]
    valY = d[y[0]]

    return valX - valY


def checkConsecutive(hand):
    for i in range(4):

        val1 = d[hand[i][0]]
        val2 = d[hand[i + 1][0]]

        if val2 - val1 != 1:
            return 0

    return 1


def whatHand(hand):
    valueDict = dict()
    suitSet = set()
    valueCount = 0
    suitCount = 0
    maxValueCount = 0
    maxValue = ''

    for card in hand:
        value = card[0]
        suit = card[1]

        if value not in valueDict.keys():
            valueCount += 1
            valueDict[value] = 1
            if valueDict[value] > maxValueCount:
                maxValueCount = 1
                maxValue = value
        else:
            valueDict[value] += 1
            if valueDict[value] > maxValueCount:
                maxValueCount = valueDict[value]
                maxValue = value

        if suit not in suitSet:
            suitCount += 1
            suitSet.add(suit)

    sortedHand = sorted(hand, key=functools.cmp_to_key(compare))

    cons = checkConsecutive(sortedHand)

    if cons == 1 and suitCount == 1 and sortedHand[4][0] == 'A':
        return [9]

    if cons == 1 and suitCount == 1:
        return [8, d[sortedHand[4][0]]]

    if suitCount == 1 and sortedHand[0][0] == '2' and sortedHand[1][0] == '3' and sortedHand[2][0] == '4' and sortedHand[3][0] == '5' and sortedHand[4][0] == 'A':
        return [8, 5]

    if maxValueCount == 4:
        for value in valueDict.keys():
            if valueDict[value] == 1:
                kicker = value
        return [7, d[maxValue], d[kicker]]

    if valueCount == 2:
        for value in valueDict.keys():
            if valueDict[value] == 3:
                full = value
            else:
                of = value

        return [6, d[full], d[of]]

    if suitCount == 1:
        list = [5]
        for card in sortedHand[::-1]:
            list.append(d[card[0]])
        return list

    if cons == 1:
        return [4, d[sortedHand[4][0]]]

    if sortedHand[0][0] == '2' and sortedHand[1][0] == '3' and sortedHand[2][0] == '4' and sortedHand[3][0] == '5' and sortedHand[4][0] == 'A':
        return [4, 5]

    if valueCount == 3 and maxValueCount == 3:
        for value in valueDict.keys():
            if valueDict[value] == 3:
                three = value

        kicker1 = ''
        kicker2 = ''

        for card in sortedHand[::-1]:
            if card[0] != three:
                if kicker1 == '':
                    kicker1 = card[0]
                else:
                    kicker2 = card[0]

        return [3, d[three], d[kicker1], d[kicker2]]

    if valueCount == 3:
        val1 = ''
        val2 = ''
        for value in valueDict.keys():
            if valueDict[value] == 2:
                if val1 == '':
                    val1 = value
                else:
                    val2 = value
            else:
                kicker = value

        val1Number = d[val1]
        val2Number = d[val2]

        if val2Number > val1Number:
            val1Number, val2Number = val2Number, val1Number

        return [2, val1Number, val2Number, d[kicker]]

    if valueCount == 4:
        for value in valueDict.keys():
            if valueDict[value] == 2:
                pair = value

        list = [1, d[pair]]

        for card in sortedHand[::-1]:
            if card[0] != pair:
                list.append(d[card[0]])

        return list

    list = [0]

    for card in sortedHand[::-1]:
        list.append(d[card[0]])

    return list


def compareHands(hand1, hand2):

    if hand1[0] < hand2[0]:
        return -1

    if hand1[0] > hand2[0]:
        return 1

    l = len(hand1)

    for i in range(1, l):
        if hand1[i] < hand2[i]:
            return -1
        if hand1[i] > hand2[i]:
            return 1

    return 0


def getBestHand(cards):
    bestHand = []

    for i1 in range(7):
        for i2 in range(i1 + 1, 7):
            for i3 in range(i2 + 1, 7):
                for i4 in range(i3 + 1, 7):
                    for i5 in range(i4 + 1, 7):
                        hand = whatHand([cards[i1], cards[i2], cards[i3], cards[i4], cards[i5]])
                        if len(bestHand) == 0:
                            bestHand = copy.deepcopy(hand)
                        elif compareHands(hand, bestHand) == 1:
                            bestHand = copy.deepcopy(hand)

    return bestHand

'''
def compareEquityPreFlop(hand1, hand2):
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suits = ['s', 'd', 'c', 'h']
    cards = []

    for value in values:
        for suit in suits:
            cards.append(value + suit)

    winHands1 = 0
    winHands2 = 0
    draw = 0
    hands = 0

    for i1 in range(52):
        if cards[i1] not in hand1 and cards[i1] not in hand2:
            for i2 in range(i1 + 1, 52):
                if cards[i2] not in hand1 and cards[i2] not in hand2:
                    for i3 in range(i2 + 1, 52):
                        if cards[i3] not in hand1 and cards[i3] not in hand2:
                            for i4 in range(i3 + 1, 52):
                                if cards[i4] not in hand1 and cards[i4] not in hand2:
                                    for i5 in range(i4 + 1, 52):
                                        if cards[i5] not in hand1 and cards[i5] not in hand2:
                                            tableCards = [cards[i1], cards[i2], cards[i3], cards[i4], cards[i5]]
                                            bestHand1 = getBestHand(tableCards + hand1)
                                            bestHand2 = getBestHand(tableCards + hand2)
                                            comp = compareHands(bestHand1, bestHand2)
                                            hands += 1
                                            if comp == 1:
                                                winHands1 += 1
                                            elif comp == -1:
                                                winHands2 += 1
                                            else:
                                                draw += 1
                                            #print(hands)

    equity1 = winHands1 / hands * 100
    equity2 = winHands2 / hands * 100
    tie = draw / hands * 100

    return [[winHands1, winHands2, draw], [equity1, equity2, tie]]
'''


def calculateOdds(hand, iterationCount):
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suits = ['s', 'd', 'c', 'h']
    cards = []
    win = 0
    loss = 0
    draw = 0

    for value in values:
        for suit in suits:
            cards.append(value + suit)

    random.shuffle(cards)

    cards.remove(hand[0])
    cards.remove(hand[1])

    for iteration in range(iterationCount):
        oppCard1 = random.choice(cards)
        cards.remove(oppCard1)
        oppCard2 = random.choice(cards)
        cards.remove(oppCard2)
        tableCards = random.choices(cards, k=5)

        bestHand1 = getBestHand(tableCards + hand)
        bestHand2 = getBestHand(tableCards + [oppCard1, oppCard2])
        comp = compareHands(bestHand1, bestHand2)
        if comp == 1:
            win += 1
        elif comp == -1:
            loss += 1
        else:
            draw += 1

        cards.append(oppCard1)
        cards.append(oppCard2)

    return [win / iterationCount, loss / iterationCount, draw / iterationCount]


h1 = ["2s", "7h"]
h2 = ["Qs", "Kh"]
h3 = ["Ac", "2h", "5s", "4d", "3h"]
h4 = ["Ah", "Th", "Jh", "2h", "7h"]

ranks = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
suits = ['h', 'd', 'c', 's']

hands = [[rank1 + suit1, rank2 + suit2] for rank1 in ranks for suit1 in suits for rank2 in ranks for suit2 in suits if rank1 != rank2 or (rank1 == rank2 and suit1 != suit2)]

# file = open("pokerOddsPreflop", "w")

'''for hand in hands:
    val = calculateOdds(hand, 10000)[0]
    file.write(hand[0][0] + hand[0][1].upper() + " " + hand[1][0] + hand[1][1].upper() + " " + str(val) + "\n")
    print(hand)

calculateEquity(h1, 10000)'''

file = open("pokerOddsPreflop", "r+")

d = dict()

for line in file.readlines():
    line = line.split()
    cards = [line[0]] + [line[1]]
    cards = sorted(cards)
    d[cards[0] + " " + cards[1]] = line[2]

for key in d.keys():
    print(key, d[key])

