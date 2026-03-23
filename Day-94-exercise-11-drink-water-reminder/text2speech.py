import pyttsx3

def get_engine():
  return pyttsx3.init()

def simple_text_to_speech(text):
  engine = get_engine()
  engine.say(text)
  engine.runAndWait()

def enhanced_text_to_speech(text):
  engine = get_engine()

  # Get available voices
  voices = engine.getProperty('voices')

  # Set the second voice (index 1 is often a female voice, index 0 male, etc., depending on OS)
  engine.setProperty('voice', voices[1].id)

  # Adjust the speaking rate (words per minute)
  engine.setProperty('rate', 150)

  # Adjust the volume (0.0 to 1.0)
  engine.setProperty('volume', 0.9)

  engine.say(text)
  engine.runAndWait()


if __name__ == '__main__':
  # simple_text_to_speech("Hello World")
  enhanced_text_to_speech("Hello World")

