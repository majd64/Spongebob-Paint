#PAINTPROJECT -- MAJD HAILAT -- ICS3U
from pygame import *
from random import *
from tkinter import *
root=Tk()
root.withdraw()
size=width,height=1280,1024 #Assigning window size
screen=display.set_mode(size) #Setting window size
#--------------------------INITIALIZING VARIABLES--------------------------------
error=0 #Increases every time theres an error
RED=(255,0,1)#Assigning variables for commonly used colours 
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
col=BLACK #Initiallizing Chosen colour var
tool=" " #Initiallizing Chosen tool var
thick=5 #Initiallizing tool thickness var
alpha=5 #Initiallizing highlighter opacity var
stickerPos=0 #Initiallizing chosen sticker var
BgPos=6 #Initiallizing chosen background var
copied=0 #Initiallizing the var that keeps track of the state of the copy and paste tool
selectTool=True #Var that allows user to change tools
drawing=True #Var that allows users to draw on the canvas
undolist=[] #Lists that keep screenshots for undo & redo
redolist=[] 
idea="" #The chosen suggested drawing idea
drawList=["A Clarinet","A Krabby Patty","Spongebob's Pineapple","A Jelly Fish","Gary","Plankton","Larry The Lobster","A Boat","Mrs. Puff","A Spatula","My Leg"] #Possible drawing ideas
drawList2=[] #List that takes drawing ideas that have been skipped
#-----
font.init() #Initiallizing fonts
showcard30=font.SysFont("Showcard Gothic",30) #Setting font for the title
calibriBold22=font.SysFont("Calibri Bold",23) #Setting fonts for headings
calibri14=font.SysFont("Calibri",14) #Setting font for the information text
#-----
mixer.init() #Initiallizing music
play=-1 #Initiallizing play/ pause var (play:1, pause:-1)
songPos=0 #Initiallizing selected song var
musicName=["music/song1.ogg","music/song2.ogg","music/song3.ogg","music/song4.ogg","music/song5.ogg","music/song6.ogg","music/song7.ogg","music/song8.ogg","music/song9.ogg","music/song10.ogg","music/song11.ogg","music/song12.ogg"] #Song file paths
mixer.music.load(musicName[songPos]) #Loading selected song
mixer.music.play(-1) #Playing selected song
mixer.music.pause() #Pausing Selected song when the program is initally launched
vol=1 #Initiallizing volume var
#--------------------LOADING IMAGES----------------------------------------
bgMain=image.load("images/UI/BackGround.png") #Loading window BG image
colorWheel=image.load("images/UI/ColorWheel.png") #Loading colour palet image
brushTool=image.load("images/tools/brush.png") #Loading tool icon images
pencilTool=image.load("images/tools/Pencil.png")
highLighterTool=image.load("images/tools/highlighter.png")
sprayTool=image.load("images/tools/spray.png")
eraserTool=image.load("images/tools/eraser.png")
lineTool=image.load("images/tools/line.png")
rectTool=image.load("images/tools/rect.png")
ovalTool=image.load("images/tools/oval.png")
copyTool=image.load("images/tools/copy.png")
dropperTool=image.load("images/tools/dropper.png")
saveUI=image.load("images/UI/save.png") #Loading other UI images
loadUI=image.load("images/UI/load.png")
playUI=image.load("images/UI/playPause.png")
nextSongUI=image.load("images/UI/nextSong.png")
previousSongUI=image.load("images/UI/previousSong.png")
undoUI=image.load("images/UI/undo.png")
redoUI=image.load("images/UI/redo.png")
clearAllUI=image.load("images/UI/clearAll.png")
#-----
stickerName=["images/stickers/spongebob.png","images/stickers/patrick.png","images/stickers/squidward.png","images/stickers/mrkrabz.png","images/stickers/sandy.png","images/stickers/gary.png","images/stickers/plankton.png","images/stickers/spongebob2.png","images/stickers/patrick2.png","images/stickers/squidward2.png","images/stickers/puff.png","images/stickers/pearl.png","images/stickers/fish.png",] #Sticker file paths
sticker=[] #List that contains loaded sticker images
for name in stickerName: #Loop to load images
    stickerPic=image.load(name) #Loading all images
    sticker.append(stickerPic) #Adding loaded images to list
stickerNum=len(stickerName)
#-----
bgName=["images/backgrounds/bg1.png","images/backgrounds/bg2.png","images/backgrounds/bg3.png","images/backgrounds/bg4.png","images/backgrounds/bg5.png","images/backgrounds/bg6.png"]
bg=[] #List that contains loaded background images
for name in bgName: #Loop to load images
    pic=image.load(name) #Loading all images
    bg.append(pic) #Adding loaded images to list
