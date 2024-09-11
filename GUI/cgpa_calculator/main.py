import customtkinter as ctk
import sqlite3
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
from fpdf import FPDF

# Initialize the main window
app = ctk.CTk()
app.title("CGPA Calculator")
app.geometry("1280x720")


# Database setup
def create_database():
    """Create the SQLite database and a table to store student results"""
    conn = sqlite3.connect("cgpa_calculator.db")
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session TEXT,
            level INTEGER,
            semester INTEGER,
            course_code TEXT,
            credit_unit INTEGER,
            grade TEXT,
            weighted_grade_point REAL
        )
    """
    )
    conn.commit()
    conn.close()


create_database()

# List of courses and their credit units
courses = {
    "MTH101": 4,
    "PHY101": 4,
    "CHM101": 4,
    "BIO101": 3,
    "ENG101": 2,
    "ENG103": 1,
    "GST101": 2,
    "GST103": 1,
    "FRN101": 1,
    "IGB101": 1,
    "MTH102": 4,
    "PHY102": 4,
    "CHM102": 4,
    "ENG102": 2,
    "ENG104": 1,
    "GST102": 2,
    "GST108": 1,
    "GST110": 1,
    "FRN102": 1,
    # Add all other courses here
}


# Function to calculate the weighted grade point for a course
def calculate_weighted_grade_point(grade, credit_unit):
    """Calculate the weighted grade point based on the grade and credit unit"""
    grade_point = 0
    if grade == "A":
        grade_point = 5
    elif grade == "B":
        grade_point = 4
    elif grade == "C":
        grade_point = 3
    elif grade == "D":
        grade_point = 2
    elif grade == "E":
        grade_point = 1
    elif grade == "F":
        grade_point = 0
    return grade_point * credit_unit


# Create the top frame with vertical buttons
top_frame = ctk.CTkFrame(app)
top_frame.pack(padx=20, pady=10, fill="x")

# Create frame2 below the top frame
frame2 = ctk.CTkFrame(app)
frame2.pack(padx=20, pady=10, fill="both", expand=True)

# Dropdown for selecting number of courses inside frame2
num_courses_sem1 = ctk.StringVar(frame2, value="Select Number of Courses")
num_courses_sem2 = ctk.StringVar(frame2, value="Select Number of Courses")

# Create Frames to hold the semester information inside frame2
frame_sem1 = ctk.CTkFrame(frame2)
frame_sem1.pack(side="left", padx=10, pady=10, expand=True, fill="both")

frame_sem2 = ctk.CTkFrame(frame2)
frame_sem2.pack(side="right", padx=10, pady=10, expand=True, fill="both")

# Labels for the semesters
ctk.CTkLabel(frame_sem1, text="First Semester").pack()
ctk.CTkLabel(frame_sem2, text="Second Semester").pack()


# Function to generate course fields dynamically
def generate_course_fields(num_courses, frame, semester):
    """Generate fields for entering course details dynamically based on the number of courses selected"""
    # Clear the frame first
    for widget in frame.winfo_children():
        widget.destroy()

    # Headers for the course fields
    headers = ["S/N", "Course Code", "Credit Unit", "Grade", "Weighted Grade Point"]
    for i, header in enumerate(headers):
        ctk.CTkLabel(frame, text=header).grid(row=0, column=i, padx=10, pady=5)

    # Store widget references
    widgets = []

    # Generate fields based on the number of courses selected
    for i in range(int(num_courses)):
        ctk.CTkLabel(frame, text=f"{i + 1}").grid(row=i + 1, column=0, padx=10, pady=5)
        course_code = ctk.CTkComboBox(frame, values=list(courses.keys()))
        course_code.grid(row=i + 1, column=1, padx=10, pady=5)
        credit_unit = ctk.CTkEntry(frame)
        credit_unit.grid(row=i + 1, column=2, padx=10, pady=5)
        grade = ctk.CTkEntry(frame)
        grade.grid(row=i + 1, column=3, padx=10, pady=5)
        weighted_grade_point = ctk.CTkLabel(frame, text="0")
        weighted_grade_point.grid(row=i + 1, column=4, padx=10, pady=5)

        # Store references in the list
        widgets.append(
            {
                "course_code": course_code,
                "credit_unit": credit_unit,
                "grade": grade,
                "weighted_grade_point": weighted_grade_point,
            }
        )

    # Define the update_weighted_gp function
    def update_weighted_gp(*args):
        for widget_set in widgets:
            try:
                credit_unit = int(widget_set["credit_unit"].get())
                grade = widget_set["grade"].get().upper()
                weighted_gp = calculate_weighted_grade_point(grade, credit_unit)
                widget_set["weighted_grade_point"].configure(text=str(weighted_gp))
            except ValueError:
                widget_set["weighted_grade_point"].configure(text="0")

    # Bind the update_weighted_gp function to the grade and credit_unit entries
    for widget_set in widgets:
        widget_set["credit_unit"].bind("<KeyRelease>", update_weighted_gp)
        widget_set["grade"].bind("<KeyRelease>", update_weighted_gp)

    # Calculation summary below the course entries
    tgp_label = ctk.CTkLabel(frame, text="Total Grade Points (TGP) = 0")
    tgp_label.grid(row=int(num_courses) + 1, column=0, columnspan=2, padx=10, pady=5)

    tcu_label = ctk.CTkLabel(frame, text="Total Credit Units (TCU) = 0")
    tcu_label.grid(row=int(num_courses) + 1, column=2, columnspan=2, padx=10, pady=5)

    gpa_label = ctk.CTkLabel(frame, text="GPA = TGP/TCU = 0.00")
    gpa_label.grid(row=int(num_courses) + 2, column=0, columnspan=5, padx=10, pady=5)

    # Save the summary labels for later updating
    if semester == 1:
        global sem1_labels
        sem1_labels = {"tgp": tgp_label, "tcu": tcu_label, "gpa": gpa_label}
    elif semester == 2:
        global sem2_labels
        sem2_labels = {"tgp": tgp_label, "tcu": tcu_label, "gpa": gpa_label}


# Dropdowns to select the number of courses
ctk.CTkComboBox(
    frame_sem1,
    values=[str(i) for i in range(1, 11)],
    variable=num_courses_sem1,
    command=lambda x: generate_course_fields(num_courses_sem1.get(), frame_sem1, 1),
    width=192,
).pack(pady=10)
ctk.CTkComboBox(
    frame_sem2,
    values=[str(i) for i in range(1, 11)],
    variable=num_courses_sem2,
    command=lambda x: generate_course_fields(num_courses_sem2.get(), frame_sem2, 2),
    width=192,
).pack(pady=10)


# Functions to calculate and display GPA and CGPA
def calculate_gpa(semester, frame, labels):
    """Calculate GPA for a given semester based on the entries in the fields"""
    tgp = 0
    tcu = 0
    for i in range(1, int(num_courses_sem1.get()) + 1):
        credit_unit = int(frame.grid_slaves(row=i, column=2)[0].get())
        weighted_gp = float(frame.grid_slaves(row=i, column=4)[0].cget("text"))
        tgp += weighted_gp
        tcu += credit_unit

    gpa = round(tgp / tcu, 2) if tcu != 0 else 0
    labels["tgp"].configure(text=f"Total Grade Points (TGP) = {tgp}")
    labels["tcu"].configure(text=f"Total Credit Units (TCU) = {tcu}")
    labels["gpa"].configure(text=f"GPA = TGP/TCU = {gpa}")
    return tgp, tcu, gpa


def calculate_cgpa():
    """Calculate CGPA based on the GPAs of the two semesters"""
    tgp1, tcu1, gpa1 = calculate_gpa(1, frame_sem1, sem1_labels)
    tgp2, tcu2, gpa2 = calculate_gpa(2, frame_sem2, sem2_labels)

    total_tgp = tgp1 + tgp2
    total_tcu = tcu1 + tcu2
    cgpa = round(total_tgp / total_tcu, 2) if total_tcu != 0 else 0

    ctk.CTkLabel(
        app,
        text=f"CGPA = (Total TGP1 + Total TGP2) / (Total TCU1 + Total TCU2) = {cgpa}",
    ).pack(pady=20)


# # Calculate CGPA button
# calculate_button = ctk.CTkButton(
#     top_frame, text="Calculate CGPA", command=calculate_cgpa
# )
# calculate_button.pack(pady=10)


# Function to save data to SQLite database
def save_to_database():
    """Save the current GPA, TGP, TCU, and CGPA data to the SQLite database"""
    conn = sqlite3.connect("cgpa_calculator.db")
    c = conn.cursor()

    # Save data for the first semester
    for i in range(1, int(num_courses_sem1.get()) + 1):
        course_code = frame_sem1.grid_slaves(row=i, column=1)[0].get()
        credit_unit = int(frame_sem1.grid_slaves(row=i, column=2)[0].get())
        grade = frame_sem1.grid_slaves(row=i, column=3)[0].get().upper()
        weighted_gp = float(frame_sem1.grid_slaves(row=i, column=4)[0].cget("text"))

        c.execute(
            """
            INSERT INTO results (session, level, semester, course_code, credit_unit, grade, weighted_grade_point)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            ("2023/2024", 100, 1, course_code, credit_unit, grade, weighted_gp),
        )

    # Save data for the second semester
    for i in range(1, int(num_courses_sem2.get()) + 1):
        course_code = frame_sem2.grid_slaves(row=i, column=1)[0].get()
        credit_unit = int(frame_sem2.grid_slaves(row=i, column=2)[0].get())
        grade = frame_sem2.grid_slaves(row=i, column=3)[0].get().upper()
        weighted_gp = float(frame_sem2.grid_slaves(row=i, column=4)[0].cget("text"))

        c.execute(
            """
            INSERT INTO results (session, level, semester, course_code, credit_unit, grade, weighted_grade_point)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            ("2023/2024", 100, 2, course_code, credit_unit, grade, weighted_gp),
        )

    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Data saved to the database successfully!")


# # Button to save data
# save_button = ctk.CTkButton(top_frame, text="Save Data", command=save_to_database)
# save_button.pack(pady=10)


# Function to load the last session's data from the database
def load_data():
    """Load the last session's data from the SQLite database and display it in the fields"""
    conn = sqlite3.connect("cgpa_calculator.db")
    c = conn.cursor()

    # Load data for first semester
    c.execute(
        """
        SELECT course_code, credit_unit, grade, weighted_grade_point FROM results
        WHERE session='2023/2024' AND level=100 AND semester=1
    """
    )
    data_sem1 = c.fetchall()

    generate_course_fields(len(data_sem1), frame_sem1, 1)

    for i, (course_code, credit_unit, grade, weighted_gp) in enumerate(
        data_sem1, start=1
    ):
        frame_sem1.grid_slaves(row=i, column=1)[0].set(course_code)
        frame_sem1.grid_slaves(row=i, column=2)[0].insert(0, credit_unit)
        frame_sem1.grid_slaves(row=i, column=3)[0].insert(0, grade)
        frame_sem1.grid_slaves(row=i, column=4)[0].configure(text=str(weighted_gp))

    # Load data for second semester
    c.execute(
        """
        SELECT course_code, credit_unit, grade, weighted_grade_point FROM results
        WHERE session='2023/2024' AND level=100 AND semester=2
    """
    )
    data_sem2 = c.fetchall()

    generate_course_fields(len(data_sem2), frame_sem2, 2)

    for i, (course_code, credit_unit, grade, weighted_gp) in enumerate(
        data_sem2, start=1
    ):
        frame_sem2.grid_slaves(row=i, column=1)[0].set(course_code)
        frame_sem2.grid_slaves(row=i, column=2)[0].insert(0, credit_unit)
        frame_sem2.grid_slaves(row=i, column=3)[0].insert(0, grade)
        frame_sem2.grid_slaves(row=i, column=4)[0].configure(text=str(weighted_gp))

    conn.close()


# # Load last session data button
# load_button = ctk.CTkButton(top_frame, text="Load Last Session", command=load_data)
# load_button.pack(pady=10)


# Function to navigate to the page to view and export saved data
def view_saved_data():
    """Navigate to the page where we can view and export the saved data"""
    view_window = ctk.CTkToplevel(app)
    view_window.title("View Saved Data")
    view_window.geometry("600x600")

    conn = sqlite3.connect("cgpa_calculator.db")
    c = conn.cursor()

    c.execute("SELECT * FROM results")
    data = c.fetchall()

    conn.close()

    # Display data in a scrollable text box
    text_box = ctk.CTkTextbox(view_window, width=580, height=350)
    text_box.pack(pady=10)

    for row in data:
        text_box.insert("end", f"{row}\n")

    # Function to export data as CSV or PDF
    def export_data(file_type):
        """Export the displayed data as CSV or PDF"""
        if file_type == "CSV":
            file_path = filedialog.asksaveasfilename(
                defaultextension=".csv", filetypes=[("CSV files", "*.csv")]
            )
            if file_path:
                df = pd.DataFrame(
                    data,
                    columns=[
                        "ID",
                        "Session",
                        "Level",
                        "Semester",
                        "Course Code",
                        "Credit Unit",
                        "Grade",
                        "Weighted Grade Point",
                    ],
                )
                df.to_csv(file_path, index=False)
                messagebox.showinfo("Success", "Data exported as CSV successfully!")

        elif file_type == "PDF":
            file_path = filedialog.asksaveasfilename(
                defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")]
            )
            if file_path:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)

                # Writing header
                for column in [
                    "ID",
                    "Session",
                    "Level",
                    "Semester",
                    "Course Code",
                    "Credit Unit",
                    "Grade",
                    "Weighted Grade Point",
                ]:
                    pdf.cell(30, 10, column, 1)
                pdf.ln()

                # Writing data rows
                for row in data:
                    for item in row:
                        pdf.cell(30, 10, str(item), 1)
                    pdf.ln()

                pdf.output(file_path)
                messagebox.showinfo("Success", "Data exported as PDF successfully!")

    # Buttons to export data
    export_csv_button = ctk.CTkButton(
        view_window, text="Export as CSV", command=lambda: export_data("CSV")
    )
    export_csv_button.pack(side="left", padx=10, pady=10)

    export_pdf_button = ctk.CTkButton(
        view_window, text="Export as PDF", command=lambda: export_data("PDF")
    )
    export_pdf_button.pack(side="right", padx=10, pady=10)


# Create 4 buttons and place them in a horizontal grid within the top frame
buttons = ["Calculate CGPA", "Save Data", "Load Last Session", "View Saved Data"]
commands = [calculate_cgpa, save_to_database, load_data, view_saved_data]
for i, text in enumerate(buttons):
    button = ctk.CTkButton(top_frame, text=text, command=commands[i])
    button.grid(row=0, column=i, padx=80, pady=10)

# Run the main loop
app.mainloop()
