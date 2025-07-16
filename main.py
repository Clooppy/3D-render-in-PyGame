import math
import pygame

pygame.init()
width = 800
hight = 800
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)

RotateY = 0
RotateX = 0
RotateZ = 0
screen = pygame.display.set_mode((width,hight))
pygame.display.set_caption("3d Render")
count = 0
Faces = []
FullRotations = True
FollowMouse = False
CubeSize = 100
NumCubes = 0

Vertexes =([[CubeSize/2, CubeSize/2, -CubeSize/2, 1, red, "vertex"]])
ShapeVertexes = ([[CubeSize/2, CubeSize/2, -CubeSize/2, 1]])
def cube (X,Y,Z,Xmult,Ymult,Zmult):
    global NumCubes
    if not X == 0 or not Y == 0 or not Z == 0:
        Vertexes.append([CubeSize/2*Xmult+X,CubeSize/2*Ymult+Y,-CubeSize/2*Zmult+Z, 1, red, "vertex"])
        ShapeVertexes.append([CubeSize/2*Xmult+X,CubeSize/2*Ymult+Y,-CubeSize/2*Zmult+Z, 1])
    Vertexes.append ([CubeSize/2*Xmult+X,-CubeSize/2*Ymult+Y,-CubeSize/2*Zmult+Z,1,blue,"vertex"])
    ShapeVertexes.append ([CubeSize/2*Xmult+X,-CubeSize/2*Ymult+Y,-CubeSize/2*Zmult+Z,1])
    Vertexes.append ([-CubeSize/2*Xmult+X,-CubeSize/2*Ymult+Y,-CubeSize/2*Zmult+Z,1,green,"vertex"])
    ShapeVertexes.append ([-CubeSize/2*Xmult+X,-CubeSize/2*Ymult+Y,-CubeSize/2*Zmult+Z,1])
    Vertexes.append ([-CubeSize/2*Xmult+X,CubeSize/2*Ymult+Y,-CubeSize/2*Zmult+Z,1,black,"vertex"])
    ShapeVertexes.append ([-CubeSize/2*Xmult+X,CubeSize/2*Ymult+Y,-CubeSize/2*Zmult+Z,1])

    Vertexes.append ([-CubeSize/2*Xmult+X,-CubeSize/2*Ymult+Y,CubeSize/2*Zmult+Z,1,red,"vertex"])
    ShapeVertexes.append ([-CubeSize/2*Xmult+X,-CubeSize/2*Ymult+Y,CubeSize/2*Zmult+Z,1])
    Vertexes.append ([CubeSize/2*Xmult+X,-CubeSize/2*Ymult+Y,CubeSize/2*Zmult+Z,1,green,"vertex"])
    ShapeVertexes.append ([CubeSize/2*Xmult+X,-CubeSize/2*Ymult+Y,CubeSize/2*Zmult+Z,1])
    Vertexes.append ([CubeSize/2*Xmult+X,CubeSize/2*Ymult+Y,CubeSize/2*Zmult+Z,1,blue,"vertex"])
    ShapeVertexes.append ([CubeSize/2*Xmult+X,CubeSize/2*Ymult+Y,CubeSize/2*Zmult+Z,1])
    Vertexes.append ([-CubeSize/2*Xmult+X,CubeSize/2*Ymult+Y,CubeSize/2*Zmult+Z,1,black,"vertex"])
    ShapeVertexes.append ([-CubeSize/2*Xmult+X,CubeSize/2*Ymult+Y,CubeSize/2*Zmult+Z,1])
    NumCubes = NumCubes + 1
    print (NumCubes)
def CubeFaces(X):
    Faces.append([0+X,1+X,2+X,(Vertexes[0+X][2]+Vertexes[1+X][2]+Vertexes[2+X][2])/3,red,"face"])
    Faces.append([0+X,3+X,2+X,(Vertexes[0+X][2]+Vertexes[3+X][2]+Vertexes[2+X][2])/3,red,"face"])

    Faces.append([4+X,5+X,6+X,(Vertexes[4+X][2]+Vertexes[5+X][2]+Vertexes[6+X][2])/3,red,"face"])
    Faces.append([4+X,7+X,6+X,(Vertexes[4+X][2]+Vertexes[7+X][2]+Vertexes[6+X][2])/3,red,"face"])

    Faces.append([0+X,6+X,5+X,(Vertexes[0+X][2]+Vertexes[6+X][2]+Vertexes[5+X][2])/3,green,"face"])
    Faces.append([0+X,1+X,5+X,(Vertexes[0+X][2]+Vertexes[1+X][2]+Vertexes[5+X][2])/3,green,"face"])

    Faces.append([3+X,2+X,4+X,(Vertexes[3+X][2]+Vertexes[2+X][2]+Vertexes[4+X][2])/3,green,"face"])
    Faces.append([3+X,7+X,4+X,(Vertexes[3+X][2]+Vertexes[7+X][2]+Vertexes[4+X][2])/3,green,"face"])

    Faces.append([0+X,6+X,7+X,(Vertexes[0+X][2]+Vertexes[6+X][2]+Vertexes[7+X][2])/3,blue,"face"])
    Faces.append([0+X,3+X,7+X,(Vertexes[0+X][2]+Vertexes[3+X][2]+Vertexes[7+X][2])/3,blue,"face"])

    Faces.append([1+X,5+X,4+X,(Vertexes[1+X][2]+Vertexes[5+X][2]+Vertexes[4+X][2])/3,blue,"face"])
    Faces.append([1+X,2+X,4+X,(Vertexes[1+X][2]+Vertexes[2+X][2]+Vertexes[4+X][2])/3,blue,"face"])
