
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

# Determines player's hand values
def hand_value(hand):
    return []

# Returns high card rank if straight exists
# Returns -1 if no straight exists
def straight(hand):
    ranks = [card.rank for card in hand] # List of only ranks
    ranks = list(set(ranks)) # Creates unique list of ranks
    ranks.sort(reverse=True) # Sorts in descending order

    # Checking sets of 5, maximum of 3 sets of 5
    for i in range(len(ranks)-4):
        # Spliced list of 5
        sub_seq = ranks[i:i+5]
        # List of [max, max-1, max-2, max-3, ..., min]
        straight_seq = list(range(max(sub_seq),min(sub_seq)-1,-1))
        if (sub_seq == straight_seq):
            return ranks[i]
        
    return -1

def flush(hand):
    suits = [card.suit for card in hand] # List of only suits
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

print("\nFLUSH TESTS--------------------------------")
test_1 = [Card(0,0),Card(0,1),Card(4,0),Card(10,0),
          Card(12,0),Card(5,3),Card(10,0)]
test_2 = [Card(0,0),Card(0,1),Card(4,1),Card(10,0),
          Card(12,0),Card(5,3),Card(10,0)]
print(test_1)
print(flush(test_1))
print(test_2)
print(flush(test_2))

print("\nSTRAIGHT TESTS--------------------------------")
test_3 = [Card(0,0),Card(1,1),Card(2,0),Card(3,0),
          Card(5,3),Card(4,3),Card(10,0)]
print(test_3)
print(straight(test_3))
