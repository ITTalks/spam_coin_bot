import subprocess
import time

token = "token"
process_value = 10


for i in range(process_value):
    # thread_name = i

    start = ((2 ** 64) // process_value) * i
    end = ((2 ** 64) // process_value) * (i + 1)

    if i == process_value - 1:
        subprocess.Popen(f"python mine.py {start} {end} {i} {token}").wait()

    else:
        subprocess.Popen(f"python mine.py {start} {end} {i} {token}")

    time.sleep(0.2)
