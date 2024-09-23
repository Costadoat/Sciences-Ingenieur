#Import the required Libraries
import PyPDF2
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
from pdf2image import convert_from_path
from PIL import ImageTk, Image
import time
from datetime import datetime
import threading
import pyaudio
import audioop
import wave
import os

#Create an instance of tkinter frame
win= Tk()
win.title("Beamer to Kdenlive")
#Set the Geometry
win.geometry("2000x1200")
# Fichier de sauvegarde
audio_list_index = Listbox(win, selectmode='single')

filesave="save.csv"
if os.path.exists(filesave):
    file=open(filesave,'r')
    contenu=file.read()
    file.close()
    lignes=contenu.split("\n")
    page_list = []
    for page_file_path in lignes[0].split(";")[:-1]:
        img = Image.open(page_file_path)
        page_list.append([ImageTk.PhotoImage(img),page_file_path,ImageTk.PhotoImage(img.resize((496,284)))])
    audio_list = []
    audio_list_order = []
    audio_list_v2 = []
    for audio_line in lignes[1:-1]:
        audio_line=audio_line.split(';')
        if audio_line[0]=='':
            audio_list[-1][2].append([int(audio_line[1]),int(audio_line[2])])
        else:
            audio_list.append([audio_line[1],int(audio_line[2]),[]])
    for audio in audio_list:
        audio_list_order.append(audio[2][0][0])
    for item in audio_list_order:
        i=0
        while audio_list[i][2][0][0]!=item:
            i+=1
        audio_list_v2.append(audio_list[i])
        audio_list_index.insert(i, "Enregistrement %02d" % (i+1))
    audio_list=audio_list_v2
            
            
                                 
else:
    page_list = []
    audio_list = []
    images = convert_from_path("02-V01.pdf")
    for idx,img in enumerate(images):
    #    img.save("img/Page_%02d.png" % (idx+1))
        page_list.append([ImageTk.PhotoImage(img),"img/Page_%02d.png" % (idx+1),ImageTk.PhotoImage(img.resize((496,284)))])


#Create a img Box
canvas = Canvas(win, width = 1260, height = 709)
canvas.pack()
canvas.place(x=100, y=100)
canvas_mini = Canvas(win, width = 496, height = 284)
canvas_mini.pack()
canvas_mini.place(x=1400, y=100)
current_page = IntVar()
current_page.set(0)
global isreading
isreading=False

#Define a function to open the pdf file
def open_pdf():
    file= filedialog.askopenfilename(title="Select a PDF", filetypes=(("PDF    Files","*.pdf"),("All Files","*.*")))
    if file:
       images = convert_from_path(file)
       for img in images:
           img = img.resize((250, 250))
           tkimage = ImageTk.PhotoImage(img)
           canvas.create_image(20,20, anchor=NW, image=img)

def save_duree_img(duree):
    audio_list[audio_list_index.curselection()[0]][2][-1][-1]=duree

def save_duree_sound(duree):
    audio_list[audio_list_index.curselection()[0]][1]=duree

def go_to_page(current):
    if current>=0 and current<len(page_list):
        current_page.set(current)
    update_page()

def next_page():
    current=current_page.get()+1
    go_to_page(current)

def init_page():
    current=0
    go_to_page(current)
    
def previous_page():
    current=current_page.get()-1
    go_to_page(current)

def get_next_page():
    current=current_page.get()
    if len(page_list)>current+1:
        return current+1
    else:
        return None

def go_to_sound(idx_sound):
    if idx_sound>=0 and idx_sound<len(audio_list):
        current=first_page_from_audio(idx_sound)
        current_page.set(current)
    update_page()

def next_sound():
    current=audio_list_index.curselection()[0]+1
    go_to_sound(current)

def init_sound():
    current=0
    go_to_sound(current)
    
def previous_sound():
    current=audio_list_index.curselection()[0]-1
    go_to_sound(current)
    
def save():
    file=open(filesave,'w')
    for page in page_list:
        file.write(page[1]+';')
    file.write('\n')
    for audio in audio_list:
        file.write('Record;'+str(audio[0])+';'+str(audio[1])+'\n')
        for img in audio[2]:
            file.write(';'+str(img[0])+';'+str(img[1])+'\n')
    file.close()
    
def update_page():
    canvas.itemconfig(image_current_page, image=page_list[current_page.get()][0])
    if get_next_page() is not None:
        canvas_mini.itemconfig(image_next_page, state="normal")
        canvas_mini.itemconfig(image_next_page, image=page_list[get_next_page()][2])
    else:
        canvas_mini.itemconfig(image_next_page, state="hidden")
    audio_list_index.selection_clear(0,len(audio_list))
    audio_idx=audio_from_page(current_page.get())
    if audio_idx is not False:
        audio_list_index.selection_set(audio_idx)
        audio_list_index.see(audio_idx)
        label_page_record_name.config(text=audio_list[audio_idx][0])
        label_page_record.config(text=["%02d" % (int(page[0])+1) for page in audio_list[audio_idx][2]])
        norecord=False
    else:
        label_page_record.config(text="Pas d'enregistrement")
        norecord=True
    label_page.config(text="Page: %02d/%02d" % (current_page.get()+1,len(page_list)))
