import pygame, sys
import hand, player
from pygame.locals import *

# Setting some constants
FPS = 30
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700
CARD_WIDTH = 130
CARD_HEIGHT = 200

# Setting colors
GREEN = ( 40,140, 70)
WHITE = (255,255,255)
BLACK = (  0,  0,  0)

clock = pygame.time.Clock()

# Initialize 2D array
# Access cards with cards[suit][rank]
# Suit 0-3 | Rank 0-12
cards = [[],[],[],[]]
suits = ['S','D','H','C']

# Fill 2D array
for i, suit in enumerate(cards):
    for rank in range(2, 15):
        img = pygame.image.load('images/cards/{}{}.png'.format(rank, suits[i]))
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        suit.append(img)

# Loads card back
back = pygame.image.load('images/red_back.png')
back = pygame.transform.scale(back, (CARD_WIDTH, CARD_HEIGHT))


def main():

    # Loading some elements from game.py
    # Necessary to start hand
    names = ["A","B","C"]
    players = []
    buy_in = 2000

    # Create players
    for name in names:
        players.append(player.Player(buy_in, name))

    # Hand creation
    h = hand.Hand(players)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    mousex = 0 # Mouse x coord
    mousey = 0 # Mouse y coord

    pygame.display.set_caption('Texas Hold\'em')

    screen.fill(GREEN)

    # Game loop
    while True:
        mouse_clicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                # Detects any mouse motion and set x,y coordinate of mouse
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                # Detects if mouse click occurs and sets x,y coordinate
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouse_clicked = True
                

        # make this a function instead later...
        if mouse_clicked:
            h.init()
            
            hand1 = players[0].hand
            card1 = hand1[0]
            card2 = hand1[1]
            screen.blit(cards[card1.suit][card1.rank], (500,400))
            screen.blit(cards[card2.suit][card2.rank], (650,400))
            #if (h.comm):
            h.clear()
            
        pygame.display.update()
        
        clock.tick(FPS)
        
# Start program
main()
