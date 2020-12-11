import manager
import cards

mgr = manager.Manager()
hand = cards.Hand()
deck = cards.Deck()
for i in range(4):
    hand.add_card(cards.Card('H', '2'))
hand.add_card(cards.Card('H', '2', "BJoker"))

hand.add_card(cards.Card('H', '2', "RJoker"))
hand.sort_cards()
print(hand.hand)

def get_card_from_hand(hand, key, num):
    result = []
    for i in range(len(hand)):
        card = hand[i]
        val = int(card.value / 10)
        if val == key:
            result.append(i)
            num -= 1
            if num == 0:
                return result
    return []

def legal_actions(hand): # hand is array
    result = dict()
    card_dict = dict()
    for card in hand:
        key = int(card.value / 10)
        if key in card_dict:
            card_dict[key] += 1
        else:
            card_dict[key] = 1
    for i in range(1, 13):
        result[i] = []
    print(result)
    # 1
    for card in hand:
        action = [card]
        result[1].append(action)
    # 2
    for key in card_dict:
        if card_dict[key] >= 2:
            card = get_card_from_hand(hand, key, 2)
            action = [hand[card[0]], hand[card[1]]]
            result[2].append(action) 
    
    # 3
    for key in card_dict:
        if card_dict[key] >= 3:
            card = get_card_from_hand(hand, key, 3)
            action = [hand[card[0]], hand[card[1]], hand[card[2]]]
            result[3].append(action)
    
    # 4
    for key in card_dict:
        if card_dict[key] >= 3:
            card = get_card_from_hand(hand, key, 3)
            action = [hand[card[0]], hand[card[1]], hand[card[2]]]
            for i in range(len(hand)):
                if not int(hand[i].value / 10) == key:
                    action.append(hand[i])
                    cards = action.copy()
                    result[4].append(cards)
                    action.remove(hand[i])
    # 5
    for key in card_dict:
        if card_dict[key] >= 3:
            card = get_card_from_hand(hand, key, 3)
            action = [hand[card[0]], hand[card[1]], hand[card[2]]]
            for cards in result[2]:
                if not int(cards[0].value / 10) == int(action[0].value / 10):
                    array = action.copy()
                    array.append(cards[0])
                    array.append(cards[1])
                    result[5].append(array)
    # 11
    for key in card_dict:
        if card_dict[key]== 4:
            card = get_card_from_hand(hand, key, 4)
            action = []
            for index in card:
                action.append(hand[index])
            result[11].append(action)
    # 12
    b_joker = False
    r_joker = False
    for key in card_dict:
        if key == 16:
            b_joker = True
        if key == 17:
            r_joker = True
    if b_joker and r_joker:
        array =[get_card_from_hand(hand, 16, 1)[0], get_card_from_hand(hand, 17, 1)[0]]
        action = []
        for index in array:
            action.append(hand[index])
        result[12].append(action)
    print(result)


legal_actions(hand.hand)