bgNum=len(bgName)
#-----
screen.blit(bgMain,(0,0)) #Adding images to screen
screen.blit(colorWheel,(19,206))
screen.blit(brushTool,(235,920))
screen.blit(pencilTool,(330,919))
screen.blit(highLighterTool,(425,920))
screen.blit(sprayTool,(520,920))
screen.blit(eraserTool,(615,920))
screen.blit(lineTool,(710,920))
screen.blit(rectTool,(805,920))
screen.blit(ovalTool,(900,920))
screen.blit(copyTool,(995,920))
screen.blit(dropperTool,(1090,920))
screen.blit(saveUI,(17,42))
screen.blit(loadUI,(169,42))
screen.blit(playUI,(93,95))
screen.blit(nextSongUI,(138.5,95))
screen.blit(previousSongUI,(48,95))
screen.blit(undoUI,(40,654))
screen.blit(redoUI,(40,714))
screen.blit(clearAllUI,(40,774))
#--------------------------DEFINING RECTS----------------------------------------
canvasRect=Rect(220,5,1055,890) #Defining drawable canvas rect
colWheelRect=Rect(19,206,182,228) #Defining colour palet rect
brushRect=Rect(235,920,75,75) #Defining tool button rects
pencilRect=Rect(330,920,75,75)
highLightRect=Rect(425,920,75,75)
sprayRect=Rect(520,920,75,75)
eraserRect=Rect(615,920,75,75)
rectLine=Rect(710,920,75,75)
rectShapeRect=Rect(805,920,75,75)
rectOval=Rect(900,920,75,75)
copyRect=Rect(995,920,75,75)
dropperRect=Rect(1090,920,75,75)
saveRect=Rect(15,40,38,38) #Defining other button rects
loadRect=Rect(167,40,38,38)
playPauseRect=Rect(91,93,38,38)
nextSongRect=Rect(136,93,38,38)
previousSongRect=Rect(46,93,38,38)
bgRect=Rect(47,488,125.5,30)
stickersRect=Rect(65,536,90,90)
undoRect=Rect(40,654,45,45)
redoRect=Rect(40,714,45,45)
clearRect=Rect(40,774,45,45)
songRect=Rect(15,136,190,40) #Defining informational boxes rects
rgbRect=Rect(55,444,110,20)
drawIdeaRect=Rect(4,845,210,30)
infoRect=Rect(4,893,210,103)
#-----
draw.rect(screen,BLACK,(219,4,1057,892),1) #Drawing canvas boarder
draw.rect(screen,WHITE,canvasRect) #Drawing canvas
#-----
firstCanvas=screen.subsurface(canvasRect).copy() #Copying blank canvas
undolist.append(firstCanvas) #Adding blank canvas to undolist
#-----
firstStickerIcon=transform.scale(sticker[0],(80,80)) #Making first sticker small to fit into the sticker preview box
screen.blit(firstStickerIcon,(70,541)) #Adding sticker icon
#========================WHILE RUNNING LOOP======================================
running=True #Setting program to run
while running: #Running program loop
    #print()
    for evt in event.get(): #Event loop
        if evt.type==QUIT: #Checking if program has been closed
            running=False #Closing program 
#-----------------------------MOUSEBUTTON UP-------------------------------------
        if evt.type==MOUSEBUTTONUP: #Checking if mouse is released
            if evt.button==3 or evt.button==2 or evt.button==4 or evt.button==5: #Checking if it was not the left click that was releases
                error+=1
            else:
                drawing=True #Allowing the user to draw
                selectTool=True #Allowing tools to be changed
#COPY & PASTE
            if copied==1 and tool=="copy": #Checking if the var copied is 1 (the user is dragging to copy)
                screen.blit(removeCopyOutlineSC,(0,0)) #Adding a SS as the user drags to remove previous copy preview oulines
                copySection=Rect(sx,sy,mx-sx,my-sy) #Getting the area the user has selected to copy
                copySection.normalize() #Normalizing the area
                copied+=1 #Increasing copy var to move onto the next copy&paste stage
                
            if copied==3 and tool=="copy": #Checking if the copied var is 3 (The user has copied and pasted) 
                copied=0 #Setting the copied var to 0 to restart the process
#UNDO LIST
            if canvasRect.collidepoint(mx,my) or bgRect.collidepoint(mx,my) or clearRect.collidepoint(mx,my): #Checking if the user has made a change
                if evt.button==1 and tool!="dropper" and copied!=2: #Checking that the user acctually made a change (changing color, right clicking and only copying does not count
                    edit=screen.subsurface(canvasRect).copy() #Taking a SS of the canvas
                    undolist.append(edit) #Adding the SS to undo list
#-------------------------------MOUSEBUTTON DOWN---------------------------------
        if evt.type==MOUSEBUTTONDOWN: #Checking if the mosue is clicked
            if evt.button==1: #Checking if its the left mouse button
                sx,sy=mouse.get_pos() #Getting the mouse pos at the click (used for dragging, acts as the starting position of the drag)
                screenShot=screen.copy() #taking a SS (used for dragging as well, removes previous positions of an object being dragged)
                
            if canvasRect.collidepoint(mx,my): #Checking if the mouse is on the canvas
                if evt.button==3 or evt.button==2 or evt.button==4 or evt.button==5: #Checking if it was not the left click that was clicked
                    error+=1
                else:
                    selectTool=False #Preventing the user from being able to change the tool
            else:
                if evt.button==3 or evt.button==2 or evt.button==4 or evt.button==5: #Checking if it was not the left click that was clicked
                    error+=1
                else:
                    drawing=False #Preventing the user from being able to draw until they release the mouse
#COPY & PASTE
            if copied==2 and tool=="copy": #Checking if copied var is 2 (The user has copied)
                try: 
                    copyArea=screen.subsurface(copySection).copy() #Adding the area the user has copied to a subsurface
                except:
                    error+=1    
