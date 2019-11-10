#Hamza Sayed-Ali ---------- Paint New York City


#sets up pygame
from pygame import *
init()
#sets up fonts
font.init()
titleFont=font.SysFont("Ariel",48)
infoFont=font.SysFont("Ariel",24)
#sets up tk window
from tkinter import *
root=Tk()
root.withdraw()

from random import *

################################################
#initializes display size and creates display
displaySize=(1024,768)
screen=display.set_mode(displaySize)
#sets constants
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

size=5

#sets display caption
display.set_caption("Paint NYC")

running=True#indicates that the program is running

####### loading lists ######
#list of all tools
tools=["pencil","eraser","brush","line","polygon","shape","colorPicker","fill","spray","filter","highlighter","save","open","undo","redo","stamp","no_tool"]

####### Loading Images #######
#loads all tool icons
pencilIcon=image.load("Images/pencil.png")
eraserIcon=image.load("Images/eraser.png")
brushIcon=image.load("Images/brush.png")
lineIcon=image.load("Images/line.png")
polygonIcon=image.load("Images/polygon.png")
shapesIcon=image.load("Images/shapes.png")
emptyShapesIcon=image.load("Images/emptyShapes.png")
fillIcon=image.load("Images/fill.png")
eyedropperIcon=image.load("Images/eyedropper.png")
spraypaintIcon=image.load("Images/spraypaint.png")
filterIcon=image.load("Images/filter.png")
highlighterIcon=image.load("Images/highlighter.png")
saveIcon=image.load("Images/save.png")
openIcon=image.load("Images/open.png")
undoIcon=image.load("Images/undo.png")
redoIcon=image.load("Images/redo.png")
#loads background images
background=image.load("Images/background.jpg")
transparent=image.load("Images/transparent.jpg")
#loads color gradient
colorPicker=image.load("Images/colorgradiant.jpg")
#loads shape icons
rectangleIcon=image.load("Images/rectangle.png")
ellipseIcon=image.load("Images/ellipse.png")
triangleIcon=image.load("Images/triangle.png")
pentagonIcon=image.load("Images/pentagon.png")
hexagonIcon=image.load("Images/hexagon.png")
#loads filter icons
blackandwhiteIcon=image.load("Images/blackandwhite.png")
sepiaIcon=image.load("Images/sepia.png")
invertIcon=image.load("Images/invert.png")

#loads stamps
stamps=[]
stampNames=["timb.png",'hat.png','bagel.png','statue.png','empire.png','mixtape.png','taxi.png','iheart.png']
for name in stampNames:
    #takes each stamp name from list and loads the files
    stamp=image.load("Images/"+name)
    stamps.append(stamp)#adds image to list of stamps
#loads backgrounds
backgrounds=[]
backgroundNames=['timesSquare.jpg','street.jpg',"centralPark.jpg",'brooklyn.jpg','clear.png']
for name in backgroundNames:
    #takes each background name from list and loads the files
    b=image.load("Images/"+name)
    backgrounds.append(b)#adds image to list of backgrounds
    


#draws background to screen
screen.blit(background,(0,0))
#draws border rectangle to screen
draw.rect(screen,BLACK,(90,50,820,620))



###### Text Stuff ########
#loads title text as a surface
title=titleFont.render("PAINT NEW YORK CITY",True,BLACK)
#draws title to screen
screen.blit(title, (130,10))

#loads info text for size
sizeInfo=infoFont.render("Size: "+str(size),True,BLACK)
#draws background rectangle
draw.rect(screen,(200,200,200),(545,15,80,25))
#draws text to screen
screen.blit(sizeInfo, (550,20))

#loads info text for tool tips
toolTipText="Up and Down to change size"
toolInfo=infoFont.render(toolTipText,True,BLACK)
draw.rect(screen,(200,200,200),(635,15,275,25))
#draws text to screen
screen.blit(toolInfo,(640,20))


