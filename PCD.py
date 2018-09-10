import sqlite3
import sys
from easygui import *

db = sqlite3.connect('Programming Club Details')
cursor = db.cursor()
cursor.execute(''' CREATE TABLE Member(id INTEGER PRIMARY KEY,name TEXT,phone INTEGER,email TEXT unique,Dept TEXT,Year INTEGER)''')
cursor.execute(''' CREATE TABLE Events(id INTEGER PRIMARY KEY,name TEXT,Date INTEGER unique,Coname TEXT, Type TEXT,NOS INTEGER)''')
cursor.execute(''' CREATE TABLE Winner(id INTEGER PRIMARY KEY,name TEXT,Event TEXT,Date INTEGER unique,Stand TEXT unique)''')
db.commit()
while 1:
    msg = "               Main Page"
    title = "Programming Club"
    choices=['Club Member Details','Events','Winners','Report','Exit']
    choice=choicebox(msg, title, choices)

    if choice=='Club Member Details':
        while 1:
            msg = "               Menu"
            title = "Member Details"
            choices1=['Add member','Update Details','Display','Search Member','Remove Member','Go to Main Menu']
            choice1=buttonbox(msg, title, choices1)
            if choice1=='Add member':
                def enbox():
                        msg= "Enter the Member details"
                        title = "Members Details"
                        fieldNames = ["Name","Phone","E-Mail ID","Department","Year"]
                        users = []
                        users = multenterbox(msg,title, fieldNames)
                        cursor.execute(''' INSERT INTO Member(name,phone,email,Dept,Year) VALUES(?,?,?,?,?)''',users)
                        db.commit()
                        print ("You Provided:", users)
                ynmsg=" Do you want to add another Member? "
                title="Add One More"
                while True:
                          enbox()
                          if not ynbox(ynmsg,title):
                                break
            elif choice1=='Remove Member':
                delname=enterbox("Enter the member name to be removed")
                cursor.execute('''DELETE FROM Member WHERE name=?''',(delname,))
                msgbox("The Member is removed")

            elif choice1=='Update Details':
                msg= "What do you want to update ?"
                title= "Update details"
                choices=['Phone','e-mail','Department','Year']
                choice2=buttonbox(msg,title,choices)
                if choice2=='Phone':
                    name=enterbox("Enter the Name :")
                    phone=enterbox("Enter the Number :")
                    cursor.execute('''UPDATE Member SET phone = ? WHERE name=?''',(phone,name,))
                    msgbox("The updated number is {}".format(phone))
                    print("You Provided",phone)
                elif choice2=='e-mail':
                    name=enterbox("Enter the Name :")
                    email=enterbox("Enter the mail id :")
                    cursor.execute('''UPDATE Member SET email = ? WHERE name=?''',(email,name))
                    msgbox("The updated mail id is {}".format(email))
                    print("You Provided",email)
                elif choice2=='Department':
                    name=enterbox("Enter the Name :")
                    dept=enterbox("Enter the Department :")
                    cursor.execute('''UPDATE Member SET Dept = ? WHERE name=?''',(dept,name))
                    msgbox("The updated number is {}".format(dept))
                    print("You Provided",dept)
                elif choice2=='Year':
                    name=enterbox("Enter the Name :")
                    yr=enterbox("Enter the Year :")
                    cursor.execute('''UPDATE Member SET Year = ? WHERE name=?''',(yr,name))
                    msgbox("The updated number is {}".format(yr))
                    print("You Provided",yr)
          
            elif choice1=='Search Member':
               name=enterbox("Enter the Name :")
               cursor.execute('''SELECT name,phone,email,Dept,Year FROM Member WHERE name=?''',(name,))
               us= cursor.fetchone()
               msgbox("The Member details are {}".format(us))

                
            elif choice1=='Display':
               cursor.execute('''SELECT * FROM Member''')
               us= cursor.fetchall()
               msgbox("The Member details are {}".format(us))
               
            elif choice1=='Go to Main Menu':
                break

    elif choice=='Winners':
        while 1:
            msg = "               Menu"
            title = "Winner Details"
            choices1=['Add Winner','Display','Update Details','Search Winner','Remove Details','Go to Main Menu']
            choice1=buttonbox(msg, title, choices1)
            if choice1=='Add Winner':
                    def enbox():
                            msg= "Enter the Winner details"
                            title = "Winner Details"
                            fieldNames = ["Name","Event","Date","Standing"]
                            users = []
                            users = multenterbox(msg,title, fieldNames)
                            cursor.execute(''' INSERT INTO Winner(name,Event,Date,Stand) VALUES(?,?,?,?)''',users)
                            db.commit()
                            print ("You Provided:", users)
                    ynmsg=" Do you want to add another? "
                    title="Add One More"
                    while True:
                              enbox()
                              if not ynbox(ynmsg,title):
                                    break
            elif choice1=='Remove Details':
                    delname=enterbox("Enter the winner name to be removed")
                    cursor.execute('''DELETE FROM Winner WHERE name=?''',(delname,))
                    msgbox("The Winner is removed")

            elif choice1=='Update Details':
                    msg= "What do you want to update ?"
                    title= "Update details"
                    choices=['Event','Date','Standing']
                    choice2=buttonbox(msg,title,choices)
                    if choice2=='Event':
                        name=enterbox("Enter the Name :")
                        phone=enterbox("Enter the Event name :")
                        cursor.execute('''UPDATE Winner SET Event = ? WHERE name = ?''',(phone,name))
                        msgbox("The updated number is {}".format(phone))
                        print("You Provided",phone)
                    elif choice2=='Date':
                        name=enterbox("Enter the Name :")
                        email=enterbox("Enter the Date :")
                        cursor.execute('''UPDATE Winner SET Date = ? WHERE name = ?''',(email,name))
                        msgbox("The updated mail id is {}".format(email))
                        print("You Provided",email)
                    elif choice2=='Standing':
                        name=enterbox("Enter the Name :")
                        dept=enterbox("Enter the Standing :")
                        cursor.execute('''UPDATE Winner SET Stand = ? WHERE name = ?''',(dept,name))
                        msgbox("The updated number is {}".format(dept))
                        print("You Provided",dept)
              
            elif choice1=='Search Winner':
                   name=enterbox("Enter the Name :")
                   cursor.execute('''SELECT name,Event,Date,Stand FROM Winner WHERE name=?''',(name,))
                   us= cursor.fetchone()
                   msgbox("The Winner details are {}".format(us))

            elif choice1=='Display':
                   cursor.execute('''SELECT * FROM Winner''')
                   us= cursor.fetchall()
                   msgbox("The Winner details are {}".format(us))
                   
                   
            elif choice1=='Go to Main Menu':
                    break

    elif choice=='Events':
         while 1:
            msg = "               Menu"
            title = "Event"
            choice3=['Contests','Workshops,etc','Go to Main Menu']
            choice4=buttonbox(msg, title, choice3)
            if choice4=='Contests':
                while 1:
                        msg = "               Menu"
                        title = "Contest details"
                        choices1=['Add Contest','Display','Update Details','Search Contest','Remove Details','Back']
                        choice1=buttonbox(msg, title, choices1)
                        if choice1=='Add Contest':
                                def enbox():
                                        msg= "Enter the Contest details"
                                        title = "Contest Details"
                                        fieldNames = ["Name","Date","Co-ordinator","Type","No. of Students Partcipated"]
                                        users = []
                                        users = multenterbox(msg,title, fieldNames)
                                        cursor.execute(''' INSERT INTO Events(name,Date,Coname,Type,NOS) VALUES(?,?,?,?,?)''',users)
                                        db.commit()
                                        print ("You Provided:", users)
                                ynmsg=" Do you want to add another? "
                                title="Add One More"
                                while True:
                                          enbox()
                                          if not ynbox(ynmsg,title):
                                                break
                        elif choice1=='Remove Details':
                                delname=enterbox("Enter the Event name to be removed")
                                cursor.execute('''DELETE FROM Events WHERE name=?''',(delname,))
                                msgbox("The Contest is removed")

                        elif choice1=='Update Details':
                                msg= "What do you want to update ?"
                                title= "Update details"
                                choices=['Co-ordinator','Date','NO. of Students Participated','Type']
                                choice2=buttonbox(msg,title,choices)
                                if choice2=='Co-ordinator':
                                    name=enterbox("Enter the Name :")
                                    phone=enterbox("Enter the Event name :")
                                    cursor.execute('''UPDATE Events SET Coname = ? WHERE name = ?''',(phone,name))
                                    msgbox("The updated Details is {}".format(phone))
                                    print("You Provided",phone)
                                elif choice2=='Date':
                                    name=enterbox("Enter the Name :")
                                    email=enterbox("Enter the Date :")
                                    cursor.execute('''UPDATE Events SET Date = ? WHERE name = ?''',(email,name))
                                    msgbox("The updated Details is {}".format(email))
                                    print("You Provided",email)
                                elif choice2=='NO. of Students Participated':
                                    name=enterbox("Enter the Name :")
                                    dept=enterbox("Enter the Standing :")
                                    cursor.execute('''UPDATE Events SET NOS = ? WHERE name = ?''',(dept,name))
                                    msgbox("The updated Details is {}".format(dept))
                                    print("You Provided",dept)
                                elif choice2=='Type':
                                    name=enterbox("Enter the Name :")
                                    dept=enterbox("Enter the Type :")
                                    cursor.execute('''UPDATE Events SET Type= ? WHERE name = ?''',(dept,name))
                                    msgbox("The updated Details is {}".format(dept))
                                    print("You Provided",dept)
                          
                        elif choice1=='Search Contest':
                               name=enterbox("Enter the Name :")
                               cursor.execute('''SELECT name,Date,Coname,Type,NOS FROM Events WHERE name=?''',(name,))
                               us= cursor.fetchone()
                               msgbox("The Event Details are {}".format(us))

                        elif choice1=='Display':
                           cursor.execute('''SELECT * FROM Events''')
                           us= cursor.fetchall()
                           msgbox("The Event details are {}".format(us))
                           
                               
                        elif choice1=='Back':
                                break

            elif choice4=='Workshops,etc':
                while 1:
                        msg = "               Menu"
                        title = "Workshops and Seminars"
                        choices1=['Add Event','Display','Update Details','Search Event','Remove Details','Back']
                        choice1=buttonbox(msg, title, choices1)
                        if choice1=='Add Event':
                                def enbox():
                                        msg= "Enter the Event details"
                                        title = "Event Details"
                                        fieldNames = ["Name","Date","Co-ordinator","Type","No. of Students Partcipated"]
                                        users = []
                                        users = multenterbox(msg,title, fieldNames)
                                        cursor.execute(''' INSERT INTO Events(name,Coname,Date,Type,NOS) VALUES(?,?,?,?,?)''',users)
                                        db.commit()
                                        print ("You Provided:", users)
                                ynmsg=" Do you want to add another? "
                                title="Add One More"
                                while True:
                                          enbox()
                                          if not ynbox(ynmsg,title):
                                                break
                        elif choice1=='Remove Details':
                                delname=enterbox("Enter the Event name to be removed")
                                cursor.execute('''DELETE FROM Events WHERE name=?''',(delname,))
                                msgbox("The Event is removed")

                        elif choice1=='Update Details':
                                msg= "What do you want to update ?"
                                title= "Update details"
                                choices=['Co-ordinator','Date','NO. of Students Participated','Type']
                                choice2=buttonbox(msg,title,choices)
                                if choice2=='Co-ordinator':
                                    name=enterbox("Enter the Name :")
                                    phone=enterbox("Enter the Event name :")
                                    cursor.execute('''UPDATE Events SET Coname= ? WHERE name = ?''',(phone,name))
                                    msgbox("The updated Details is {}".format(phone))
                                    print("You Provided",phone)
                                elif choice2=='Date':
                                    name=enterbox("Enter the Name :")
                                    email=enterbox("Enter the Date :")
                                    cursor.execute('''UPDATE Events SET Date = ? WHERE name = ?''',(email,name))
                                    msgbox("The updated Details is {}".format(email))
                                    print("You Provided",email)
                                elif choice2=='NO. of Students Participated':
                                    name=enterbox("Enter the Name :")
                                    dept=enterbox("Enter the Standing :")
                                    cursor.execute('''UPDATE Events SET NOS = ? WHERE name = ?''',(dept,name))
                                    msgbox("The updated Details is {}".format(dept))
                                    print("You Provided",dept)
                                elif choice2=='Type':
                                    name=enterbox("Enter the Name :")
                                    dept=enterbox("Enter the Type :")
                                    cursor.execute('''UPDATE Events SET Type= ?, WHERE name = ?''',(dept,name))
                                    msgbox("The updated Details is {}".format(dept))
                                    print("You Provided",dept)
                          
                        elif choice1=='Search Event':
                               name=enterbox("Enter the Name :")
                               cursor.execute('''SELECT name,Date,Coname,Type,NOS FROM Events WHERE name=?''',(name,))
                               us= cursor.fetchone()
                               msgbox("The Event Details are {}".format(us))

                        elif choice1=='Display':
                           cursor.execute('''SELECT * FROM Events''')
                           us= cursor.fetchall()
                           msgbox("The Event details are {}".format(us))
                           
                               
                        elif choice1=='Back':
                                break
            elif choice4=='Go to Main Menu':
                        break

    elif choice=='Report':
        cursor.execute('''SELECT * FROM Member''')
        member=cursor.fetchall()
        n=len(member)
        msgbox("The number of Club Members {}".format(n))
        cursor.execute('''SELECT * FROM Winner''')
        winer=cursor.fetchall()
        m=len(winer)
        msgbox("The number of Events {}".format(m)) 
        cursor.execute('''SELECT * FROM Events''')
        event=cursor.fetchall()
        o=len(event)
        msgbox("The number of Winner {}".format(o))

    elif choice=='Exit':
        exit(0)
        
                
             