#SAVE & LOAD
            if saveRect.collidepoint(mx,my) and selectTool==True and evt.button==1: #Checking if the save button has been clicked
                file=filedialog.asksaveasfilename(defaultextension=".png") #Opening file dialogue
                if file!="": #Checking that the user has typed a file name
                    image.save(screen.subsurface(canvasRect),file) #Saving the canvas
            if loadRect.collidepoint(mx,my) and selectTool==True and evt.button==1: #Checking if the load button has been clicked
                fileName=filedialog.askopenfilename() #Opening file dialogue
                if fileName!="": #Checking the user clicked a file
                    loadedImage=image.load(fileName) #Loading select image
                    loadedImageWidth=loadedImage.get_width() #Getting width and height of the imahe
                    loadedImageHeight=loadedImage.get_height()
                    if loadedImageWidth!=1055 or loadedImageHeight!=890: #Checking if the image is larger than the canvas
                        loadedImage=transform.scale(loadedImage,(1055,890)) #Scaling the image to fit the canvas
                    screen.blit(loadedImage,(220,5)) #adding loaded image 
#THICKNESS
            if evt.button==4: #Checking if the user scrolled up
                if thick<35: #Checking if the max thickness has been reached 
                    thick+=1 #Increasing the thickness
            if evt.button==5: #Checking if the user scrolled down
                if thick>1: #Checking if the min thickness has been reached 
                    thick-=1 #Decreasing thickness
#FILLED/ UNFILLED
            if keys[K_LSHIFT]==1 or keys[K_RSHIFT]==1: #Checking if shift has been clicked
                fill=0 #Setting fill var to 0 (filled)
            else:
                fill=1 #Setting fill var to 0 (unfilled)
#STICKER SELECTION
            if stickersRect.collidepoint(mx,my) and selectTool==True and evt.button==1: #Checking if the sticker button has been clicked
                stickerSize=1 #Setting sticker size var to 1
                stickerRotation=0 #Setting sticker rotation var to 0
                if tool in sticker: #Checking if the tool is already sticker
                    stickerPos=(stickerPos+1)%stickerNum #Increasing sticker pos and making sure it doesnt go over the amount of stickers
                tool=sticker[stickerPos] #Changing tool to sticker without changing the sticker
#BACKGROUND SELECTION
            if  bgRect.collidepoint(mx,my) and selectTool==True and evt.button==1: #Checking if the BG button has been clicked
                BgPos=(BgPos+1)%(bgNum+1) #Increasing BG pos and making sure it doesnt go over the amount of BGs
                if BgPos==6: #Checking if the BG is at the white BG
                    draw.rect(screen,WHITE,canvasRect) #Drawing a white canvas
                else:
                    sub=bg[BgPos] #Getting the BG image from the list
                    screen.blit(sub,(220,5)) #Changing the BG
#DRAWING IDEA
            if drawIdeaRect.collidepoint(mx,my) and selectTool==True and evt.button==1: #Checking if the BG button has been clicked
                if len(drawList)==0: #Checking if all the drawing ideas have been skipped
                    drawLen=len(drawList2) #Getting the amount of drawing ideas 
                    for l in range (0,drawLen): #Loop to reset drawing ideas
                        drawList.append(drawList2[l]) #Adding all drawing ideas to list
                    drawList2=[] #Clearing skipped drawing ideas list
                    
                ideaPos=randint(0,(len(drawList))-1) #Getting random drawing idea pos from list
                idea=drawList[ideaPos] #getting drawing idea from random pos
                drawList2.append(drawList[ideaPos]) #Adding skipped/used drawing idea to the skipped ideas list
                drawList.remove(drawList[ideaPos]) #Removing skipped/used drawing idea from the drawing idea list
#UNDO AND REDO
            if undoRect.collidepoint(mx,my) and selectTool==True and evt.button==1: #Checking if the undo button has been clicked
                if len(undolist) > 1: #Checking if the undo list is not empty
                    redolist.append(undolist[-1]) #Adding SS to redo list
                    undolist.remove(undolist[-1]) #Removing SC from undo list 
                    screen.blit(undolist[-1],(220,5)) #Adding SS to canvas
            if redoRect.collidepoint(mx,my) and selectTool==True and evt.button==1: #Checking if the redo button has been clicked
                if len(redolist) > 0: #Checking if the redo list is not empty
                    screen.blit(redolist[-1],(220,5)) #Adding SS to canvas
                    undolist.append(redolist[-1]) #Adding SS to undo list      
                    redolist.remove(redolist[-1]) #Removing SS from redo list
#CLEAR CANVAS
            if clearRect.collidepoint(mx,my) and selectTool==True and evt.button==1: #Checking if the clear canvas button has been clicked
                if BgPos==6: #Checking if the BG pos is the blank (white) BG
                    draw.rect(screen,WHITE,canvasRect) #Drawing a white BG
                else:
                    sub=bg[BgPos] #Getting the BG image from the list
                    screen.blit(sub,(220,5)) #Adding the BG
#MUSIC   
            if playPauseRect.collidepoint(mx,my) and selectTool==True and evt.button==1: #Checking if the music button has been clicked
                play=play*-1 #Switching the play var between 1 and -1
                if play==1: #Checking is the music is playing
                    mixer.music.unpause() #Playing the music
                else:
                    mixer.music.pause() #Pausing the music
#---
            if nextSongRect.collidepoint(mx,my) and selectTool==True and evt.button==1: #Checking if the next song button has been clicked
                if play==1: #Checking if the music is playing
                    if songPos+1<len(musicName): #Checking if the last song has been reached
                        songPos+=1 #Changing song
                        mixer.music.load(musicName[songPos]) #Loaing new song
                        mixer.music.play(-1) #Playing new song
                    else:
                        songPos=0 #Restarting song list
                        mixer.music.load(musicName[songPos]) #Loading first song
                        mixer.music.play(-1) #playing first song
