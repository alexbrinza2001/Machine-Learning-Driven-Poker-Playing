import random
from PokerEvaluator import PokerEvaluator

class AveragePokerPlayer:
    def __init__(self):
        self.evaluator = PokerEvaluator()
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

