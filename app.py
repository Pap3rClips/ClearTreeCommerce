import tkinter
import tkinter.messagebox

# ROOT VARIABLES
MAIN_COLOR = "blue"
SECOND_COLOR = "green"
GENERAL_PADDING = 10

def show_home_page()->None:
    pass

def show_auth_page()->None:
    # Création des frames
    login_frame = tkinter.Frame(root, bg=MAIN_COLOR, padx=GENERAL_PADDING, pady=GENERAL_PADDING)
    register_frame = tkinter.Frame(root, bg=SECOND_COLOR ,padx=GENERAL_PADDING, pady=GENERAL_PADDING)
    
    login_frame.pack()
    register_frame.pack()

    # Events
    def on_login_button_click()->None:
        tkinter.messagebox.showinfo(message="Login action")

    def on_register_button_click()->None:
        tkinter.messagebox.showinfo(message="Register action")

    # Login
    login_username_label = tkinter.Label(login_frame, text="Login : ")
    login_password_label = tkinter.Label(login_frame, text="Password : ")
    login_username_entry = tkinter.Entry(login_frame)
    login_password_entry = tkinter.Entry(login_frame)
    login_button = tkinter.Button(login_frame, text="Login", command=on_login_button_click)

    login_username_label.pack()
    login_username_entry.pack()
    login_password_label.pack()
    login_password_entry.pack()
    login_button.pack()

    # Register
    register_email_label = tkinter.Label(register_frame, text="Email : ")
    register_username_label = tkinter.Label(register_frame, text="Username : ")
    register_password_label = tkinter.Label(register_frame, text="Password : ")
    register_email_entry = tkinter.Entry(register_frame)
    register_username_entry = tkinter.Entry(register_frame)
    register_password_entry = tkinter.Entry(register_frame)
    register_button = tkinter.Button(register_frame, text="Register", command=on_register_button_click)
    
    register_email_label.pack()
    register_email_entry.pack()
    register_username_label.pack()
    register_username_entry.pack()
    register_password_label.pack()
    register_password_entry.pack()
    register_button.pack()

root = tkinter.Tk()
root.title("TreeCommerce")

show_auth_page()

root.mainloop()