#---           
            if previousSongRect.collidepoint(mx,my) and selectTool==True and evt.button==1: #Checking if the previous song button has been clicked
                if play==1: #Checking if the music is playing
                    if songPos!=0: #Checking that its not the first song
                        songPos-=1 #Changing song
                        mixer.music.load(musicName[songPos]) #Loaing new song
                        mixer.music.play(-1) #Playing new song
                    else:
                        songPos=(len(musicName))-1 #Getting last song
                        mixer.music.load(musicName[songPos]) #Loading last song
                        mixer.music.play(-1) #Playing last song
#-------------------------------------KEYBOARD-----------------------------------
        keys=key.get_pressed() #Key has been pressed
        if evt.type==KEYDOWN:
#STICKER SIZE & STICKER ROTATION
            if tool in sticker: #Checking if the sticker tool is selected
                if keys[K_UP]==1: #Checking if the up arrow key is pressed
                    stickerSize+=.12 #Increasing sticker size
                    if stickerSize>4.0: #Checking if max sticker size has been reached
                        stickerSize=4.0 #Not allowing sticker size to increase
                if keys[K_DOWN]==1: #Checking if the down arrow key is pressed
                    stickerSize-=.12 #Decreasing sticker size
                    if stickerSize<0.16: #Checking if min sticker size has been reached
                        stickerSize=0.16 #Not allowing sticker size to decrease
#-----
                if keys[K_RIGHT]==1: #Checking if the right arrow key is pressed
                    stickerRotation-=15 #Rotatibg sticker to the right
                if keys[K_LEFT]==1: #Checking if the left arrow key is pressed
                    stickerRotation+=15 #Rotatibg sticker to the left
#HIGHLIGHTER OPACITY CHANGE
            if tool=="highlighter": #Checking if the highlighter tool is selected
                if alpha!=35: #Checking if max opacity has been reached
                    if keys[K_UP]==1: #Checking if the up arrow key is pressed
                        alpha+=1 #Increasing opacity
                if alpha!=1: #Checking if min opacity has been reached
                    if keys[K_DOWN]==1: #Checking if the down arrow key is pressed
                        alpha-=1 #Decreasing opacity
#CHANGE VOLUME
            if play==1: #Checking if music is playing
                if keys[K_RIGHTBRACKET]==1: #Checking if the right bracket is pressed
                    if vol<1: #Checking if max vol has been reached
                        vol+=0.1 #Increasing vol
                        mixer.music.set_volume(vol) #Setting vol
                if keys[K_LEFTBRACKET]==1: #Checking if the left bracket is pressed
                    if vol>0.1: #Checking if min vol has been reached
                        vol-=0.1 #Decreasing vol
                        mixer.music.set_volume(vol) #Setting vol
#------------------------------------MOUSE---------------------------------------
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos() #Getting mouse pos
#CHANGING THE COLOR
    if mb[0]==1 and selectTool==True: #Checking if left mouse has been clicked
        if colWheelRect.collidepoint(mx,my): #checking if Color box has been clicked
            col=screen.get_at((mx,my)) #Getting col
#TOOL SELECTION HIGHLIGHTS
    saveOnCol=BLACK #Setting colour of buttons that cannot be selected (only clicked)
    loadOnCol=BLACK
    nextSongOnCol=BLACK
    previousSongOnCol=BLACK
    bgOnCol=BLACK
    nextStickerOnCol=BLACK
    undoOnCol=BLACK
    redoOnCol=BLACK
    clearOnCol=BLACK
    ideaOnCol=BLACK
#-----
    if selectTool==True: #Checking if tool can be changed
        if tool=="brush": #Chaging tool
            brushOnCol=BLUE #Highlighting selected tool
        else:
            brushOnCol=BLACK
        if tool=="pencil":
            pencilOnCol=BLUE
        else:
            pencilOnCol=BLACK
        if tool=="highlighter":
            highlighterOnCol=BLUE
        else:
            highlighterOnCol=BLACK
        if tool=="spray":
            sprayOnCol=BLUE
        else:
            sprayOnCol=BLACK
        if tool=="eraser":
            eraserOnCol=BLUE
        else:
            eraserOnCol=BLACK
        if tool=="line":
            lineOnCol=BLUE
        else:
            lineOnCol=BLACK
        if tool=="rectShape":
            rectOnCol=BLUE
        else:
            rectOnCol=BLACK
        if tool=="oval":
            ovalOnCol=BLUE
        else:
            ovalOnCol=BLACK
        if tool=="copy":
            copyOnCol=BLUE
        else:
            copyOnCol=BLACK
        if tool=="dropper":
            dropperOnCol=BLUE
        else:
            dropperOnCol=BLACK
        if tool in sticker:
            stickersOnCol=BLUE
        else:
            stickersOnCol=BLACK
        if play==1:
            playPauseOnCol=BLUE
        else:
            playPauseOnCol=BLACK
