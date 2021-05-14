import sys, pygame, random, math,time
import tkinter as tk
import matplotlib.pyplot as plt
pygame.init()
pygame.font.init()
root = tk.Tk()
mnk.mainloop()

size = width, height = 1000, 650
running = True
#Velocity in pixels per hour and time step is in hours
Yellow = (255, 255, 0)
earthM = 5.972 * 10**24
SunM = 1.989 * 10**30

sunmmmm = 5.972 * 10**24
Black = (0,0,0)
Red = (255,0,0)
#Gravitational Constant
G = 6.67408 *10 **-11
#Time step
ts = 1
tsm = 3600
#scaling from pixels to meters
scaleFactor = 1.33333333 *10 **-9
Green = (0, 153, 51)
color = (0,0,0)
body2Yvelocity = -.14266666666
B2Xplot = []

#Dictionary Containing Sun Data
Body1 = {
    "mass": SunM,
    "diam" : 0,
    "velocityX": 0,
    "velocityY": 0,
    "color": Yellow,
    "positionX" : 300,
    "positionY" : 300}

#Dictionary containing Earth Data
Body2 = {
    "mass": earthM,
    "diam": 0,
    "velocityX": 0,
    "velocityY": -.14266666666,
    "color": Green,
    "positionX" : 500,
    "positionY" : 300}

#Pygame setup
screen = pygame.display.set_mode(size)

#Function for distance between two bodies
def rSquared(x1,y1,x2,y2):
    aSquared =(x1-x2)**2
    bSquared =(y1-y2)**2

    cSquared = aSquared + bSquared
    
    return cSquared


#Function for finding gravitational force between two bodies
def GravitionalForce(m1,m2,R):
    GForce = (G*m1*m2)/R
    #print(GForce)
    return (GForce)
#Function for X component of Gravity Vector
def GraphComponentsX(R,x1,x2,GForce):
    sqrtR = math.sqrt(R)
    a = x1-x2
    

    GforceX = a*GForce/sqrtR
    #print(GforceX)
    return(GforceX)
#Function for Y component of Gravity Vector
def GraphComponentsY(R,y1,y2,GForce):
    sqrtR = math.sqrt(R)
    b = y1-y2

    GForceY = b*GForce/sqrtR
    #print(GForceY)
    return(GForceY)
#Function for animating a Circle
def MoveBlob(x,y,vx,vy,ts,color,size):
    DeltaX = vx*ts
    DeltaY = vy*ts
    xn = DeltaX + x
    yn = DeltaY + y
    PutBlob(color, xn,yn,size)
    return(xn,yn)
#Function For Placing a circle in a specific place
def PutBlob(color, locationx, locationy, size):
    pygame.draw.circle(screen, color, (math.ceil(locationx), math.ceil(locationy)), size)
    pygame.display.flip()
    
#function for determing Velocity using gravity
def DeltaVe(GForce,tsm,m,vx,vy):
    DeltaVy = GraphComponentsY(R,y1m,y2m,GForce)*tsm/m
    DeltaVx = GraphComponentsX(R,x1m,x2m,GForce)*tsm/m
    #print(GraphComponentsY(R,y1m,y2m,GForce))
    #print(GraphComponentsX(R,x1m,x2m,GForce))
    
    vxn = vx - DeltaVx 
    vyn = vy - DeltaVy
    #print(DeltaVx)
    #print(DeltaVy)
    return (vxn,vyn)

if Body1.get("mass") < Body2.get("mass"):
    Body1["diam"] = 15
    Body2["diam"] = 20

elif Body1.get("mass") == Body2.get("mass"):
    Body1["diam"] = 20
    Body2["diam"] = 20

else :
    Body2["diam"] = 15
    Body1["diam"] = 20

while running == True:
    #Setting up variables
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
    #main calculation for Earth
    (DV1x,DV1y) = DeltaVe(GF, tsm,Body1.get("mass"),Body1.get("velocityX")/scaleFactor/tsm,Body1.get("velocityY")/scaleFactor/tsm)
    
    #main calculation for Sun
    (DV2x,DV2y) = DeltaVe(-GF, tsm,Body2.get("mass"),Body2.get("velocityX")/scaleFactor/tsm,Body2.get("velocityY")/scaleFactor/tsm)

   #Setting up more Variables
    Body1["velocityX"] = DV1x * scaleFactor * tsm 
    Body1["velocityY"] = DV1y * scaleFactor * tsm 
    Body2["velocityX"] = DV2x * scaleFactor * tsm
    Body2["velocityY"] = DV2y * scaleFactor * tsm

    #"Trouble shooting"
    #print("DV1x ", DV1x * scaleFactor)
    #print("DV1y ", DV1y * scaleFactor)
    #print("DV2x ", DV2x * scaleFactor)
    #print("DV2y ", DV2y * scaleFactor)
    #print("R ", R)
    #print("GF ", GF)
    #print(Body2.get("positionX"))
    #print(Body2.get("positionX"))
    #print(Body2.get("positionY"))
    
    #displaying Calculations
    (Body2["positionX"],Body2["positionY"]) = MoveBlob(x2,y2,Body2.get("velocityX"),Body2.get("velocityY"),ts,Body2.get("color"),Body2.get("diam"))
    
    (Body1["positionX"],Body1["positionY"]) = MoveBlob(x1,y1,Body1.get("velocityX"),Body1.get("velocityY"),ts,Body1.get("color"),Body1.get("diam"))

    #B2Xplot.append(Body2.get("positionY"))
    def ChgB1m():
        Body1[mass] = Body1MassEntry.get()
    Label1 = Label(root,text = "change values")
    Label1.grid(column = 0, row = 1)

    Body1MassEntry = Entry(root,bd = 5)
    Body1MassEntry.grid(column = 0,row = 2) 

    ChangeBody1m = Button(root, text = "Change Body 1 mass", bg ="blue", command = ChgB1m)
    ChangeBody1m.grid(column = 1,row = 3)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #fig, ax = plt.subplots()
            #Create a figure containing a single axes.
            #ax.plot(B2Xplot)
            #Plot some data on the axes.
            #plt.show(B2Xplot)
            sys.exit()
            

    pygame.display.flip()



