#0 = closed, 1 = open
door = [False] * 101

''' 
def doors(step=1):
    for x in range(1, 101, step):
        door[x] = not door[x]
        print(door[x])
            
doors()

def loop():
    for i in range(1, 100):
        doors(i)
         '''
for a in range (1, 101):
    for b in range(a, 100, a):
        door[b] = not door[b]
        print(door[b])
        
for x in range(1, 101):
    if door[x] is True:
        print(f"{x}, ")