###### Creating rectangles ######
menuRect=Rect(0,0,40,440)
draw.rect(screen,(200,200,200),menuRect)#draws background rect for tools menu
#creates canvas and canvas rect
canvasRect=Rect(100,60,800,600)
screen.set_clip(canvasRect)
screen.blit(transparent,(100,60))
screen.set_clip(None)
canvas=Surface((displaySize),SRCALPHA)
#creates color pallette rect and draws color pallette to screen
palRect=Rect(20,680,200,80)
pallette=Surface((200,80))
pallette.blit(colorPicker,(0,0))
screen.blit(pallette,(20, 680))
#creates rectangles for all the shapes
rectangleRect=Rect(41,200,40,40)
ellipseRect=Rect(41,240,40,40)
triangleRect=Rect(41,280,40,40)
pentagonRect=Rect(41,320,40,40)
hexagonRect=Rect(41,360,40,40)
#creates surface and rect for the shapes menu bar
shapesBar=Surface((40,200))
shapesBarRect=Rect(40,200,42,200)
#draws each shape icon to the menu bar surface
draw.rect(shapesBar,(200,200,200),(1,0,40,200))
shapesBar.blit(rectangleIcon,(1,0))
shapesBar.blit(ellipseIcon,(1,40))
shapesBar.blit(triangleIcon,(1,80))
shapesBar.blit(pentagonIcon,(1,120))
shapesBar.blit(hexagonIcon,(1,160))
#draws each shape rectangle to the menu bar surface
draw.rect(shapesBar,(100,100,230),(0,0,40,40),2)
draw.rect(shapesBar,(100,100,230),(0,40,40,40),2)
draw.rect(shapesBar,(100,100,230),(0,80,40,40),2)
draw.rect(shapesBar,(100,100,230),(0,120,40,40),2)
draw.rect(shapesBar,(100,100,230),(0,160,40,40),2)
#creates surface for filters menu bar
filtersBar=Surface((40,120))
filtersBarRect=Rect(40,120,42,360)
#creates rectangles for each filter
greyscaleRect=Rect(41,360,40,40)
sepiaRect=Rect(41,400,40,40)
invertRect=Rect(41,440,40,40)
#draws icons for each surface onto filters menu bar surface
filtersBar.blit(blackandwhiteIcon,(1,0))
filtersBar.blit(sepiaIcon,(1,40))
filtersBar.blit(invertIcon,(1,80))
#draws rectangles for each filter onto filters menu bar surface
draw.rect(filtersBar,(100,100,230),(0,0,40,40),2)
draw.rect(filtersBar,(100,100,230),(0,40,40,40),2)
draw.rect(filtersBar,(100,100,230),(0,80,40,40),2)


##tools##
#creates list fot all the too' rectangles
toolsRects=[]

pencilRect=Rect(0,0,40,40)#creates tool's rectangle
toolsRects.append(pencilRect)#adds the tool's rectangle to the list
screen.blit(pencilIcon,(0,0))#draws tool's icon to the screen

eraserRect=Rect(0,40,40,40)
toolsRects.append(eraserRect)
screen.blit(eraserIcon,(0,40))

brushRect=Rect(0,80,40,40)
toolsRects.append(brushRect)
screen.blit(brushIcon,(0,80))

lineRect=Rect(0,120,40,40)
toolsRects.append(lineRect)
screen.blit(lineIcon,(0,120))

polygonRect=Rect(0,160,40,40)
toolsRects.append(polygonRect)
screen.blit(polygonIcon,(0,160))

shapeRect=Rect(0,200,40,40)
toolsRects.append(shapeRect)
screen.blit(shapesIcon,(0,200))

colorPickerRect=Rect(0,240,40,40)
toolsRects.append(colorPickerRect)
screen.blit(eyedropperIcon,(0,240))

fillRect=Rect(0,280,40,40)
toolsRects.append(fillRect)
screen.blit(fillIcon,(0,280))

sprayRect=Rect(0,320,40,40)
toolsRects.append(sprayRect)
screen.blit(spraypaintIcon,(0,320))

filterRect=Rect(0,360,40,40)
toolsRects.append(filterRect)
screen.blit(filterIcon,(0,360))

highlighterRect=Rect(0,400,40,40)
toolsRects.append(highlighterRect)
screen.blit(highlighterIcon,(0,400))

saveRect=Rect(944,0,40,40)
toolsRects.append(saveRect)
screen.blit(saveIcon,(944,0))

openRect=Rect(984,0,40,40)
toolsRects.append(openRect)
screen.blit(openIcon,(984,0))

undoRect=Rect(40,0,40,40)
toolsRects.append(undoRect)
screen.blit(undoIcon,(40,0))

redoRect=Rect(80,0,40,40)
toolsRects.append(redoRect)
screen.blit(redoIcon,(80,0))


##stamps##
#draws rectangles for all the stamps to the screen
for i in range(0,8):
    draw.rect(screen,(200,200,200,150),(920,50+i*90,80,80))
#creates a list for all the stamp rectangles
stampsRects=[]

timbRect=Rect(920,50,80,80)#creates a rectangle for the stamp
stampsRects.append(timbRect)#adds the stamp's rectangle to tyhe list of stamps
screen.blit(transform.scale(stamps[0],(80,80)),(920,50))#draws stamp icon to screen

hatRect=Rect(920,140,80,80)
stampsRects.append(hatRect)
screen.blit(transform.scale(stamps[1],(80,80)),(920,140))

bagelRect=Rect(920,230,80,80)
stampsRects.append(bagelRect)
screen.blit(transform.scale(stamps[2],(80,80)),(920,230))

statueRect=Rect(920,320,80,80)
stampsRects.append(statueRect)
screen.set_clip(statueRect)#only allows drawing on the surface of the rectangle to fit the icon better
screen.blit(transform.scale(stamps[3],(80,150)),(920,320))
screen.set_clip(None)#allows drawing anywhere again

