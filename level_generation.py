#*************************************************
#level_generation.py
#Has all the code to generate each level
#Can be called from main to generate a list of rooms
#Stefan Salewski
#*************************************************

from Entity_Classes import Wall
import random
class level_generation():

#fun initialization
    def __init__(self, pygame_instance, screen, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.screen = screen
        self.pygame = pygame_instance
        self.RED = (255, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 255, 0)
        print("HELLO WORLD")

    def create_room(self, x, y, prevdoor, door):
        room = []

        # Top wall
        topleft = Wall(x, y, 400, 10)
        topright = Wall(x + 600, y, 400, 10)
        room.append(topleft)
        room.append(topright)
        if prevdoor != 0 and door != 2:
            topdoor = Wall(x + 400, y, 200, 10)
            room.append(topdoor)

        # Left wall
        lefttop = Wall(x, y, 10, 400)
        leftbot = Wall(x, y + 600, 10, 400)
        room.append(lefttop)
        room.append(leftbot)
        if prevdoor != 3 and door != 1:
            leftdoor = Wall(x, y + 400, 10, 200)
            room.append(leftdoor)

        # Bottom wall
        botleft = Wall(x, y + 1000, 400, 10)
        botright = Wall(x + 600, y + 1000, 400, 10)
        room.append(botleft)
        room.append(botright)
        if prevdoor != 2 and door != 0:
            botdoor = Wall(x + 400, y + 1000, 200, 10)
            room.append(botdoor)

        # Right wall
        righttop = Wall(x + 1000, y, 10, 400)
        rightbot = Wall(x + 1000, y + 600, 10, 400)
        room.append(righttop)
        room.append(rightbot)
        if prevdoor != 1 and door != 3:
            rightdoor = Wall(x + 1000, y + 400, 10, 200)
            room.append(rightdoor)

        return room

#lets go we can draw stuff in classes
    def generate_level(self, numrooms, roomlist, iteration, prevx, prevy, randomnum):
        iteration = iteration
        prevx = prevx
        prevy = prevy

        rooms = roomlist
        if len(rooms) > 0:
            generating = True
            max_attempts = 100  # Maximum number of attempts to avoid infinite loop
            attempts = 0
            while generating and attempts < max_attempts:
                attempts += 1
                nextrandomnum = random.randint(0, 3)

                # Determine the new room position based on the random number
                if randomnum == 0:  # up
                    newx = prevx[-1]
                    newy = prevy[-1] + 1000
                elif randomnum == 1:  # left
                    newx = prevx[-1] - 1000
                    newy = prevy[-1]
                elif randomnum == 2:  # down
                    newx = prevx[-1]
                    newy = prevy[-1] - 1000
                elif randomnum == 3:  # right
                    newx = prevx[-1] + 1000
                    newy = prevy[-1]

                occupied = any(newx == x and newy == y for x, y in zip(prevx, prevy))

                if not occupied:
                    # Check nextrandomnum placement
                    if nextrandomnum == 0:  # up
                        checkx = newx
                        checky = newy + 1000
                    elif nextrandomnum == 1:  # left
                        checkx = newx - 1000
                        checky = newy
                    elif nextrandomnum == 2:  # down
                        checkx = newx
                        checky = newy - 1000
                    elif nextrandomnum == 3:  # right
                        checkx = newx + 1000
                        checky = newy

                    if any(checkx == x and checky == y for x, y in zip(prevx, prevy)):
                        continue  # Skip this iteration if the next position is occupied

                    newroom = self.create_room(newx, newy, randomnum, nextrandomnum)
                    prevx.append(newx)
                    prevy.append(newy)
                    rooms.append(newroom)
                    generating = False
            #this should only happen with a layout that cant make more rooms
            #if it does then we can end it early
            if attempts == max_attempts:

                return rooms
        else:
            nextrandomnum = random.randint(0, 3)
            rooms.append(self.create_room(0, 0, 4, nextrandomnum))
            prevx.append(0)
            prevy.append(0)

        if iteration == numrooms - 1:
            return rooms
        else:
            return self.generate_level(numrooms, rooms, iteration + 1, prevx, prevy, nextrandomnum)


