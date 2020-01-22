# electionic_guitarist
Scripts for engineering diploma project - Electronic guitarist playing based on music notation

## Requirements

- Raspberry Pi
- Python >= 3.6
- OpenCv >= 3.4

## Scripts and directories
### dictio.py
This script contains dictionaries useful to translate number of GPIO output. Thanks to that solution code is more clear.

### notes.py
This script contains classes of note and staff

### note_recognition
This is crucial script in recognizing notes. It contains algorithms used to detect staff, notes and determine their pitch, length.

### raspi.py
This script is responsible for operating GPIO outputs. It sends proper electric signals to the actuator hitting and pressing string on the corrent fret.

### samples
In this directory are place templates for detecting notes. There are also songs to play on guitar. To add a new song you have to just paste new photo with staffs and notes.
