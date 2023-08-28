import time
import playsound

def alarm(alarmTime, file, text):
    print(f"Alarm set for {alarmTime} seconds.")
    time.sleep(int(alarmTime))
    playsound.playsound(file) # used quack.wav for testing porpuses. Worked.
    print(text)
    
if __name__ =="__main__":
    alarmTime = input("Seconds: ")
    sound = input("Sound url: ")
    alarmText = input("Alarm note: ")
    
    alarm(alarmTime, sound, alarmText)