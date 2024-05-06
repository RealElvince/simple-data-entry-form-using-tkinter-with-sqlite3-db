# import useful libraries
import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3


# Button Clicked Function
def submit_data():
    accept = accept_var.get()
    if accept == "Accepted":
        # Student Info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            age = age_spinbox.get()
            title = title_combo.get()
            nationality = nationality_combo.get()

            # Course Info
            num_courses = number_of_courses_spinbox.get()
            num_semester = number_of_semester_spinbox.get()
            reg_status = reg_status_var.get()

            # Database Connection sqlite3
            conn = sqlite3.connect("students.db")
            cur = conn.cursor()

            # Create table
            create_table_query = '''
             CREATE TABLE IF NOT EXISTS StudentsTable(
             Title VARCHAR ,
             First_Name VARCHAR,
             Last_Name VARCHAR ,
             Age INTEGER,
             Nationality VARCHAR,
             No_Courses INTEGER,
             No_Semesters INTEGER,
             Registration_status VARCHAR
             );
            '''
            cur.execute(create_table_query)

            # Insert data query
            data_insert_query = '''
              INSERT INTO StudentsTable(Title,First_Name,Last_Name,Age,Nationality,No_Courses,No_Semesters,Registration_status) VALUES(?,?,?,?,?,?,?,?)
            '''
            data_insert_tuple = (title, firstname, lastname, age, nationality, num_courses, num_semester, reg_status)
            cur.execute(data_insert_query,
                        data_insert_tuple)
            conn.commit()
            conn.close()
        else:
            tkinter.messagebox.showwarning(title="Error", message="First Name and last name are required!")

    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms and conditions.")


# create root app
window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# create user info frame
user_info_frame = tkinter.LabelFrame(frame, text="Student Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_label.grid(row=0, column=2)
title_combo = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_combo.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_label.grid(row=2, column=0)
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_label.grid(row=2, column=1)

nationality_combo = ttk.Combobox(user_info_frame, values=["", "Kenyan", "Tanzania", "Ugandan", "Ethiopian"])
nationality_combo.grid(row=3, column=1)
first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

# padding for children widgets in user_info_frame
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Create course frame
course_info_frame = tkinter.LabelFrame(frame, text="Course information")
course_info_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_label = tkinter.Label(course_info_frame, text="Registration Status")
registered_label.grid(row=0, column=0)
registration_check = tkinter.Checkbutton(course_info_frame, text="Currently Registered", variable=reg_status_var,
                                         onvalue="Registered", offvalue="Not Registered")
registration_check.grid(row=1, column=0)

number_of_courses = tkinter.Label(course_info_frame, text="# Completed Courses")
number_of_courses_spinbox = tkinter.Spinbox(course_info_frame, from_=0, to=100)
number_of_courses.grid(row=0, column=1)
number_of_courses_spinbox.grid(row=1, column=1)

number_of_semester = tkinter.Label(course_info_frame, text="# Semester")
number_of_semester_spinbox = tkinter.Spinbox(course_info_frame, from_=0, to=8)
number_of_semester.grid(row=0, column=2)
number_of_semester_spinbox.grid(row=1, column=2)

# padding for children widgets in course_info_frame
for widget in course_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# terms and condition frame
terms_frame = tkinter.LabelFrame(frame, text="Terms & Condition")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_condition_check = tkinter.Checkbutton(terms_frame, text="I accept the Terms and Condition.", variable=accept_var,
                                            onvalue="Accepted", offvalue="Not Accepted")
terms_condition_check.grid(row=0, column=0)

# Submit data button

button = tkinter.Button(frame, text="Submit Data", command=submit_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
