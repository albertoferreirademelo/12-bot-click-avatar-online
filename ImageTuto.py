#import ImageGrab
import os
import time
import win32api, win32con
import SendKeys


#Globals
#------------
x_pad = 279
y_pad = 225
Names = ["Tiskwan", "baskwan", "beskwan", "biskwan", "boskwan", "buskwan", "caskwan", "ceskwan", "ciskwan", "coskwan", "cuskwan"]
NewNames = ["daskwan", "deskwan", "diskwan", "doskwan", "duskwan","faskwan", "feskwan", "fiskwan", "foskwan", "fuskwan","gaskwan", "geskwan", "giskwan", "goskwan", "guskwan","haskwan", "heskwan", "hiskwan", "hoskwan", "huskwan","jaskwan", "jeskwan", "jiskwan", "joskwan", "juskwan","kaskwan", "keskwan", "kiskwan", "koskwan", "kuskwan","laskwan", "leskwan", "liskwan", "loskwan", "luskwan","maskwan", "meskwan", "miskwan", "moskwan", "muskwan","naskwan", "neskwan", "niskwan", "noskwan", "nuskwan","paskwan", "peskwan", "piskwan", "poskwan", "nuskwan"]
Farm18 = ["Farmerz1", "Farmerz2", "Farmerz3", "Farmerz4", "Farmerz5", "Farmerz6"]
Farm20 = ["Heh1", "Heh2", "Heh3", "Heh4", "Heh5", "Heh6", "Heh7", "Heh8", "Heh9"]
Farm23 = ["cog1", "cog2", "cog3", "cog4", "cog5", "cog6", "cog7", "cog8", "cog9"]
Farm26 = ["gungrave1", "gungrave2", "gungrave3", "gungrave4", "gungrave5", "gungrave6", "gungrave7", "gungrave8", "gungrave9"]
Farm28 = ["other4", "other5", "other6", "other7", "other8", "other9"]
Farm38 = ["evo1", "evo2", "evo3", "evo4", "evo5", "evo6", "evo7", "evo8", "evo9"]



Cord:
    #Login Menu
    l_login = (536,420)
    l_signUp = (500,350)
    l_ok = (500,560)
    #First menu
    m_menu = (49,576)
    m_home = (241,429)
    m_arena = (241,529)
    m_minerals = (792,371)
    m_logout = (976,116)
    m_logoutok = (513,383)
    m_setting = (900,110)
    settings_ok = (500,380)
    settings_exit = (1000,20)
    settings_User = (500,800)
    min_one = (170,130)
    min_oneClick = (170,80)
    min_two = (500,130)
    min_twoClick = (500,80)
    min_three = (840,130)
    min_threeClick = (840,80)
    min_exit = (1000,20)
    
    #--------Arena menu
    a_search = (644,54)
    a_searchok = (957,58)
    a_reload = (150,60)
    a_leftone = (112,164)
    a_lefttwo = (88,300)
    a_leftthree = (79,478)
    a_rightone = (218,170)
    a_righttwo = (219,321)
    a_rightthree = (192,478)
    a_fight = (347,575)
    #-------Inside the fight (skip)
    fight_skip = (722,447)
    #Ovrigt
    centerClick = (480,300)
    failedConnect = (620,230)
    StorX = (1100,-20)


 

    
### Not necessary anymore    
''' 
def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+1023, y_pad+599)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print 'left Down'
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print 'left release'
    
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
'''
    
def leftClick(tempo):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(tempo)
    
    
def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
     

def LogOff():
    mousePos(Cord.m_menu)
    leftClick(.5)
    mousePos(Cord.m_home)
    leftClick(.5)
    #logout of the game
    mousePos(Cord.m_logout)
    leftClick(.5)
    mousePos(Cord.m_logoutok)
    leftClick(.5)
    
