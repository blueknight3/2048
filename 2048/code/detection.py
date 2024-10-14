import random as rand
import turtle as trtl
wn =trtl.Screen()
arr = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
minen = {"00":None, "01":None, "02":None, "03":None, "10":None, "11":None, "12":None, "13":None, "20":None, "21":None, "22":None, "23":None, "30":None, "31":None, "32":None, "33":None}
hoopla = []
font_setup = ("Arial", 20, "normal")
for i in range (1,17):
    m = trtl.Turtle()
    m.penup()
    hoopla.append(m)
time = 0
row=0
for t in hoopla:
    if (time ==4):
        row+=1
        time =0
    t.goto((50*time),(-50*row))
    time+=1




def update():
    for index in range(0,4):
        for inden in range(0,4):
            if (arr[index][inden]==None):
                minen[f"{index}{inden}"]= None
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
    
def change():
    index = 0
    inden =0
    for m in hoopla:
        m.write(minen.get(f"{index}{inden}"),font_setup)
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
    
def rand_normal():
    g=0
    for index in range(0,4):
        for inden in range(0,4):
            if (arr[index][inden]!=None):
                g+=1

    if (g==16):
        print("Game Over")


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



    

rand_start()
print(arr)
wn.onkeypress(change,"n")
wn.onkeypress(right,"Right")
wn.onkeypress(left,"Left")
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.listen()
wn.mainloop()