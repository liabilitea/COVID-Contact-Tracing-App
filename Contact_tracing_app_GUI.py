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
        root.geometry("700x400")
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
        self.entry_phone = tk.Entry(root, width = 60)
        self.entry_phone.grid(row = 1, column = 1, padx = 5, pady = 5, columnspan = 4, sticky = tk.W)

        self.label_email = tk.Label(root, text = "Email:")
        self.label_email.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.entry_email = tk.Entry(root, width = 60)
        self.entry_email.grid(row = 2, column = 1, padx = 5, pady = 5, columnspan = 4, sticky = tk.W)
    
        self.label_date = tk.Label(root, text = "Date (YYYY-MM-DD):")
        self.label_date.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.entry_date = tk.Entry(root, width = 60)
        self.entry_date.grid(row = 3, column = 1, padx = 5, pady = 5, columnspan = 4, sticky = tk.W)

        self.label_vaccination = tk.Label(root, text="Vaccination Status:", bg="#FFADAD", fg="black")
        self.label_vaccination.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.var_vaccination_status = tk.StringVar()
        vaccination_options = ["Not Yet", "1st Dose", "Fully Vaccinated", "Boosted"]
        # Create radiobuttons for each option
        for i, option in enumerate(vaccination_options):
            rb_vaccine = tk.Radiobutton(root, text = option, variable = self.var_vaccination_status, value = option)
            rb_vaccine.grid(row = 4, column = i+1, padx = 2, pady = 2)
            
        
        self.label_tested_covid = tk.Label(root, text="Have you been tested for Covid-19 in the last 14 days?", bg="#FFADAD", fg="black")
        self.label_tested_covid.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.var_tested_covid = tk.StringVar()
        test_options = ["No", "Yes-Positive", "Yes-Negative", "Yes-Pending"]
        # Create radiobuttons for each option
        for i, option in enumerate(test_options):
            rb_test = tk.Radiobutton(root, text = option, variable = self.var_tested_covid, value = option)
            rb_test.grid(row = 5, column = i+1, padx = 2, pady = 2)   
    
        self.label_contact_person_name = tk.Label(root, text="Contact Person Name:")
        self.label_contact_person_name.grid(row = 6, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.entry_contact_person_name = tk.Entry(root, width = 60)
        self.entry_contact_person_name.grid(row = 6, column = 1, padx = 5, pady = 5, columnspan = 4, sticky = tk.W)

        self.label_contact_person_phone = tk.Label(root, text="Contact Person Phone Number:")
        self.label_contact_person_phone.grid(row=7, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.entry_contact_person_phone = tk.Entry(root, width = 60)
        self.entry_contact_person_phone.grid(row=7, column = 1, padx = 5, pady = 5, columnspan = 4, sticky = tk.W)

    # Buttons for search add and checklist
        
        self.add_entry_button = tk.Button(root, text = "Add Entry")
        self.add_entry_button.grid(row = 8, column = 0, padx = 5, pady = 5, columnspan = 5, sticky = tk.W+tk.E)

        self.label_search_entry = tk.Label(root, text = "Search Entry:")
        self.label_search_entry.grid(row = 9, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.entry_search = tk.Entry(root, width=40)
        self.entry_search.grid(row = 9, column = 1, padx = 5, pady = 5, columnspan = 4, sticky = tk.W+tk.E)
    
        self.search_entry_button = tk.Button(root, text = "Search")
        self.search_entry_button.grid(row = 10, column = 0, padx = 5, pady = 5, columnspan = 5, sticky = tk.W+tk.E)

# Function to retrieve data from gui
    def add_entry_gui(self):
        name = self. entry_name.get()
        phone = self. entry_phone.get()
        email = self. entry_email.get()
        date = self. entry_date.get()
        vaccination_status = self. entry_.get()
        covid_test = self. entry_.get()
        contact_person_name = self. entry_contact_person_name.get()
        contact_person_number = self. entry_contact_person_phone.get()
    
# Function to retrieve key term from gui

if __name__ == "__main__":
    root = tk.Tk()  
    app_gui = ContactTracingAppGUI(root)
    root.mainloop()
