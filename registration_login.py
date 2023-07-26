#hw login registration addprocuct 
import tkinter as t
import os
#design screen for registration
def register():
    global register_screen
    register_screen = t.Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x290")

    global username
    global password
    global username_entry
    global password_entry
    global age
    global mobile
    global age_entry
    global mobile_entry
   
    username = t.StringVar()
    password = t.StringVar()
    age=t.StringVar()
    mobile=t.StringVar()
    t.Label(register_screen, text="Please enter details below", bg='#A1CCD1').pack()
    t.Label(register_screen, text="").pack()
    username_lable = t.Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = t.Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = t.Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = t.Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    t.Label(register_screen, text="").pack()
    age_lablel = t.Label(register_screen, text="age")
    age_lablel.pack()
    age_entry = t.Entry(register_screen, textvariable=age)
    age_entry.pack()
    mobile_lable = t.Label(register_screen, text="Mobile")
    mobile_lable.pack()
    mobile_entry = t.Entry(register_screen, textvariable=mobile)
    mobile_entry.pack()
    t.Button(register_screen, text="Register", width=10, height=1, bg="#A1CCD1", command = register_user).pack()


# design screen for login 

def login():
    global login_screen
    login_screen = t.Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x400")
    t.Label(login_screen, text="Please enter details below to login").pack()
    t.Label(login_screen, text="").pack()

    global username_verify
    global password_verify
    global age_verify
    global mobile_verify
    

    username_verify = t.StringVar()#string variable of us_name
    password_verify = t.StringVar()
    age_verify=t.StringVar()
    mobile_verify=t.StringVar()

    global username_login_entry
    global password_login_entry
    global user_age
    global user_mobile

    t.Label(login_screen, text="Username * ").pack()
    username_login_entry = t.Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    t.Label(login_screen, text="").pack()
    t.Label(login_screen, text="Password * ").pack()
    password_login_entry = t.Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    t.Label(login_screen, text="").pack()
    
    t.Label(login_screen, text="age * ").pack()
    user_age = t.Entry(login_screen)
    user_age.pack()
    t.Label(login_screen, text="mobile * ").pack()
    user_mobile = t.Entry(login_screen)
    user_mobile.pack()
    t.Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
    
# implementing event on register button

def register_user():

    username_info = username.get()
    password_info = password.get()
    age1=age.get()
    mobile1=mobile.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info+"\n")
    file.write(age1+"\n")
    file.write(mobile1)
    file.close()

    username_entry.delete(0,10)
    password_entry.delete(0,10)

    t.Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

# implement on login button 

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    # username_login_entry.delete(0,10)
    # password_login_entry.delete(0,10)
    age1=age_verify.get()
    mobile1=mobile_verify.get()
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if age1 in verify :
            login_sucess()

        else:
            password_not_recognised()
        # print(verify)
        print(age1)

    else:
        user_not_found()
        print(age1)

# design popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = t.Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    t.Label(login_success_screen, text="Login Success").pack()
    t.Button(login_success_screen, text="OK", command=delete_login_success).pack()

# design popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = t.Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    t.Label(password_not_recog_screen, text="Invalid Password ").pack()
    t.Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# design popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = t.Toplevel(login_screen)
    user_not_found_screen.title("success")
    user_not_found_screen.geometry("150x100")
    t.Label(user_not_found_screen, text="user Not Found").pack()
    t.Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# designing main(first) window

def main_account_screen():
    global main_screen
    main_screen = t.Tk()
    main_screen.geometry("300x400")
    main_screen.title("account login")
    t.Label(text="select Your Choice", bg="#A1CCD1", width="300", height="2", font=("Calibri", 13)).pack()
    t.Label(text="").pack()
    t.Button(text="Login", height="2", width="30", command = login).pack()
    t.Label(text="").pack()
    t.Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()
