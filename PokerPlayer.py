import random

from PokerGame import PokerGame
from PokerEvaluator import PokerEvaluator

class PokerPlayer:
    def __init__(self):
        self.game = PokerGame()
        self.evaluator = PokerEvaluator()
        self.file = open("cfr_results", "w")
        self.ownHand = []
        self.oppHand = []
        self.board = []
        self.testDict = dict()

        self.testDict[1] = dict()
        self.testDict[1][1] = dict()
        self.testDict[1][1][1] = dict()

        self.equityPreFlop = dict()

        file = open("pokerOddsPreflop", "r+")

        for line in file.readlines():
            line = line.split()
            cards = [line[0]] + [line[1]]
            cards = sorted(cards)
            self.equityPreFlop[cards[0] + " " + cards[1]] = float(line[2])

        self.prob = {
            'PreFlop': {
                '40 and lower': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                '40-45': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                '45-50': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                '50-60': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                '60+': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                }

            },
            'Flop': {
                'High Card': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'OverPair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Pocket Pair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Top Pair Top Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Top Pair Low Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Middle Pair Top Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Middle Pair Low Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Low Pair Top Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Low Pair Low Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Two Pair Top Two': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Two Pair Top One': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Two Pair Two Low': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Top Set': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Middle Set': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Low Set': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Straight OverCard': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Straight Middle Card': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Straight Lower Card': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Flush With 2 Overs': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Flush With 1 Over': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Flush': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'High Full House High Pair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'High Full House Low Pair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Low Full House High Pair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Low Full House Low Pair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Four Of A Kind': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Straight Flush': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Royal Flush': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                }

            },
            'Turn': {
                'High Card': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'OverPair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Pocket Pair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Top Pair Top Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Top Pair Low Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Middle Pair Top Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Middle Pair Low Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Low Pair Top Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Low Pair Low Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Two Pair Top Two': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Two Pair Top One': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Two Pair Two Low': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Top Set': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Middle Set': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Low Set': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Straight OverCard': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Straight Middle Card': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Straight Lower Card': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Flush With 2 Overs': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Flush With 1 Over': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Flush': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'High Full House High Pair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'High Full House Low Pair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Low Full House High Pair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Low Full House Low Pair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Four Of A Kind': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Straight Flush': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Royal Flush': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                }
            },
            'River': {
                'High Card': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'OverPair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Pocket Pair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Top Pair Top Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Top Pair Low Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Middle Pair Top Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Middle Pair Low Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Low Pair Top Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Low Pair Low Kicker': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Two Pair Top Two': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Two Pair Top One': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Two Pair Two Low': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Top Set': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Middle Set': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Low Set': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Straight OverCard': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Straight Middle Card': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Straight Lower Card': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Flush With 2 Overs': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Flush With 1 Over': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Flush': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'High Full House High Pair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'High Full House Low Pair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Low Full House High Pair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Low Full House Low Pair': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Four Of A Kind': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Straight Flush': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                },
                'Royal Flush': {
                    'Check': {
                        'Check': 20,
                        'Bet 1/3': 20,
                        'Bet 2/3': 20,
                        'Bet Pot': 20,
                        'All In': 20
                    },
                    'Bet 1/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet 2/3': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'Bet Pot': {
                        'Call': 50,
                        'Fold': 50
                    },
                    'All In': {
                        'Call': 50,
                        'Fold': 50
                    }
                }

            }

        }

    def getHandName(self, hand):

        while hand[-1] in ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]:
            hand = hand[:-2]

        hand = hand.strip()

        return hand

    def play(self, cards, oppCards, board, handStage, firstToAct, lastAction, player, history, money, pot):

        if handStage == "PreFlop":
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

            if firstToAct == 1:
                probs = self.prob["PreFlop"][eqGroup]["Check"]
                history = "PreFlop action: "

                for action in probs.keys():
                    if action == "Check":
                        self.play(oppCards, cards, board, "PreFlop", 0, action, 3 - player, history + "Player " + str(player) + " " + action + " ", money, pot)
                    else:
                        bet = 0
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = money

                        self.play(oppCards, cards, board, "PreFlop", 0, action, 3 - player, history + "Player " + str(player) + " " + action + " ", money - bet, pot + bet)

            elif lastAction == "All In":
                probs = self.prob["PreFlop"][eqGroup]["All In"]

                for action in probs.keys():
                    if action == "Call":

                        comp = self.evaluator.compareHands(cards, oppCards, board)

                        if comp == 1:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Player " + str(player) + " wins 1000")
                        elif comp == -1:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Player " + str(3 - player) + " wins 1000")
                        else:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Draw")

                    else:
                        print(history + "Player " + str(player) + " " + action + " Player " + str(3 - player) + " wins " + str(pot))


            else:
                probs = self.prob["PreFlop"][eqGroup][lastAction]

                for action in probs.keys():
                    if action == "Fold":
                        print(history + "Player " + str(player) + " " + action + " Player " + str(3 - player) + " wins " + str(pot))
                    elif action == "Call":
                        self.play(oppCards, cards, board, "Flop", 1, action, 3 - player, history + "Player " + str(player) + " " + action + " ", money, 2 * (500 - money))

                    elif "Bet" in action or action == "All In":

                        bet = 0
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = money

                        self.play(oppCards, cards, board, "PreFlop", 0, action, 3 - player, history + "Player " + str(player) + " " + action + " ", money - bet, pot + bet)
                    else:
                        self.play(oppCards, cards, board, "Flop", 1, action, 3 - player, history + "Player " + str(player) + " " + action + " ", money, pot)

        elif handStage == "Flop":

            hand = self.evaluator.handEvaluation(cards, board[:3])
            hand = self.getHandName(hand[0])

            if firstToAct == 1:
                probs = self.prob["Flop"][hand]["Check"]
                history = history + " Flop action: "

                for action in probs.keys():

                    if action == "Check":
                        self.play(oppCards, cards, board, "Flop", 0, action, 3 - player, history + "Player " + str(player) + " " + action + " ", money, pot)
                    else:
                        bet = 0
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = money

                        self.play(oppCards, cards, board, "Flop", 0, action, 3 - player,history + "Player " + str(player) + " " + action + " ", money - bet, pot + bet)

            elif lastAction == "All In":
                probs = self.prob["Flop"][hand]["All In"]

                for action in probs.keys():
                    if action == "Call":
                        comp = self.evaluator.compareHands(cards, oppCards, board)

                        if comp == 1:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Player " + str(player) + " wins 1000")
                        elif comp == -1:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Player " + str(3 - player) + " wins 1000")
                        else:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Draw")

                    else:
                        print(history + "Player " + str(player) + " " + action + " Player " + str(3 - player) + " wins " + str(pot))

            else:

                probs = self.prob["Flop"][hand][lastAction]

                for action in probs.keys():
                    if action == "Fold":
                        print(history + "Player " + str(player) + " " + action + " Player " + str(3 - player) + " wins " + str(pot))
                    elif action == "Call":
                        self.play(oppCards, cards, board, "Turn", 1, action, 3 - player, history + "Player " + str(player) + " " + action + " ", money, 2 * (500 - money))

                    elif "Bet" in action or action == "All In":

                        bet = 0
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = money

                        self.play(oppCards, cards, board, "Flop", 0, action, 3 - player, history + "Player " + str(player) + " " + action + " ", money - bet, pot + bet)
                    else:
                        self.play(oppCards, cards, board, "Turn", 1, action, 3 - player, history + "Player " + str(player) + " " + action + " ", money, pot)

        elif handStage == "Turn":

            hand = self.evaluator.handEvaluation(cards, board[:4])
            hand = self.getHandName(hand[0])

            if firstToAct == 1:
                probs = self.prob["Turn"][hand]["Check"]

                history = history + " Turn action: "

                for action in probs.keys():

                    if action == "Check":
                        self.play(oppCards, cards, board, "Turn", 0, action, 3 - player, history + "Player " + str(player) + " " + action + " ", money, pot)
                    else:
                        bet = 0
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = money

                        self.play(oppCards, cards, board, "Turn", 0, action, 3 - player,history + "Player " + str(player) + " " + action + " ", money - bet, pot + bet)

            elif lastAction == "All In":
                probs = self.prob["Turn"][hand]["All In"]

                for action in probs.keys():
                    if action == "Call":
                        comp = self.evaluator.compareHands(cards, oppCards, board)

                        if comp == 1:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Player " + str(player) + " wins 1000")
                        elif comp == -1:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Player " + str(3 - player) + " wins 1000")
                        else:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Draw")

                    else:
                        print(history + "Player " + str(player) + " " + action + " Player " + str(3 - player) + " wins " + str(pot))

            else:
                probs = self.prob["Turn"][hand][lastAction]

                for action in probs.keys():
                    if action == "Fold":
                        print(history + "Player " + str(player) + " " + action + " Player " + str(3 - player) + " wins " + str(pot))
                    elif action == "Call":
                        self.play(oppCards, cards, board, "River", 1, action, 3 - player, history + "Player " + str(player) + " " + action + " ", money, 2 * (500 - money))

                    elif "Bet" in action or action == "All In":

                        bet = 0
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = money

                        self.play(oppCards, cards, board, "Turn", 0, action, 3 - player, history + "Player " + str(player) + " " + action + " ", money - bet, pot + bet)
                    else:
                        self.play(oppCards, cards, board, "River", 1, action, 3 - player, history + "Player " + str(player) + " " + action + " ", money, pot)

        elif handStage == "River":
            hand = self.evaluator.handEvaluation(cards, board)
            hand = self.getHandName(hand[0])

            if firstToAct == 1:
                probs = self.prob["River"][hand]["Check"]

                history = history + " River action: "

                for action in probs.keys():

                    if action == "Check":
                        self.play(oppCards, cards, board, "River", 0, action, 3 - player, history + "Player " + str(player) + " " + action + " ", money, pot)
                    else:
                        bet = 0
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = money

                        self.play(oppCards, cards, board, "River", 0, action, 3 - player,history + "Player " + str(player) + " " + action + " ", money - bet, pot + bet)

            elif lastAction == "All In":
                probs = self.prob["River"][hand]["All In"]

                for action in probs.keys():
                    if action == "Call":
                        comp = self.evaluator.compareHands(cards, oppCards, board)

                        if comp == 1:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Player " + str(player) + " wins 1000")
                        elif comp == -1:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Player " + str(3 - player) + " wins 1000")
                        else:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Draw")

                    else:
                        print(history + "Player " + str(player) + " " + action + " Player " + str(3 - player) + " wins " + str(pot))

            else:
                probs = self.prob["River"][hand][lastAction]

                for action in probs.keys():
                    if action == "Fold":
                        print(history + "Player " + str(player) + " " + action + " Player " + str(3 - player) + " wins " + str(pot))
                    elif action == "Call":
                        comp = self.evaluator.compareHands(cards, oppCards, board)

                        if comp == 1:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Player " + str(player) + " wins " + str(1000 - 2 * money))
                        elif comp == -1:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Player " + str(3 - player) + " wins " + str(1000 - 2 * money))
                        else:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Draw")

                    elif "Bet" in action or action == "All In":

                        bet = 0
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = money

                        self.play(oppCards, cards, board, "River", 0, action, 3 - player, history + "Player " + str(player) + " " + action + " ", money - bet, pot + bet)
                    else:
                        comp = self.evaluator.compareHands(cards, oppCards, board)

                        if comp == 1:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Player " + str(player) + " wins " + str(1000 - 2 * money))
                        elif comp == -1:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Player " + str(3 - player) + " wins " + str(1000 - 2 * money))
                        else:
                            print(history + "Player " + str(player) + " " + action + " Showdown: Draw")


    def oppPlay(self, stage, lastAction):

        probs = dict()

        if stage == "PreFlop":
            stringHand = self.oppHand[0] + " " + self.oppHand[1]
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
            hand = self.evaluator.handEvaluation(self.oppHand, self.board[:3])
            hand = self.getHandName(hand[0])
            probs = self.prob[stage][hand][lastAction]
        elif stage == "Turn":
            hand = self.evaluator.handEvaluation(self.oppHand, self.board[:4])
            hand = self.getHandName(hand[0])
            probs = self.prob[stage][hand][lastAction]
        elif stage == "River":
            hand = self.evaluator.handEvaluation(self.oppHand, self.board)
            hand = self.getHandName(hand[0])
            probs = self.prob[stage][hand][lastAction]

        actions = []
        probList = []

        for act in probs.keys():
            actions.append(act)
            probList.append(probs[act])

        action = random.choices(actions, weights=probList, k=1)

        return action[0]