#    print(audio_list)
    try:
        record
    except NameError:
        notrecording=True
    else:
        if record.isrecording:
            notrecording=False
        else:
            notrecording=True
    try:
        sound
    except NameError:
        notreading=True
    else:
        if sound.isreading:
            notreading=False
        else:
            notreading=True

    next_button["state"] = 'disabled'
    previous_button["state"] = 'disabled'
    init_button["state"] = 'disabled'
    delete_record_button["state"] = 'disabled'
    start_record_button["state"] = 'disabled'
    stop_record_button["state"] = 'disabled'
    next_record_button["state"] = 'disabled'
    next_record_button_init["state"] = 'disabled'
    start_read_button["state"] = 'disabled'
    stop_read_button["state"] = 'disabled'

    if notrecording==True:
        if notreading==True:
            next_button["state"] = 'normal'
            previous_button["state"] = 'normal'
            init_button["state"] = 'normal'
            start_record_button["state"] = 'normal'
            if norecord is False:
                delete_record_button["state"] = 'normal'
                start_read_button["state"] = 'normal'
        else:
            stop_read_button["state"] = 'normal'
    else:
        stop_record_button["state"] = 'normal'
        next_record_button["state"] = 'normal'
        next_record_button_init["state"] = 'normal'
    save()


    
def audio_from_page(idx_page):

    for idx_audio,sound in enumerate(audio_list):
        if idx_page in [img[0] for img in sound[2]]:
            return idx_audio
    return False

def audio_from_current_page(idx_page):
    for idx_audio,sound in enumerate(audio_list):
        if idx_page==sound[2][0][0]:
            return idx_audio
    return False

def label_pages():
    if len(audio_list)>0:
        return ["%02d" % page[0] for page in audio_list[idx_audio][2]]
    else:
        return ""

def first_page_from_audio(idx_audio):
    return audio_list[idx_audio][2][0][0]

def update_page_select(event):
    current=first_page_from_audio(audio_list_index.curselection()[0])
    current_page.set(current)
    update_page()

def start_record():
    global record
    # Chercher si un enregistrement existe déjà sur cette page
    audio=audio_from_current_page(current_page.get())
    if audio is not False:
        print('Attention, il existe déjà un enregistrement sur cette page.')
    else:
        # Démarrer le chrono
        chrono.start_over()
        idx=len(audio_list)
        now=datetime.now()
        filename=now.strftime("Record_%Y%m%d%H%M%S.wav")
        audio_list.append([filename,0,[[current_page.get(),0]]])
        audio_list_index.insert(idx, "Enregistrement %02d" % (idx+1))
        audio_list_index.selection_set(idx)
        audio_list_index.see(idx)
        record=SoundRecorder(win,filename)
        record.startrecording()
    update_page()

def stop_record():
    global record
    save_duree_img(chrono.get_duree_img())
    save_duree_sound(chrono.get_duree_sound())
    chrono.stop()
    record.stoprecording()
    update_page()

def start_read():
    global sound
    # Démarrer le chrono
    chrono.start_over()
    sound=SoundReader(win,audio_list[audio_list_index.curselection()[0]])
    sound.startreading()
    update_page()

def stop_read():
    global sound
    chrono.stop()
    sound.stopreading()
    update_page()

def next_record():
    save_duree_img(chrono.get_duree_img())
    if audio_from_page(current_page.get()+1) is not False:
        stop_record()
        print('Il existe déjà un enregistrement sur la page suivante')
    else:
        audio_list[audio_list_index.curselection()[0]][2].append([current_page.get()+1,0])
        next_page()
    update_page()

def next_record_init():
    stop_record()
    next_page()
    start_record()

class Chrono(Label):
    def __init__(self,win):
        Label.__init__(self,win,text='')

        self.value=0
        self.t0_sound=0
        self.t0_img=0
        self.font=('Helvetica', 36, 'normal')
        self.__setitem__('font',self.font)
        self.stopchrono = True

    def formatTime(self):
        m="%02d" % (int(self.value/600))
        s="%02d" % (int((self.value%600)/10))
        d=str((self.value%600)%10)
        return m+': '+s+': '+d

    def get_value(self):
        return self.value

    def get_duree_img(self):
        t1=self.value
        duree=t1-self.t0_img
        self.set_init_img()
        return duree

    def get_duree_sound(self):
        t1=self.value
        duree=t1-self.t0_sound
        self.set_init_sound()
        return duree

    def set_init_img(self):
        self.t0_img=self.value

    def set_init_sound(self):
        self.t0_img=self.value

    def count(self):
        if not self.stopchrono:
            self.value=self.value+1
            self.__setitem__('text',self.formatTime())
            self.after(100,self.count)

    def stop(self):
        self.stopchrono = True

    def start(self):
        self.stopchrono = False
        self.count()

    def start_over(self):
        self.value=0
        self.set_init_img()
        self.set_init_sound()
        self.stopchrono = False
        self.count()

