import tkinter as tk
from tkinter.font import BOLD
import subprocess
import sys
app = tk.Tk()  
tx = "Connecting User..."
back = "black"
fore = "white"

#User defined Function area
def restart():
  subprocess.Popen([sys.executable, __file__])

def send():
  user_input = tplace.get()
  if user_input == "":
      return
  txt1.insert(tk.END, f"User: {user_input}\n")
  tplace.delete(0, tk.END)
def new_chat():
  exec(open('main.py').read())

def end_chat():
  txt1.insert(tk.END, "Chat Ended\n")
  txt1.config(state=tk.DISABLED)

#GUI area
#Menu bar
options=tk.Menu(app)
menu=tk.Menu(options,tearoff=0)
menu.add_command(label="New Chat",command=restart)
menu.add_command(label="End Chat",command=end_chat)
menu.add_command(label="Exit", command=app.quit)
options.add_cascade(label="File", menu=menu)
app.config(menu=options)



app.title('Chat Window') #title of the window
app.geometry('500x500') #size of the window
app.configure(bg=back) #default background color

#text containing "Connecting User..."
txt = tk.Label(text=tx, font=('Helvetica', 13), bg=back, fg=fore)
txt.place(x=0, y=0)

#Space container for reading containing sender as well as receiver messages
space=tk.Frame(app,  width=500, height=400)
space.place(x=10, y=100)

txt1 = tk.Text(space,font=('Helvetica', 13))
txt1.grid(row=1, column=0, columnspan=2)

#scroll property toggle
scrollbar = tk.Scrollbar(space)
scrollbar.place(relheight=1, relx=0.974)

#User input
tplace_frame = tk.Frame(app)
tplace_frame.place(x=0, y=space.winfo_height()+570, width=500, height=40)

#text box
tplace = tk.Entry(tplace_frame, bg=fore, fg=back)
tplace.place(x=10, y=0, width=380, height=30)

#Send Button
post = tk.Button(tplace_frame, text='Send', font=('Helvetica', 14,BOLD), command=send)
post.place(x=390, y=0, width=80, height=30)

#Chat window execution
app.mainloop()



