import random as rand
import turtle as trtl
wn =trtl.Screen()
arr = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]
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
    print(arr[y][x]+arr[y2][x2])
    
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
    print(arr)

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
    print(arr)

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
    print(arr)

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
    print(arr)

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
     print(arr)

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
     print(arr)


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
    print(arr)


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
     print(arr)


    

rand_start()
print(arr)
wn.onkeypress(right,"Right")
wn.onkeypress(left,"Left")
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.listen()
wn.mainloop()