def startGame():
    #Starting BlueStacks
    os.startfile("C:\Program Files (x86)\BlueStacks\HD-StartLauncher.exe")
    time.sleep(10)
    #click on Avatar Fight
    mousePos((434,286))
    leftClick(10)    
    #second click to enter the game
    mousePos((434,286))
    leftClick(3)
    #logout of the game
    LogOff()
    
def Login_Start(count):
    mousePos(Cord.l_login)
    leftClick(.5)
    LoginInfo = """
    {ENTER} {PAUSE 1}
    password{ENTER}{PAUSE 1}
    {ENTER}{PAUSE 1}
    {ENTER}{PAUSE 1}
    """
    SendKeys.SendKeys(Names[count]+LoginInfo)
    time.sleep(15)
    leftClick(.2)
    leftClick(.2)
    mousePos(Cord.centerClick)
    leftClick(.5)
    mousePos(Cord.centerClick)
    leftClick(.5)
    
def Create_Char(count):
    mousePos(Cord.l_signUp)
    leftClick(.5)
    mousePos(Cord.l_ok)
    leftClick(15)
    mousePos(Cord.centerClick)
    leftClick(1)
    leftClick(1)
    leftClick(1)
    leftClick(1)
    mousePos(Cord.m_setting)
    leftClick(20)
    mousePos(Cord)
    LoginInfo = """
    {ENTER} {PAUSE 1}
    password{ENTER}{PAUSE 1}
    {ENTER}{PAUSE 1}
    {ENTER}{PAUSE 1}
    """
    SendKeys.SendKeys(NewNames[count]+LoginInfo)
    time.sleep(20)    
    mousePos(Cord.centerClick)
    leftClick(1)
    mousePos(Cord.settings_ok)
    leftClick(1)
    mousePos(Cord.settings_exit)
    
def Mining():
    mousePos(Cord.m_minerals)
    leftClick(.5)
    mousePos(Cord.min_one)
    leftClick(10)
    mousePos(Cord.centerClick)
    leftClick(.2)
    mousePos(Cord.min_one)
    leftClick(.2)
    mousePos(Cord.min_oneClick)
    leftClick(10)
    mousePos(Cord.min_two)
    leftClick(5)
    mousePos(Cord.centerClick)
    leftClick(5)
    mousePos(Cord.min_two)
    leftClick(5)
    mousePos(Cord.min_twoClick)
    leftClick(5)
    mousePos(Cord.min_three)
    leftClick(5)
    mousePos(Cord.centerClick)
    leftClick(5)
    mousePos(Cord.min_three)
    leftClick(5)
    mousePos(Cord.min_threeClick)
    leftClick(5)
    mousePos(Cord.min_exit)
    leftClick(5)
    
    
def Fighting():
    def Enemies(where):
        mousePos(where)
        leftClick(.2)    
        mousePos(Cord.a_fight)
        leftClick(3)
        mousePos(Cord.fight_skip)
        leftClick(.2)    
        mousePos(Cord.fight_skip)
        leftClick(.2)    
        mousePos(Cord.fight_skip)
        leftClick(.2)
        leftClick(.2)
        leftClick(1)
        leftClick(3)
        mousePos(Cord.centerClick)
        leftClick(.5)
        mousePos(Cord.centerClick)
        leftClick(2)
        
    mousePos(Cord.m_menu)
    leftClick(1)    
    mousePos(Cord.m_arena)
    leftClick(5)
    mousePos(Cord.centerClick)
    leftClick(.5)
    mousePos(Cord.centerClick)
    leftClick(.5)
     
    Enemies(Cord.a_leftone)
    Enemies(Cord.a_lefttwo)
    Enemies(Cord.a_leftthree)
    Enemies(Cord.a_rightone)
    Enemies(Cord.a_righttwo)
    Enemies(Cord.a_rightthree)
    
def Farming(Level):
    LevelCount = 0    
    while (LevelCount < (len(Level))):
        print LevelCount        
        LevelCount = LevelCount+1
    
    
def main():
    Farming(Farm26)                
    
if __name__ == '__main__':
    main()