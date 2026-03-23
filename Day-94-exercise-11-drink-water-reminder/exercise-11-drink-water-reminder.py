# Drink water reminder
# after some interval the computer should say something like "Drink water"
# for now it should be small interval of time like 1 minute but for real use case use 30-60 minutes

# somehow the win32com.client is not working, saying module not found so we need to install it
# i already installed it before and was working fine but i don't know if mistakenly removed....
# import win32com.client
import time

# speaker = win32com.client.Dispatch("SAPI.SpVoice")
noError = True

try:
  waiting_in_minutes = int(input("Number of minutes of interval? "))
  waiting_in_seconds = waiting_in_minutes * 60
  print(f"Waiting for {waiting_in_minutes} minutes for water!")

  while noError:
    time_taken_in_seconds = 0;


    # Fancy thing to show the . or time count 1, 2, 3, ....
    # but then we need to remove: time.sleep(waiting_in_seconds)
    # while time_taken_in_seconds < waiting_in_seconds - 1:
    #   time_taken_in_seconds += 1
    #   # print('.', end=' ')
    #   print(time_taken_in_seconds)
    #   time.sleep(1)


    time.sleep(waiting_in_seconds)

    print(".....Drink water.....")
    # speaker.Speak("Drink water")
except Exception as e:
  noError = False
  print(e)
