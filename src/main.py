import os
import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk
import sqlite3
from datetime import date


bg_color = "#DE3163"
burgundy = "#800020"
pastel_red = "#FAA0A0"
todays_date = date.today()


#change dir to the database's location
os.chdir(r"C:\Users\tugra\OneDrive\Desktop\fun\valentines-data\data")
#create database
connection = sqlite3.connect("valentine_tracker.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS dates (year integer, date text)")


#get data from db
def fetch_db():
    cursor.execute("SELECT * FROM dates")
    table_records = cursor.fetchall()
    return table_records

#clean the data from db
def pre_process():
    table_records = fetch_db()
    
    dates = []
    for i in table_records:
        year = i[0]
        valentine = i[1]
        dates.append(str(year) + " ----> " + valentine)
    
    return dates


def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    #stops from children from changing  frame1
    frame1.pack_propagate(False)

    logo_img = ImageTk.PhotoImage(file=r"C:\Users\tugra\OneDrive\Desktop\fun\valentines-data\assets\white_heart.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    #the question
    tk.Label(
        frame1,
        text="Do you have a date for Valentine's Day this year?",
        bg=bg_color,
        fg="white",
        font=("Comic Sans", 14),
        ).pack(side="top")
    
    
    button = ctk.CTkButton(
        master=frame1,
        width=250,
        height=60,
        border_width=0,
        corner_radius=7,
        fg_color=burgundy,
        hover_color=pastel_red,
        border_color="black",
        text="Yes",
        font=('Comic Sans', 30),
        command=lambda:button_yes()
        )
    button.pack(pady=20)

    button = ctk.CTkButton(
        master=frame1,
        width=250,
        height=60,
        border_width=0,
        corner_radius=7,
        fg_color=burgundy,
        hover_color=pastel_red,
        border_color="black",
        text="No",
        font=('Comic Sans', 30),
        command=lambda:button_no()
        )
    button.pack(pady=20)

    button = ctk.CTkButton(
        master=frame1,
        width=250,
        height=60,
        border_width=0,
        corner_radius=7,
        fg_color=burgundy,
        hover_color=pastel_red,
        border_color="black",
        text="Previous Years",
        font=('Comic Sans', 30),
        command=lambda:load_frame2()
        )
    button.pack(pady=20)


def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()

    logo_img = ImageTk.PhotoImage(file=r"C:\Users\tugra\OneDrive\Desktop\fun\valentines-data\assets\white_heart_horizontal.png")
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    #title
    tk.Label(
        frame2,
        text="Dating Records for Valentine's Day in the Past Years",
        bg=bg_color,
        fg="white",
        font=("TkHeadingFont", 20),
        ).pack()


    dates = pre_process()

    for i in dates:
        tk.Label(
            frame2,
            text=i,
            bg=burgundy,
            fg="white",
            font=("TkMenuFont", 12),
            ).pack(fill="both", padx=630)


    button = ctk.CTkButton(
        master=frame2,
        width=250,
        height=60,
        border_width=0,
        corner_radius=7,
        fg_color=burgundy,
        hover_color=pastel_red,
        border_color="black",
        text="Back",
        font=('Comic Sans', 30),
        command=lambda:load_frame1()
        )
    button.pack(pady=20)


def button_yes():
    cursor.execute("INSERT INTO dates Values (?,?)",(todays_date.year, "Got a date") )
    connection.commit()
    
    close()


def button_no():
    cursor.execute("INSERT INTO dates Values (?,?)",(todays_date.year, "Loner") )
    connection.commit()
    
    close()


def close():
   root.destroy()

def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    
# initialize the app
root = tk.Tk()
root.title("Valentine's Date Tracker")
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=1920, height=1080, bg=bg_color)
frame2 = tk.Frame(root, bg=bg_color)

for frame in(frame1, frame2):
    frame.grid(row=0, column=0, sticky="nesw")

def main():
    load_frame1()

if __name__ == '__main__':
    main()


root.mainloop( )