import asyncio
import random

# Производитель: добавляет задачи в очередь
async def producer(queue, n):
    for i in range(1, n + 1):
        task_time = random.randint(1, 5)  # Время обработки задачи (случайное)
        await queue.put((i, task_time))   # Добавляем задачу в очередь
        print(f"Task {i} added to queue (processing time: {task_time}s)")
    await queue.put(None)  # Добавляем маркер окончания

# Потребитель: берёт задачи из очереди и обрабатывает их
async def consumer(queue, name):
    while True:
        task = await queue.get()  # Получаем задачу из очереди
        if task is None:  # Проверяем маркер окончания
            print(f"Consumer {name}: No more tasks. Exiting...")
            queue.task_done()
            break
        task_id, task_time = task
        print(f"Consumer {name}: Processing task {task_id} for {task_time}s...")
        await asyncio.sleep(task_time)  # Эмуляция обработки задачи
        print(f"Consumer {name}: Finished task {task_id}")
        queue.task_done()  # Сообщаем, что задача выполнена

# Основная функция
async def main():
    queue = asyncio.Queue()  # Создаём очередь
    num_tasks = 3        # Количество задач
    num_consumers = 1        # Количество потребителей

    # Запускаем производителя
    producer_task = asyncio.create_task(producer(queue, num_tasks))

    # Запускаем потребителей
    consumer_tasks = [
        asyncio.create_task(consumer(queue, f"Consumer-{i+1}")) 
        for i in range(num_consumers)
    ]

    # Дожидаемся завершения всех задач
    await producer_task
    await queue.join()  # Ждём, пока все задачи в очереди будут выполнены

    # Завершаем потребителей
    for c in consumer_tasks:
        await c

# Запуск программы
asyncio.run(main())