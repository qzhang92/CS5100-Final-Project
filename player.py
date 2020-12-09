import cards

LANDLORD_UTIL = 50

class Player:
    '''
    Represents the three player. The default role is peasant. 
    Player 3 is human
    Player 1 is search_AI
    Player 2 reinforcement_AI

    Search_AI:
    1. DFS
    2. A* search
    3. Heuristic search

    4. Reinforcement learning
    '''
    def __init__(self, id):
        '''
        id is 1 indexed
        '''
        self.id = id
        self.role = 'Peasant'
        self.hand = cards.Hand()

    def set_landlord(self, id):
        if self.id != id:
            raise ValueError("Wrong user!")
        self.role = "Landlord"

    
    def add_card(self, card):
        self.hand.add_card(card)
    
    def landlord_choice(self, index):
        if index == 3:   #If this is the last player in the round
            return True
        if self.id == 3:
            while True:
                is_landlord = input("Do you wnat to become the landlord? (Y/N)")
                if is_landlord == 'Y':
                    return True
                elif is_landlord == 'N':
                    return False
        else:
            return self.landlord_util() >= LANDLORD_UTIL

    def landlord_util(self):
        '''
        Calculate the utility of the current cards
        Todo:
        '''
        return 30

