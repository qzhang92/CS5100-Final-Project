import cards

class Manager:
    '''
    Rules and regulations of the game
    '''
    def __init__(self):
        self.card_style = dict() # a hash of ways to win
        self.card_style['solo'] = 1
        self.card_style['pair'] = 2
        self.card_style['trio'] = 3
        self.card_style['triosolo'] = 4
        self.card_style['triopair'] = 5
        self.card_style['chain'] = 6
        self.card_style['pairchain'] = 7
        self.card_style['airplane'] = 8
        self.card_style['airplanewingsolo'] = 9
        self.card_style['airplanewingpair'] = 10
        self.card_style['bomb'] = 11
        self.card_style['rocket'] = 12
        
    
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
        plane = []
        for card in card_list:
            if card.value < 150 : #does not apply to 2, Joker
                key = card.value / 10
                if key not in card_dict:
                    card_dict[key] = 1
                else:
                    card_dict[key] += 1
        for key in card_dict:
            if card_dict[key] == 3:
                plane.append(key)
        if len(plane) < 2:
            return False
        
        plane.sort()
        prev = 1
        for num in plane:
            if prev == 1:
                prev = num + 1
            elif prev != num:
                return False
            else:
                prev += 1
        return True

    def is_valid_play(self, card_list, hand, positive, prev_action, prev_cards):
        '''
        check if cards in card_list is good
        return bool
        '''
        cur_cards = []
        for index in card_list:
            cur_cards.append(hand[index])
        if positive:
            return self.get_action(cur_hands) != -1
        if len(card_list) != len(prev_cards):
            return False
        if prev_action != self.get_action(cur_cards):
            return False
        return self.evaluate_cards(cur_cards, prev_action) > self.evaluate_cards(prev_cards, prev_action)
        
    
    def get_action(self, card_list):
        '''
        return value -> key seen in init
        if value == -1:
            this is not a valid play
        '''
        size = len(card_list)
        if size == 1: #solo
            return 1
        elif size == 2:  # pair and rocket
            card0 = card_list[0]
            card1 = card_list[1]
            if card0.value > 150 and card1.value > 150: # Joker Joker
                return 12
            elif int(card0.value / 10) == int(card1.value / 10): #same rank
                return 2
            else:
                return -1 #invalid
        elif size == 3: # size == 3 is only possible with trio
            val = int(card_list[0].value / 10)
            for card in card_list:
                if int(card.value / 10) != val:
                    return -1 # not Trio
            return 3
        else:
            card_dict = dict()
            for card in card_list:
                key = int(card.value / 10)
                if key in card_dict:
                    card_dict[key] += 1
                else:
                    card_dict[key] = 1
            if size == 4:
                if len(card_dict) == 1: #bomb
                    return 11
                elif len(card_dict) == 2: # 3 + 1 or 2 + 2
                    for key in card_dict:
                        if card_dict[key] != 2:
                            return 4 #Triosolo
                else: 
                    return -1
            elif size == 5:
                if len(card_dict) == 5: # 5 different cards. maybe chain
                    return self.handle_chain(card_dict)
                elif len(card_dict) == 2: #only 3 + 2 is ok.
                    for key in card_dict:
                        if card_dict[key] == 3 or card_dict[key] == 2:
                            return 5
                        else:
                            return -1
                else: #len(card_dict) won't be 1, can be 3, 4, which are invalid
                    return -1
            elif size == 6:
                if len(card_dict) == size: # 6 different cards. maybe chain
                    return self.handle_chain(card_dict) ? 6 : -1
                elif len(card_dict) == 2: # 3 + 3, 4 + 2
                    for key in card_dict:
                        if card_dict[key] == 3: #airplane
                            return 8
                        else: #4 + 2 is invalid
                            return -1
                elif len(card_dict) == 3: # pair chain
                    return self.handle_chain(card_dict) ? 7 : -1
                else: #  1 not possible,  4 5 not valid
                    return -1
            elif size == 7:
                if len(card_dict) == size: # 7 different cards. maybe chain
                    return self.handle_chain(card_dict) ? 6 : -1
                else: # 1 not possible, 2 3 4 5 6invalid
                    return -1
            elif size == 8: 
                if len(card_dict) == size: # 8 different cards. maybe chain
                    return self.handle_chain(card_dict) ? 6 : -1
                elif len(card_dict) == 3 : # 3 + 3 + 2, airplane wing solo
                    items = card_dict.items()
                    items.sort()
                    if items[0] == 2 and items[1] == 3 and items[2] == 3:
                        return self.has_airplane(card_list) ? 9 : -1
                    else:
                        return -1
                elif len(card_dict) == 4: # pair chain or 3 + 3 + 1 + 1
                    if self.has_airplane(card_list):
                        return 9
                    if self.handle_chain(card_dict):
                        for key in card_dict:
                            if card_dict[key] != 2:
                                return -1
                        return 7
                else: #5 6 invalid
                    return -1
            elif size == 9:
                if len(card_dict) == size: # 9 different cards. maybe chain
                    return self.handle_chain(card_dict) ? 6 : -1
                elif len(card_dict) == 3: # 3 + 3 + 3 / 1 + 4 + 4
                    return self.has_airplane(card_list) ? 8 : -1
                else:
                    return -1
            else:
                if len(card_dict) == size: # 9 different cards. maybe chain
                    return self.handle_chain(card_dict) ? 6 : -1
                elif size % 2 == 0 and len(card_dict) == size / 2: #pair chain 
                    return self.handle_chain(card_dict) ? 7 : -1
                elif size % 3 == 0 and len(card_dict) == size / 3: #air plane
                    for key in card_dict:
                        if card_dict[key] != 3:
                            return -1
                    return self.handle_chain(card_dict) ? 8 : -1
                #else if size % 4 == 0: #air plane with solo too hard, return -1
                #else if size % 5 == 0: #air plane with double pair too hard, return -1
                else:
                    return -1

    def evaluate_cards(cur_cards, prev_action):
        '''
        Bsed on the prev_action(that is also the current action), provide util score of the card
        '''
        card_dict = dict()
        for card in cur_cards:
            key = int(card.value / 10)
            if key in card_dict:
                card_dict[key] += 1
            else:
                card_dict[key] = 1
        if prev_action == 1:
            return int(cur_cards[0].value / 10)
        elif prev_action == 2:
            return int(cur_cards[0].value / 10)
        elif prev_action == 3:
            return int(cur_cards[0].value / 10)
        elif prev_action == 4:
            for key in card_dict:
                if card_dict[key] == 3:
                    return key
            return -1
        elif prev_action == 5:
            for key in card_dict:
                if card_dict[key] == 3:
                    return key
            return -1
        elif prev_action == 6:
            score = 0
            for key in card_dict:
                score += key
            return score
        elif prev_action == 7:
            score = 0
            for key in card_dict:
                score += key
            return score
        elif prev_action == 8:
            score = 0
            for key in card_dict:
                score += key
            return score
        elif prev_action == 9:
            score = 0
            for key in card_dict:
                if card_dict[key] == 3:
                    score += key
            return score
        elif prev_action == 10:
            score = 0
            for key in card_dict:
                if card_dict[key] == 3:
                    score += key
            return score
        elif prev_action == 11:
            return int(cur_cards[0].value / 10)
        elif prev_action == 12:
            return 200
        else:
            return -1

    
    def handle_chain(self, card_dict):
        '''
        check if the car_dict keys can make a chain
        '''
        prev_key = -1
        keys = list(card_dict.keys())
        keys.sort()
        for key in keys:
            if prev_key == -1:
                prev_key = key
            elif prev_key != key - 1:
                return False  #wrong chain
            else:
                prev_key = key
        return True #chain




    def AI_play(self, player, id, positive, prev_action, prev_cards):
        '''
        AI is required here.
        Ai methods should be in manager.py or player.py?
        return a list of card index. Card is 1 indexed
        need to list all possible ways during positive play
        '''
        pass

    def legal_actions(hand):
        '''
        List legal actions
        hand: current hand of the game
        '''
