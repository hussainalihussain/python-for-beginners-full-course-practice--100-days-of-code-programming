from time import sleep

'''
REMINDER_MINUTES is the number of minutes to remind to you to drink water
it should be something like 30-60 minutes, best is 45 minutes
but for quick test we can use '1' minute or even less like seconds by doing this:
REMINDER_MINUTES = 0.1
'''
REMINDER_MINUTES = 1

async def remind(callback, reminder_minutes = None):
  while True:
    wait_for_minutes = REMINDER_MINUTES

    if reminder_minutes != None:
      wait_for_minutes = reminder_minutes

    sleep(wait_for_minutes * 60)
    await callback()
  
