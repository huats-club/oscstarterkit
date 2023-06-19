# Tutorial 2
In this tutorial, we are going to use a push button as a triggering device to transmit an **OSC message** from one **Raspberry Pi** to another.

## System Flowchat
```mermaid
graph LR
A[Push Button<br>Raspberry Pi Pin 27] --> B[RPi B]
B --> C[RPi A]
```

## About RPi.GPIO
**RPI.GPIO** is a python library for controlling the General Purpose Input / Output (GPIO) pins on a Raspberry Pi. We are using the **RPi.GPIO** library to configure the **Raspberry Pi** internal **Pull Up/Down** resistor.

### Installation
```
sudo apt update
sudo apt install python3-rpi.gpio
```
or 
```
pip3 install RPi.GPIO==0.7.0
```

### GPIO default states when pins are set to input mode on Raspberry Pi
```
GPIO 0 - 8 : HIGH (3.3V)
GPIO 9 - 27 : LOW (0V)
```

### Checking GPIO states on Raspberry Pi
1. You can run `gpio_states.py` located in `./tutorial2` directory 
```
python3 gpio_states.py
```

or 

2. 
```
raspi-gpio get <Pin Number>
```