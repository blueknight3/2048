from tkinter import PhotoImage
from turtle import Turtle, Screen, Shape
import random as rand
import turtle as trtl
wn =trtl.Screen()
wn.bgpic("2048 background.png")

min1= PhotoImage(file=r"minion 1.png").subsample(17,17)
min2= PhotoImage(file=r"minion 2.png").subsample(8,8)
min3= PhotoImage(file=r"minion 3.png").subsample(3,3)
min4= PhotoImage(file=r"minion 4.png").subsample(2,2)
min5= PhotoImage(file=r"minion 5.png").subsample(3,3)
min6= PhotoImage(file=r"minion 6.png").subsample(3,3)
min7= PhotoImage(file=r"minion 7.png").subsample(13,13)
min8= PhotoImage(file=r"minion 8.png").subsample(5,5)
min9= PhotoImage(file=r"minion 9.png").subsample(3,3)
min10= PhotoImage(file=r"minion 10.png").subsample(15,15)
min11= PhotoImage(file=r"minion 11.png").subsample(8,8)

wn.addshape("min1", Shape("image", min1))
wn.addshape("min2", Shape("image", min2))
wn.addshape("min3", Shape("image", min3))
wn.addshape("min4", Shape("image", min4))
wn.addshape("min5", Shape("image", min5))
wn.addshape("min6", Shape("image", min6))
wn.addshape("min7", Shape("image", min7))
wn.addshape("min8", Shape("image", min8))
wn.addshape("min9", Shape("image", min9))
wn.addshape("min10", Shape("image", min10))
wn.addshape("min11", Shape("image", min11))


arr = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
minen = {"00":0, "01":0, "02":0, "03":0, "10":0, "11":0, "12":0, "13":0, "20":0, "21":0, "22":0, "23":0, "30":0, "31":0, "32":0, "33":0}
hoopla = []
for i in range (1,17):
    m = trtl.Turtle("blank")
    m.speed("fastest")
    m.penup()
    hoopla.append(m)
time = 0
row=0
for t in hoopla:
    if (time ==4):
        row+=1
        time =0
    t.goto((78*time-110),(-78*row+60))
    time+=1

def Game_Over():
    go =trtl.Turtle("blank")
    go.penup
    go.speed("fastest")
    go.goto(-100,0)
    go.write("GAME OVER",font =("Arial", 30, "bold"))


def update():
    for index in range(0,4):
        for inden in range(0,4):
            if (arr[index][inden]==None):
                minen[f"{index}{inden}"]= 0
            elif (arr[index][inden]==1):
                minen[f"{index}{inden}"]= 1
            elif (arr[index][inden]==2):
                minen[f"{index}{inden}"]= 2
            elif (arr[index][inden]==3):
                minen[f"{index}{inden}"]= 3
            elif (arr[index][inden]==4):
                minen[f"{index}{inden}"]= 4
            elif (arr[index][inden]==5):
                minen[f"{index}{inden}"]= 5
            elif (arr[index][inden]==6):
                minen[f"{index}{inden}"]= 6
            elif (arr[index][inden]==7):
                minen[f"{index}{inden}"]= 7
            elif (arr[index][inden]==8):
                minen[f"{index}{inden}"]= 8
            elif (arr[index][inden]==9):
                minen[f"{index}{inden}"]= 9
            elif (arr[index][inden]==10):
                minen[f"{index}{inden}"]= 10
            elif (arr[index][inden]==11):
                minen[f"{index}{inden}"]= 11

def imgstore(int):
    if (int==0):
        return("blank")
    elif (int==1):
        return("min1")
    elif (int==2):
        return("min2")
    elif (int==3):
        return("min3")
    elif (int==4):
        return("min4")
    elif (int==5):
        return("min5")
    elif (int==6):
        return("min6")
    elif (int==7):
        return("min7")
    elif (int==8):
        return("min8")
    elif (int==9):
        return("min9")
    elif (int==10):
        return("min10")
    elif (int==11):
        return("min11")



    
def change():
    index = 0
    inden =0
    for m in hoopla:
        m.shape(imgstore(minen.get(f"{index}{inden}")))
        inden+=1
        if (inden>3):
            index+=1
            inden=0




