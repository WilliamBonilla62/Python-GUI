import serial
from tkinter import *
import threading

mutex=threading.Lock()
write_bytes=b''


#Code fait par William Ricardo Bonilla Villatoro
root =Tk()
root.title("MASVUS INC.")
root.minsize(600,600)
theLabel=Label(root, text="Logiciel MASVUS", bg="green",fg="white")
theLabel.pack(fill=X)
topFrame= Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

#Declaration de button de communication
button1=Button(topFrame, text="Connection", fg="green", command="init_serial")
button1.pack(side=LEFT)
port_com=Entry(topFrame)
port_com.pack(side=LEFT)

button2=Button(topFrame, text="Lecture du coeur et de l'oxygen", fg="red", command="ReadHeartBeat")
button2.pack(side=LEFT)

button3=Button(topFrame, text="Lecture activité musculaire", fg="blue", command="ReadMuscle")
button3.pack(side=LEFT)

button3=Button(topFrame, text="Lecture activité musculaire", fg="blue", command="Fermer")
button3.pack(side=LEFT)

def init_serial():
    com.port=port_com.get()
    com.open()
    com1 = serial.Serial(port_com.get(),9600)
    read_thread = threading.Thread(target=worker)
    read_thread.start()
    print('Connection au port',port_com.get())

def ReadHeartBeat():
    global write_bytes
    mutex.acquire()
    write_bytes+=b'1'
    mutex.release()

def ReadMuscle():
    global write_bytes
    mutex.acquire()
    write_bytes+=b'0'
    mutex.release()

#Communication serie

root.mainloop()
