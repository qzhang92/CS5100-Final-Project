import cards

class Manager:
    '''
    Rules and regulations of the game
    '''
        
    
    def has_chain(self, card_list):
        card_rank = []
        for card in card_list:
            if card.value < 150 : #does not apply to 2, Joker
                key = card.value / 10
                if key not in card_rank:
                    card_rank.append(key)
        prev = 1
        continuos = 0
        for rank in card_rank:
            if rank == prev + 1:
                continuos += 1
                if continuos >= 5:
                    return True
            else:
                continuos = 0
        
        return False
    
    def has_pair_chain(self, card_list):
        card_dict = dict()
        for card in card_list:
            if card.value < 150 : #does not apply to 2, Joker
                key = card.value / 10
                if key not in card_dict:
                    card_dict[key] = 1
                else:
                    card_dict[key] += 1
        prev = 1
        continuos = 0
        for rank in card_dict:
            if rank == prev + 1 and card_dict[rank] >= 2 and card_dict[prev] >= 2:
                continuos += 1
                if continuos >= 5:
                    return True
            else:
                continuos = 0
        return False
    
    def has_airplane(self, card_list):
        card_dict = dict()
        for card in card_list:
            if card.value < 150 : #does not apply to 2, Joker
                key = card.value / 10
                if key not in card_dict:
                    card_dict[key] = 1
                else:
                    card_dict[key] += 1
        prev = 1
        for rank in card_dict:
            if rank == prev + 1 and card_dict[rank] > 2 and card_dict[prev] > 2:
                return True
        return False

    def is_valid_play(self, card_list, positive, prev_action):
        '''
        check if cards in card_list is good
        '''
        pass
    
    def get_action(self, card_list):
        pass

    def AI_play(self, player, id, positive):
        '''
        AI is required here.
        Ai methods should be in manager.py or player.py?
        '''
        pass
