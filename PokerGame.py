import random


class PokerGame:
    def __init__(self):
        self.deck = [card + suit for card in ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'] for suit in ['H', 'D', 'S', 'C']]
        random.shuffle(self.deck)

    def getHand(self):
        hand = random.sample(self.deck, 2)
        self.deck.remove(hand[0])
        self.deck.remove(hand[1])

        return hand

    def getFlop(self):
        flop = random.sample(self.deck, 3)
        self.deck.remove(flop[0])
        self.deck.remove(flop[1])
        self.deck.remove(flop[2])

        return flop

    def getNextCard(self):
        card = random.sample(self.deck, 1)
        self.deck.remove(card[0])

        return card

'''
game = PokerGame()
hnd1 = game.getHand()
hnd2 = game.getHand()
flop = game.getFlop()
turn = game.getNextCard()
river = game.getNextCard()

print(hnd1)
print(hnd2)
print(flop)
print(turn)
print(river)'''