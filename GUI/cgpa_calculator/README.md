# Academic Performance Tracker

## Overview

The Academic Performance Tracker is a Python GUI application built using `customTkinter`. It helps students manage and track their academic performance across multiple semesters. The application allows students to enter and view their course registrations, calculate their Grade Point Average (GPA) and Cumulative Grade Point Average (CGPA), and save this data to a SQLite database. Additionally, users can export their data to PDF or CSV formats.

## Features

- **Semester-wise Course Registration:**
  - The GUI displays a rectangular box divided into two sections representing the first and second semesters.
  - Students can select the number of registered courses for each semester from a dropdown menu.

- **Course Management:**
  - The application maintains a list of all available courses (course codes) from 100 level to 500 level along with their respective credit units.

- **Course Details Entry:**
  - For each semester, students can input details for each course, including:
    - Serial Number (S/N)
    - Course Code
    - Credit Unit
    - Grade
    - Weighted Grade Point

- **Performance Calculation:**
  - The application calculates and displays:
    - Total Grade Points (TGP)
    - Total Credit Units (TCU)
    - GPA for each semester
    - CGPA across both semesters

- **Data Storage and Management:**
  - Save data to a SQLite database.
  - Load previously saved data upon launching the app.
  - Option to enter data for new academic sessions, appending it to the existing records.

- **Data Visualization:**
  - View saved data in a scrollable format.
  - Option to export data to PDF or CSV files.

## How It Works

1. **Initial Setup:**
   - Upon launching the application, the user selects the number of courses registered for the first and second semesters from a dropdown menu.

2. **Data Entry:**
   - The user fills in the course details for each registered course for both semesters. The GUI dynamically adjusts to display the required number of rows for course input.

3. **Calculations:**
   - The application computes TGP, TCU, GPA for each semester, and CGPA across both semesters based on the input data.

4. **Data Saving and Loading:**
   - The user can save their data to a SQLite database. On subsequent launches, the app loads and displays previously saved data.
   - The user can also enter data for new academic sessions.

5. **Data Export:**
   - The application provides options to export the displayed data to PDF or CSV files.

6. **Navigation:**
   - The GUI includes navigation features to view and manage saved data, with options to scroll through and export data.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/judedotdev/python.git
   cd python/GUI/cgpa_calculator
   python main.py
   ```
