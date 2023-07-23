# COVID-Contact-Tracing-App

## Description

This Python project serves as a simple Contact Tracing App for COVID-19, where users can input information about their contacts (name, email, phone number, date of visit), COVID-19 status (vaccination and covid test), and contact of the person in case of emergency. The program writes the data collected in a file and provides a search feature to look up specific entries based on user-provided search terms. The project was separated into 3 files, namely Main_contact_tracing_app.py, Contact_tracing_app_GUI.py, and Contact_tracing_app.py.

The code executes the calculation in a GUI, which was made by employing the Tkinter library. 

## Files: Summary

- Main_contact_tracing_app.py
  > Starts the main event loop for the user interface, enabling its display and interaction with the user.

- Contact_tracing_app_GUI.py
  > Sets up the main window and handles user interactions and calls functions from ContactTracingApp.

- Contact_tracing_app.py
  > Contains the main logic (search and write).

## How To Use / Run 

1. Install Python on your computer to run the code. You can download its latest version here: https://www.python.org/downloads/
2. Make sure that you Tkinker and PIL installed.
3. Open an IDE and paste the code from the 3 separate files. Make sure that the files are separated into three, as seen in the repository.
4. Save the files with a .py extension.
5. Run the Main_contact_tracing_app.py.
6. A Graphical User Interface will appears with input fields for users to enter contact details and COVID-19-related information.
7. Fill in the necessary fields
8. Click the "Add Entry" button once one with filling out the form to save the data.
9. You can search for your added entries by typing keywords on the search field.

## Customization

- You change fonts, add colors, resize the code.
- You can add background using PIL with this code
  

        background = Image.open("File Directory/File Name")
        self.background_image = ImageTk.PhotoImage(background)

## Demo

You can access my demo through this link:

https://drive.google.com/file/d/1vSg5dFQhhNHCYKJpcotKeTtvcFtaZ_cO/view?usp=sharing

