# Tutorial 1
In this tutorial, we are going to send a simple **OSC** message from one raspberry pi to another. 

Sample code is located under the `tutorial1` folder. 

## System Flowchart (Scenario 1)

```mermaid
graph LR

A[RPi B<br>osc_client.py] --> B[RPi A<br>osc_server.py]
```

### Instruction
 
1.  Identify the IP address of the Raspberry Pi Server, in this particular case, **RPi A**. Type the following command on the terminal of **RPi A**.
```
ifconfig
```

If you are using **Ethernet Connection**, identify the *IP address* under the `eth0` section.

If you are using **WiFi Connection**, identify the *IP address* under the `wlan0` section. 

2. Edit the server IP address `receiver_ip` (*line 4*) in `osc_server.py` file (**RPi A**)

Open and edit `osc_server.py` (please make sure you are in the correct directory)
```
nano osc_server.py
```

Enter corresponding **IP Address** retrieved in **Step 1** into `line 4`. Below is an example
```
receiver_ip = "192.168.1.100"
```

Save and exit **nano editor**
```
Crtl + O
Crtl + X
```

3. Edit the desination IP address `PI_A_ADDR` (*line 16*) in `osc_client.py` file (**RPi B**).

Open and edit `osc_client.py` 
```
nano osc_client.py
```

Enter corresponding **IP Address** retrieved in **Step 1** into `line 16`. Below is an example
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
<br><br>

## System Flowchart (Scenario 2)

```mermaid
graph LR
A[RPi B<br>osc_client] --> B[RPi A<br>osc_ptp.py]
B --> C[RPi B<br>osc_server.py]
```

### Instruction

1. Identify **IP Address** of both **RPi A** and **RPi B**
2. Open and edit `osc_ptp.py` file on **RPi A**. 
```
nano osc_ptp.py
```
Edit `server_ip` (`line 4`) with the **IP Address** of **RPi A**. Below is an example
```
server_ip = "192.168.1.100"
```

Edit `receiver_ip` (`line 8`) with the **IP Address** of **RPi B**. Below is an example
```
receiver_ip = "192.168.1.101"
```
Save and edit **nano editor**
```
Crtl + O
Crtl + X
```
3. Open and edit `osc_client` file on **RPi B**.
```
nano osc_client.py
```
Enter **RPi A IP Address** into `line 16`. Below is an example
```
PI_A_ADDR = "192.168.1.100"
```
Save and edit **nano editor**
```
Crtl + O
Crtl + X
```
4. Open and edit `osc_server` file on **RPi B**.
```
nano osc_server.py
```
Enter corresponding **RPi B IP Address** into `line 4`. Below is an example
```
receiver_ip = "192.168.1.100"
```

Save and exit **nano editor**
```
Crtl + O
Crtl + X
```

5. Run the following python file on **RPi A**
```
python3 osc_ptp.py
```
6. Run the following python files on **RPi B**
```
python3 osc_server.py (seperate terminal)
python3 osc_client.py (seperate terminal)
```