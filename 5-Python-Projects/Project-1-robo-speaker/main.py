import os

def say(text):
    command = f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"'
    os.system(command)

if __name__ == '__main__':
    while True:
        user_input  = input("Say something to speak: ")

        if  user_input == 'q':
            say("Good bay friend!")
            break

        say(user_input)