#-----
        if mx>235 and mx<310 and my>920 and my<995: #Checking if button is being hovered over
            brushOnCol=RED #Highlighting hovered image       
        if mx>330 and mx<405 and my>920 and my<995:
            pencilOnCol=RED
        if mx>425 and mx<500 and my>920 and my<995:
            highlighterOnCol=RED
        if mx>520 and mx<595 and my>920 and my<995:
            sprayOnCol=RED
        if mx>615 and mx<690 and my>920 and my<995:
            eraserOnCol=RED
        if mx>710 and mx<785 and my>920 and my<995:
            lineOnCol=RED
        if mx>805 and mx<880 and my>920 and my<995:
            rectOnCol=RED
        if mx>900 and mx<975 and my>920 and my<995:
            ovalOnCol=RED
        if mx>995 and mx<1070 and my>920 and my<995:
            copyOnCol=RED
        if mx>1090 and mx<1165 and my>920 and my<995:
            dropperOnCol=RED
        if mx>15 and mx<53 and my>40 and my<78:
            saveOnCol=RED
        if mx>167 and mx<205 and my>40 and my<78:
            loadOnCol=RED
        if mx>91 and mx<129 and my>93 and my<131:
            playPauseOnCol=RED
        if mx>136 and mx<174 and my>93 and my<131:
            nextSongOnCol=RED
        if mx>46 and mx<84 and my>93 and my<131:
            previousSongOnCol=RED
        if mx>45 and mx<172.5 and my>488 and my<518:
            bgOnCol=RED
        if mx>63 and mx<156 and my>536 and my<626:
            stickersOnCol=RED
        if mx>40 and mx<85 and my>654 and my<699:
            undoOnCol=RED
        if mx>40 and mx<85 and my>714 and my<759:
            redoOnCol=RED
        if mx>40 and mx<85 and my>774 and my<819:
            clearOnCol=RED
        if mx>4 and mx<214 and my>845 and my<875:
            ideaOnCol=RED
#-------------------------------CREATING UI--------------------------------------         
#RECTANGLES(BUTTONS)
    draw.rect(screen,col,(15,202,188,236),6) #Drawing buttons and boxes
    draw.rect(screen,brushOnCol,brushRect,3)
    draw.rect(screen,pencilOnCol,pencilRect,3)
    draw.rect(screen,highlighterOnCol,highLightRect,3)
    draw.rect(screen,sprayOnCol,sprayRect,3)
    draw.rect(screen,eraserOnCol,eraserRect,3)
    draw.rect(screen,lineOnCol,rectLine,3)
    draw.rect(screen,rectOnCol,rectShapeRect,3)
    draw.rect(screen,ovalOnCol,rectOval,3)
    draw.rect(screen,copyOnCol,copyRect,3)
    draw.rect(screen,dropperOnCol,dropperRect,3)
    draw.rect(screen,saveOnCol,saveRect,2)
    draw.rect(screen,loadOnCol,loadRect,2)
    draw.rect(screen,playPauseOnCol,playPauseRect,2)
    draw.rect(screen,nextSongOnCol,nextSongRect,2)
    draw.rect(screen,previousSongOnCol,previousSongRect,2)
    draw.rect(screen,bgOnCol,bgRect,3)
    draw.rect(screen,stickersOnCol,stickersRect,3)
    draw.rect(screen,undoOnCol,undoRect,3)
    draw.rect(screen,redoOnCol,redoRect,3)
    draw.rect(screen,clearOnCol,clearRect,3)
    draw.rect(screen,WHITE,songRect,0)
    draw.rect(screen,BLACK,songRect,2)
    draw.rect(screen,WHITE,rgbRect,0)
    draw.rect(screen,col,rgbRect,2)
    draw.rect(screen,WHITE,drawIdeaRect) 
    draw.rect(screen,ideaOnCol,drawIdeaRect,2)
    draw.rect(screen,WHITE,infoRect)
    draw.rect(screen,BLACK,infoRect,2)
#STICKERS ICONS
    if tool in sticker: #Checking if sticker tool is selected
        stickerIcon=transform.scale(sticker[stickerPos],(80,80)) #Making selected sticker small
        draw.rect(screen,(254,245,42),(68,539,83,83)) #Drawing the BG color over the previous sticker icon to hide it
        screen.blit(stickerIcon,(70,541)) #Adding new sticker icon
#SPONGEBOB PAINT TITLE TEXT
    titleSpongebob=showcard30.render("SpongeBob",True,BLACK) #Rendering Title text
    titlePaint=showcard30.render("Paint",True,BLACK)
    screen.blit(titleSpongebob,(20,10)) #Adding title text
    screen.blit(titlePaint,(65,40))
#BUTTON TEXT
    bgText=calibriBold22.render("Background",True,bgOnCol) #Rendering Heading text
    screen.blit(bgText,(64,496)) #Adding heading text
    stickersText=calibriBold22.render("Stickers",True,stickersOnCol)
    screen.blit(stickersText,(76,628))
    undoText=calibriBold22.render("Undo",True,undoOnCol)
    screen.blit(undoText,(90,670))
    redoText=calibriBold22.render("Redo",True,redoOnCol)
    screen.blit(redoText,(90,730))
    clearText=calibriBold22.render("Clear All",True,clearOnCol)
    screen.blit(clearText,(90,790))
#MUSIC INFO BOX
    songText=calibri14.render("Song:",True,BLACK) #Rendering "Song" text
    screen.blit(songText,(20,140)) #Adding text

    if songPos==0: #Checking song
        songName="Theme Song" #Changning the song name var
    elif songPos==1:
        songName="The Goofy Goober Song"
    elif songPos==2:
        songName="F.U.N. Song"
    elif songPos==3:
        songName="Campfire Song Song"
    elif songPos==4:
        songName="Ripped Pants"
    elif songPos==5:
        songName="My Tighty Whiteys"
    elif songPos==6:
        songName="Doing The Sponge"
    elif songPos==7:
        songName="Stadium Rave"
    elif songPos==8:
        songName="Goofy Goober Rock"
    elif songPos==9:
        songName="The Best Day Ever"
    elif songPos==10:
        songName="Gary's Song"
    elif songPos==11:
        songName="This Grill is Not a Home"
    
    songNameText=calibri14.render(songName,True,BLACK) #Rendering song name text
    screen.blit(songNameText,(55,140)) #Adding song name text

    volWordText=calibri14.render("Vol:",True,BLACK) #Rendering "Vol" text
    screen.blit(volWordText,(20,158)) #Adding text

    volStr=str(round(vol*10)) #Making vol into a string
    volText=calibri14.render(volStr,True,BLACK) #Rendering vol text
    screen.blit(volText,(50,158)) #Adding vol text

    volChangeText=calibri14.render("Vol+  ]          Vol-  [",True,BLACK) #Rendering vol instruction text
    screen.blit(volChangeText,(85,158)) #Adding text
