import win32com.client

people = ['Amir', 'Junaid', 'Akbar']

speaker = win32com.client.Dispatch("SAPI.SpVoice")


for person in people:
    speaker.Speak(f"Shoutout to {person}")