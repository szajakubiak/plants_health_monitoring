# Plants health monitoring
 Plants health assessment using image analysis methods

## Goals
To optimize the use of water and fertilizers while producing food there is a need to assess plants health in real time. This can be done by analyzing images taken in different light conditions, optimially using camera capable of recording IR light.

## Methods
The following hardware was used:
* Raspberry Pi Compute Module 4 with dedicated IO board
* Raspberry Pi Camera Module 2 (V2.1)
* Raspberry Pi NOIR Camera Module 2 (V2.1)
* IR LED
* four RGBW LEDs
* filter passing only IR light

Both cameras are used to take images in different light conditions. Green LEDs and combinations of red and blue LEDs can be used to search for plant's leafs in the image. IR LED is used to plant's health assessment, which is assumed to be proportional to the amount of reflected light of this wavelength.

## Connections
Camera modules were connected as follows:
| IO board | Camera  |
| -------- | --------|
| CAM0     | Regular |
| CAM1     | NoIR    |

## Links
[Libcamera documentation](https://www.raspberrypi.com/documentation/computers/camera_software.html#getting-started)

[Picamera2 documentation](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf)

[Setting up cameras with Compute Module](https://www.raspberrypi.com/documentation/computers/compute-module.html#attaching-a-raspberry-pi-camera-module)

[Signature Optical Cues: Emerging Technologies for Monitoring Plant Health](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3675540/)

[Active and Passive Electro-Optical Sensors for Health Assessment in Food Crops](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7795220/)

[Using near IR to look for photosynthesis and plant health with NDVI](https://www.richardmudhar.com/blog/2015/07/using-near-ir-to-look-for-photosynthesis-and-plant-health-with-ndvi/)

[Raspberry Pi Infragram](https://publiclab.org/wiki/raspberry-pi-infragram)
