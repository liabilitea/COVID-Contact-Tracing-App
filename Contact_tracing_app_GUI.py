# Import
    # tk
import tkinter as tk
from tkinter import messagebox
    # contact tracing app
from Contact_tracing_app import ContactTracingApp

# Create class

class ContactTracingAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID Contact Tracing App")
        root.geometry("700x500")
        self.root.resizable(False, False)
        self.app = ContactTracingApp()

# Set elements per info
    # Info
        self.label_name = tk.Label(root, text = "Name:")
        self.label_name.grid(row = 0, column = 0, padx = 5, pady = 5, sticky=tk.W)
        self.entry_name = tk.Entry(root, width = 60)
        self.entry_name.grid(row = 0, column = 1, padx = 5, pady = 5, columnspan = 4, sticky = tk.W)

        self.label_phone = tk.Label(root, text = "Phone Number:")
        self.label_phone.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.entry_phone = tk.Entry(root, width=60)
        self.entry_phone.grid(row = 1, column = 1, padx = 5, pady = 5, columnspan = 4, sticky = tk.W)

        self.label_email = tk.Label(root, text = "Email:")
        self.label_email.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.entry_email = tk.Entry(root, width=60)
        self.entry_email.grid(row = 2, column = 1, padx = 5, pady = 5, columnspan = 4, sticky = tk.W)
    
        self.label_date = tk.Label(root, text = "Date (YYYY-MM-DD):")
        self.label_date.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.entry_date = tk.Entry(root, width=60)
        self.entry_date.grid(row = 3, column = 1, padx = 5, pady = 5, columnspan = 4, sticky = tk.W)

        self.label_vaccination = tk.Label(root, text="Vaccination Status:", bg="#FFADAD", fg="black")
        self.label_vaccination.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
    
        self.label_tested_covid = tk.Label(root, text="Have you been tested for Covid-19 in the last 14 days?", bg="#FFADAD", fg="black")
        self.label_tested_covid.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
    
    
    # Buttons for search add and checklist

# Function to retrieve data from gui

# Function to retrieve key term from gui

if __name__ == "__main__":
    root = tk.Tk()  
    app_gui = ContactTracingAppGUI(root)
    root.mainloop()
