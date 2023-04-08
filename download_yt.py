import tkinter as tk 
from tkinter import *
from pytube import YouTube 
from tkinter import messagebox, filedialog 
  
def Widgets(): 
    link_label = Label(root, text="YouTube link  :",  bg="#E8D579") 
    link_label.grid(row=1,  column=0,  pady=5,  padx=5) 
   
    root.linkText = Entry(root,  width=55,  textvariable=video_Link) 
    root.linkText.grid(row=1,   column=1,  pady=5,  padx=5,  columnspan = 2) 
   
    destination_label = Label(root,   text="Destino    :",  bg="#E8D579") 
    destination_label.grid(row=2,  column=0,  pady=5,  padx=5) 
   
    root.destinationText = Entry(root,  width=40,  textvariable=download_Path) 
    root.destinationText.grid(row=2,   column=1,  pady=5,  padx=5) 
   
    browse_B = Button(root,   text="Navegar",  command=Browse,  width=10,  bg="#05E8E0") 
    browse_B.grid(row=2, column=2,  pady=1,  padx=1) 
   
    Download_B = Button(root,  text="Download",   command=Download,   width=20,  bg="#05E8E0") 
    Download_B.grid(row=3,  column=1,  pady=3,  padx=3) 
  
  
def Browse():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH") 
    download_Path.set(download_Directory) 

def Download(): 
    Youtube_link = video_Link.get() 
    download_Folder = download_Path.get() 
    getVideo = YouTube(Youtube_link) 
    videoStream = getVideo.streams.first() 
    videoStream.download(download_Folder) 
   
    
    messagebox.showinfo(f"COM SUCESSO",  "BAIXADO E SALVO EM\n {download_Folder}") 
root = tk.Tk() 
root.geometry("600x120") 
root.resizable(False, False) 
root.title("YouTube_Video_Downloader") 
root.config(background="#000000") 
video_Link = StringVar() 
download_Path = StringVar() 
Widgets()
root.mainloop() 




























# import tkinter as tk 
# from tkinter import *
# from pytube import YouTube 
# from tkinter import messagebox, filedialog 
  
# def Widgets(): 
#     link_label = Label(root, text="YouTube link  :",  bg="#E8D579") 
#     link_label.grid(row=1,  column=0,  pady=5,  padx=5) 
   
#     root.linkText = Entry(root,  width=55,  textvariable=video_Link) 
#     root.linkText.grid(row=1,   column=1,  pady=5,  padx=5,  columnspan = 2) 
   
#     destination_label = Label(root,   text="Destination    :",  bg="#E8D579") 
#     destination_label.grid(row=2,  column=0,  pady=5,  padx=5) 
   
#     root.destinationText = Entry(root,  width=40,  textvariable=download_Path) 
#     root.destinationText.grid(row=2,   column=1,  pady=5,  padx=5) 
   
#     browse_B = Button(root,   text="Browse",  command=Browse,  width=10,  bg="#05E8E0") 
#     browse_B.grid(row=2, column=2,  pady=1,  padx=1) 
   
#     Download_B = Button(root,  text="Download",   command=Download,   width=20,  bg="#05E8E0") 
#     Download_B.grid(row=3,  column=1,  pady=3,  padx=3) 
  
  
# def Browse():
#     download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH") 
#     download_Path.set(download_Directory) 

# def Download(): 
#     Youtube_link = video_Link.get() 
#     download_Folder = download_Path.get() 
#     getVideo = YouTube(Youtube_link) 
#     videoStream = getVideo.streams.first() 
#     videoStream.download(download_Folder) 
   
    
#     messagebox.showinfo(f"COM SUCESSO",  "BAIXADO E SALVO EM\n {download_Folder}") 
# root = tk.Tk() 
# root.geometry("600x120") 
# root.resizable(False, False) 
# root.title("YouTube_Video_Downloader") 
# root.config(background="#000000") 
# video_Link = StringVar() 
# download_Path = StringVar() 
# Widgets()
# root.mainloop() 