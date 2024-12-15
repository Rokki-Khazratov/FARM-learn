import asyncio
import time

# # Синхронная версия
# def download_file():
#     start_time = time.perf_counter()  # Засекаем время
#     print('sync')
#     print("Downloading file1...")
#     time.sleep(3)
#     print("file1 downloaded!")
#     print("Downloading file2...")
#     time.sleep(2)
#     print("file2 downloaded!")
#     print("Downloading file3...")
#     time.sleep(1)
#     print("file3 downloaded!")
#     end_time = time.perf_counter()  # Засекаем время
#     print(f"Sync download completed in {end_time - start_time:.2f} seconds") itog:6.01s

# # Асинхронная версия
# async def async_download_file():
#     start_time = time.perf_counter()  # Засекаем время
#     print('Async')
#     print("Downloading file1...")
#     await asyncio.sleep(3)
#     print("file1 downloaded!")
#     print("Downloading file2...")
#     await asyncio.sleep(2)
#     print("file2 downloaded!")
#     print("Downloading file3...")
#     await asyncio.sleep(1)
#     print("file3 downloaded!")
#     end_time = time.perf_counter()  # Засекаем время
#     print(f"Async download completed in {end_time - start_time:.2f} seconds") itog:6.00s

# # Запуск
# download_file()
# asyncio.run(async_download_file())


#async way using gather as a loop:

async def download_file(file_count,sleep_time):
    print(f"Downloading {file_count}...")
    await asyncio.sleep(sleep_time)
    print(f"{file_count} downloaded!")    

async def main():
    start_time = time.perf_counter()  # Засекаем время
    files = [
        download_file("File1", 3),
        download_file("File2", 2),
        download_file("File3", 1),
    ]
    await asyncio.gather(*files)
    end_time = time.perf_counter()  # Засекаем конец
    print(f"Total execution time: {end_time - start_time:.2f} seconds") #itog 3.00s
    

asyncio.run(main())