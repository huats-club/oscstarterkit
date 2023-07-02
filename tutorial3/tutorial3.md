# Tutorial 3
In this tutorial, we are going to control **Christie Widget Designer** [link](https://www.christiepandorasbox.com/products/widgetdesigner/) with **python udp messaging protocol**.

**Note for user**

As there are not official support for **Open Sound Control (OSC)** in **Widget Designer**. The resources in this tutorial will leverage on **UDP messaging** as a workaround. Communication between OSC and UDP can still be maintain with some translate to embed/de-embed OSC/UDP messages.  

## System Flowchart 
```mermaid
graph LR
A[Raspberry Pi<br>or<br>Computer] --LAN--> B[Christie Widget Designer]
B --> C[Christie Pandora Box]
```

## Installation / Operation
### Sending UDP Message to Widget Designer

1. Edit the **IP Address / Port Number** to the respective Widget designer **Host Computer** (`line 5 and 6`) in `udpmessage.py`
```
UDP_IP = "192.168.0.100"
UDP_PORT = 10066
```

2. Edit the message to embed (`line 11`) in `udpmessage.py`
```
MESSAGE= "Hello There!"
```

3. Run python file
```
python udpmessage.py
or 
python3 udpmessage.py
```

### Receiving UDP Message from Widget Designer

1. Edit the port number for the **UDP server** to listen to (`line 6`) in `udpserver.py`
```
server_port = 10096
```

2. Run `udpserver.py`
```
python udpserver.py
or
python3 udpserver.py
```