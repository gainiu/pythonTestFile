
import asyncio
import datetime

async def worker1():
    print('worker1 start')
    await asyncio.sleep(1)
    print('worker1 end')

async def worker2():
    print('worker2 start')
    await asyncio.sleep(2)
    print('worker2 end')

async def main():
    task1=asyncio.create_task(worker1())
    task2=asyncio.create_task(worker2())
    print('before start')
    await task1
    print('await worker1')
    await task2
    print('await worker2')
start=datetime.datetime.now()
asyncio.run(main())
end=datetime.datetime.now()
print('wait time :{}s'.format((end-start).seconds))