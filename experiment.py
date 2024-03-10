import os
from time import time, sleep

# Settings
IMAGES_COUNT = 10
CAPTURE_DELAY_SEC = 30
LIGHTS = ["r", "g", "b", "w", "i"]
FILTERS = ["i", "v"]
COMMAND = "sudo ~/cam/bin/python capture.py -l {lights} -f {filters}".format

time_last = 0
for i in range(IMAGES_COUNT):
    if time() - time_last >= CAPTURE_DELAY_SEC:
        time_last = time()
        for light in LIGHTS:
            for filter in FILTERS:
                os.system(COMMAND(lights=light, filters=filter))
                sleep(1)
    else:
        sleep(1)
