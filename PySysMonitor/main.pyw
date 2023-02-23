from tkinter import *
import sv_ttk
import serial
import serial.tools.list_ports
from tkinter import ttk
from tkinter import messagebox
import psutil
from time import sleep
import sys

# Create an instance of tkinter frame or window
win=Tk()

win.title("Set settings")
# Set the size of the window
win.geometry("250x150")

def get_port_names():
    retlist = []
    for i in serial.tools.list_ports.comports():
        retlist.append(str(i.device))
    return retlist
def launch_transmitting():
    cpl = comport.get()
    if cpl == "":
        messagebox.showerror("Error!", "Not selected com port, verify your choice.")
    else:
        messagebox.showinfo("Info", "Now, the window will gone and send data to your device.\nYou can shut down the window only by task manager!")
        win.withdraw()
        start_transmitting(cpl)
def start_transmitting(comp):
    ser = serial.Serial(comp, 9600)
    while True:
        cpul = round(psutil.cpu_percent())
        memal = round(psutil.virtual_memory().available / 1024 / 1024 / 1024, 1)
        memtot = round(psutil.virtual_memory().total / 1024 / 1024 / 1024)
        memus = memtot - memal
        meml = str(round(memus, 1)) + "/" + str(memtot) + "GB"
        ser.write(str.encode("#CPU" + str(cpul)) + str.encode("MEM" + meml))
        sleep(1)
sv_ttk.set_theme("dark")
comport = ttk.Combobox(values=get_port_names())
startbtn = ttk.Button(win, text="Start!", width=23, command=launch_transmitting)
hintlbl = ttk.Label(win, text="To start transmitting, please\nconnect your device, select\nCOM port and click start button.")
comport.pack(pady=5)
startbtn.pack(pady=5)
hintlbl.pack(pady=5)
win.mainloop()