def rand_start():
    x= rand.randint(0,3)
    x2= rand.randint(0,3)
    y= rand.randint(0,3)
    y2= rand.randint(0,3)
    while (x2==x) and (y2==y):
        x2= rand.randint(0,3)
        y2= rand.randint(0,3)
    arr[y][x] =1
    arr[y2][x2] =1
    print(arr)
    update()
    change()
    
def rand_normal():
    g=0
    for index in range(0,4):
        for inden in range(0,4):
            if (arr[index][inden]!=None):
                g+=1

    if (g==16):
        print("Game Over")
        Game_Over()


    else:
        x = rand.randint(0,3)
        y = rand.randint(0,3)
        while (arr[y][x] != None):
            x= rand.randint(0,3)
            y= rand.randint(0,3)
            print("L",x)
            print("L2",y)
        ran = rand.randint(1,2)
        arr[y][x]=ran
        print(arr)

def allleft():
    for index in range(0,4):
        for inden in range(0,3):
            if(arr[index][inden]==None):
                space = 1
                check = arr[index][inden+space]
                while (check==None) and (space<(3-inden)):
                    space+=1
                    check = arr[index][inden+space]
                if (check != None):
                    arr[index][inden]=arr[index][inden+space]
                    arr[index][inden+space]= None
            else:
                pass

def allright():
    for index in range(0,4):
        for inden in range(-3,0):
            if(arr[index][-inden]==None):
                space = -1
                check = arr[index][-inden+space]
                while (check==None) and (space>(inden)):
                    space-=1
                    check = arr[index][-inden+space]
                if (check != None):
                    arr[index][-inden]=arr[index][-inden+space]
                    arr[index][-inden+space]= None
            else:
                pass

def allup():
    for index in range(0,4):
        for inden in range(0,3):
            if(arr[inden][index]==None):
                space = 1
                check = arr[inden+space][index]
                while (check==None) and (space<(3-inden)):
                    space+=1
                    check = arr[inden+space][index]
                if (check != None):
                    arr[inden][index]=arr[inden+space][index]
                    arr[inden+space][index]= None
            else:
                pass

def alldown():
    for index in range(0,4):
        for inden in range(-3,0):
            if(arr[-inden][index]==None):
                space = -1
                check = arr[-inden+space][index]
                while (check==None) and (space>(inden)):
                    space-=1
                    check = arr[-inden+space][index]
                if (check != None):
                    arr[-inden][index]=arr[-inden+space][index]
                    arr[-inden+space][index]= None
            else:
                pass

def right():
     allright()
     for index in range(0,4):
        for inden in range(-3,0):
            if (arr[index][-inden]!=None):
                space = -1
                normal = arr[index][-inden]
                check = arr[index][-inden+space]
                if (check == normal):
                    arr[index][-inden]+=1
                    arr[index][-inden+space]= None
            else:
                pass
     allright()
     rand_normal()
     update()
     change()

def left():
     allleft()
     for index in range(0,4):
        for inden in range(0,3):
            if (arr[index][inden]!=None):
                space = 1
                normal = arr[index][inden]
                check = arr[index][inden+space]
                if (check == normal):
                    arr[index][inden]+=1
                    arr[index][inden+space]=None
            else:
                pass
     allleft()
     rand_normal()
     update()
     change()


def up():
    allup()
    for index in range(0,4):
        for inden in range(0,3):
            if (arr[inden][index]!=None):
                space = 1
                normal = arr[inden][index]
                check = arr[inden+space][index]
                if (check == normal):
                    arr[inden][index]+=1
                    arr[inden+space][index]=None
            else:
                pass
    allup()
    rand_normal()
    update()
    change()


def down():
     alldown()
     for index in range(0,4):
        for inden in range(-3,0):
            if (arr[-inden][index]!=None):
                space = -1
                normal = arr[-inden][index]
                check = arr[-inden+space][index]
                if (check == normal):
                    arr[-inden][index]+=1
                    arr[-inden+space][index]= None
            else:
                pass
     alldown()
     rand_normal()
     update()
     change()



    

rand_start()
print(arr)
wn.onkeypress(right,"Right")
wn.onkeypress(left,"Left")
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.listen()
wn.mainloop()