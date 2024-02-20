import tkinter as tk

app = tk.Tk()  
tx = "Connecting User..."
back = "black"
fore = "white"
options=tk.Menu(app)
menu=tk.Menu(options,tearoff=0)
menu.add_command(label="New Chat")
menu.add_command(label="End Chat")
menu.add_command(label="Exit", command=app.quit)
options.add_cascade(label="File", menu=menu)
app.config(menu=options)

def send():
    user_input = tplace.get()
    if user_input == "":
        return
    txt1.insert(tk.END, f"User: {user_input}\n")
    tplace.delete(0, tk.END) 

app.title('Chat Window')
app.geometry('500x500')
app.configure(bg=back)

txt = tk.Label(text=tx, font=('Arial', 12), bg=back, fg=fore)
txt.place(x=0, y=0)

conn = tk.Button(text='Connect', font=('Arial', 12), bg=back, fg=fore)
conn.place(x=10, y=50, width=100, height=30)

space=tk.Frame(app,  width=500, height=400)
space.place(x=10, y=100)

txt1 = tk.Text(space,font=('Arial', 12))
txt1.pack(padx=10, pady=10)

scrollbar = tk.Scrollbar(space)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
txt1.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=txt1.yview)

tplace_frame = tk.Frame(app, bg=back)
tplace_frame.place(x=10, y=510, width=400, height=40)

tplace = tk.Entry(tplace_frame, bg=fore, fg=back)
tplace.place(x=10, y=0, width=380, height=30)

post = tk.Button(tplace_frame, text='Send', font=('Arial', 12), command=send)
post.place(x=390, y=0, width=80, height=30)

app.mainloop()
