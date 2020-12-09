import Player
import Deck

class manager:
    def __init__(self):
        self.deck = []
        for i in range(4):
            for j in range(13):
                self.deck.append(Card(i + 1, j + 1))
        self.deck.append(Card(BJoker))
        self.deck.append(Card(CJoker))

        self.times = 1

        self.players = []
        self.players.append(You())
        self.players.append(Cpu())
        self.players.append(Cpu())

        self.reserved = []

        self.stack = [Put()]

        self.state = None
        self.landlord = None
        self.winner = None

    def clear(self):
        self.times = 1

        for p in self.players:
            p.clear()

        del self.reserved[:]

        del self.stack[:]
        self.stack.append(Put())

        self.state = None
        self.landlord = None

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        for i in range(3):
            self.players[i].clear()

        n = 0
        for i in range(17):
            for j in range(3):
                self.players[j].add(self.deck[n])
                n += 1
        for i in range(3):
            self.players[i].sort()

        self.reserved.append(Card(self.deck[n].suit, self.deck[n].index))
        n += 1
        self.reserved.append(Card(self.deck[n].suit, self.deck[n].index))
        n += 1
        self.reserved.append(Card(self.deck[n].suit, self.deck[n].index))
        n += 1
        self.reserved.sort()

        assert (n == len(self.deck)), 'Impossible'
