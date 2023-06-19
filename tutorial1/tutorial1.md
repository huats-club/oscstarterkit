# Tutorial 1
In this tutorial, we are going to send a simple **OSC** message from one raspberry pi to another. 

Sample code is located under the `tutorial1` folder. 

## System Flowchart

```mermaid
graph LR

A[RPi A<br><font size=2>osc_server.py] --> B[RPi B<br><font size=2>osc_client.py]
```

## Instruction
 
1.  Identify the IP address of the Raspberry Pi Server, in this particular case, **RPi A**. Type the following command on the terminal of **RPi A**.
```
ifconfig
```

If you are using **Ethernet Connection**, identify the *IP address* under the `eth0` section.

If you are using **WiFi Connection**, identify the *IP address* under the `wlan0` section. 

2. Edit the server IP address `receiver_ip` (*line 4*) in `osc_server.py file.

Open and edit `osc_server.py` (please make sure you are in the correct directory)
```
nano osc_server.py
```

Enter corresponding *IP Address* retrieved in **Step 1** into `line 4`. Below is an example
```
receiver_ip = "192.168.1.100"
```

Save and exit **nano editor**
```
Crtl + O
Crtl + X
```

3. Edit the desination IP address `PI_A_ADDR` (*line 16*) in `osc_client.py` file.

Open and edit `osc_client.py` 
```
nano osc_client.py
```

Enter corresponding *IP Address* retrieved in **Step 1** into `line 16`. Below is an example
```
PI_A_ADDR = "192.168.1.100"
```

Save and exit **nano editor**
```
Crtl + O
Crtl + X
```

4. Execute `osc_server.py` 
```
python3 osc_server.py
```

5. Excute `osc_client.py` 
```
python3 osc_client.py
```