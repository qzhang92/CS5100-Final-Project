import cards
import manager

LANDLORD_UTIL = 40

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
        self.manager = manager.Manager()

    def set_landlord(self, id):
        if self.id != id:
            raise ValueError("Wrong user!")
        self.role = "Landlord"
        msg = "Player {} is landlord".format(id)
        print(msg)

    def add_card(self, card):
        self.hand.add_card(card)

    def sort_cards(self):
        self.hand.sort_cards()
    
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
        '''
        score = 0
        card_list = self.hand.hand
        length = len(card_list)
        if card_list[length - 1].value == 170 and card_list[length - 2].value == 160:
            score += 16
        if self.manager.has_chain(card_list) or self.manager.has_pair_chain(card_list) or self.manager.has_airplane(card_list):
            score += 5
        i = 0
        val = 0
        while i < length:
            # bomb
            if i <= length - 4 and card_list[i].value / 10 == card_list[i + 3].value / 10:
                score += 8
            # black joker, red joker
            if card_list[i].value == 170:
                score += 6
            if card_list[i].value == 160:
                score += 4
            val += int(card_list[i].value / 10)
            i += 1
        score += int(val / 5)
        return score

    def card_play((self, card_list):
        '''
        play the card in the list
        return a list of cards
        '''
        card_list.sort(reverse = True)
        result = []
        for card_index in card_list:
            card = self.hand.remove_card(card_index)
            result.append(card)
        return result

    def is_hand_empty(self):
        '''
        return if the hand is empty
        '''
        return len(self.hand.hand) == 0
        
       
        

