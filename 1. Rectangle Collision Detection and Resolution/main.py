
# Import the pygame module
import pygame
import sys

def checkKeyEvents(player):
    # Get the state of the keyboard keys
    keys = pygame.key.get_pressed()
    # Check if the left arrow key is pressed
    if keys[pygame.K_LEFT]:
        # Move the rectangle to the left
        #player.move_ip(-5, 0)
        player.move(-5, 0)
    # Check if the right arrow key is pressed
    if keys[pygame.K_RIGHT]:
        # Move the rectangle to the right
        player.move(5, 0)
    # Check if the up arrow key is pressed
    if keys[pygame.K_UP]:
        # Move the rectangle up
        player.move(0, -5)
    # Check if the down arrow key is pressed
    if keys[pygame.K_DOWN]:
        # Move the rectangle down
        player.move(0, 5)
class Object(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.oTop = self.top
        self.oBottom = self.bottom
        self.oRight = self.right
        self.oLeft = self.left
    def move(self, x , y ):
        self.x += x
        self.y += y
    def updateOldPos(self):
        self.oTop = self.top
        self.oBottom = self.bottom
        self.oRight = self.right
        self.oLeft = self.left
    def checkCollisions(self, listOfObjectsToDraw):
        c = listOfObjectsToDraw[0]
        #print(self.top, " ", self.oTop)
        #print(self.right, " ", self.oRight)

        if self.bottom < c.top or self.top > c.bottom or self.left > c.right or self.right < c.left:
            return

        if self.bottom >= c.top and self.oBottom <  c.oTop:
            self.bottom = c.top - 1
        elif self.top <= c.bottom  and self.oTop > c.oBottom:
            self.top = c.bottom +1
        elif self.right >= c.left and self.oRight < c.oLeft:
            self.right = c.left -1
        elif self.left <= c.right and self.oLeft > c.oRight:
            self.left = c.right + 1

class Player(Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color = (255, 0, 0)  # Red color

class Wall(Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color = (255, 0, 0)  # Red color

def createObjectsToDraw():
    wall = Wall(400, 300, 100, 50)
    listOfObjectsToDraw = []
    listOfObjectsToDraw.append(wall)
    return listOfObjectsToDraw

#wall:
def drawObjects(listOfObjectsToDraw):
    for rect in listOfObjectsToDraw:
        pygame.draw.rect(screen, (0,110,255), rect)

def drawControlableObject(player):
    pygame.draw.rect(screen, (255,10,10), player)



# Initialize pygame
pygame.init()
# Create a display surface
screen = pygame.display.set_mode((800, 600))
# Set the caption of the window
pygame.display.set_caption("Moving Rectangle")
# Create a clock object
clock = pygame.time.Clock()

#Create objects to draw:
listOfObjectsToDraw = createObjectsToDraw()
#create human controlled object with keyboard:
player = Player(350, 300, 32, 32)

# Create a color object
color = pygame.Color(255, 0, 0)

# Create a variable for the game loop
running = True

# Start the game loop
while running:
    # Handle the events
    for event in pygame.event.get():
        # Check if the user clicked the close button
        if event.type == pygame.QUIT:
            # Exit the loop
            running = False
            sys.exit()

    # Fill the screen with black
    screen.fill((0, 0, 0))
    checkKeyEvents(player)
    player.checkCollisions(listOfObjectsToDraw)
    player.updateOldPos()
    #so to set old position:
    for i in listOfObjectsToDraw:
        i.updateOldPos()


    #draw your objects on the screen:
    drawObjects(listOfObjectsToDraw)
    drawControlableObject(player)


    # Update the display
    pygame.display.update()
    # Control the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
