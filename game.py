import sys
import random

import cards
import player
import manager

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
        player.sort_cards()
        print(player.hand) #Todo delete it 
        

def handle_landlord(players, deck):
    '''
    Get the landlord in the players
    We first generate a random number in the players. Then loop through the players list.
    If we meet a computer (player 1 and 2), we calcuate the score of the cards and decide if 
    it is landlord
    If we meet human, we do this based on input
    If it is the last one in the round, then it has to be landlord.
    We need to add three cards to landlord
    return player id of the landlord
    '''
    cur = random.randint(0, 2)
    index = 0
    while index < 3:
        index += 1
        is_landlord = players[cur].landlord_choice(index)
        if is_landlord:
            players[cur].set_landlord(cur + 1)
            for i in range(3):  #landlord will get 3 extra cards
                card = deck.deal_card()
                players[cur].add_card(card)
            return cur
        cur += 1
        cur = cur % 3

def game_play(players, landlord):
    '''
    Game process.
    players will take turns to play cards.
    There are two ways to play cards. One is positive play. You can play whatever valid ways you want
    The other one is negtive play. You have to play the way the previos player did.
    '''
    cur = landlord
    positive = True
    manager = manager.Manager()
    prev_action = ""
    last_player = 0
    while not game_over(players):

        if last_player == cur and not positive:
            positive = True

        if cur == 3: #human
            valid = False
            while not valid:
                # handle input
                cards = input("Please choose what card you want to play. \n Example: if you want to play H3 C3, type in: H3 C3 \n")
                card_list, valid = handle_input(cards)
                if valid and len(card_list) == 0 and positive:
                    print("Fisrt player must play cards.")
                    continue
                if valid and len(card_list) == 0: # Did not play card
                    break
                if manager.is_valid_play(card_list, positive, prev_action):
                    print("Play : {}".format(card_list))
                    players[cur].card_play(card_list)
                    prev_action = manager.get_action(card_list)
                    valid = True
                    last_player = cur
                else:
                    print("Wrong cards. Please choose again.")
            # Change positive if possible
            if positive:
                positive = False
        else: # Computer
            card_list = manager.AI_play(players[cur], cur, positive) # AI should play when it can play
            if len(card_list) == 0:
                continue
            players[cur].card_play(card_list)
            last_player = cur
            # Change positive if possible
            if positive:
                positive = False


def game_over(players):
    return False

def handle_input(cards):
    '''
    Turn the input string to a list of card
    return the list of card and if the input is valid
    '''
    if cards == None or len(cards) == 0:
        return [], True
    # Todo 
    cards = cards.strip().split()
    pass
    

if __name__ == '__main__':
    main(sys.argv)