class SoundRecorder():
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100

    frames = []
    def __init__(self, master, filename):
        self.filename = filename
        self.isrecording = False

    def startrecording(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.sample_format,channels=self.channels,rate=self.fs,frames_per_buffer=self.chunk,input=True)
        self.isrecording = True

        print('Recording')
        t = threading.Thread(target=self.record)
        t.start()

    def stoprecording(self):
        self.isrecording = False
        print('recording complete')
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def record(self):
        while self.isrecording:
            data = self.stream.read(self.chunk)
            volume=audioop.rms(data,2)
            progress['value'] = volume/100
            win.update_idletasks()
            self.frames.append(data)

class SoundReader():
    chunk = 1024

    frames = []
    def __init__(self, master, audio):
        if audio is not False:
            self.audio = audio
            self.filename = audio[0]
        self.isreading = False

    def startreading(self):
        self.f = wave.open(self.filename,"rb")
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format = self.p.get_format_from_width(self.f.getsampwidth()),
                    channels = self.f.getnchannels(),
                    rate = self.f.getframerate(),
                    output = True)
        self.isreading = True

        print('Reading')
        self.t = threading.Thread(target=self.read)
        self.t.start()
        
    def read(self):
        self.data = self.f.readframes(self.chunk)
        duree=0
        i=1
        duree=self.audio[2][0][1]
        go_to_page(self.audio[2][0][0])
        while chrono.get_value()<self.audio[1] and self.isreading:
            if chrono.get_value()>=duree and i<len(self.audio[2]):
                duree+=self.audio[2][i][1]
                go_to_page(self.audio[2][i][0])
                i+=1
            self.stream.write(self.data)
            self.data = self.f.readframes(self.chunk)
            volume=audioop.rms(self.data,2)
            progress['value'] = volume/100
            win.update_idletasks()
        chrono.stop()
        self.stream.stop_stream()
        self.stream.close()
        self.isreading = False
        update_page()

        #close PyAudio
        self.p.terminate()

    def stopreading(self):
        self.isreading = False
        
def delete_record():
    current=audio_list_index.curselection()[0]
    filename=audio_list[current][0]
    os.remove(filename)
    del audio_list[current]
    audio_list_index.delete(current)
    if current>0:
        current_page.set(current)
    update_page()

image_current_page=canvas.create_image(20,20, anchor=NW, image=page_list[current_page.get()][0])
    
image_next_page=canvas_mini.create_image(20,20, anchor=NW, image=page_list[get_next_page()][2])
#Define function to Quit the window
def quit_app():
    win.destroy()
#Create a Menu
my_menu= Menu(win)
win.config(menu=my_menu)
#Add dropdown to the Menus
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu= file_menu)
file_menu.add_command(label="Open",command=open_pdf)
file_menu.add_command(label="Quit",command=quit_app)
next_button = Button(win, text =">", command = next_page)
next_button.place(x=1000, y=1050)
init_button = Button(win, text ="0", command = init_page)
init_button.place(x=350, y=1050)
previous_button = Button(win, text ="<", command = previous_page)
previous_button.place(x=400, y=1050)
start_record_button = Button(win, text ="Start", command = start_record)
start_record_button.place(x=500, y=1050)
stop_record_button = Button(win, text ="Stop", command = stop_record)
stop_record_button.place(x=600, y=1050)
next_record_button = Button(win, text ="Next", command = next_record)
next_record_button.place(x=700, y=1050)
next_record_button_init = Button(win, text ="Next Init", command = next_record_init)
next_record_button_init.place(x=800, y=1050)
start_read_button = Button(win, text ="Play", command =start_read)
start_read_button.place(x=1420,y=850)
stop_read_button = Button(win, text ="Stop", command =stop_read)
stop_read_button.place(x=1520,y=850)
delete_record_button = Button(win, text ="Delete", command =delete_record)
delete_record_button.place(x=1620,y=850)
init_sound_button = Button(win, text ="0", command = init_sound)
init_sound_button.place(x=1420, y=800)
previous_sound_button = Button(win, text ="<", command = previous_sound)
previous_sound_button.place(x=1520, y=800)
next_sound_button = Button(win, text =">", command = next_sound)
next_sound_button.place(x=1620, y=800)
chrono = Chrono(win)
chrono.pack()
chrono.place(x=550, y=850)
# Progress bar widget
progress = Progressbar(win, orient = HORIZONTAL,length = 500, mode = 'determinate')
progress.pack()
progress.place(x=480, y=950)
audio_list_index.pack()
audio_list_index.place(x=1420, y=420)
audio_list_index.bind('<<ListboxSelect>>', update_page_select)
label_page=Label(win,text="Page: %02d/%02d" % (1,len(page_list)))
label_page.place(x=1400,y=1000)
label_page_record_name=Label(win,text="Nom l'enregistrement")
label_page_record_name.place(x=1400,y=950)
label_page_record_txt=Label(win,text="Pages liées à l'enregistrement")
label_page_record_txt.place(x=1400,y=1000)
label_page_record=Label(win,text="Pas d'enregistrement")
label_page_record.place(x=1400,y=1050)
update_page()
win.mainloop()