towerRect=Rect(920,410,80,80)
stampsRects.append(towerRect)
screen.set_clip(towerRect)#only allows drawing on the surface of the rectangle to fit the icon better
screen.blit(transform.scale(stamps[4],(80,200)),(920,390))
screen.set_clip(None)#allows drawing anywhere again

mixtapeRect=Rect(920,500,80,80)
stampsRects.append(mixtapeRect)
screen.blit(transform.scale(stamps[5],(80,80)),(920,500))

taxiRect=Rect(920,590,80,80)
stampsRects.append(taxiRect)
screen.blit(transform.scale(stamps[6],(80,60)),(920,600))

iheartRect=Rect(920,680,80,80)
stampsRects.append(iheartRect)
screen.blit(transform.scale(stamps[7],(80,80)),(920,680))

##Backgrounds##

backgroundsRects=[]#creates a list for all the background rectangles

timesSquareRect=Rect(280,680,80,80)#creates a rectangle for the background
backgroundsRects.append(timesSquareRect)#adds the background's rectangle to the list of all backgrounds
tsIcon=transform.scale(backgrounds[0],(120,80))#makes the icon smaller to fit the rectangle
screen.set_clip(timesSquareRect)#only allows drawing on the background's rectangle to make the icon fit nicer
screen.blit(tsIcon,(280,680))#draws the icon to the screen


streetRect=Rect(370,680,80,80)
backgroundsRects.append(streetRect)
screen.set_clip(streetRect)
sIcon=transform.scale(backgrounds[1],(120,80))
screen.blit(sIcon,(370,680))

parkRect=Rect(460,680,80,80)
backgroundsRects.append(parkRect)
screen.set_clip(parkRect)
pIcon=transform.scale(backgrounds[2],(120,80))
screen.blit(pIcon,(460,680))

brooklynRect=Rect(550,680,80,80)
backgroundsRects.append(brooklynRect)
screen.set_clip(brooklynRect)
bIcon=transform.scale(backgrounds[3],(120,80))
screen.blit(bIcon,(540,680))

clearRect=Rect(640,680,80,80)
backgroundsRects.append(clearRect)
screen.set_clip(clearRect)
cIcon=transform.scale(backgrounds[4],(120,80))
screen.blit(cIcon,(640,680))


screen.set_clip(None)#allows drawing on the whole screen

####### setting tracker variables
backImage=transparent
backImage.fill((255,255,255,255))#makes the background white

history=[]#creates a list for the history of changes to allow undoing
frame=canvas.copy()#copies the canvas before any changes
history.append(frame)#adds the blank canvas to the history


redoList=[]#creates a list for redoing

tool="pencil"#creates a tool variable

size=5#creates size variable

col=GREEN#creates color variable
draw.rect(screen,col,(240,720,25,25))#draws color indicator

shape="rectangle"#sets shape variable
shapesBarOpened=False#keeps track of if the shapes menu is opened
fill=1#keeps track of if the shape is filled or unfilled

filtersBarOpened=False#keeps track of if the filters menu is opened

shift=False#keeps track of if the user is pressing shift

polygonStarted=False#keeps track of if the user is currently drawing a polygon
polygonPoints=[]#keeps track of polygon points

usedPixels=set()#keeps track of pixels used in filter

highlighter=Surface(displaySize,SRCALPHA)#creates a surface for the highlighter