# -----------------------------------------------------------------------------------------------------------

    def playHand(self, stage, lastAction, moneyBet):

        rewards = []
        field1 = []
        field2 = []
        field3 = []
        field4 = []

        if stage == "PreFlop":

            stringHand = self.ownHand[0] + " " + self.ownHand[1]
            eq = self.equityPreFlop[stringHand]
            eqGroup = ""

            eq = eq * 100

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

            if lastAction == "Nothing":
                probs = self.prob["PreFlop"][eqGroup]["Check"]

                for action in probs.keys():
                    if action == "Check":
                        oppAction = self.oppPlay("PreFlop", "Check")

                        if oppAction == "Check":
                            val = self.playHand("Flop", "Nothing", moneyBet)
                            rewards.append(val)
                            field1.append("PreFlop")
                            field2.append(eqGroup)
                            field3.append("Check")
                            field4.append("Check")
                        else:
                            val = self.playHand("PreFlop", oppAction, moneyBet)
                            rewards.append(val)
                            field1.append("PreFlop")
                            field2.append(eqGroup)
                            field3.append("Check")
                            field4.append("Check")
                    else:
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        oppAction = self.oppPlay("PreFlop", action)

                        if oppAction == "Call":
                            if action != "All In":
                                val = self.playHand("Flop", "Nothing", moneyBet + bet)
                                rewards.append(val)
                                field1.append("PreFlop")
                                field2.append(eqGroup)
                                field3.append("Check")
                                field4.append(action)
                            else:
                                comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                if comp == 1:
                                    rewards.append(500)
                                    field1.append("PreFlop")
                                    field2.append(eqGroup)
                                    field3.append("Check")
                                    field4.append(action)
                                elif comp == -1:
                                    rewards.append(-500)
                                    field1.append("PreFlop")
                                    field2.append(eqGroup)
                                    field3.append("Check")
                                    field4.append(action)
                                else:
                                    rewards.append(0)
                                    field1.append("PreFlop")
                                    field2.append(eqGroup)
                                    field3.append("Check")
                                    field4.append(action)
                        elif oppAction == "Fold":
                            rewards.append(moneyBet)
                            field1.append("PreFlop")
                            field2.append(eqGroup)
                            field3.append("Check")
                            field4.append(action)

            elif lastAction == "Check":
                probs = self.prob["PreFlop"][eqGroup]["Check"]

                for action in probs.keys():
                    if action == "Check":
                        val = self.playHand("Flop", "Nothing", moneyBet)
                        rewards.append(val)
                        field1.append("PreFlop")
                        field2.append(eqGroup)
                        field3.append("Check")
                        field4.append(action)
                    else:
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        oppAction = self.oppPlay("PreFlop", action)

                        if oppAction == "Call":
                            if action != "All In":
                                val = self.playHand("Flop", "Nothing", moneyBet + bet)
                                rewards.append(val)
                                field1.append("PreFlop")
                                field2.append(eqGroup)
                                field3.append("Check")
                                field4.append(action)
                            else:
                                comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                if comp == 1:
                                    rewards.append(500)
                                    field1.append("PreFlop")
                                    field2.append(eqGroup)
                                    field3.append("Check")
                                    field4.append(action)
                                elif comp == -1:
                                    rewards.append(-500)
                                    field1.append("PreFlop")
                                    field2.append(eqGroup)
                                    field3.append("Check")
                                    field4.append(action)
                                else:
                                    rewards.append(0)
                                    field1.append("PreFlop")
                                    field2.append(eqGroup)
                                    field3.append("Check")
                                    field4.append(action)
                        elif oppAction == "Fold":
                            rewards.append(moneyBet)
                            field1.append("PreFlop")
                            field2.append(eqGroup)
                            field3.append("Check")
                            field4.append(action)
            else:
                probs = self.prob["PreFlop"][eqGroup][lastAction]

                for action in probs.keys():
                    if action == "Call":
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        if action != "All In":
                            val = self.playHand("Flop", "Nothing", moneyBet + bet)
                            rewards.append(val)
                            field1.append("PreFlop")
                            field2.append(eqGroup)
                            field3.append(lastAction)
                            field4.append(action)
                        else:
                            comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                            if comp == 1:
                                rewards.append(500)
                                field1.append("PreFlop")
                                field2.append(eqGroup)
                                field3.append(lastAction)
                                field4.append(action)
                            elif comp == -1:
                                rewards.append(-500)
                                field1.append("PreFlop")
                                field2.append(eqGroup)
                                field3.append(lastAction)
                                field4.append(action)
                            else:
                                rewards.append(0)
                                field1.append("PreFlop")
                                field2.append(eqGroup)
                                field3.append(lastAction)
                                field4.append(action)
                    elif action == "Fold":
                        rewards.append(-moneyBet)
                        field1.append("PreFlop")
                        field2.append(eqGroup)
                        field3.append(lastAction)
                        field4.append(action)

        elif stage == "Flop":
            hand = self.evaluator.handEvaluation(self.ownHand, self.board[:3])
            hand = self.getHandName(hand[0])

            if lastAction == "Nothing":
                probs = self.prob["Flop"][hand]["Check"]

                for action in probs.keys():

                    if action == "Check":
                        oppAction = self.oppPlay("Flop", "Check")

                        if oppAction == "Check":
                            val = self.playHand("Turn", "Nothing", moneyBet)
                            rewards.append(val)
                            field1.append("Flop")
                            field2.append(hand)
                            field3.append("Check")
                            field4.append(action)
                        else:
                            val = self.playHand("Flop", oppAction, moneyBet)
                            rewards.append(val)
                            field1.append("Flop")
                            field2.append(hand)
                            field3.append("Check")
                            field4.append(action)

                    else:
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        oppAction = self.oppPlay("Flop", action)

                        if oppAction == "Call":
                            if action != "All In":
                                val = self.playHand("Turn", "Nothing", moneyBet + bet)
                                rewards.append(val)
                                field1.append("Flop")
                                field2.append(hand)
                                field3.append("Check")
                                field4.append(action)
                            else:
                                comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                if comp == 1:
                                    rewards.append(500)
                                    field1.append("Flop")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                                elif comp == -1:
                                    rewards.append(-500)
                                    field1.append("Flop")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                                else:
                                    rewards.append(0)
                                    field1.append("Flop")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                        elif oppAction == "Fold":
                            rewards.append(moneyBet)
                            field1.append("Flop")
                            field2.append(hand)
                            field3.append("Check")
                            field4.append(action)

            elif lastAction == "Check":
                probs = self.prob["Flop"][hand]["Check"]

                for action in probs.keys():
                    if action == "Check":
                        val = self.playHand("Turn", "Nothing", moneyBet)
                        rewards.append(val)
                        field1.append("Flop")
                        field2.append(hand)
                        field3.append("Check")
                        field4.append(action)
                    else:
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        oppAction = self.oppPlay("Flop", action)

                        if oppAction == "Call":
                            if action != "All In":
                                val = self.playHand("Turn", "Nothing", moneyBet + bet)
                                rewards.append(val)
                                field1.append("Flop")
                                field2.append(hand)
                                field3.append("Check")
                                field4.append(action)
                            else:
                                comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                if comp == 1:
                                    rewards.append(500)
                                    field1.append("Flop")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                                elif comp == -1:
                                    rewards.append(-500)
                                    field1.append("Flop")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                                else:
                                    rewards.append(0)
                                    field1.append("Flop")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                        elif oppAction == "Fold":
                            rewards.append(moneyBet)
                            field1.append("Flop")
                            field2.append(hand)
                            field3.append("Check")
                            field4.append(action)
            else:
                probs = self.prob["Flop"][hand][lastAction]

                for action in probs.keys():
                    if action == "Call":
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        if action != "All In":
                            val = self.playHand("Turn", "Nothing", moneyBet + bet)
                            rewards.append(val)
                            field1.append("Flop")
                            field2.append(hand)
                            field3.append(lastAction)
                            field4.append(action)
                        else:
                            comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                            if comp == 1:
                                rewards.append(500)
                                field1.append("Flop")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                            elif comp == -1:
                                rewards.append(-500)
                                field1.append("Flop")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                            else:
                                rewards.append(0)
                                field1.append("Flop")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                    elif action == "Fold":
                        rewards.append(-moneyBet)
                        field1.append("Flop")
                        field2.append(hand)
                        field3.append(lastAction)
                        field4.append(action)

        elif stage == "Turn":
            hand = self.evaluator.handEvaluation(self.ownHand, self.board[:3])
            hand = self.getHandName(hand[0])

            if lastAction == "Nothing":
                probs = self.prob["Turn"][hand]["Check"]

                for action in probs.keys():

                    if action == "Check":
                        oppAction = self.oppPlay("Turn", "Check")

                        if oppAction == "Check":
                            val = self.playHand("River", "Nothing", moneyBet)
                            rewards.append(val)
                            field1.append("Turn")
                            field2.append(hand)
                            field3.append("Check")
                            field4.append(action)
                        else:
                            val = self.playHand("Turn", oppAction, moneyBet)
                            rewards.append(val)
                            field1.append("Turn")
                            field2.append(hand)
                            field3.append("Check")
                            field4.append(action)

                    else:
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        oppAction = self.oppPlay("Turn", action)

                        if oppAction == "Call":
                            if action != "All In":
                                val = self.playHand("River", "Nothing", moneyBet + bet)
                                rewards.append(val)
                                field1.append("Turn")
                                field2.append(hand)
                                field3.append("Check")
                                field4.append(action)
                            else:
                                comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                if comp == 1:
                                    rewards.append(500)
                                    field1.append("Turn")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                                elif comp == -1:
                                    rewards.append(-500)
                                    field1.append("Turn")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                                else:
                                    rewards.append(0)
                                    field1.append("Turn")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                        elif oppAction == "Fold":
                            rewards.append(moneyBet)
                            field1.append("Turn")
                            field2.append(hand)
                            field3.append("Check")
                            field4.append(action)

            elif lastAction == "Check":
                probs = self.prob["Turn"][hand]["Check"]

                for action in probs.keys():
                    if action == "Check":
                        val = self.playHand("River", "Nothing", moneyBet)
                        rewards.append(val)
                        field1.append("Turn")
                        field2.append(hand)
                        field3.append("Check")
                        field4.append(action)
                    else:
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        oppAction = self.oppPlay("Turn", action)

                        if oppAction == "Call":
                            if action != "All In":
                                val = self.playHand("River", "Nothing", moneyBet + bet)
                                rewards.append(val)
                                field1.append("Turn")
                                field2.append(hand)
                                field3.append("Check")
                                field4.append(action)
                            else:
                                comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                if comp == 1:
                                    rewards.append(500)
                                    field1.append("Turn")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                                elif comp == -1:
                                    rewards.append(-500)
                                    field1.append("Turn")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                                else:
                                    rewards.append(0)
                                    field1.append("Turn")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                        elif oppAction == "Fold":
                            rewards.append(moneyBet)
                            field1.append("Turn")
                            field2.append(hand)
                            field3.append("Check")
                            field4.append(action)
            else:
                probs = self.prob["Turn"][hand][lastAction]

                for action in probs.keys():
                    if action == "Call":
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        if action != "All In":
                            val = self.playHand("River", "Nothing", moneyBet + bet)
                            rewards.append(val)
                            field1.append("Turn")
                            field2.append(hand)
                            field3.append(lastAction)
                            field4.append(action)
                        else:
                            comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                            if comp == 1:
                                rewards.append(500)
                                field1.append("Turn")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                            elif comp == -1:
                                rewards.append(-500)
                                field1.append("Turn")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                            else:
                                rewards.append(0)
                                field1.append("Turn")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                    elif action == "Fold":
                        rewards.append(-moneyBet)
                        field1.append("Turn")
                        field2.append(hand)
                        field3.append(lastAction)
                        field4.append(action)

        elif stage == "River":
            hand = self.evaluator.handEvaluation(self.ownHand, self.board[:3])
            hand = self.getHandName(hand[0])

            if lastAction == "Nothing":
                probs = self.prob["River"][hand]["Check"]

                for action in probs.keys():

                    if action == "Check":
                        oppAction = self.oppPlay("River", "Check")

                        if oppAction == "Check":
                            comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                            if comp == 1:
                                rewards.append(moneyBet)
                                field1.append("River")
                                field2.append(hand)
                                field3.append("Check")
                                field4.append(action)
                            elif comp == -1:
                                rewards.append(-moneyBet)
                                field1.append("River")
                                field2.append(hand)
                                field3.append("Check")
                                field4.append(action)
                            else:
                                rewards.append(0)
                                field1.append("River")
                                field2.append(hand)
                                field3.append("Check")
                                field4.append(action)

                        else:
                            val = self.playHand("River", oppAction, moneyBet)
                            rewards.append(val)
                            field1.append("River")
                            field2.append(hand)
                            field3.append("Check")
                            field4.append(action)

                    else:
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        oppAction = self.oppPlay("River", action)

                        if oppAction == "Call":
                            if action != "All In":
                                comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                if comp == 1:
                                    rewards.append(moneyBet)
                                    field1.append("River")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                                elif comp == -1:
                                    rewards.append(-moneyBet)
                                    field1.append("River")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                                else:
                                    rewards.append(0)
                                    field1.append("River")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                            else:
                                comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                if comp == 1:
                                    rewards.append(500)
                                    field1.append("River")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                                elif comp == -1:
                                    rewards.append(-500)
                                    field1.append("River")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                                else:
                                    rewards.append(0)
                                    field1.append("River")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                        elif oppAction == "Fold":
                            rewards.append(moneyBet)
                            field1.append("River")
                            field2.append(hand)
                            field3.append("Check")
                            field4.append(action)

            elif lastAction == "Check":
                probs = self.prob["River"][hand]["Check"]

                for action in probs.keys():
                    if action == "Check":
                        comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                        if comp == 1:
                            rewards.append(moneyBet)
                            field1.append("River")
                            field2.append(hand)
                            field3.append("Check")
                            field4.append(action)
                        elif comp == -1:
                            rewards.append(-moneyBet)
                            field1.append("River")
                            field2.append(hand)
                            field3.append("Check")
                            field4.append(action)
                        else:
                            rewards.append(0)
                            field1.append("River")
                            field2.append(hand)
                            field3.append("Check")
                            field4.append(action)
                    else:
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        oppAction = self.oppPlay("River", action)

                        if oppAction == "Call":
                            if action != "All In":
                                comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                if comp == 1:
                                    rewards.append(moneyBet)
                                    field1.append("River")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                                elif comp == -1:
                                    rewards.append(-moneyBet)
                                    field1.append("River")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                                else:
                                    rewards.append(0)
                                    field1.append("River")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                            else:
                                comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                if comp == 1:
                                    rewards.append(500)
                                    field1.append("River")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                                elif comp == -1:
                                    rewards.append(-500)
                                    field1.append("River")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                                else:
                                    rewards.append(0)
                                    field1.append("River")
                                    field2.append(hand)
                                    field3.append("Check")
                                    field4.append(action)
                        elif oppAction == "Fold":
                            rewards.append(moneyBet)
                            field1.append("River")
                            field2.append(hand)
                            field3.append("Check")
                            field4.append(action)
            else:
                probs = self.prob["River"][hand][lastAction]

                for action in probs.keys():
                    if action == "Call":
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        if action != "All In":
                            comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                            if comp == 1:
                                rewards.append(moneyBet)
                                field1.append("River")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                            elif comp == -1:
                                rewards.append(-moneyBet)
                                field1.append("River")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                            else:
                                rewards.append(0)
                                field1.append("River")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                        else:
                            comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                            if comp == 1:
                                rewards.append(500)
                                field1.append("River")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                            elif comp == -1:
                                rewards.append(-500)
                                field1.append("River")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                            else:
                                rewards.append(0)
                                field1.append("River")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                    elif action == "Fold":
                        rewards.append(-moneyBet)
                        field1.append("River")
                        field2.append(hand)
                        field3.append(lastAction)
                        field4.append(action)

        reward = self.eval2(rewards, field1, field2, field3, field4)

        return reward

    # --------------------------------------------PLAY HAND V2------------------------------------------------

    def oppPlayV2(self, stage, lastAction):

        probs = dict()

        if stage == "PreFlop":
            stringHand = self.oppHand[0] + " " + self.oppHand[1]
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
            hand = self.evaluator.handEvaluation(self.oppHand, self.board[:3])
            hand = self.getHandName(hand[0])
            probs = self.prob[stage][hand][lastAction]
        elif stage == "Turn":
            hand = self.evaluator.handEvaluation(self.oppHand, self.board[:4])
            hand = self.getHandName(hand[0])
            probs = self.prob[stage][hand][lastAction]
        elif stage == "River":
            hand = self.evaluator.handEvaluation(self.oppHand, self.board)
            hand = self.getHandName(hand[0])
            probs = self.prob[stage][hand][lastAction]

        actions = []
        probList = []

        for act in probs.keys():
            actions.append(act)
            probList.append(probs[act])

        # print(actions)

        return actions, probList

    def playHandV2(self, stage, lastAction, moneyBet):

        rewards = []
        field1 = []
        field2 = []
        field3 = []
        field4 = []

        if stage == "PreFlop":

            stringHand = self.ownHand[0] + " " + self.ownHand[1]
            eq = self.equityPreFlop[stringHand]
            eqGroup = ""

            eq = eq * 100

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

            if lastAction == "Nothing":
                probs = self.prob["PreFlop"][eqGroup]["Check"]

                for action in probs.keys():
                    if action == "Check":
                        oppActions, pr = self.oppPlayV2("PreFlop", "Check")
                        val = 0
                        ind = 0

                        for oppAction in oppActions:

                            if oppAction == "Check":
                                val += pr[ind] * self.playHandV2("Flop", "Nothing", moneyBet)
                            else:
                                val += pr[ind] * self.playHandV2("PreFlop", oppAction, moneyBet)

                            ind += 1

                        rewards.append(val)
                        field1.append("PreFlop")
                        field2.append(eqGroup)
                        field3.append("Check")
                        field4.append("Check")

                    else:
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        oppActions, pr = self.oppPlayV2("PreFlop", action)
                        val = 0
                        ind = 0

                        for oppAction in oppActions:

                            if oppAction == "Call":
                                if action != "All In":
                                    val += pr[ind] * self.playHandV2("Flop", "Nothing", moneyBet + bet)
                                else:
                                    comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                    if comp == 1:
                                        val += pr[ind] * 500
                                    elif comp == -1:
                                        val += pr[ind] * (-500)
                                    else:
                                        val += pr[ind] * 0
                            elif oppAction == "Fold":
                                val += pr[ind] * moneyBet

                            ind += 1

                        rewards.append(val)
                        field1.append("PreFlop")
                        field2.append(eqGroup)
                        field3.append("Check")
                        field4.append(action)

            elif lastAction == "Check":
                probs = self.prob["PreFlop"][eqGroup]["Check"]

                for action in probs.keys():
                    if action == "Check":
                        val = self.playHandV2("Flop", "Nothing", moneyBet)
                        rewards.append(val)
                        field1.append("PreFlop")
                        field2.append(eqGroup)
                        field3.append("Check")
                        field4.append(action)
                    else:
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        oppActions, pr = self.oppPlayV2("PreFlop", action)
                        val = 0
                        ind = 0

                        for oppAction in oppActions:

                            if oppAction == "Call":
                                if action != "All In":
                                    val += pr[ind] * self.playHandV2("Flop", "Nothing", moneyBet + bet)
                                else:
                                    comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                    if comp == 1:
                                        val += pr[ind] * 500
                                    elif comp == -1:
                                        val += pr[ind] * (-500)
                                    else:
                                        val += pr[ind] * 0
                            elif oppAction == "Fold":
                                val += pr[ind] * moneyBet

                            ind += 1

                        rewards.append(val)
                        field1.append("PreFlop")
                        field2.append(eqGroup)
                        field3.append("Check")
                        field4.append(action)

            else:
                probs = self.prob["PreFlop"][eqGroup][lastAction]

                for action in probs.keys():
                    if action == "Call":
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        if action != "All In":
                            val = self.playHandV2("Flop", "Nothing", moneyBet + bet)
                            rewards.append(val)
                            field1.append("PreFlop")
                            field2.append(eqGroup)
                            field3.append(lastAction)
                            field4.append(action)
                        else:
                            comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                            if comp == 1:
                                rewards.append(500)
                                field1.append("PreFlop")
                                field2.append(eqGroup)
                                field3.append(lastAction)
                                field4.append(action)
                            elif comp == -1:
                                rewards.append(-500)
                                field1.append("PreFlop")
                                field2.append(eqGroup)
                                field3.append(lastAction)
                                field4.append(action)
                            else:
                                rewards.append(0)
                                field1.append("PreFlop")
                                field2.append(eqGroup)
                                field3.append(lastAction)
                                field4.append(action)
                    elif action == "Fold":
                        rewards.append(-moneyBet)
                        field1.append("PreFlop")
                        field2.append(eqGroup)
                        field3.append(lastAction)
                        field4.append(action)

        elif stage == "Flop":
            hand = self.evaluator.handEvaluation(self.ownHand, self.board[:3])
            hand = self.getHandName(hand[0])

            if lastAction == "Nothing":
                probs = self.prob["Flop"][hand]["Check"]

                for action in probs.keys():

                    if action == "Check":
                        oppActions, pr = self.oppPlayV2("Flop", "Check")
                        val = 0
                        ind = 0

                        for oppAction in oppActions:

                            if oppAction == "Check":
                                val += pr[ind] * self.playHandV2("Turn", "Nothing", moneyBet)
                            else:
                                val += pr[ind] * self.playHandV2("Flop", oppAction, moneyBet)

                            ind += 1

                        rewards.append(val)
                        field1.append("Flop")
                        field2.append(hand)
                        field3.append("Check")
                        field4.append(action)

                    else:
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        oppActions, pr = self.oppPlayV2("Flop", action)
                        val = 0
                        ind = 0

                        for oppAction in oppActions:

                            if oppAction == "Call":
                                if action != "All In":
                                    val += pr[ind] * self.playHandV2("Turn", "Nothing", moneyBet + bet)
                                else:
                                    comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                    if comp == 1:
                                        val += pr[ind] * 500
                                    elif comp == -1:
                                        val += pr[ind] * (-500)
                                    else:
                                        val += pr[ind] * 0
                            elif oppAction == "Fold":
                                val += pr[ind] * moneyBet

                            ind += 1

                        rewards.append(val)
                        field1.append("Flop")
                        field2.append(hand)
                        field3.append("Check")
                        field4.append(action)

            elif lastAction == "Check":
                probs = self.prob["Flop"][hand]["Check"]

                for action in probs.keys():
                    if action == "Check":
                        val = self.playHandV2("Turn", "Nothing", moneyBet)
                        rewards.append(val)
                        field1.append("Flop")
                        field2.append(hand)
                        field3.append("Check")
                        field4.append(action)
                    else:
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        oppActions, pr = self.oppPlayV2("Flop", action)
                        val = 0
                        ind = 0

                        for oppAction in oppActions:

                            if oppAction == "Call":
                                if action != "All In":
                                    val += pr[ind] * self.playHandV2("Turn", "Nothing", moneyBet + bet)
                                else:
                                    comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                    if comp == 1:
                                        val += pr[ind] * 500
                                    elif comp == -1:
                                        val += pr[ind] * (-500)
                                    else:
                                        val += pr[ind] * 0
                            elif oppAction == "Fold":
                                val += pr[ind] * moneyBet

                            ind += 1

                        rewards.append(val)
                        field1.append("Flop")
                        field2.append(hand)
                        field3.append("Check")
                        field4.append(action)

            else:
                probs = self.prob["Flop"][hand][lastAction]

                for action in probs.keys():
                    if action == "Call":
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        if action != "All In":
                            val = self.playHandV2("Turn", "Nothing", moneyBet + bet)
                            rewards.append(val)
                            field1.append("Flop")
                            field2.append(hand)
                            field3.append(lastAction)
                            field4.append(action)
                        else:
                            comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                            if comp == 1:
                                rewards.append(500)
                                field1.append("Flop")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                            elif comp == -1:
                                rewards.append(-500)
                                field1.append("Flop")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                            else:
                                rewards.append(0)
                                field1.append("Flop")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                    elif action == "Fold":
                        rewards.append(-moneyBet)
                        field1.append("Flop")
                        field2.append(hand)
                        field3.append(lastAction)
                        field4.append(action)

        elif stage == "Turn":
            hand = self.evaluator.handEvaluation(self.ownHand, self.board[:3])
            hand = self.getHandName(hand[0])

            if lastAction == "Nothing":
                probs = self.prob["Turn"][hand]["Check"]

                for action in probs.keys():

                    if action == "Check":
                        oppActions, pr = self.oppPlayV2("Turn", "Check")
                        val = 0
                        ind = 0

                        for oppAction in oppActions:

                            if oppAction == "Check":
                                val += pr[ind] * self.playHandV2("River", "Nothing", moneyBet)
                            else:
                                val += pr[ind] * self.playHandV2("Turn", oppAction, moneyBet)

                            ind += 1

                        rewards.append(val)
                        field1.append("Turn")
                        field2.append(hand)
                        field3.append("Check")
                        field4.append(action)

                    else:
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        oppActions, pr = self.oppPlayV2("Turn", action)
                        val = 0
                        ind = 0

                        for oppAction in oppActions:

                            if oppAction == "Call":
                                if action != "All In":
                                    val += pr[ind] * self.playHandV2("River", "Nothing", moneyBet + bet)
                                else:
                                    comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                    if comp == 1:
                                        val += pr[ind] * 500
                                    elif comp == -1:
                                        val += pr[ind] * (-500)
                                    else:
                                        val += pr[ind] * 0
                            elif oppAction == "Fold":
                                val += pr[ind] * moneyBet

                            ind += 1

                        rewards.append(val)
                        field1.append("Turn")
                        field2.append(hand)
                        field3.append("Check")
                        field4.append(action)

            elif lastAction == "Check":
                probs = self.prob["Turn"][hand]["Check"]

                for action in probs.keys():
                    if action == "Check":
                        val = self.playHandV2("River", "Nothing", moneyBet)
                        rewards.append(val)
                        field1.append("Turn")
                        field2.append(hand)
                        field3.append("Check")
                        field4.append(action)
                    else:
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        oppActions, pr = self.oppPlayV2("Turn", action)
                        val = 0
                        ind = 0

                        for oppAction in oppActions:

                            if oppAction == "Call":
                                if action != "All In":
                                    val += pr[ind] * self.playHandV2("River", "Nothing", moneyBet + bet)
                                else:
                                    comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                    if comp == 1:
                                        val += pr[ind] * 500
                                    elif comp == -1:
                                        val += pr[ind] * (-500)
                                    else:
                                        val += pr[ind] * 0
                            elif oppAction == "Fold":
                                val += pr[ind] * moneyBet

                            ind += 1

                        rewards.append(val)
                        field1.append("Turn")
                        field2.append(hand)
                        field3.append("Check")
                        field4.append(action)

            else:
                probs = self.prob["Turn"][hand][lastAction]

                for action in probs.keys():
                    if action == "Call":
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        if action != "All In":
                            val = self.playHandV2("River", "Nothing", moneyBet + bet)
                            rewards.append(val)
                            field1.append("Turn")
                            field2.append(hand)
                            field3.append(lastAction)
                            field4.append(action)
                        else:
                            comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                            if comp == 1:
                                rewards.append(500)
                                field1.append("Turn")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                            elif comp == -1:
                                rewards.append(-500)
                                field1.append("Turn")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                            else:
                                rewards.append(0)
                                field1.append("Turn")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                    elif action == "Fold":
                        rewards.append(-moneyBet)
                        field1.append("Turn")
                        field2.append(hand)
                        field3.append(lastAction)
                        field4.append(action)

        elif stage == "River":
            hand = self.evaluator.handEvaluation(self.ownHand, self.board[:3])
            hand = self.getHandName(hand[0])

            if lastAction == "Nothing":
                probs = self.prob["River"][hand]["Check"]

                for action in probs.keys():

                    if action == "Check":
                        oppActions, pr = self.oppPlayV2("River", "Check")
                        val = 0
                        ind = 0

                        for oppAction in oppActions:

                            if oppAction == "Check":
                                comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                if comp == 1:
                                    val += pr[ind] * moneyBet
                                elif comp == -1:
                                    val += pr[ind] * (-moneyBet)
                                else:
                                    val += pr[ind] * 0

                            else:
                                val += pr[ind] * self.playHandV2("River", oppAction, moneyBet)

                        rewards.append(val)
                        field1.append("River")
                        field2.append(hand)
                        field3.append("Check")
                        field4.append(action)

                    else:
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        oppActions, pr = self.oppPlayV2("River", action)
                        val = 0
                        ind = 0

                        for oppAction in oppActions:

                            if oppAction == "Call":
                                if action != "All In":
                                    comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                    if comp == 1:
                                        val += pr[ind] * moneyBet
                                    elif comp == -1:
                                        val += pr[ind] * (-moneyBet)
                                    else:
                                        val += pr[ind] * 0
                                else:
                                    comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                    if comp == 1:
                                        val += pr[ind] * 500
                                    elif comp == -1:
                                        val += pr[ind] * (-500)
                                    else:
                                        val += pr[ind] * 0
                            elif oppAction == "Fold":
                                val += pr[ind] * moneyBet

                            ind += 1

                        rewards.append(val)
                        field1.append("River")
                        field2.append(hand)
                        field3.append("Check")
                        field4.append(action)

            elif lastAction == "Check":
                probs = self.prob["River"][hand]["Check"]

                for action in probs.keys():
                    if action == "Check":
                        comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                        if comp == 1:
                            rewards.append(moneyBet)
                            field1.append("River")
                            field2.append(hand)
                            field3.append("Check")
                            field4.append(action)
                        elif comp == -1:
                            rewards.append(-moneyBet)
                            field1.append("River")
                            field2.append(hand)
                            field3.append("Check")
                            field4.append(action)
                        else:
                            rewards.append(0)
                            field1.append("River")
                            field2.append(hand)
                            field3.append("Check")
                            field4.append(action)
                    else:
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        oppActions, pr = self.oppPlayV2("River", action)
                        val = 0
                        ind = 0

                        for oppAction in oppActions:

                            if oppAction == "Call":
                                if action != "All In":
                                    comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                    if comp == 1:
                                        val += pr[ind] * moneyBet
                                    elif comp == -1:
                                        val += pr[ind] * (-moneyBet)
                                    else:
                                        val += pr[ind] * 0
                                else:
                                    comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                                    if comp == 1:
                                        val += pr[ind] * 500
                                    elif comp == -1:
                                        val += pr[ind] * (-500)
                                    else:
                                        val += pr[ind] * 0
                            elif oppAction == "Fold":
                                val += pr[ind] * moneyBet

                            ind += 1

                        rewards.append(val)
                        field1.append("River")
                        field2.append(hand)
                        field3.append("Check")
                        field4.append(action)

            else:
                probs = self.prob["River"][hand][lastAction]

                for action in probs.keys():
                    if action == "Call":
                        bet = 0
                        pot = 2 * moneyBet
                        if action == "Bet 1/3":
                            bet = pot // 3
                        elif action == "Bet 2/3":
                            bet = 2 * pot // 3
                        elif action == "Bet Pot":
                            bet = pot
                        else:
                            bet = 500 - moneyBet

                        if action != "All In":
                            comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                            if comp == 1:
                                rewards.append(moneyBet)
                                field1.append("River")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                            elif comp == -1:
                                rewards.append(-moneyBet)
                                field1.append("River")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                            else:
                                rewards.append(0)
                                field1.append("River")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                        else:
                            comp = self.evaluator.compareHands(self.ownHand, self.oppHand, self.board)

                            if comp == 1:
                                rewards.append(500)
                                field1.append("River")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                            elif comp == -1:
                                rewards.append(-500)
                                field1.append("River")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                            else:
                                rewards.append(0)
                                field1.append("River")
                                field2.append(hand)
                                field3.append(lastAction)
                                field4.append(action)
                    elif action == "Fold":
                        rewards.append(-moneyBet)
                        field1.append("River")
                        field2.append(hand)
                        field3.append(lastAction)
                        field4.append(action)

        # print(rewards, field1, field2, field3, field4)

        reward = self.eval2(rewards, field1, field2, field3, field4)

        return reward

    # -------------------------------EVAL FUNCTIONS---------------------------------------------

    def eval1(self, rewards, field1, field2, field3, field4):
        l = len(rewards)
        overall = 0

        regrets = []
        newProb = []

        regretSum = 0

        for index in range(l):
            p = self.prob[field1[index]][field2[index]][field3[index]][field4[index]] / 100

            overall = overall + p * rewards[index]

        for index in range(l):

            regret = rewards[index] - overall
            regrets.append(regret)

            if regret > 0:
                regretSum += regret

        for index in range(l):

            newP = 0

            if regrets[index] > 0:
                newP = regrets[index] / regretSum

            newProb.append(newP)

        if regretSum == 0:
            for index in range(l):
                newProb[index] = 1 / l

        for index in range(l):
            self.prob[field1[index]][field2[index]][field3[index]][field4[index]] = newProb[index] * 100

        return overall

    def eval2(self, rewards, field1, field2, field3, field4):
        l = len(rewards)
        overall = 0
        regrets = []
        negRegretSum = 0
        posRegretSum = 0
        negRegrets = []
        posRegrets = []
        decProc = []
        incProc = []
        initialProbs = []

        changeRate = 3

        for index in range(l):
            self.prob[field1[index]][field2[index]][field3[index]][field4[index]] = round(self.prob[field1[index]][field2[index]][field3[index]][field4[index]], 4)

        for ind in range(l):
            initialProbs.append(self.prob[field1[ind]][field2[ind]][field3[ind]][field4[ind]])

        for index in range(l):
            if self.prob[field1[index]][field2[index]][field3[index]][field4[index]] > 0:
                changeRate = min(changeRate, min(self.prob[field1[index]][field2[index]][field3[index]][field4[index]], 100 - self.prob[field1[index]][field2[index]][field3[index]][field4[index]]))

        for index in range(l):
            p = self.prob[field1[index]][field2[index]][field3[index]][field4[index]] / 100

            overall = overall + p * rewards[index]

        overall = round(overall, 4)

        for index in range(l):

            if self.prob[field1[index]][field2[index]][field3[index]][field4[index]] > 0:

                regret = rewards[index] - overall
                regret = round(regret, 4)
                regrets.append(regret)

                if regret > 0:
                    posRegrets.append(index)
                    posRegretSum += regret
                elif regret < 0:
                    negRegrets.append(index)
                    negRegretSum += regret
            else:
                regret = rewards[index] - overall
                regret = round(regret, 4)
                regrets.append(regret)

        '''for index in range(l):
            print(self.prob[field1[index]][field2[index]][field3[index]][field4[index]], end = " ")
            
        print(rewards, overall, regrets)'''

        for index in range(l):

            if self.prob[field1[index]][field2[index]][field3[index]][field4[index]] > 0:

                if regrets[index] > 0:
                    if posRegretSum != 0:
                        incProc.append(round(changeRate * regrets[index] / posRegretSum, 4))
                    else:
                        incProc.append(0)
                elif regrets[index] < 0:
                    if negRegretSum != 0:
                        decProc.append(round(changeRate * regrets[index] / negRegretSum, 4))
                    else:
                        decProc.append(0)

        for index in range(len(negRegrets)):
            ind = negRegrets[index]
            self.prob[field1[ind]][field2[ind]][field3[ind]][field4[ind]] -= decProc[index]

        for index in range(len(posRegrets)):
            ind = posRegrets[index]
            self.prob[field1[ind]][field2[ind]][field3[ind]][field4[ind]] += incProc[index]

        for index in range(l):
            self.prob[field1[index]][field2[index]][field3[index]][field4[index]] = round(self.prob[field1[index]][field2[index]][field3[index]][field4[index]], 4)

        ok = 0

        while ok == 0:
            ok = 1
            procSum = 0

            for index in range(l):
                if 0 < self.prob[field1[index]][field2[index]][field3[index]][field4[index]] < 1:
                    procSum += self.prob[field1[index]][field2[index]][field3[index]][field4[index]]
                    self.prob[field1[index]][field2[index]][field3[index]][field4[index]] = 0
                    ok = 0
                elif self.prob[field1[index]][field2[index]][field3[index]][field4[index]] < 0:
                    procSum -= self.prob[field1[index]][field2[index]][field3[index]][field4[index]]
                    self.prob[field1[index]][field2[index]][field3[index]][field4[index]] = 0
                    ok = 0


            procSum = round(procSum, 4)
            rap = 0
            if len(posRegrets) > 0:
                rap = procSum / len(posRegrets)
                rap = round(rap, 4)

            if procSum > 0:
                for index in range(len(posRegrets)):
                    ind = posRegrets[index]
                    self.prob[field1[ind]][field2[ind]][field3[ind]][field4[ind]] += rap

        ok = 0

        for index in range(l):
            if self.prob[field1[index]][field2[index]][field3[index]][field4[index]] >= 100:
                self.prob[field1[index]][field2[index]][field3[index]][field4[index]] = 100
                for ind in range(l):
                    if ind != index:
                        self.prob[field1[ind]][field2[ind]][field3[ind]][field4[ind]] = 0

        for index in range(l):
            self.prob[field1[index]][field2[index]][field3[index]][field4[index]] = round(self.prob[field1[index]][field2[index]][field3[index]][field4[index]], 4)

        '''for index in range(l):
            print(self.prob[field1[index]][field2[index]][field3[index]][field4[index]])'''

        # print("----------------------------------------------------------------------")

        summ = 0

        for index in range(l):
            summ = summ + self.prob[field1[index]][field2[index]][field3[index]][field4[index]]

        if summ < 100:
            diff = 100 - summ
            diff = round(diff, 4)
            # print(diff)

            if diff < 0.001:
                for index in range(l):
                    if self.prob[field1[index]][field2[index]][field3[index]][field4[index]] > 0:
                        self.prob[field1[index]][field2[index]][field3[index]][field4[index]] = round(self.prob[field1[index]][field2[index]][field3[index]][field4[index]] + diff, 4)
                        break

        if summ > 100:
            diff = summ - 100
            diff = round(diff, 4)
            # print(diff)

            if diff < 0.001:
                for index in range(l):
                    if self.prob[field1[index]][field2[index]][field3[index]][field4[index]] > 0:
                        self.prob[field1[index]][field2[index]][field3[index]][field4[index]] = round(self.prob[field1[index]][field2[index]][field3[index]][field4[index]] - diff, 4)
                        break

        summ = 0

        for index in range(l):
            # print(self.prob[field1[index]][field2[index]][field3[index]][field4[index]], summ)
            summ = summ + self.prob[field1[index]][field2[index]][field3[index]][field4[index]]
            summ = round(summ, 4)


        if summ != 100:
            print("NOT 100")
            '''print(summ)
            print(changeRate)
            print(initialProbs)
            print(rewards, field1, field2, field3, field4)
            for ind in range(l):
                print(self.prob[field1[ind]][field2[ind]][field3[ind]][field4[ind]])
            print(overall, regrets)
            print(negRegrets)
            print(posRegrets)
            print(incProc)
            print(decProc)
        print("-----------------------------------------")
        print("NEXT")
        print("-----------------------------------------")'''

        return overall


    def StartHand(self):
        ownMoney = 497
        oppMoney = 497
        pot = 6
        history = ""
        self.game = PokerGame()
        self.ownHand = sorted(self.game.getHand())
        self.oppHand = sorted(self.game.getHand())

        self.board = self.game.getFlop()
        self.board = self.board + self.game.getNextCard()
        self.board = self.board + self.game.getNextCard()

        self.playHandV2("PreFlop", "Nothing", 3)


cfr = PokerPlayer()

'''cfr.testDict[1][1][1][1] = 1
cfr.testDict[1][1][1][2] = 2
cfr.testDict[1][1][1][3] = 2
cfr.testDict[1][1][1][4] = 95

cfr.eval2([-2, -1, 2, 4], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 2, 3, 4])

print(cfr.testDict[1][1][1][1])
print(cfr.testDict[1][1][1][2])
print(cfr.testDict[1][1][1][3])
print(cfr.testDict[1][1][1][4])'''


for index in range(10000):
    print(index)
    cfr.StartHand()

for field1 in cfr.prob.keys():
    for field2 in cfr.prob[field1].keys():
        for field3 in cfr.prob[field1][field2].keys():
            for field4 in cfr.prob[field1][field2][field3].keys():
                cfr.file.write(field1 + "," + field2 + "," + field3 + "," + field4 + "," + str(cfr.prob[field1][field2][field3][field4]) + "\n")
