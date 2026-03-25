'''
🧩 Python example (super simple)

You:
1. Put Maggi on stove
2. While it cooks → you do homework
3. When ready → you eat

👉 Smart use of time
👉 Both run together

'''

import asyncio

async def cook():
  print("Cooking Maggi...")
  await asyncio.sleep(3)
  print("Maggi ready")

async def homework():
  print("Doing homework...")
  await asyncio.sleep(2)
  print("Homework done")

async def main():
  await asyncio.gather(
    cook(),
    homework()
  )

asyncio.run(main())