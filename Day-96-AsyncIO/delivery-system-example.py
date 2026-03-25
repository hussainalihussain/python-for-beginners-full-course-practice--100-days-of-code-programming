import asyncio

async def deliver(vehicle, time):
  print(f"Delivering {vehicle} in {time} seconds")

  await asyncio.sleep(time)

  print(f"{vehicle} delivered in {time} seconds")

async def main():
  await asyncio.gather(
    deliver("Car", 5),
    deliver("Truck", 6),
    deliver("Bike", 3),
  )

asyncio.run(main())