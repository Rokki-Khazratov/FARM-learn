import asyncio
import time

# Синхронная версия
def download_file():
    start_time = time.perf_counter()  # Засекаем время
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
    end_time = time.perf_counter()  # Засекаем время
    print(f"Sync download completed in {end_time - start_time:.2f} seconds")

# Асинхронная версия
async def async_download_file():
    start_time = time.perf_counter()  # Засекаем время
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
    end_time = time.perf_counter()  # Засекаем время
    print(f"Async download completed in {end_time - start_time:.2f} seconds")

# Запуск
download_file()
asyncio.run(async_download_file())
