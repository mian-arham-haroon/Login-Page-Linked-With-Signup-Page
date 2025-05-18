from tkinter import *
from PIL import ImageTk
import pymysql
from tkinter import messagebox
def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    chack.set(0)
    
def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()==''or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All fileds are required')
    elif passwordEntry.get()!=confirmEntry.get():
        messagebox.showerror('Error','Password not match')
    elif chack.get()==0:
        messagebox.showerror('Error','Please accept term and conditions')
    else:
        try:
            # Connect to MySQL
            con = pymysql.connect(host='localhost', user='root', password='arham@12345678@')
            mycursor = con.cursor()

            # Create database if not exists
            mycursor.execute('CREATE DATABASE IF NOT EXISTS userdata')
            mycursor.execute('USE userdata')

            # Create table if not exists
            mycursor.execute('''
                CREATE TABLE IF NOT EXISTS data (
                    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                    email VARCHAR(50),
                    username VARCHAR(100),
                    password VARCHAR(20)
                )
            ''')
            query='select * from data where username=%s'
            mycursor.execute(query,(usernameEntry.get()))

            row=mycursor.fetchone()
            if row !=None:
                messagebox.showerror('Error', f'Username alrady exists')
            else:
                # Insert user data
                query = 'INSERT INTO data(email, username, password) VALUES (%s, %s, %s)'
                mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
                con.commit()
                con.close()

                messagebox.showinfo('Success', 'Registration is successful')
                clear()
                signup_window.destroy()
                import signin

        except Exception as e:
            messagebox.showerror('Error', f'Database connectivity issue: {e}')



def login_page():
    signup_window.destroy()
    import signin

signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(signup_window,image=background)

bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',18,'bold'),
              bg='white',fg='firebrick1')
heading.grid(row=0 ,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',bg='white',fg='firebrick1',font=('Microsoft Yahei UI Light',10,'bold'))
emailLabel.grid(row=1,column=0,sticky='w',padx=25)
emailEntry=Entry(frame,width=30,bg='firebrick1',fg='white',font=('Microsoft Yahei UI Light',10,'bold'))
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',bg='white',fg='firebrick1',font=('Microsoft Yahei UI Light',10,'bold'))
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
usernameEntry=Entry(frame,width=30,bg='firebrick1',fg='white',font=('Microsoft Yahei UI Light',10,'bold'))
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',bg='white',fg='firebrick1',font=('Microsoft Yahei UI Light',10,'bold'))
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry=Entry(frame,width=30,bg='firebrick1',fg='white',font=('Microsoft Yahei UI Light',10,'bold'))
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmLabel=Label(frame,text='Confirm Password',bg='white',fg='firebrick1',font=('Microsoft Yahei UI Light',10,'bold'))
confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
confirmEntry=Entry(frame,width=30,bg='firebrick1',fg='white',font=('Microsoft Yahei UI Light',10,'bold'))
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

chack=IntVar()
termsandconditions=Checkbutton(frame,bg='white',fg='firebrick1',text='I agree to the Terms & Conditions',
                               variable=chack,activeforeground='firebrick1',cursor='hand2',activebackground='white',font=('Microsoft Yahei UI Light',9,'bold'))
termsandconditions.grid(row=9,column=0,pady=10,padx=15)



signupButton=Button(frame,text='Signup',font=('open sans',16,'bold')
                    ,activeforeground='white',bd=0,width=17,activebackground='firebrick1'
                    ,cursor='hand2',fg='white',background='firebrick1',command=connect_database)

signupButton.grid(row=10,column=0,pady=10)

alradyaccountLabel=Label(frame,bg='white',text="Don't have an account?",font=('open sans',9,'bold'),fg='firebrick1')
alradyaccountLabel.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text='Login',font=('open sans',9,'bold underline')
                        ,activeforeground='blue',bd=0,activebackground='white',cursor='hand2'
                        ,fg='blue',background='white',command=login_page)
loginButton.place(x=170,y=394)

























signup_window.mainloop()