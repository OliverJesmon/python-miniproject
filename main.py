
import tkinter as tk
import socket
import sys
import threading
import alias
import subprocess

app = tk.Tk()
user=str()
def restart():
    app.quit()
    subprocess.Popen([sys.executable, __file__])

def user_receive():
    while True:
        try:
            message = users.recv(1024).decode('utf-8')
                txt1.insert(tk.END, message)
        except:
            txt1.insert(tk.END, "Error")
            end_chat()
            break

def send():
    user_input = tplace.get()
    if user_input == "":
        return
    letter = f"{user}: {user_input}\n"
    txt1.insert(tk.END, letter)
    users.send(letter.encode('utf-8'))
    tplace.delete(0, tk.END)

#Function to end the chat conversation
def end_chat():
    end="Chat Ended\n"
    txt1.insert(tk.END, end)
    users.send(end.encode('utf-8'))
    txt1.config(state=tk.DISABLED)
    return

def begin():
    name = alias.dialogue()
    data=f'{name} has joined the chat'
    rec_thread = threading.Thread(target=user_receive)
    rec_thread.start()
    txt1.insert(tk.END, data)
    users.send(data.encode('utf-8'))
    return

address = input("Enter the server address: ")
users = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
users.connect((address, 59000))
print(f"Connected to {address}")
begin()

options = tk.Menu(app)
menu = tk.Menu(options, tearoff=0)
menu.add_command(label="Start new Chat", command=restart)
menu.add_command(label="End Chat", command=end_chat)
menu.add_command(label="Exit", command=app.quit)
options.add_cascade(label="File", menu=menu)
app.config(menu=options)

app.title('Chat Window')
app.geometry('500x500')
app.configure(bg='Grey')


txt = tk.Label(text="Connecting User...", font=('Helvetica', 13), fg='Brown')
txt.place(x=0, y=30)

space = tk.Frame(app, width=500, height=400)
space.place(x=10, y=100)

txt1 = tk.Text(space, font=('Helvetica', 13))
txt1.grid(row=1, column=0, columnspan=2)

scrollbar = tk.Scrollbar(space)
scrollbar.place(relheight=1, relx=0.974)

tplace_frame = tk.Frame(app)
tplace_frame.place(x=0, y=space.winfo_height()+570, width=500, height=40)

tplace = tk.Entry(tplace_frame, bg='green', fg='Black', font=('Helvetica', 13), cursor='xterm')
tplace.config()  # Added line to set highlighting color to green
tplace.place(x=10, y=0, width=380, height=30)

post = tk.Button(tplace_frame, text='Send', font=('Helvetica', 14, 'bold'), command=send)
post.place(x=390, y=0, width=80, height=30)

app.mainloop()
#programmed by Oliver
