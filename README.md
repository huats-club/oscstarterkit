# oscstarterkit
This repository contains resources to get you started on using **Python Open Sound Control (OSC)** messaging protocol between several devices.
1. Raspberry Pi 
2. Desktop / Laptop
3. Audio Visual Equipment

In this starterkit, we will explore the following scenarios to expand our understanding on integrating **OSC**:
1. **Tutorial 1**: Raspberry Pi to Raspberry Pi OSC Communication - Click [here](./tutorial1/tutorial1.md)
2. **Tutorial 2**: Push Button (GPIO) to Pi to Pi OSC Communication - Click [here](./tutorial2/tutorial2.md)
3. **Tutorial 3**: Python UDP Message (Raspberry Pi) to Christie Widget Designer - Click [here](./tutorial3/tutorial3.md)
4. **Tutorial 4**: Raspberry Pi to Yamaha CL/QL Console - Click [here](./tutorial4/tutorial4.md)

## Dependencies
The code base in this repository has been test using **Python 3.9 or higher**.

## Setting Up
If you new to setting up a **Raspberry Pi** single board computer, please visit [**Huats Club rpistarterkit**](https://github.com/huats-club/rpistarterkit) as a quick setup guide. 

## Installing Python OSC
**Python-osc** is a Python library for sending and receiving **Open Sound Control (OSC)** messages. OSC is a protocol for communication among computers, sound synthesizers, and other multimedia devices that is widely used in the field of electronic music and multimedia applications.

Python-osc provides a convenient way to work with OSC in Python by offering functions and classes for creating OSC messages, handling OSC bundles (a collection of OSC messages), and establishing OSC communication between different devices or software applications. It supports both OSC over UDP (User Datagram Protocol) and OSC over TCP (Transmission Control Protocol) for network communication.

### To Install Python-OSC
**On Raspberry Pi**
```
pip3 install python-osc==1.8.1
```

**On Desktop/Laptop**
```
pip install python-osc==1.8.1
```


Special Shoutout to Huats Member, Ms Hannah Lee for contributing her time in building this repository.