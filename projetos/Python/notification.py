# Simple Desktop Notification App
# This simple program will pop a notification every few minutes

from plyer import notification      # Imports from Plyer the class used to create the notification
from time import sleep

def notifyMe(title,message):        # Creates the notifyMe function, which will have a title and a message that can be
                                    # changed later
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\Dregthannum\\Desktop\\water-64.ico",     #"https://www.iconsdb.com/icons/preview/royal-blue/water-xxl.png"
        timeout = 5,                # The time the notification stays on screen

    )


if __name__ == "__main__":
    while True:                     # While the progran runs, this code will keep on going
        notifyMe("Olá Usurário","Lembre de se levantar e tomar água.")
        sleep(1800)                 # Every 30 minutes the notification will pop up