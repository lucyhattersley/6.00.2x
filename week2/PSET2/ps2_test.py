from ps2 import *

robot = Robot(RectangularRoom(5,8), 1.0)
print robot.getRobotPosition()
for l in range(10):
    x = random.randint(0,5)
    print "x is: " + str(x)
    y = random.randint(0,8)
    print "y is: " + str(y)
    if robot.room.isPositionInRoom(Position(x,y)):
        robot.setRobotPosition(Position(x,y))
        print robot.getRobotPosition()
    else:
        print "Robot not updated"
    