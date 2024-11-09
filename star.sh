#!/bin/bash

###### EJECUTAR E-READER ############

#Asignar el modulo de audio
	pacmd set-default-sink alsa_output.usb-Solid_State_System_Co._Ltd._USB_PnP_Audio_Device_000000000000-00.analog-stereo


#sudo su -c "source .venv/bin/activate && python tk.py"
sudo su -c "cd /home/unl/unl2024 && source .venv/bin/activate && python tk.py"
