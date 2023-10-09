# Plants health monitoring
Plants health assessment using image analysis methods

## Goals
To optimize the use of water and fertilizers while producing food there is a need to assess plants health in real time. This can be done by analyzing images taken in different light conditions, optimially using camera capable of recording IR light. Additional visible light filter can be used to quantify amount of IR light reflected by plant's leafs.

## Hardware
### Raspberry Pi computer with a day / night camera
* Raspberry Pi 3 Model A
* OV5647 camera module with switchable IR filter
* two IR LEDs
* four RGBW LEDs
* filter passing only IR light (wavelength from 700 nm to 1600 nm)

### Raspberry Pi Pico with a day / night camera
* Raspberry Pi Pico W
* OV7670 camera module
* switchable IR filter
* filter passing only IR light (wavelength from 700 nm to 1600 nm)

### PySpectrometer2
Results obtained using camera observation were compared with spectrograms recorded using [PySpectrometer2](https://github.com/leswright1977/PySpectrometer2).

## IR filter control
Both cameras are equipped with lens mount with switchable IR filter. OV5647 module is additionaly equipped with phtoresistors and potentiometers to automatically control IR filter and brightness of IR LEDs.

## Links
[Libcamera documentation](https://www.raspberrypi.com/documentation/computers/camera_software.html#getting-started)

[Picamera2 documentation](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf)

[Using OV7670 camera in CircuitPython](https://docs.circuitpython.org/projects/ov7670/en/latest/)

[Wiring camera to Raspberry Pi Pico](https://learn.adafruit.com/capturing-camera-images-with-circuitpython/raspberry-pi-pico-wiring)

[Signature Optical Cues: Emerging Technologies for Monitoring Plant Health](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3675540/)

[Active and Passive Electro-Optical Sensors for Health Assessment in Food Crops](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7795220/)

[Using near IR to look for photosynthesis and plant health with NDVI](https://www.richardmudhar.com/blog/2015/07/using-near-ir-to-look-for-photosynthesis-and-plant-health-with-ndvi/)

[Raspberry Pi Infragram](https://publiclab.org/wiki/raspberry-pi-infragram)

## TODO:
* Connection diagram for device with Pico W
* 3D printed stand for PySpectrometer2
* Connection diagram for IR filter controller
* 3D printed mounts for RGB LED rings for both cameras
* 3D printed mount for IR LED for OV7670 camera module
