class Player:
    '''
    Represents the three player. The default role is peasant. 
    '''
    def __init__(self, id):
        self.id = id
        self.role = 'Peasant'
        self.hand = []

    def set_landlord(id):
        if self.id != id:
            raise ValueError("Wrong user!")
        self.role = "Landlord"
    
    def draw_card(card):
        self.hand.append(card)
