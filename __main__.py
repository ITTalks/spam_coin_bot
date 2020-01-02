import threading
import os

threads_value = 10


for i in range(threads_value):
    start = ((2 ** 64) // threads_value) * i
    end = ((2 ** 64) // threads_value) * (i + 1)

    threading.Thread(
        target=os.system, args=(f"python mine.py {start} {end} {i}",)
    ).start()
