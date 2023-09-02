from tkinter import *
import pyshorteners

root = Tk()
root.title("URL Shortener")
root.geometry("700x600")
root.config(bg="#696967")
root.resizable(False,False)

def url():
    if url1.get() == '':
        print("Please Enter URL")
    else:
        url_entry = url1.get()
        result = pyshorteners.Shortener().tinyurl.short(url_entry)
        urlE.insert(END, result)
Label(root,text="URL Shortener ",font=("Times",15,"bold"),fg="black",bg="#696969").pack(pady=10)
frame = Frame(root)
label = Label(frame,text="URL :",font=("Times",15,"bold"),fg="black",bg="#696969").pack(side=LEFT)
url1 = Entry(frame,width=43,font=("Times",15,"bold"),fg="green")
url1.pack()
frame.pack(pady=10)

Button(root,text="Click to Generate Link",font=("Times",15),fg="red",bg="#5996F3",command=url).pack(pady=20)

frame2 = Frame(root)
label1 = Label(frame2,text="Shortened URL : ",font=("Times",15,"bold",),fg="black",bg="#696969").pack(side=LEFT)
urlE = Entry(frame2,width=40,font=("Times",15),fg="blue")
urlE.pack()
frame2.pack(pady=20)
root.mainloop()