import os
from time import time, sleep

# Settings
IMAGES_COUNT = 10
CAPTURE_DELAY_SEC = 30
LIGHTS = ["r", "g", "b", "w", "i"]
FILTERS = ["i", "v"]
COMMAND = "sudo ~/cam/bin/python capture.py -l {lights} -f {filters}".format
DEBUG = True

time_last = 0
for i in range(IMAGES_COUNT):
    if time() - time_last >= CAPTURE_DELAY_SEC:
        time_last = time()
        if debug:
            print("Taking image", i + 1)
        for light in LIGHTS:
            for filter in FILTERS:
                command = COMMAND(lights=light, filters=filter)
                if debug:
                    print("Command:", command)
                os.system(command)
                sleep(1)
    else:
        sleep(1)
