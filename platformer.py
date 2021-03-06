"""
platformer.py
Author: Brian S
Credit: Finn H
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

blue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)

thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, black)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, pink)
gridline = LineStyle(1, grey)
grid=RectangleAsset(30,30,gridline,white)


black = Color(0, 1)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, red)
bg = Sprite(bg_asset, (0,0))
        
class Guy(Sprite):
    guy = RectangleAsset(20, 40, coolline, green)
    def __init__(self, x, y):
        super().__init__(Guy.guy, (x, y))
        self.x = x
        self.y = y
        
class Brick(Sprite):
    brick = RectangleAsset(30, 30, thinline, pink)
    def __init__(self, x, y):
        super().__init__(Brick.brick, (x, y))
        self.x = x
        self.y = y
        
    def step(self):
        self.grav += 0.25
        self.y += self.grav
        collide = self.collidingWithSprites(Brick)
        if collide:
            self.y -= self.grav
            self.grav = 0
class Spring(Sprite):
    spring = RectangleAsset(30, 5, thinline, blue)
    def __init__(self, x, y):
        super().__init__(Spring.spring, (x, y))
        self.x = x
        self.y = y
grav=0
springgrav = 0

class Platformer(App):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.mousex = 0
        self.mousey = 0
        self.guy = 0
        self.guysprite = None
        self.brick = None
        self.spring = None
        self.listenKeyEvent('keydown', 'p', self.createGuy)
        self.listenKeyEvent('keydown', 'w', self.createBrick)
        self.listenMouseEvent('mousemove', self.motion)
        self.listenKeyEvent('keydown', 'right arrow', self.R)
        self.listenKeyEvent('keydown', 'left arrow', self.L)
        self.listenKeyEvent('keydown', 'up arrow', self.U)
        self.listenKeyEvent('keydown', 'down arrow', self.D)
        self.listenKeyEvent('keydown', 's', self.createSpring)




    def motion(self, event):
        self.mousex = event.x
        self.mousey = event.y
    
    def createBrick(self, event):
        x = self.mousex - self.mousex%30
        y = self.mousey - self.mousey%30
        Brick(x-10, y-10)
    
    def createSpring(self, event):
        global springgrav
        x = self.mousex
        y = self.mousey
        Spring(x, y)
        
    def createGuy (self, event):
        global grav
        if self.guysprite:
            self.guysprite.destroy()
            grav = 0
        self.guysprite = Guy(self.mousex - 30, self.mousey - 30)

    def U(self, event):
        global grav
        if grav == 0:
            grav = -10
            collisions = self.guysprite.collidingWithSprites(Brick)
            if collisions:
                self.guysprite.y += 50

    def D(self, event):
        self.guysprite.y += 5
        collisions = self.guysprite.collidingWithSprites(Brick)
        if collisions:
            self.guysprite.y -= 5
            
    def R(self, event):
        self.guysprite.x += 10
        collisions = self.guysprite.collidingWithSprites(Brick)
        if collisions:
            self.guysprite.x -= 10
            
    def L(self, event):
        self.guysprite.x -= 10
        collisions = self.guysprite.collidingWithSprites(Brick)
        if collisions:
            self.guysprite.x += 10
    
            
    def step(self):
        global grav
        global springgrav
        if self.guysprite:
            grav += 0.5
            self.guysprite.y += grav
            collisions = self.guysprite.collidingWithSprites(Brick)
            if collisions:
                self.guysprite.y -= grav
                grav = 0
            sprang = self.guysprite.collidingWithSprites(Spring)
            if sprang:
                grav -= 10
                self.guysprite.y += grav




myapp = Platformer(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()