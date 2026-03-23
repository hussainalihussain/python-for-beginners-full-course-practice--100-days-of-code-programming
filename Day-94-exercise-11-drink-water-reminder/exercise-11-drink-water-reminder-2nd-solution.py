from text2speech import enhanced_text_to_speech
from reminder import remind
from notification import notify
import asyncio

async def reminder_voice():
  title = "Drik water"
  message = "Please drink water!"

  await notify(title, message)
  enhanced_text_to_speech(message)

asyncio.run(remind(reminder_voice))