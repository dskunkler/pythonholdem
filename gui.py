import pygame, sys
import hand, player
from pygame.locals import *

def first_deal_animation(h, screen, players):
    '''Animation for dealing at the beginning of a new hand'''
    h.init()
    BET_BOX = pygame.Rect(100, 100, 140, 32)
    DEAL_BOX = pygame.Rect(100,200,140,32)
    
            
    hand1 = players[0].hand
    card1 = hand1[0]
    card2 = hand1[1]     
            
    screen.blit(BACK, (575,100))
    pygame.draw.rect(screen, BLACK, BET_BOX, 2)
    pygame.draw.rect(screen, BLACK,DEAL_BOX, 2)
    dealleft = 575
    dealtop = 100
    while(dealtop != 400):
        screen.fill(GREEN)
        screen.blit(BACK, (575,100))
        dealtop += 4
        dealleft -= 1
        screen.blit(BACK,(dealleft,dealtop))
        pygame.draw.rect(screen, BLACK, BET_BOX, 2)
        pygame.draw.rect(screen, BLACK,DEAL_BOX, 2)
        pygame.display.update()
        CLOCK.tick(FPS)
        
    dealleft = 575
    dealtop = 100
            
    while(dealtop != 400):
        screen.fill(GREEN)
        screen.blit(BACK, (575,100))
        screen.blit(CARDS[card1.suit][card1.rank], (500,400))
        dealtop += 4
        dealleft += 1
        screen.blit(BACK,(dealleft,dealtop))
        pygame.draw.rect(screen, BLACK, BET_BOX, 2)
        pygame.draw.rect(screen, BLACK,DEAL_BOX, 2)
        pygame.display.update()
        CLOCK.tick(FPS)
            
    screen.fill(GREEN)
    screen.blit(BACK, (575,100))
    screen.blit(CARDS[card1.suit][card1.rank], (500,400))        
    screen.blit(CARDS[card2.suit][card2.rank], (650,400))
    pygame.draw.rect(screen, BLACK, BET_BOX, 2)
    pygame.draw.rect(screen,BLACK,DEAL_BOX, 2)
            
            #if (h.comm):
    h.clear()

# Setting some constants
FPS = 30
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700
CARD_WIDTH = 130
CARD_HEIGHT = 200
BET_BOX = pygame.Rect(100, 100, 140, 32)
INACTIVE_COL = pygame.Color('lightskyblue3')
ACTIVE_COL = pygame.Color('dodgerblue2')
DEAL_BOX = pygame.Rect(100,200,140,32)


# Setting colors
GREEN = ( 40,140, 70)
WHITE = (255,255,255)
BLACK = (  0,  0,  0)

CLOCK = pygame.time.Clock()

# Initialize 2D array
# Access cards with cards[suit][rank]
# Suit 0-3 | Rank 0-12
CARDS = [[],[],[],[]]
SUITS = ['S','D','H','C']

# Fill 2D array
for i, suit in enumerate(CARDS):
    for rank in range(2, 15):
        img = pygame.image.load('images/cards/{}{}.png'.format(rank, SUITS[i]))
        img = pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))
        suit.append(img)

# Loads card back
BACK = pygame.image.load('images/back1.png')
BACK = pygame.transform.scale(BACK, (CARD_WIDTH, CARD_HEIGHT))


def main():

    # Loading some elements from game.py
    # Necessary to start hand
    names = ["A","B","C"]
    players = []
    buy_in = 2000
    color = INACTIVE_COL
    active = False
    user_bet = ''

    # Create players
    for name in names:
        players.append(player.Player(buy_in, name))

    # Hand creation
    h = hand.Hand(players)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    font = pygame.font.Font(None, 32)
    deal_obj = font.render('DEAL', True, BLACK,GREEN)
    deal_box = deal_obj.get_rect()
    deal_box.center = (130, 200)

    mousex = 0 # Mouse x coord
    mousey = 0 # Mouse y coord

    pygame.display.set_caption('Texas Hold\'em')

    screen.fill(GREEN)

    # Game loop
    while True:
        deal_clicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                # Detects any mouse motion and set x,y coordinate of mouse
                '''
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                # Detects if mouse click occurs and sets x,y coordinate
                
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                deal_clicked = True
                '''
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if BET_BOX.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                elif deal_box.collidepoint(event.pos):
                    deal_clicked = True
                else:
                    active = False
                # Change the current color of the input box.
                color = ACTIVE_COL if active else INACTIVE_COL
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(user_bet)
                        user_bet = ''
                    elif event.key == pygame.K_BACKSPACE:
                        user_bet = user_bet[:-1]
                    else:
                        user_bet += event.unicode
        screen.fill(GREEN)
        # Render the current text.
        txt_surface = font.render(user_bet, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        BET_BOX.w = width
        # Blit the text.
        screen.blit(txt_surface, (BET_BOX.x+5, BET_BOX.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, BET_BOX, 2)

        screen.blit(deal_obj, deal_box)
        
        
        
        pygame.display.flip()
        CLOCK.tick(FPS)
                

        # make this a function instead later...
        if deal_clicked:
            first_deal_animation(h, screen, players)
            
        pygame.display.update()
        
        CLOCK.tick(FPS)
        
# Start program
        
if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
