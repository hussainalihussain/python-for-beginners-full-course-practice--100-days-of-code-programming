'''
🍽️ Example 2: Restaurant kitchen
You have multiple orders (of burgers) in restaurants
....
👉 5 burgers cook together, not one by one
'''
import asyncio

async def make_burger(order):
  print(f"Making burger {order}")
  await asyncio.sleep(3)
  print(f"Burger {order} ready")

async def main():
  tasks = []

  for i in range(5):   # 5 orders
    tasks.append(make_burger(i))
  
  # if something = [task1, task2, task3]
  # *something = task1, task2, task3
  # so
  # fun_call(*something) = fun_call(task1, task2, task3)

  await asyncio.gather(*tasks)

asyncio.run(main())
