import random
from tkinter import*
root=Tk()
root.geometry("1000x1000")
root.title("Lucky Friend Wheel")
names=["Aarav","Shrut","Aahana","Vrinda","Farzan","Anirudh","Shaurya","Noor","Miheer","Aayush","Veer","Ritika","Ritwik","Aryan"]


list_1=Label(root, text=names)
list_1.place(relx=0.5,rely=0.3,anchor=CENTER)

random_name=Label(root)
random_name.place(relx=0.5,rely=0.5,anchor=CENTER)

def random_friend():
    lucky_friend=random.randint(0,13)
    index_friend=names[lucky_friend]
    random_name["text"]="Your lucky friend is "+index_friend

work=Button(root,text="Spin the Wheel",command=random_friend)
work.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()
