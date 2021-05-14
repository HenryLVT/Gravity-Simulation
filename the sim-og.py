import sys, pygame, random, math,time
import matplotlib.pyplot as plt
pygame.init()
pygame.font.init()

size = width, height = 600, 600

running = True
#Velocity in pixels per hour and time step is in hours
Yellow = (255, 255, 0)
earthM = 5.972 * 10**24
SunM = 1.989 * 10**30
Black = (0,0,0)
Red = (255,0,0)
G = 6.67408 *10 **-11
ts = 1
tsm = 3600
scaleFactor = 1.33333333 *10 **-9
Green = (0, 153, 51)
color = (0,0,0)
body2Yvelocity = -.14266666666
B2Xplot = []

Body1 = {
    "mass": SunM,
    "diam" : 0,
    "velocityX": 0,
    "velocityY": 0,
    "color": Yellow,
    "positionX" : 300,
    "positionY" : 300}

Body2 = {
    "mass": earthM,
    "diam": 0,
    "velocityX": 0,
    "velocityY": -.14266666666,
    "color": Green,
    "positionX" : 500,
    "positionY" : 300}


screen = pygame.display.set_mode(size)


def rSquared(x1,y1,x2,y2):
    aSquared =(x1-x2)**2
    bSquared =(y1-y2)**2

    cSquared = aSquared + bSquared
    
    return cSquared



def GravitionalForce(m1,m2,R):
    GForce = (G*m1*m2)/R

    return (GForce)
# X value of gravity
def GraphComponentsX(R,x1,x2,GForce):
    sqrtR = math.sqrt(R)
    a = x1-x2
    

    GforceX = a*GForce/sqrtR
    #print(GforceX)
    return(GforceX)
#Y value of gravity
def GraphComponentsY(R,y1,y2,GForce):
    sqrtR = math.sqrt(R)
    b = y1-y2

    GForceY = b*GForce/sqrtR
    #print(GForceY)
    return(GForceY)

def MoveBlob(x,y,vx,vy,ts,color,size):
    DeltaX = vx*ts
    DeltaY = vy*ts
    xn = DeltaX + x
    yn = DeltaY + y
    PutBlob(color, xn,yn,size)
    return(xn,yn)

def PutBlob(color, locationx, locationy, size):

    pygame.draw.circle(screen, color, (math.ceil(locationx), math.ceil(locationy)), size)
    pygame.display.flip()
    
def DeltaVe(GForce,tsm,m,vx,vy):
    DeltaVx = GraphComponentsY(R,y1m,y2m,GForce)*tsm/m
    DeltaVy = GraphComponentsX(R,x1m,x2m,GForce)*tsm/m
    #print(GraphComponentsY(R,y1m,y2m,GForce))
    #print(GraphComponentsX(R,x1m,x2m,GForce))
    
    vxn = DeltaVx + vx
    vyn = DeltaVy + vy
    #print(DeltaVx)
    #print(DeltaVy)
    return (vxn,vyn)

if Body1.get("mass") < Body2.get("mass"):
    Body1["diam"] = 15
    Body2["diam"] = 20

else :
    Body2["diam"] = 15
    Body1["diam"] = 20

while running == True:

    screen.fill((0,0,0))
    x1 = Body1.get("positionX")
    x2 = Body2.get("positionX")
    y1 = Body1.get("positionY")
    y2 = Body2.get("positionY")
    x1m = Body1.get("positionX")/scaleFactor
    x2m = Body2.get("positionX")/scaleFactor
    y1m = Body1.get("positionY")/scaleFactor
    y2m = Body2.get("positionY")/scaleFactor
    
    R = rSquared(x1m,y1m,x2m,y2m)
    GF = GravitionalForce(Body1.get("mass"),Body2.get("mass"),R)
    
    (DV1x,DV1y) = DeltaVe(GF, tsm,Body1.get("mass"),Body1.get("velocityX")/scaleFactor/3600,Body1.get("velocityY")/scaleFactor/3600)
    (DV2x,DV2y) = DeltaVe(-GF, tsm,Body2.get("mass"),Body2.get("velocityX")/scaleFactor/3600,Body2.get("velocityY")/scaleFactor/3600)

   
    Body1["velocityX"] = DV1x * scaleFactor * 3600
    
    Body1["velocityY"] = DV1y * scaleFactor * 3600
    Body2["velocityX"] = DV2x * scaleFactor * 3600
    Body2["velocityY"] = DV2y * scaleFactor * 3600

    #print("DV1x ", DV1x * scaleFactor)
    #print("DV1y ", DV1y * scaleFactor)
    #print("DV2x ", DV2x * scaleFactor)
    #print("DV2y ", DV2y * scaleFactor)
    #print("R ", R)
    #print("GF ", GF)
    #print(Body2.get("positionX"))
    #print(Body2.get("positionX"))
    #print(Body2.get("positionY"))
    
    
    (Body2["positionX"],Body2["positionY"]) = MoveBlob(x2,y2,Body2.get("velocityX"),Body2.get("velocityY"),ts,Body2.get("color"),Body2.get("diam"))
    
    (Body1["positionX"],Body1["positionY"]) = MoveBlob(x1,y1,Body1.get("velocityX"),Body1.get("velocityY"),ts,Body1.get("color"),Body1.get("diam"))

    B2Xplot.append(Body2.get("positionY"))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            fig, ax = plt.subplots()  # Create a figure containing a single axes.
            #ax.plot(B2Xplot)  # Plot some data on the axes.
            #plt.show(B2Xplot)
            sys.exit()

    pygame.display.flip()
