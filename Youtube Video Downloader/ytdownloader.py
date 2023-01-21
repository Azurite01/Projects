from pytube import YouTube
from tkinter import*

root = Tk()
root.title("YT Downloader")

def download_mp4(video):
    ys = video.streams.first()
    ys.download()

    dow_ins = Label(root, text="The file has been downloaded in the same ", font=("Helvetica", 12), fg="red")
    dow_ins.grid(row=10, column=0, padx=5, pady=7)
    dow_ins = Label(root, text="file location where this app is present i.e. Downloads.",
                    font=("Helvetica", 12), fg="red")
    dow_ins.grid(row=11, column=0, padx=5, pady=5)
    dow_ins1 = Label(root, text="Thank You for Using !!",
                    font=("Helvetica", 12), fg="red")
    dow_ins1.grid(row=12, column=0, padx=5, pady=5)
    #close = Button(root, text="Close", font=("Helvetica", 10), border=3, command=root.quit())
    #close.grid(row=13, column=0, padx=10, pady=10)



def search_video():
    my_vid = YouTube(link_box.get())
    mero_title = my_vid.title
    title = Label(root, text="Video Title = ", font=("Helvetica", 12))
    title.grid(row=7, column=0, padx=10)
    title2 = Label(root, text= str(mero_title), font=("Helvetica", 12), fg= "red")
    title2.grid(row=8, column=0, padx =10, pady =10)
    downloadmp4 = Button(root, text="Download MP4 FILE (VIDEO)", font=("Helvetica", 10), border=3, command=lambda :download_mp4(my_vid))
    downloadmp4.grid(row=9, column=0, padx=10, pady=10)


info = Label(root,text="Hello everyone. This is a self-made YT video downloader.", font=("Helvetica",11))
info1 = Label(root,text="It downloads the video in mp4 format and the highest available quality",
              font=("Helvetica",11))
info2 = Label(root,text="For using it, please enter the video link exactly from the browser.", font=("Helvetica",11))
info3= Label(root,text="And follow the instructions provided in each step.      Copyright: SWASTIK ARYAL", font=("Helvetica",11))

info.grid(row=0,column=0, padx=5, pady=5)
info1.grid(row=1,column=0, padx=5, pady=5)
info2.grid(row=2,column=0, padx=5, pady=5)
info3.grid(row=3,column=0, padx=5, pady=5)


link_write= Label(root,text="Please enter the video link below.", font=("Helvetica",12), fg="red")
link_write.grid(row=4,column=0,padx=50)

link_box=Entry(root,text="",font=("Helvetica",18),border=10)
link_box.grid(row=5,column=0,pady=10)

Search=Button(root,text="Search",font=("Helvetica",10),border=3, command=search_video)
Search.grid(row=6,column=0, padx=10, pady=10)


root.mainloop()


