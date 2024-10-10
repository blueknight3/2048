import random as rand
arr = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
def rand_start():
    for start in range(0,2):
        x= rand.randint(0,3)
        y= rand.randint(0,3)
        print(x)
        print(y)
        arr[y][x] =1
        print(arr)
rand_start()