#RGB INFO BOX
    if tool=="highlighter": #Checking if highlighter tool is selected
        col=(col[0],col[1],col[2],alpha) #Getting the col with alpha
        rgb=str(col) #Making col into a string
        rgbText=calibri14.render(rgb,True,BLACK) #Rendering col text
        screen.blit(rgbText,(59,448)) #Adding col text
    else:
        col=(col[0],col[1],col[2])#Getting the col
        rgb=str(col) #Making col into a string
        comma=0 #Initiallizing comma count var
        for z in rgb: #Starting loop that removes alpha
            if z==",": #Checking if a comma has been found
                comma+=1 #Increasing comma count var
                if comma==3: #Checking if the col text has reached the place right before the alpha
                    rgb=(rgb[:-6]+")") #Adding a bracket to the text
                    comma=0 #Resetting comma var
        rgbText=calibri14.render(rgb,True,BLACK) #Rendering col text
        screen.blit(rgbText,(59,448)) #Adding col text
#TOOL INFO BOX
    draw.line(screen,BLACK,(8,915),(210,915),1) #Drawing line that seperates the col and thickness info from the tool info

    adjustTxtX=0 #Initiallizing text adjustment vars
    adjustTxtY=0

    if tool=="highlighter": #Checking if the highlighted tool is selected
        adjustText2=-5 #Adjusting text pos
    else:
        adjustText2=0
    
    if tool=="brush": #Checking selected tool
        adjustTxtX=0 #Changing adjustment for text pos
        toolText="Brush Tool" #Setting tool info text
        toolText2="Draw brush strokes, use mouse"
        toolText3="wheel to change thickness"
        toolText4=""
    elif tool=="pencil":
        adjustTxtX=-2
        toolText="Pencil Tool"
        toolText2="Draw pencil lines"
        toolText3=""
        toolText4=""
    elif tool=="eraser":
        adjustTxtX=-2
        toolText="Eraser Tool"
        toolText2="Erase marks, use mouse wheel"
        toolText3="to change thickness"
        toolText4=""
    elif tool=="line":
        adjustTxtX=2
        toolText="Line Tool"
        toolText2="Draw straight lines, use mouse"
        toolText3="wheel to change thickness"
        toolText4=""
    elif tool=="rectShape":
        adjustTxtX=-15
        toolText="Rectangle Tool"
        toolText2="Draw rectangles, use mouse"
        toolText3="wheel to change thickness,"
        toolText4="hold shift to fill"
    elif tool=="oval":
        adjustTxtX=0
        toolText="Ellipse Tool"
        toolText2="Draw Ovals, use mouse wheel"
        toolText3="to change thickness, hold"
        toolText4="shift to fill"
    elif tool=="spray":
        adjustTxtX=-20
        toolText="Spray Paint Tool"
        toolText2="Draw spray patterns, use mouse"
        toolText3="wheel to change thickness"
        toolText4=""
    elif tool=="highlighter":
        adjustTxtX=-20
        toolText="Highlighter Tool"
        toolText2="Draw translucent strokes, use"
        toolText3="mouse wheel to change thickness,"
        toolText4="use arrow keys to change opacity"
    elif tool in sticker:
        adjustTxtX=0
        toolText="Sticker Tool"
        toolText2="Place stickers, use arrow keys"
        toolText3="to change size and rotate"
        toolText4=""
    elif tool=="copy":
        adjustTxtX=-20
        toolText="Copy&Paste Tool"
        toolText2="Drag over an area to copy it"
        toolText3="click again to paste"
        toolText4=""
    elif tool=="dropper":
        adjustTxtX=-10
        toolText="Dropper Tool"
        toolText2="Click a colour on the canvas"
        toolText3="to select it"
        toolText4=""
    else:
        toolText="By Majd H"
        toolText2=""
        toolText3=""
        toolText4=""
    
    infoText=calibriBold22.render(toolText,True,BLACK) #Rendering tool info text
    screen.blit(infoText,(65+adjustTxtX,921)) #Adding tool info text

    infoText2=calibri14.render(toolText2,True,BLACK)
    screen.blit(infoText2,(15+adjustText2,939))
    
    infoText3=calibri14.render(toolText3,True,BLACK)
    screen.blit(infoText3,(15+adjustText2,957))

    infoText4=calibri14.render(toolText4,True,BLACK)
    screen.blit(infoText4,(15+adjustText2,975))
#-----
    thickWord=calibri14.render("Thickness:",True,BLACK) #Rendering "Thickness" text
    screen.blit(thickWord,(112,899)) #Adding text 
    thickStr=str(thick) #Making thikness into a string
    thickText=calibri14.render(thickStr,True,BLACK) #Rendering thickness text
    screen.blit(thickText,(176,899)) #Adding thickness text