def point():
    Vertexes.append ([0,0,200,1,black,"vertex"])
    ShapeVertexes.append ([0,0,200,1])
def PointFaces(X):
    Faces.append([4+X,5+X,8+X,(Vertexes[4+X][2]+Vertexes[5+X][2]+Vertexes[8+X][2])/3,red,"face"])
    Faces.append([5+X,6+X,8+X,(Vertexes[5+X][2]+Vertexes[6+X][2]+Vertexes[8+X][2])/3,red,"face"])
    Faces.append([6+X,7+X,8+X,(Vertexes[6+X][2]+Vertexes[7+X][2]+Vertexes[8+X][2])/3,red,"face"])
    Faces.append([7+X,4+X,8+X,(Vertexes[7+X][2]+Vertexes[4+X][2]+Vertexes[8+X][2])/3,red,"face"])

cube(0,0,0,1,1,1)
cube(0,0,100,4,1,1)
running = True
Held = False
screen.fill((75, 75, 75))
while running is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    KeysPressed = pygame.key.get_pressed()
    count = 0

    Faces = []
    for items in range(NumCubes):
        CubeFaces(8*items)

    RCords = Faces + Vertexes
    SRCords = sorted(RCords, key=lambda x: x[3])

    for items in SRCords:
        if items[5] == "face":
            pygame.draw.polygon(screen, items[4], ((Vertexes[items[0]][0] + width / 2, Vertexes[items[0]][1] + hight / 2),(Vertexes[items[1]][0] + width / 2, Vertexes[items[1]][1] + hight / 2),(Vertexes[items[2]][0] + width / 2, Vertexes[items[2]][1] + hight / 2)))
            pygame.draw.polygon(screen, black, ((Vertexes[items[0]][0] + width / 2, Vertexes[items[0]][1] + hight / 2),(Vertexes[items[1]][0] + width / 2, Vertexes[items[1]][1] + hight / 2),(Vertexes[items[2]][0] + width / 2, Vertexes[items[2]][1] + hight / 2)),1)
        if items[5] == "vertex":
            #pygame.draw.rect(screen, black, (items[0]*(1/(math.tan(30/2)*2)) + 395, items[1]*(1/(math.tan(30/2))) + 395, 10, 10))
            pygame.draw.rect(screen, black, (items[0]+ 395, items[1] + 395, 10, 10))

    if FollowMouse is True:
        RotateY = (pygame.mouse.get_pos()[0]-400)/400
        RotateX = (pygame.mouse.get_pos()[1]-400)/-400

    if KeysPressed[pygame.K_UP] is True:
        for items in Vertexes:
            RotateX = RotateX - math.pi/10000
    if KeysPressed[pygame.K_DOWN] is True:
        for items in Vertexes:
            RotateX = RotateX + math.pi/10000
    if KeysPressed[pygame.K_RIGHT] is True:
        for items in Vertexes:
            RotateY = RotateY + math.pi/10000
    if KeysPressed[pygame.K_LEFT] is True:
        for items in Vertexes:
            RotateY = RotateY - math.pi/10000
    if KeysPressed[pygame.K_q] is True:
        for items in Vertexes:
            RotateZ = RotateZ - math.pi/10000
    if KeysPressed[pygame.K_e] is True:
        for items in Vertexes:
            RotateZ = RotateZ + math.pi/10000


    count = 0
    if FullRotations is False:
        for items in Vertexes:

            items[2] = ShapeVertexes[count][2] * math.cos(RotateZ)
            items[0] = ShapeVertexes[count][0] * math.cos(RotateZ) - ShapeVertexes[count][1] * math.sin(RotateZ) + ShapeVertexes[count][2] * math.sin(RotateY)/2/math.pi
            items[1] = ShapeVertexes[count][0] * math.sin(RotateZ) + ShapeVertexes[count][1] * math.cos(RotateZ) - ShapeVertexes[count][2] * math.sin(RotateX)/2/math.pi
            count = count + 1

    elif FullRotations is True:
        for items in Vertexes:

            items[0] =  ShapeVertexes[count][0] * math.cos(RotateZ) - ShapeVertexes[count][1] *math.sin(RotateZ)
            items[1] =  ShapeVertexes[count][0] * math.sin(RotateZ) + ShapeVertexes[count][1] *math.cos(RotateZ)
            items[2] =  ShapeVertexes[count][2]

            TempY = items[1]
            TempX = items[0]
            TempZ = items[2]

            items[1] =  TempY * math.cos(RotateX) - TempZ *math.sin(RotateX)
            items[2] =  TempY * math.sin(RotateX) + TempZ *math.cos(RotateX)

            TempY = items[1]
            TempZ = items[2]

            items[0] =  TempX * math.cos(RotateY) + TempZ *math.sin(RotateY)
            items[2] =  TempX * -math.sin(RotateY) + TempZ *math.cos(RotateY)

            items[3] = items[2]
            count = count + 1

    pygame.display.flip()
    pygame.display.update()
    screen.fill((75, 75, 75))
# Quit Pygame
pygame.quit()