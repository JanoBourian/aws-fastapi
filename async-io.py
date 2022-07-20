import asyncio
import time 

## sync execute

def sync_count(sleep_time):
    print(f"One with sleep_time {sleep_time}")
    time.sleep(sleep_time)
    print(f"Two with sleep_time {sleep_time}")

def sync_main():
    for num in (2, 1, 3):
        sync_count(num)

## async execute

async def async_count(sleep_time):
    print(f"One with sleep_time {sleep_time}")
    await asyncio.sleep(sleep_time)
    print(f"Two with sleep_time {sleep_time}")

async def async_main():
    await asyncio.gather(async_count(2), async_count(1), async_count(3))

start = time.time()
# sync_main()
asyncio.run(async_main())
end = time.time()

elapsed = end - start
print(f"{__file__} executed in {elapsed:0.2f} seconds")
