from tkinter import*
from PIL import Image , ImageTk
import action 


def User_send():
    send = entry1.get()
    bot = action.Action(send)
    text.insert(END, "Me --> "+send+"\n")
    if bot != None:
        text.insert(END, "Bot <-- "+ str(bot)+"\n")
    if bot == "ok sir":
          root.destroy()  
          

def delete_text():
    text.delete("1.0", "end")


root = Tk()
root.geometry("550x675")
root.title("Assistant")
root.resizable(False,False)
root.config(bg="#6F8FAF")

  
# Main Frame
Main_frame = LabelFrame(root , padx=100 ,  pady=7 , borderwidth=3 ,  relief="raised")
Main_frame.config(bg="#6F8FAF")
Main_frame.grid(row = 0 ,  column= 1 ,  padx= 55 ,  pady =  10)

# Text Lable 
Text_lable = Label(Main_frame, text = "Assistant" , font=("comic Sans ms" ,  14 , "bold" ) , bg = "#356696")
Text_lable.grid(row=0 ,  column=0 , padx=20 , pady= 10)


# Image 
Display_Image = ImageTk.PhotoImage(Image.open("image/assitant.png"))
Image_Lable = Label(Main_frame, image= Display_Image)
Image_Lable.grid(row = 1 ,  column=0 , pady=20)



# Add a text widget
text=Text(root , font= ('Courier 10 bold') , bg = "#356696")
text.grid(row = 2,  column= 0)
text.place(x= 100, y= 375, width= 375, height= 100) 




# Add a entry widget
entry1 = Entry(root, justify = CENTER)
entry1.place(x=100 , y = 500 , width= 350, height= 30)




# Add a text button2
button2 =  Button(root,  text="Send" , bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=User_send)
button2.place(x= 120, y= 575,width=150)

# Add a text button3
button3 = Button(root, text="Delete", bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,command=delete_text)
button3.place(x= 300,y= 575, width=150)
root.mainloop()

# python -m pip install pillow
# python -m pip install SpeechRecognition
# python -m pip install PyAudio
# pip install pyttsx3
# pip install requests-html==0.10.0
# pip install lxml==4.9.1