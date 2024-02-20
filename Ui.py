import tkinter as tk

app = tk.Tk()  
tx = "Connecting User..."
back = "black"
fore = "white"
def send():
  user_input = tplace.get()
  txt1.insert(tk.END, f"User: {user_input}\n")


app.title('Chat Window')
app.geometry('500x00')
app.configure(bg=back)



txt = tk.Label(text=tx, font=('Arial', 12), bg=back, fg=fore)
txt.place(x=0, y=0)


conn = tk.Button(text='Connect', font=('Arial', 12), bg=back, fg=fore)
conn.place(x=0, y=20)

space=tk.Frame(app,width=70)
space.bind()
space.place(x=0, y=60)
txt1 = tk.Text(space,font=('Arial', 12))
txt1.pack()


scrollbar = tk.Scrollbar(space)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
txt1.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=txt1.yview)




tplace = tk.Entry(bg=fore, fg=back)
tplace.bind()
tplace.place(x=0, y=500)
'''def send():
  user_input = tplace.get()
  txt1.insert(tk.END, f"User: {user_input}\n")
'''
post = tk.Button(text='Send', font=('Arial', 12), command=send)
post.bind()
post.place(x=170, y=498)



app.mainloop()
