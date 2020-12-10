# CS5100-Final-Project

Use the pdf to present. No need for ppt.


TODO:
1. Create UML
2. Implement the game rules and basic elements
3. AI integeration
4. Final report



Game Play process:
1. 出牌 positive vs negative
evaluate hand legal_actions(hand) 
positive:  loop through all legal actions
negative: actions = legal_actions(hand)
            action[prev_action] -> null skip
            -> not null: loop though all action[prev_action]
            for act in action[prev_action]:
                action < prev_card -> skip
            valid_actions = []
            DFS a* search
2. Round by round
3. Game over

int(card.value/10)