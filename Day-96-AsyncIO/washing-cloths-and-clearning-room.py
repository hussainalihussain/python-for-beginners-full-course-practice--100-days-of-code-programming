import asyncio

async def washing():
  print("Washing clothes started")
  await asyncio.sleep(5)
  print("Clothes washed")

async def cleaning():
  print("Cleaning room")
  await asyncio.sleep(3)
  print("Room clean")

async def main():
  await asyncio.gather(
    washing(),
    cleaning()
  )
  print("Both works done")

asyncio.run(main())