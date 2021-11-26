from random import choice
pointZero=[0,0]
pointNow=pointZero.copy()
dictionary={'north':[1,0],'east':[0,1],'south':[-1,0],'west':[0,-1]}
def random_walk(cycles):
    for _ in range(cycles):
        direction=choice(list(dictionary.keys()))
        pointNow[0]+=dictionary[direction][0]
        pointNow[1]+=dictionary[direction][1]
def check_blocks():
    return abs(pointNow[0])+abs(pointNow[1])
def check(cycles):
    random_walk(cycles)
    print("return by bus because your pointNow is bigger than 7 blocks:",pointNow)\
    if check_blocks()>7\
    else print("return by foot because your pointNow is smaller than 7 blocks:",pointNow)
    pointZero=[0,0]   
check(55)