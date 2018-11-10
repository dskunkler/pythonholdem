
# 1 Straight flush
# 2 Four of a kind
# 3 Full house
# 4 Flush
# 5 Straight
# 6 Three of a kind
# 7 Two pair
# 8 Pair
# 9 High card

#Tests for a royal flush Returns high cards if it is or -1 if not
def straight_flush(all_cards):
    x = 0
    flushl = [] #this is the list of all same suits
    for i in all_cards:
        x += 1 # iterator for splicing rank for j
        temp = []
        temp.append(i) #creates a temporary list with i in it
        for j in all_cards[x:]: #compares rest of list past i
            if i.suit == j.suit:
                temp.append(j)# if suit is equal to our first val we add it
        if len(temp) > len(flushl) and len(temp) >= 5: #temp must be greater
            flushl = temp                              #then flush list & 5     
    flushl.sort(key=lambda card: card.rank, reverse = True) #orders by rank
    straight_f = False     
    for i in range(len(flushl)-4):
        # Spliced list of 5
        sub_seq = flushl[i:i+5]
        for j in range(1,5):
            if sub_seq[0].rank -j == sub_seq[j].rank:
                if j == 4:# will be true if we've gotten to the 4th element
                    straight_f = True
            else:# otherwise we don't keep iterating
                break
        if straight_f == True:
            return sub_seq[0].rank
        else:
            return -1

#Full house function        
def full_house(all_cards):
    ranks = [card.rank for card in all_cards] #list of all ranks
    three_of = [] 
    two_of = [] 
    x = 0
    three = False
    two = False
    for i in ranks:
        x += 1 # iterator for splicing rank for j
        temp = []
        temp.append(i) #creates a temporary list with i in it
        for j in ranks[x:]: #compares rest of list past i
            if i == j:
                temp.append(j)# if rank is equal to our list val we add it
        if len(temp) == 3:# if our temp = 3
            if len(three_of) == 3:
                if temp[0] > three_of[0]:
                    three_of = temp
                    three = True
            else:
                three_of = temp
                three = True
    for i in range(3): #I have to remove them or it will create a list of two from the 3 of a kind
        ranks.remove(three_of[0])
    x = 0 #We now repeat the process for the pair
    for i in ranks:
        x += 1 # iterator for splicing rank for j
        temp = []
        temp.append(i) #creates a temporary list with i in it
        for j in ranks[x:]: #compares rest of list past i
            if i == j:
                temp.append(j)# if rank is equal to our list val we add it
        if len(temp) == 2:
            if len(two_of) == 2:
                if temp[0] > two_of[0]:
                    two_of = temp
                    two = True
            else:
                two_of = temp
                two = True
            
    if two == True and three == True:
        return three_of[0]
    else:
        return -1

#Royal flush will return true if there is a straight flush with ace high
'''
def royal_flush(all_cards):
    x = 0
    flushl = [] #this is the list of all same suits
    for i in all_cards:
        x += 1 # iterator for splicing rank for j
        temp = []
        temp.append(i) #creates a temporary list with i in it
        for j in all_cards[x:]: #compares rest of list past i
            if i.suit == j.suit:
                temp.append(j)# if suit is equal to our first val we add it
        if len(temp) > len(flushl) and len(temp) >= 5: #temp must be greater
            flushl = temp                              #then flush list & 5     
    flushl.sort(key=lambda card: card.rank, reverse = True) #orders by rank
    royal_f = False     
    if flushl[0].rank == 12:    #first in list must be an Ace
        royal_f = True          #will be false if first isnt Ace
        for i in range(5):
            if flushl[i].rank != 12 - i:
                royal_f = False #if it doesn't descend incrementally its False
    return royal_f
'''

# Using player hands and community cards, determines winner
def get_winner(player_list, comm_cards):
    []

# Determines player's hand values
def hand_value(all_cards):
    return []

#Makes longest list possible of equal ranks
#if length of list is equal to kind, we return the card
#return False otherwise
def of_a_kind(all_cards, kind):
    ranks = [card.rank for card in all_cards] #list of all ranks
    best = [] #this will be the longest list of equal ranks
    x = 0
    for i in ranks:
        x += 1 # iterator for splicing rank for j
        temp = []
        temp.append(i) #creates a temporary list with i in it
        for j in ranks[x:]: #compares rest of list past i
            if i == j:
                temp.append(j) # if rank is equal to our list val we add it
        if len(temp) > len(best): # if our temp is longest its our best
            best = temp
        elif len(temp) == len(best):
            if temp[0] > best[0]:
                best = temp
        
                
    if len(best) == kind: #checking if its equal to what we want
        return best[0] #returns rank of our best type
    else:
        return False
                 


# Returns high card rank if straight exists
# Returns -1 if no straight exists
def straight(all_cards):
    ranks = [card.rank for card in all_cards] # List of only ranks
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

def flush(all_cards):
    suits = [card.suit for card in all_cards] # List of only suits
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

print("\nSTRAIGHT FLUSH TEST-------------------------------")
test_1 = [Card(12,3),Card(11,0),Card(9,0),Card(10,0),
          Card(3,0),Card(7,0),Card(8,0)]
print(test_1)
print(straight_flush(test_1))

print("\nROYAL TEST-------------------------------")
test_2 = [Card(12,3),Card(11,0),Card(9,0),Card(10,0),
          Card(3,0),Card(12,0),Card(8,0)]
print(test_2)
print(straight_flush(test_2))

print("\n4 OF A KIND TEST---------------------------")
test_3 = [Card(3,0),Card(8,0),Card(7,0),Card(8,0),
          Card(8,3),Card(7,3),Card(8,0)]
print(test_3)
print(of_a_kind(test_3,4))

print("\n3 OF A KIND TEST---------------------------")

test_4 = [Card(3,0),Card(0,0),Card(7,0),Card(8,0),
          Card(8,3),Card(7,3),Card(8,0)]
print(test_3)
print(of_a_kind(test_3,3))
print(test_4)
print(of_a_kind(test_4,3))

print("\n2 OF A KIND TEST---------------------------")

test_5 = [Card(3,0),Card(8,0),Card(7,0),Card(10,0),
          Card(8,3),Card(5,3),Card(8,0)]
print(test_4)
print(of_a_kind(test_4,2))
print(test_5)
print(of_a_kind(test_5,2))


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

print("\nFULL HOUSE TEST-------------------------------")
test_5 = [Card(9,0),Card(8,0),Card(9,0),Card(4,0),
          Card(8,3),Card(7,3),Card(8,2)]
print(test_5)
print(full_house(test_5))