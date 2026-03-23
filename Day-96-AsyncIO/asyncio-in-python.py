from time import sleep
import asyncio

async def fun1():
  print('fun1 started....')
  await asyncio.sleep(10)
  print('fun1 called!')

  return 'fun1'

async def fun2():
  print('fun2 started....')
  await asyncio.sleep(3)
  print('fun2 called!')

async def fun3():
  print('fun3 started....')
  await asyncio.sleep(3)
  print('fun3 called!')

async def main():
  # Normal calling
  # await fun1()
  # await fun2()
  # await fun3()
  # return

  # Async calling
  results = await asyncio.gather( 
    fun1(),
    fun2(),
    fun3()
  )

  print(results)


asyncio.run(main())