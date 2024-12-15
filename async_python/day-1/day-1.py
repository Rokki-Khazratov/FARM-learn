# Асинхронный Python (синхронность vs асинхронность).
import asyncio


# Задача: Эмуляция скачивания файлов
import time

# sinxronnaya verisya
def download_file():
    print('sync')
    print("Downloading file1...")
    time.sleep(3)
    print("file1 downloaded!")
    print("Downloading file2...")
    time.sleep(2)
    print("file2 downloaded!")
    print("Downloading file3...")
    time.sleep(1)
    print("file3 downloaded!")

run = download_file()


#asinxronnaya verisya
async def async_download_file():
    print('Async')
    print("Downloading file1...")
    await asyncio.sleep(3) 
    print("file1 downloaded!")
    print("Downloading file2...")
    await asyncio.sleep(2) 
    print("file2 downloaded!")
    print("Downloading file3...")
    await asyncio.sleep(1) 
    print("file3 downloaded!")


asyncio.run(async_download_file())