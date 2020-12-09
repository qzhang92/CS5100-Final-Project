import sys

import cards
import player

HUMAN_ID = 3

def main(argv):
    # Create all players. Player 3 will be human
    players = []
    for i in range(1, 4):
        players.append(player.Player(i))
    
    
    
    #Initiate deck
    deck = cards.deck()
    
    # Deal the cards
    hanlde_deal(players, deck)

    # Get the landlord
    handle_landlord(players, deck)

def handle_deal(players, deck):
    pass

def handle_landlor(players, deck):
    pass
    

if __name__ == '__main__':
    main(sys.argv)