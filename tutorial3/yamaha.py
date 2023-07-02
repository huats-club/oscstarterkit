# This python file works with the Raspberry Pi
# Huats 2023

import subprocess
import time 

def run_command(command):
    text = 'python3 command.py '
    config = text + command
    print(config)
    try:
        output = subprocess.check_output(config, shell=True)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}, {e.output.decode('utf-8')}")

def run_recall(command):
    text = 'python3 recall.py '
    config = text + command
    print(config)
    try:
        output = subprocess.check_output(config, shell=True)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}, {e.output.decode('utf-8')}")
    


if __name__ == "__main__":
    command = 'set MIXER:Current/InCh/Fader/Level 0 0 1000'
    run_command(command)
    time.sleep(3)
    command = 'set MIXER:Current/InCh/Fader/Level 1 0 1000'
    run_command(command)
    time.sleep(3)
    command = 'set MIXER:Current/InCh/Fader/Level 2 0 1000'
    run_command(command)
    time.sleep(3)
    command = 'set MIXER:Current/InCh/Fader/Level 3 0 1000'
    run_command(command)
    time.sleep(3)
    command = '8'
    run_recall(command)
    time.sleep(3)
    command = '1'
    run_recall(command)

    x = -5120
    while x < 1128:
        command = 'set MIXER:Current/InCh/Fader/Level 4 0 ' + str(x)
        run_command(command)
        x += 128

    time.sleep(3)
    command = '1'
    run_recall(command)
