
# 1 Straight flush
# 2 Four of a kind
# 3 Full house
# 4 Flush
# 5 Straight
# 6 Three of a kind
# 7 Two pair
# 8 Pair
# 9 High card

# Using player hands and community cards, determines winner
def get_winner(player_list, comm_cards):
    []

# Determines player's hand
def hand_value(hand):
    hand.sort(key = lambda card: card.suit)
    hand.sort(key = lambda card: card.rank)
    return []
    
def straight(hand):
    '''
    straight_len = 0
    ranks = [card.rank for card in hand] # Get only ranks
    ranks = list(set(seq)) # Creates unique list of ranks
    
    # Middle two comparisons must be in order for straight to exist
    if (ranks[2]-ranks[3]==1 and ranks[3]-ranks[4]==1):
    '''
    return []

def flush(hand):
    suits = [card.suit for card in hand]
    suits.sort()
    suit_len = 1
    for i in range(1, len(suits)):
        if (suits[i] == suits[i-1]):
            suit_len += 1
        elif (suit_len < 5):
            suit_len = 0

    if (suit_len >= 5):
        return True
    else:
        return False
        

##############
# Some testing routines
# Add tests as needed
##############

from deck import Deck, Card

#random selection testing
d = Deck()
d.shuffle_deck()

comm = d.deck[:5] #take 5 cards
hand = d.deck[5:7] #take 2 cards after
combined = comm+hand

print(combined)

print(combined[0].rank)
combined.sort(key=lambda card: card.rank, reverse=True)
print(combined)

print("\nFLUSH TEST1--------------------------------")
test_1 = [Card(0,0),Card(0,1),Card(4,0),Card(10,0),
          Card(12,0),Card(5,3),Card(10,0)]
test_2 = [Card(0,0),Card(0,1),Card(4,1),Card(10,0),
          Card(12,0),Card(5,3),Card(10,0)]
print(test_1)
print(flush(test_1))
print(test_2)
print(flush(test_2))