#main running loop, runs every frame
while running:
    #resets one time variables
    clicked=False
    released=False
    #event loop
    for evt in event.get():
        if evt.type==QUIT:
            running=False#exits if the x is clicked
        #checks if the user clicked down
        if evt.type==MOUSEBUTTONDOWN:
            if mouse.get_pressed()[0]==1:
                cPos=mouse.get_pos()#keeps track of where the user first clicks
                back=canvas.copy()#copies the canvas when clicked down to allow for drawing shapes and lines
                clicked=True#indicates the user clicked down during this iteration
            if mouse.get_pressed()[2]==1:
                if polygonStarted:#closes the polygon if the user is drawing a polygon
                    draw.line(canvas,col,polygonPoints[0],polygonPoints[-1],size)
                    polygonStarted=False
                    polygonPoints=[]
                    redoList=[]
                    frame=canvas.copy()#adds frame to the undo list
                    history.append(frame)
        if evt.type==MOUSEBUTTONUP:
            if evt.button==1:
                released=True#indicates the user released the mouse during that iteration
                if tool=="highlighter":#draws the highlighter surface to the canvas
                    canvas.blit(highlighter,(0,0))
                    highlighter.fill((0,0,0,0))
        if evt.type==KEYDOWN:
            if evt.key==K_UP:
                size+=1#increases the size
                if size>200:
                    size=200
                sizeInfo=infoFont.render("Size: "+str(size),True,BLACK)#updates the size info and draws the new size to the info bar
                draw.rect(screen,(200,200,200),(545,15,80,25))
                screen.blit(sizeInfo, (550,20))
            
                
            if evt.key==K_DOWN:
                size-=1#decreases the size
                if size<1:
                    size=1
                sizeInfo=infoFont.render("Size: "+str(size),True,BLACK)#updates the size info and draws the new size to the info bar
                draw.rect(screen,(200,200,200),(545,15,80,25))
                screen.blit(sizeInfo, (550,20))

            if evt.key==K_z:
                try:#tries to undo and passes if it cannot do it
                    if len(history)>1:#checks if there is more than one thing in the history to undo
                        screen.set_clip(canvasRect)
                        canvas.fill((0,0,0,0))#clears canvas
                        canvas.blit(history[-2],(0,0))#draws the second last thing from the history
                        redoList.append(history.pop())#adds the last thing from the history to the redo list
                        screen.set_clip(None)

                        polygonStarted=False#stopps drawing a polygon if its being drawn
                except:
                    pass
            if evt.key==K_r:
                try:#tries to redo and passes it it cannot
                    if len(redoList)>0:#checks if there is something to redo
                        screen.set_clip(canvasRect)
                        canvas.fill((0,0,0,0))#clears the canvas
                        canvas.blit(redoList[-1],(0,0))#draws the last thing from the redo list
                        history.append(redoList.pop())#adds the last thing from the redo list to the undo list
                except:
                    pass
                    
                    
            if evt.key==K_RSHIFT or evt.key==K_LSHIFT:
                shift=True#indicates the user is pressing shift
        if evt.type==KEYUP:
            if evt.key==K_RSHIFT or evt.key==K_LSHIFT:
                shift=False#indicates the user is not pressing shift
            
    mx,my=mouse.get_pos()#gets the mouse's current position
    mb=mouse.get_pressed()#gets the state of the mouse buttons
    
    for rect in toolsRects:
        draw.rect(screen,(100,100,230),rect,2)#draws rectangles for all the tools

    for rect in stampsRects:
        draw.rect(screen,(100,100,230),rect,2)#draws rectangles for all the stamps

    for rect in backgroundsRects:
        draw.rect(screen,(100,100,230),rect,2)#draws rectangles for all the backgrounds

    for i in range(0,5):#draws rectangles for all shapes in the menu bar
        draw.rect(shapesBar,(100,100,230),(0,i*40,40,40),2)
        if shape == "rectangle":#draws a red rectangle around the selected tool
            draw.rect(shapesBar,(RED),(0,0,40,40),2)
        if shape == "ellipse":
            draw.rect(shapesBar,(RED),(0,40,40,40),2)
        if shape == "triangle":
            draw.rect(shapesBar,(RED),(0,80,40,40),2)
        if shape == "pentagon":
            draw.rect(shapesBar,(RED),(0,120,40,40),2)
        if shape == "hexagon":
            draw.rect(shapesBar,(RED),(0,160,40,40),2)
        

    if palRect.collidepoint(mx,my) and mb[0]==1:#checks if the user clicks on the color pallette
        col=screen.get_at((mx,my))#sets the color to the one at the point they clicked
        draw.rect(screen,col,(240,720,25,25))#draws the color indicator rect

    toolInfo=infoFont.render(toolTipText,True,BLACK)#renders the updated tool info
    draw.rect(screen,(200,200,200),(635,15,275,25))
    screen.blit(toolInfo,(640,20))#draws the updated tool info
    

    ##### selecting tool

    if pencilRect.collidepoint(mx,my):#checks if the mouse is over the specific tool
        draw.rect(screen,BLUE,pencilRect,2)#highlights the tool with a bright blue rectangle indicating it can be selected
        if mb[0]==1:#checks if the user clicks on the tool rectangle
            tool="pencil"#sets the tool to the intended tool
            toolTipText="Pencil - Click to draw"#changes the tool tip to match the tool
            draw.rect(screen,RED,pencilRect,2)#draws a red indicator rectangle indicating the tool is selected
    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,eraserRect,2)
        if mb[0]==1:
            tool="eraser"
            toolTipText="Eraser - Click to erase"
            draw.rect(screen,RED,eraserRect,2)
    if brushRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,brushRect,2)
        if mb[0]==1:
            tool="brush"
            toolTipText="Brush - Click to paint"
            draw.rect(screen,RED,brushRect,2)
    if lineRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,lineRect,2)
        if mb[0]==1:
            tool="line"
            toolTipText="Line - Click and drag to draw"
            draw.rect(screen,RED,lineRect,2)
    if polygonRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,polygonRect,2)
        if mb[0]==1:
            tool="polygon"
            toolTipText="Left click to draw, Right to finish"
            draw.rect(screen,RED,polygonRect,2)
    if shapeRect.collidepoint(mx,my):
        shapesBarOpened=True#indicates that the shape bar should be opened and drawn on the screen
        screen.blit(shapesBar,(41,200))#draws the shape bar to the screen
        draw.rect(screen,BLUE,shapeRect,2)#highlights the tool with a bright blue rectangle indicating it can be selected
        
        if mb[0]==1 and clicked:#checks if the user clicked during that specific itteration of the loop
            toolTipText="Click to fill or unfill"#changes the tool tip to match the tool
            fill*=-1#toggles the fill or unfill of the shapes
            draw.rect(screen,(200,200,200),shapeRect)#draws the background rectangle for the shape bar
            if fill==1:
                screen.blit(shapesIcon,(0,200))#draws filled in shapes icon if the fill is true
            else:
                screen.blit(emptyShapesIcon,(0,200))#draws empty shapes icon if the fill is false
            tool="shape"#sets the tool variable to the correct tool
            draw.rect(screen,RED,shapeRect,2)#draws a red rectangle highlighting the fact that the shapes tool is selected
    if shapesBarOpened and shapesBarRect.collidepoint(mx,my):#checks if the shapes bar should be opened and the mose if over the shapes bar
        screen.blit(shapesBar,(41,200))#draws shapes menu to screen
        if rectangleRect.collidepoint(mx,my):#checks if the mouse is over the intended shape
            draw.rect(screen,(BLUE),rectangleRect,1)
            if mb[0]==1:
                shape="rectangle"#sets the shape variable to the intended shape
                toolTipText="Rectangle - Shift for square"
                tool="shape"
            
        if ellipseRect.collidepoint(mx,my):
            draw.rect(screen,(BLUE),ellipseRect,1)
            if mb[0]==1:
                shape="ellipse"
                toolTipText="Ellipse - Shift for circle"
                tool="shape"
                
        if triangleRect.collidepoint(mx,my):
            draw.rect(screen,(BLUE),triangleRect,1)
            
            if mb[0]==1:
                shape="triangle"
                toolTipText="Isoceles triangle"
                tool="shape"
        if pentagonRect.collidepoint(mx,my):
            draw.rect(screen,(BLUE),pentagonRect,1)
            if mb[0]==1:
                shape="pentagon"
                toolTipText="Pentagon"
                tool="shape"
        if hexagonRect.collidepoint(mx,my):
            draw.rect(screen,(BLUE),hexagonRect,1)
            if mb[0]==1:
                shape="hexagon"
                toolTipText="Hexagon"
                tool="shape"
                
    if shapesBarOpened and shapesBarRect.collidepoint(mx,my) == False and shapeRect.collidepoint(mx,my) == False:#checks if the shape menu shoulf be closed
        screen.set_clip(shapesBarRect)#only allows the area on the menu rect to be edited
        screen.blit(background,(0,0))#redraws the background over the shapes menu
        screen.set_clip(None)#allows drawing on the whole screen
        shapesBarOpened=False#indicates the shapes bar should stay closed
        
            

    for i in range(0,len(stampsRects)):#goes through all the stamps
        if stampsRects[i].collidepoint(mx,my):
            draw.rect(screen,BLUE,stampsRects[i],2)
            if mb[0]==1:#checks if the user clicked on the stamp rectangle
                draw.rect(screen,RED,stampsRects[i],2)
                tool="stamp"
                toolTipText="Stamp - Click and drag"
                stamp=stamps[i]#sets the stamp to the intended stamp

    for i in range(0,len(backgroundsRects)):#goes through all the backgrounds
        if backgroundsRects[i].collidepoint(mx,my):
            draw.rect(screen,BLUE,backgroundsRects[i],2)
            if mb[0]==1:#checks if the user clicked on a background
                draw.rect(screen,RED,backgroundsRects[i],2)
                bg=backgrounds[i]#sets the background to the intended background
                bg=transform.scale(bg,(800,600))#scales the background to fit the canvas
                backImage.fill((0,0,0,0))#clears the background
                backImage.blit(bg,(canvasRect[0],canvasRect[1]))#draws the new background
            
                
    if colorPickerRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,colorPickerRect,2)
        if mb[0]==1:
            tool="colorPicker"
            toolTipText="Eye dropper - click to pick a color"
            draw.rect(screen,RED,colorPickerRect,2)
    if fillRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,fillRect,2)
        if mb[0]==1:
            toolTipText="Fill bucket"
            tool="fill"
            draw.rect(screen,RED,fillRect,2)
    if sprayRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,sprayRect,2)
        if mb[0]==1:
            toolTipText="Spray paint"
            tool="spray"
            draw.rect(screen,RED,sprayRect,2)
            
    if filterRect.collidepoint(mx,my):
        filtersBarOpened=True
        screen.blit(filtersBar,(41,360))
        draw.rect(screen,BLUE,filterRect,2)
                
        if mb[0]==1 and clicked:
            tool="filter"
            draw.rect(screen,RED,filterRect,2)
    if filtersBarOpened and filtersBarRect.collidepoint(mx,my):
        if clicked:#checks if the user clicked the filter menu
            if greyscaleRect.collidepoint(mx,my):#checks if the filter was clicked on
                for x in range(0,799):#goes through all the pixels on the canvas
                    for y in range(0,599):
                        r,g,b,a=canvas.get_at((canvasRect[0]+x,canvasRect[1]+y))#gets the rgba of the given pixel
                        s=int(0.2126*r + 0.7152*g + 0.0722*b)#modifies the rgba to make it match the filter
                        canvas.set_at((canvasRect[0]+x,canvasRect[1]+y),(s,s,s,a))#redraws the pixel with the new rgba
                
                tool="filter"#sets the tool to filter
                toolTipText="Black and white"#updates the tool tip text
            if sepiaRect.collidepoint(mx,my):
                for x in range(0,799):
                    for y in range(0,599):
                        r,g,b,a=canvas.get_at((canvasRect[0]+x,canvasRect[1]+y))
                        r2=min(255,int(r*.393+g*.769+b*.189))
                        g2=min(255,int(r*.349+g*.686+b*.168))
                        b2=min(255,int(r*.272+g*.534+b*.131))
                        canvas.set_at((canvasRect[0]+x,canvasRect[1]+y),(r2,g2,b2,a))
                    
                tool="filter"
                toolTipText="Sepia"
            if invertRect.collidepoint(mx,my):
                for x in range(0,799):
                    for y in range(0,599):
                        r,g,b,a=canvas.get_at((canvasRect[0]+x,canvasRect[1]+y))
                        r2=255-r
                        g2=255-g
                        b2=255-b
                        canvas.set_at((canvasRect[0]+x,canvasRect[1]+y),(r2,g2,b2,a))
                tool="filter"
                toolTipText="Invert colors"
            frame=canvas.copy()#copies the canvas 
            history.append(frame)#adds the copy to the history list for undoing
    if filtersBarOpened and filtersBarRect.collidepoint(mx,my) == False and filterRect.collidepoint(mx,my) == False:
        screen.set_clip(filtersBarRect)
        screen.blit(background,(0,0))
        screen.set_clip(None)
        filtersBarOpened=False

    if highlighterRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,highlighterRect,2)
        if mb[0]==1:
            tool="highlighter"
            toolTipText="Highlighter"
            draw.rect(screen,RED,highlighterRect,2)
    
    if saveRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,saveRect,2)
        if mb[0]==1:
            tool="save"
            draw.rect(screen,RED,saveRect,2)
    if openRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,openRect,2)
        if mb[0]==1:
            tool="open"
            draw.rect(screen,RED,openRect,2)

    if undoRect.collidepoint(mx,my):#same as undo in event loop
        draw.rect(screen,BLUE,undoRect,2)
        if clicked:
            draw.rect(screen,RED,undoRect,2)
            try:
                if len(history)>1:
                    screen.set_clip(canvasRect)
                    canvas.fill((0,0,0,0))
                    canvas.blit(history[-2],(0,0))
                    redoList.append(history.pop())
                    screen.set_clip(None)

                    polygonStarted=False
            except:
                pass
    if redoRect.collidepoint(mx,my):#same as redo in event loop
        draw.rect(screen,BLUE,redoRect,2)
        if clicked:
            draw.rect(screen,RED,redoRect,2)
            try:
                if len(redoList)>0:
                    screen.set_clip(canvasRect)
                    canvas.fill((0,0,0,0))
                    canvas.blit(redoList[-1],(0,0))
                    history.append(redoList.pop())
            except:
                pass
            
    for rect in toolsRects:
        if toolsRects.index(rect)==tools.index(tool):
          draw.rect(screen,RED,rect,2)#draws red rectangle around selected tool to indicate to user

    

    #### using tool

    if canvasRect.collidepoint(mx,my) and mb[0]==1:#checks if the user clicked on the canvas
        canvas.set_clip(canvasRect)#only allows the canvas to be modified
        
        if tool=="pencil":#checks if the user has selected that tool
            draw.line(canvas,col,(omx,omy),(mx,my))#draws a line between the mouses current position and its previous position
        if tool=="eraser":
            dx=mx-omx
            dy=my-omy
            dist=int((dx**2+dy**2)**0.5)#finds the length of how far the user has moved the mouse since the last frame
            for i in range(1,dist+1):#goes through all the points between the mouses current position and its last
                dotX=int(omx+i*dx/dist)
                dotY=int(omy+i*dy/dist)
                try:
                    eraser=Rect(dotX-size/2,dotY-size/2,size,size)
                    canvas.subsurface(eraser).fill((0,0,0,0))#sets the eraser area to transparent at every point between the current and previous position
                except:
                    pass
        if tool=="brush":
            draw.circle(canvas,(col),(mx,my),int(size/2))#draws a circle at the location of the mouse
            dx=mx-omx
            dy=my-omy
            dist=int((dx**2+dy**2)**0.5)#finds the length of how far the user has moved the mouse since the last frame
            for i in range(1,dist+1):
                dotX=int(omx+i*dx/dist)
                dotY=int(omy+i*dy/dist)
                draw.circle(canvas,(col),(dotX,dotY),int(size/2))#draws circles at every point between the mouses current and previous position
        if tool=="line":
            canvas.fill((0,0,0,0))#clears the canvas
            canvas.blit(back,(0,0))#redraws the canvas as it was before the user first clicked the screen
            dx=mx-cPos[0]
            dy=my-cPos[1]
            dist=int((dx**2+dy**2)**0.5)
            for i in range(1,dist+1):
                dotX=int(cPos[0]+i*dx/dist)
                dotY=int(cPos[1]+i*dy/dist)
                draw.circle(canvas,col,(dotX,dotY),int(size/2))#draws circles at every point between where the user originally clicked down and the current mouse position
            
        if tool=="polygon":
            if polygonStarted==False:#checks if the user hasn't already started drawing a polygon
                polygonPoints=[]#clears the list of polygon points
                polygonPoints.append((mx,my))#adds the starting position to the list
                polygonStarted=True#indicates the user has started drawing a polygon
            if clicked==False:
                polygonPoints.pop()#removes the current point if the user hasn't clicked down in that itteration
            canvas.fill((0,0,0,0))
            canvas.blit(back,(0,0))#clears the canvas and redraws what was on it before the user clicked down
            dx=mx-polygonPoints[-1][0]
            dy=my-polygonPoints[-1][1]
            dist=int((dx**2+dy**2)**0.5)
            for i in range(1,dist+1):
                dotX=int(polygonPoints[-1][0]+i*dx/dist)
                dotY=int(polygonPoints[-1][1]+i*dy/dist)
                draw.circle(canvas,col,(dotX,dotY),int(size/2))#draws circles between the last point in the list of polygon points and the current mouse loaction
                
            polygonPoints.append((mx,my))#adds the current mouse location to the list of polygon points
                
                
        if tool=="shape":
            canvas.fill((0,0,0,0))
            canvas.blit(back,(0,0))#clears the canvas and redraws what was on it before the user clicked down
            

            x=min(cPos[0],mx)
            y=min(cPos[1],my)#x and y used for ellipse, find the minimum value to be the starting point of the shape
            w=mx-cPos[0]#calculates the width of the shape
            h=my-cPos[1]#caslculates the height of the shape
            
            s=min(abs(w),abs(h))#size used for square and circle, minimum of width and height
            
            if fill==1:
                f=0#sets the fill to be completely full if fill is true
            else:
                f=1#sets the fill to the size if fill is false
            
            if shape=="no_shape":
                pass #checks if no shape is selected
            elif shape=="rectangle":
                w=max(cPos[0],mx)-x
                h=max(cPos[1],my)-y
                if f==0:#draws filled in rectangle
                    if shift==True:#draws a square if shift is pressed
                        w=abs(mx-cPos[0])
                        h=abs(my-cPos[1])
                        draw.rect(canvas,col,(cPos[0],cPos[1],s,s),0)#draws the square
                    else:
                        draw.rect(canvas,col,(x,y,abs(w),abs(h)),0)#draws normal rectangle if shift isnt pressed
                else:
                    if shift==True:
                        w=abs(mx-cPos[0])
                        h=abs(my-cPos[1])
                        for i in range(0,size):#draws the correct number of small rectangles to fit the size to make a clean rectangle, each one is 1 pixel smaller than the last
                            draw.rect(canvas,col,(cPos[0]+i,cPos[1]+i,s-2*i,s-2*i),1)
                    else:
                        for i in range(0,size):
                            draw.rect(canvas,col,(x+i,y+i,w-2*i,h-2*i),1)      
                
            elif shape=="ellipse":
    
                x=min(cPos[0],mx)
                y=min(cPos[1],my)
                w=abs(mx-cPos[0])
                h=abs(my-cPos[1])
                try:#attempts to draw the ellipse
                    if shift==True:
                        draw.ellipse(canvas,col,(cPos[0],cPos[1],s,s),f*size)#draws ellipse with equal width and height if shift is pressed
                    else:
                        draw.ellipse(canvas,col,(x,y,w,h),f*size)#draws normal ellipse if shift isn't pressed
                except:
                    pass
            elif shape=="triangle":

                x = (mx+cPos[0])/2
                y = my
                
                draw.polygon(canvas,col,((mx,cPos[1]),(cPos),(x,y)),f*size)#draws triangle with 2 equal sides
            elif shape=="pentagon":
                x = (mx+cPos[0])/2
                y = my
                #calculates points and draws pentagon
                draw.polygon(canvas,col,((int(cPos[0]+w/2),cPos[1]),(cPos[0]+w,cPos[1]+int(2*h/5)),(cPos[0]+int(4*w/5),cPos[1]+h),(cPos[0]+int(w/5),cPos[1]+h),(cPos[0],cPos[1]+int(2*h/5))),f*size)
            elif shape=="hexagon":
                x = (mx+cPos[0])/2
                y = my
                #calculates points and draws pentagon
                draw.polygon(canvas,col,((int(cPos[0]+w/4),cPos[1]),(int(cPos[0]+3*w/4),cPos[1]),(cPos[0]+w,cPos[1]+h/2),(int(cPos[0]+3*w/4),cPos[1]+h),(int(cPos[0]+w/4),cPos[1]+h),((cPos[0],cPos[1]+h/2))),f*size)
        if tool=="colorPicker":
            col=screen.get_at((mx,my))#gets the color at where the user is clicking
            screen.set_clip(None)
            draw.rect(screen,col,(240,720,25,25))#draws color indicator rectangle next to color pallette
            screen.set_clip(canvasRect)
        
        if tool=="fill":
            if clicked:
                rc=canvas.get_at((mx,my))#gets the color where the user clicked 
                spots=[(mx,my)]#list to contain all spots that need to get colored in
                while len(spots)>0:
                    newSpots=[]#clears the list of the old spots that have already been checked
                    for fx,fy in spots:#goes through all the spots to be checked
                        if 100<fx<900 and 60<fy<660 and canvas.get_at((fx,fy))==rc:#checks if the spot is within the canvas and is the same color as the original spot
                            canvas.set_at((fx,fy),col)#sets the spot to be the desired color
                            newSpots+=[(fx+1,fy),(fx-1,fy),(fx,fy+1),(fx,fy-1)]#adds all the adjacent spots to the list of spots to check
                        spots=newSpots#sets the list of new spots to the old list of spots to be checked in the next iteration
        if tool=="spray":
            for n in range(size*4):
                x=mx+randint(int(-size/2),int(size/2))
                y=my+randint(int(-size/2),int(size/2))#creates a random spot within the size range around the location of the mouse
                dx=mx-x
                dy=my-y
                dist=int((dx**2+dy**2)**0.5)
                if abs(dist)<=size/2:#checks if the spot is within the radius of the size
                    canvas.set_at((x,y),col)#sets the pixel to the intended color

        if tool=="highlighter":
            canvas.fill((0,0,0,0))
            canvas.blit(back,(0,0))#clears the canvas and redraws the screen to how it looked before the user clicked down
            dx=mx-omx
            dy=my-omy
            dist=int((dx**2+dy**2)**0.5)
            for i in range(1,dist+1):
                dotX=int(omx+i*dx/dist)
                dotY=int(omy+i*dy/dist)
                #sets pixels on the highlighted surface to the highlighter color at every point between the current and previous mouse position
                highlighter.subsurface(dotX-size/2,dotY-size/2,size,size).fill((col[0],col[1],col[2],100))
            canvas.blit(highlighter,(0,0))#draws the highlighter surface to the canvas
              
        if tool=="stamp":
            canvas.fill((0,0,0,0))
            canvas.blit(back,(0,0))#clears the canvas and redraws the screen to how it looked before the user clicked down
            canvas.blit(stamp,(mx-stamp.get_width()/2,my-stamp.get_height()/2))#draws the stamp to the screen centered on the mouse position
                
        screen.set_clip(None)#allows the entire screen to be edited

            ############################### Saving and loading #####################
        
    if saveRect.collidepoint(mx,my) and mb[0]==1:#checks if the user pressed the save button
        try:
            fname=filedialog.asksaveasfilename(defaultextension=".png")#opens tk window for user to input file name
            #asks the user to input a file name they would like to save as
            image.save(screen.subsurface(canvasRect),fname)#saves the canvas as a png file
        except:
            pass#if the above doesn't work then continue
    #loading a picture
    if openRect.collidepoint(mx,my) and mb[0]==1:
        try:
            fname=filedialog.askopenfilename(filetypes=[("Images","*.png;*.jpg;*.jpeg;*.bmp")])#opens tk window and only displays compatible file types
            openedImage=image.load(fname)#renders selected image
            openedImage=transform.scale(openedImage,(800,600))#scales image to fit canvas
            canvas.fill((0,0,0,0))#clears the canvas
            canvas.blit(openedImage,(canvasRect[0],canvasRect[1]))#draws the new image
        except:
            pass

        ######################### Drawing all layers to screen ##############################
        
    screen.set_clip(canvasRect)#only allows canvas rect to be modified
    screen.blit(backImage,(0,0))#draws background to screen
    screen.blit(canvas,(0,0))#draws canvas layer to screen
    screen.blit(highlighter,(0,0))#draws highlighter layer to screen
    screen.set_clip(None)#allows the whole screen to be edited again

    
    if released==True:#checks if the user released the mouse over the canvas or drew something on the canas
        if canvasRect.collidepoint(cPos) or canvasRect.collidepoint(mx,my):
            redoList=[]#clears redo list
            frame=canvas.copy()#copies canvas
            history.append(frame)#adds canvas copy to histoy for undoing
        if tool=="stamp":#deselects stamp tool
            tool="no_tool"
    
   
    omx,omy=mx,my#sets the old mouse position to the current mouse position
    display.flip()#updates the display

quit()#exits the program
