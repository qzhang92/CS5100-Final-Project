import sys
import random

import cards
import player

HUMAN_ID = 3

def main(argv):
    # Create all players. Player 3 will be human
    players = []
    for i in range(1, 4):
        players.append(player.Player(i))

    #Initiate deck
    deck = cards.Deck()
    
    # Deal the cards
    handle_deal(players, deck)

    # Get the landlord
    landlord = handle_landlord(players, deck)

    # Game play
    game_play(players, landlord)

def handle_deal(players, deck):
    index = 0
    for i in range(51):
        card = deck.deal_card()
        players[index].add_card(card)
        index += 1
        index = index % 3
    
    for player in players:
        player.hand.sort_card()
        print(player.hand)
        

def handle_landlord(players, deck):
    cur = random.randomint(0, 2)
    index = 0
    while index < 3:
        index += 1
        is_landlord = players[cur].landlord_choice(index)
        if is_landlord:
            players[cur].set_landlord(start + 1)
            for i in range(3):  #landlord will get 3 extra cards
                card = deck.deal_card()
                players[cur].add_card(card)
            return cur
        start +=1
        cur = cur % 3

def game_play(players, landlord):
    pass
    

if __name__ == '__main__':
    main(sys.argv)