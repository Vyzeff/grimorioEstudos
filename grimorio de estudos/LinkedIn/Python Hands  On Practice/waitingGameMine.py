from random import randint
import time

def waitingGame():
    
    waitTime = randint(1, 5)
    print(f"Once you press enter, you will have to wait for {waitTime}, then press enter again. The more accurate you are the better\n")
    input("=============PRESS ENTER=============")
    start = time.perf_counter()

    input("Waiting....\n")
    timeCount = time.perf_counter() - start
    
    print(f"Time passed: {timeCount:0.3f} seconds.")
    
    if timeCount == waitTime:
        print("WOW you actually got it.")
    elif timeCount > waitTime:
        print(f"Damn, {(timeCount - waitTime):0.3f} seconds too late.")
    else:
        print(f"{(waitTime - timeCount):0.3f} seconds too soon")
    return 0

if __name__ == "__main__":
    waitingGame()