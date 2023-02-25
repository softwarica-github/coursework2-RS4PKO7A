from tkinter import *
import subprocess


# create the main window
root = Tk()
root.geometry("300x200")
root.title("Authentication")

# create a label for username
user_label = Label(root, text="Username:")
user_label.pack()

# create an entry for username
user_entry = Entry(root, width=30)
user_entry.pack()

# create a label for password
pass_label = Label(root, text="Password:")
pass_label.pack()

# create an entry for password
pass_entry = Entry(root, width=30, show="*")
pass_entry.pack()


# function to authenticate the user
def authenticate():
    # read the username and password from the file
    with open("accounts.txt", "r") as f:
        accounts = [line.strip().split(":") for line in f]

    # check if the entered username and password match any account
    for account in accounts:
        if user_entry.get() == account[0] and pass_entry.get() == account[1]:
            # authentication succeeded, close the window and run the program
            root.destroy()
            subprocess.call(['python','image_steganography_second.py'])
            return

    # authentication failed, clear the entry fields and put the user in a loop of authentication
    user_entry.delete(0, END)
    pass_entry.delete(0, END)
    user_entry.focus()

# create a button to authenticate the user
auth_button = Button(root, text="Authenticate", command=authenticate)
auth_button.pack()


# function to create a new account
def create_account():
    # create a new window for creating an account
    new_window = Toplevel()
    new_window.geometry("300x200")
    new_window.title("Create Account")

    # create a label for username
    user_label = Label(new_window, text="Username:")
    user_label.pack()

    # create an entry for username
    user_entry = Entry(new_window, width=30)
    user_entry.pack()

    # create a label for password
    pass_label = Label(new_window, text="Password:")
    pass_label.pack()

    # create an entry for password
    pass_entry = Entry(new_window, width=30, show="*")
    pass_entry.pack()

    # function to save the new account to a file
    def save_account():
        # open the file in append mode and write the username and password
        with open("accounts.txt", "a") as f:
            f.write(user_entry.get() + ":" + pass_entry.get() + "\n")

        # close the window
        new_window.destroy()

    # create a button to save the new account
    save_button = Button(new_window, text="Create Account", command=save_account)
    save_button.pack()

# create a button to create a new account
create_button = Button(root, text="Create Account", command=create_account)
create_button.pack()

# run the main event loop
root.mainloop()