#-----
    posText=calibri14.render("Pos:",True,BLACK) #Rendering "Pos" text
    screen.blit(posText,(15,899)) #Adding text 
    if canvasRect.collidepoint(mx,my): #Checking if mouse is on the canvas
        mxStr=str(mx-220) #Getting mousepos relative to the canvas
        myStr=str(my-5)
    else:
        mxStr="0"
        myStr="0"
  
    mxText=calibri14.render(mxStr,True,BLACK) #Rendering mouse pos text
    screen.blit(mxText,(45,899)) #Adding mouse pos text

    myText=calibri14.render(myStr,True,BLACK)
    screen.blit(myText,(80,899))
#DRAW IDEA BOX
    drawText=calibriBold22.render("Draw:",True,BLACK) #Rendering "Draw" text
    screen.blit(drawText,(12,854)) #Adding text 
    ideaText=calibri14.render(idea,True,BLACK) #Rendering idea text
    screen.blit(ideaText,(60,854)) #Adding idea text
#------------------------------SELECTING TOOLS-----------------------------------
    if mb[0]==1 and selectTool==True: #Checking if left mouse button is clicked and changing tool is allowed
        if brushRect.collidepoint(mx,my): #Checking if the tool button has been clicked
            tool="brush" #Changing tool
        elif eraserRect.collidepoint(mx,my):
            tool="eraser"
        elif rectShapeRect.collidepoint(mx,my):
            tool="rectShape"
        elif rectLine.collidepoint(mx,my):
            tool="line"
        elif rectOval.collidepoint(mx,my):
            tool="oval"
        elif sprayRect.collidepoint(mx,my):
            tool="spray"
        elif pencilRect.collidepoint(mx,my):
            tool="pencil"
        elif copyRect.collidepoint(mx,my):
            tool="copy"
            copied=0
        elif highLightRect.collidepoint(mx,my):
            tool="highlighter"
        elif dropperRect.collidepoint(mx,my):
            tool="dropper"
