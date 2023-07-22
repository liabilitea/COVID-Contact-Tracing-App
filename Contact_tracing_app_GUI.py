# Import
    # TK
import tkinter as tk
from tkinter import messagebox
    # Contact Tracing App
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
        # Name
        self.label_name = tk.Label(root, text = "Name:")
        self.label_name.grid(row = 0, column = 0, padx = 5, pady = 5, sticky=tk.W)
        self.entry_name = tk.Entry(root, width = 60)
        self.entry_name.grid(row = 0, column = 1, padx = 5, pady = 5, columnspan = 4, sticky = tk.W)
        # Phone
        self.label_phone = tk.Label(root, text = "Phone Number:")
        self.label_phone.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.entry_phone = tk.Entry(root, width = 60)
        self.entry_phone.grid(row = 1, column = 1, padx = 5, pady = 5, columnspan = 4, sticky = tk.W)
        # Email
        self.label_email = tk.Label(root, text = "Email:")
        self.label_email.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.entry_email = tk.Entry(root, width = 60)
        self.entry_email.grid(row = 2, column = 1, padx = 5, pady = 5, columnspan = 4, sticky = tk.W)
        # Date
        self.label_date = tk.Label(root, text = "Date (YYYY-MM-DD):")
        self.label_date.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.entry_date = tk.Entry(root, width = 60)
        self.entry_date.grid(row = 3, column = 1, padx = 5, pady = 5, columnspan = 4, sticky = tk.W)
        # Vaccination Status
        self.label_vaccination = tk.Label(root, text="Vaccination Status:", bg="#FFADAD", fg="black")
        self.label_vaccination.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.var_vaccination_status = tk.StringVar()
        vaccination_options = ["Not Yet", "1st Dose", "Fully Vaccinated", "Boosted"]
        # Create radiobuttons for each option
        for i, option in enumerate(vaccination_options):
            rb_vaccine = tk.Radiobutton(root, text = option, variable = self.var_vaccination_status, value = option)
            rb_vaccine.grid(row = 4, column = i+1, padx = 2, pady = 2) 
        # COVID Test Status        
        self.label_covid_test = tk.Label(root, text="Have you been tested for Covid-19 in the last 14 days?", bg="#FFADAD", fg="black")
        self.label_covid_test.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.var_covid_test = tk.StringVar()
        test_options = ["No", "Yes-Positive", "Yes-Negative", "Yes-Pending"]
        # Create radiobuttons for each option
        for i, option in enumerate(test_options):
            rb_test = tk.Radiobutton(root, text = option, variable = self.var_covid_test, value = option)
            rb_test.grid(row = 5, column = i+1, padx = 2, pady = 2)   
        # Contact Person Name    
        self.label_contact_person_name = tk.Label(root, text="Contact Person Name:")
        self.label_contact_person_name.grid(row = 6, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.entry_contact_person_name = tk.Entry(root, width = 60)
        self.entry_contact_person_name.grid(row = 6, column = 1, padx = 5, pady = 5, columnspan = 4, sticky = tk.W)
        # Contact Person Phone  
        self.label_contact_person_phone = tk.Label(root, text="Contact Person Phone Number:")
        self.label_contact_person_phone.grid(row=7, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.entry_contact_person_phone = tk.Entry(root, width = 60)
        self.entry_contact_person_phone.grid(row=7, column = 1, padx = 5, pady = 5, columnspan = 4, sticky = tk.W)

        # Buttons for add method        
        self.add_entry_button = tk.Button(root, text = "Add Entry", command = self.add_entry_gui)
        self.add_entry_button.grid(row = 8, column = 0, padx = 5, pady = 5, columnspan = 5, sticky = tk.W+tk.E)

        # Label and entry field for search methid
        self.label_search_entry = tk.Label(root, text = "Search Entry:")
        self.label_search_entry.grid(row = 9, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.entry_search = tk.Entry(root, width=40)
        self.entry_search.grid(row = 9, column = 1, padx = 5, pady = 5, columnspan = 4, sticky = tk.W+tk.E)
        # Buttons for search method 
        self.search_entry_button = tk.Button(root, text = "Search", command = self.search_entry_gui)
        self.search_entry_button.grid(row = 10, column = 0, padx = 5, pady = 5, columnspan = 5, sticky = tk.W+tk.E)

        #Display for search results
        self.search_result_display = tk.Text(root, height = 8, width = 60, state = tk.DISABLED)
        self.search_result_display.grid(row = 11, column = 0, padx = 5, pady = 5, columnspan = 5)

# Function to retrieve data from gui
    def add_entry_gui(self):
        name = self. entry_name.get()
        phone = self. entry_phone.get()
        email = self. entry_email.get()
        date = self. entry_date.get()
        vaccination_status = self.var_vaccination_status.get()
        covid_test = self.var_covid_test.get()
        contact_person_name = self. entry_contact_person_name.get()
        contact_person_phone = self. entry_contact_person_phone.get()

        # Check if everything is filled out
        if not all[(name, phone, email, date, vaccination_status, covid_test, contact_person_name, contact_person_phone)]:
            messagebox.showerror("Error", "Please fill out all fields.")
            return
    
        # Exception handling: phone numbers as digit only
        try:
            if not phone.isdigit():
                raise ValueError ("User phone number should contain only digits.")
            if not contact_person_phone.isdigit():
                raise ValueError("Contact person phone number should contain only digits.")
    
        # Add the data collected from GUI to Apps's records
            self.app.add_entry(name, phone, email, date, vaccination_status, covid_test, contact_person_name, contact_person_phone)
            # Add message box for succesful entries
            messagebox.showinfo("Success", "Entry added successfully!")

        # Clear fields after successful entry
            self.entry_name.delete(0, tk.END)
            self.entry_phone.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_date.delete(0, tk.END)
            self.entry_contact_person_name.delete(0, tk.END)
            self.entry_contact_person_phone.delete(0, tk.END)
            self.var_vaccination_status.set("")
            self.var_covid_test.set("")

        # Add message box for erros
        except ValueError as err:
            messagebox.showerror("Error", str(err))
        except Exception as e:
            messagebox.showerror("Error", "An error occurred while adding the entry.")
        
# Function to retrieve key term from gui
    def search_entry_gui(self):
        key_term = self.entry_search.get()
        search_results = self.app.search_contact_entry(key_term)

    # Clear fields after search
        # Change state of text box to modify
        self.search_result_display.config(state=tk.NORMAL)
        self.search_result_display.delete("1.0", tk.END)

    # Add display for search result
        if search_results:
            self.search_result_display.insert(tk.END, "\n\n".join(search_results))
        else:
            self.search_result_display.insert(tk.END, "No matching entry found.")
        # Disable it again after events
        self.search_result_display.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()  
    app_gui = ContactTracingAppGUI(root)
    root.mainloop()