#---------------------------------USING TOOLS------------------------------------           
    if mb[0]==1 and drawing==True: #Checking if left mouse button is clicked and drawing is allowed 
        if canvasRect.collidepoint(mx,my): #Checking if the mouse is on the canvas
            screen.set_clip(canvasRect) #ONLY THE CANVAS CAN BE UPDATED
        #BRUSH#
            if tool=="brush": #Checking tool
                dist=((my-myI)**2+(mx-mxI)**2)**0.5 #Finding distance between initial and final mouse pos
                if dist!=0: #Checking if the dist is not 0
                    bx=(mx-mxI)/dist #Finding pos between your final and initial mouse position 
                    by=(my-myI)/dist
                    for i in range(int(dist)+1): #Starting draw loop
                        draw.circle(screen,col,(int(mxI+bx*i),int(myI+by*i)),thick) #Drawing brush circle
        #PENCIL#
            if tool=="pencil":
                draw.line(screen,col,(mxI,myI),(mx,my),2) #Drawing pencil line
        #HIGHLIGHTER
            if tool=="highlighter":
                marker=Surface((thick*2,thick*2),SRCALPHA) #Creating clear subsurface
                draw.circle(marker,col,(thick,thick),thick) #Drawing circle on the subsurface
                dx=mx-mxI #Finding pos between your final and initial mouse position 
                dy=my-myI
                brushDist=int((dx**2+dy**2)**0.5) #Finding distance between initial and final mouse pos
                for d in range(1,brushDist+1): #Starting drawing loop
                    dotX=int(mxI+dx*d/brushDist) #Getting pos to draw highlight circle
                    dotY=int(myI+dy*d/brushDist)
                    if mx!=mxI or my!=myI: #Checking the user moved the mouse
                        screen.blit(marker,(dotX-thick,dotY-thick)) #Drawing highlight circle
        #SPRAY PAINT#
            if tool=="spray":
                for i in range(int(thick**1.5)): #Getting a pos inside the thickness
                    sx=randint(mx-thick,mx+thick) #Getting a random pos in a rect as large as the thickness
                    sy=randint(my-thick,my+thick)
                    if ((mx-sx)**2+(my-sy)**2)**0.5<=thick: #Checking if the pos is within a cirlce 
                        draw.line(screen,col,(sx,sy),(sx,sy)) #drawing a line
        #ERASER#
            if tool=="eraser":
                dist=((my-myI)**2+(mx-mxI)**2)**0.5 #Finding distance between initial and final mouse pos
                if dist!=0: #Checking the mouse has been moved
                    bx=(mx-mxI)/dist #Finding pos between your final and initial mouse position 
                    by=(my-myI)/dist
                    for i in range(int(dist)+1): #Starting draw loop
                        if BgPos==6: #Checking if the white background is selected
                            draw.circle(screen,WHITE,(int(mxI+bx*i),int(myI+by*i)),thick) #Drawing white circle
                        else:
                            try:
                                bgEraser=bg[BgPos].subsurface((int(mxI+bx*i)-220-thick,int(myI+by*i)-5-thick,thick*2,thick*2)) #Gettting area where mouse is on a subsurface of the bg
                                screen.blit(bgEraser,(int(mxI+bx*i)-thick,int(myI+by*i)-thick)) #Adding that area to the same pos on the canvas
                            except:
                                error+=1
        #LINE SHAPE#
            if tool=="line":
                screen.blit(screenShot,(0,0)) #Adding SS so that when the line is moved the previous one is deleted
                draw.line(screen,col,(sx,sy),(mx,my),thick) #Adding a line from the initial mouse pos to the current mouse pos
        #RECTANGLE SHAPE#
            if tool=="rectShape":
                screen.blit(screenShot,(0,0)) #Adding SS so that when the rect is moved the previous one is deleted
                for w in range (thick): #Loop the length of the thickness
                    if mx>sx and my>sy or mx<sx and my<sy: #Checking if the rect is being draw from top right to bottom left, top left to bottom right ETC
                        draw.rect(screen,col,(sx+w,sy+w,mx-sx-w,my-sy-w),fill) #Drawing multiple rectangles to fix the missing corners
                        draw.rect(screen,col,(mx+w,my+w,(mx-sx+w)*-1,(my-sy+w)*-1),fill)
                    if mx<sx and my>sy:
                        draw.rect(screen,col,(sx,sy+w,mx-sx,my-sy),fill)
                        draw.rect(screen,col,(sx+w,sy,mx-sx,my-sy),fill)
                        draw.rect(screen,col,(sx,my,w+1,w))
                    if mx>sx and my<sy:
                        draw.rect(screen,col,(sx,sy+w,mx-sx,my-sy),fill)
                        draw.rect(screen,col,(sx+w,sy,mx-sx,my-sy),fill)
                        draw.rect(screen,col,(mx,sy,w,w+1))
        #OVAL SHAPE#
            if tool=="oval":
                if fill==1 and (abs(sx-mx)>thick*2 and abs(sy-my)>thick*2): #Checking if the oval is unfilled and the size of the unfilled oval is big enough for it to have a gap
                    xAbs=abs(sx-mx) #Finding the absolute values of distance between sx,sy and mx,my
                    yAbs=abs(sy-my)
                    newEllRect=Rect(sx,sy,xAbs,yAbs) #Create a default ellipse Rect
                    newEllRect.normalize() #Normalizing the rect 
                    try:
                        if sx<mx and sy>my: #Checking if the oval is being draw from top right to bottom left, top left to bottom right ETC
                            screen.blit(screenShot,(0,0)) #Adding SS so that when the oval is moved the previous one is deleted
                            newEllRect=Rect(sx,my,xAbs,yAbs) 
                            draw.arc(screen,col,newEllRect,0,360,thick) #Drawing the ellipse/ oval
                        if sx<mx and sy<my:
                            screen.blit(screenShot,(0,0))
                            newEllRect=Rect(sx,sy,xAbs,yAbs)
                            draw.arc(screen,col,newEllRect,0,360,thick)
                        if sx>mx and sy>my:
                            screen.blit(screenShot,(0,0))
                            newEllRect=Rect(mx,my,xAbs,yAbs)
                            draw.arc(screen,col,newEllRect,0,360,thick)
                        if sx>mx and sy<my:
                            screen.blit(screenShot,(0,0))
                            newEllRect=Rect(mx,sy,xAbs,yAbs)
                            draw.arc(screen,col,newEllRect,0,360,thick)
                    except:
                        error+=1
                else: #The oval is filled
                    x=min(sx,mx) #Getting the ovals direction (similar to .normalize())
                    x_2=max(sx,mx)
                    y=min(sy,my)
                    y_2=max(sy,my)
                    screen.blit(screenShot,(0,0)) #Adding SS so that when the oval is moved the previous one is deleted
                    draw.ellipse(screen,col,(x,y,x_2-x,y_2-y)) #Drawing oval
        #COPY AND PASTE#  
            if tool=="copy" and (copied==0 or copied==1): #Checking if the var copied is 1 (the user is dragging to copy)
                screen.blit(screenShot,(0,0)) #Adding SS so that when the preview copy rect is moved the previous one is deleted
                removeCopyOutlineSC=screen.copy() #A screenshot is taken after the copy preview rect is drawn so it can be removed later
                draw.rect(screen,BLACK,(sx,sy,mx-sx,my-sy),1) #Drawing copy preview rect
                if copied==0: #Checking is the copied var is 0 so that the var is not increased more than once
                    copied+=1 #Increasing copied var 

            if tool=="copy" and (copied==2 or copied==3): #Checking if the var copied is 1 or 2 (the user is dragging to copy)
                screen.blit(screenShot,(0,0)) #Adding SS so that when the copied image is moved the previous one is deleted
                try: 
                    screen.blit(copyArea,(mx,my)) #Adding the copied image
                except:
                    error+=1
                    
                if copied==2: #Checking is the copied var is 2 so that the var is not increased more than once
                    copied+=1 #Increasing copied var
        #DROPPER#
            if tool=="dropper":
                col=screen.get_at((mx,my)) #Getting colour at mouse pos        
        #STICKERS#
            if tool in sticker: 
                stickerWidth=int(150*(stickerSize/1)) #Getting sticker size
                stickerHeight=int(150*(stickerSize/1))

                newSticker=transform.scale(sticker[stickerPos],(stickerWidth,stickerHeight)) #Setting sticker size
                newSticker=transform.rotate(newSticker,stickerRotation) #Setting sticker rotation

                newStickerWidth = newSticker.get_width() #Getting new sticker size
                newStickerHeight = newSticker.get_height()

                screen.blit(screenShot,(0,0)) #Adding SS so that when the sticker image is moved the previous one is deleted
                screen.blit(newSticker,(mx-newStickerWidth//2,my-newStickerHeight//2)) #Adding sticker
                     
        screen.set_clip(None)#THE ENTIRE SCREEN CAN BE UPDATED
#--------------------------------------END---------------------------------------
    mxI=mx #Getting initial mouse pos
    myI=my

    display.flip() #Showing screen

font.quit() #Quitting and deleting fonts
del showcard30
del calibri14
del calibriBold22
print("Errors:", error) #Printing 
quit() #Closing window
