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
        
    
    # Buttons for search add and checklist

# Function to retrieve data from gui

# Function to retrieve key term from gui

if __name__ == "__main__":
    root = tk.Tk()  
    app_gui = ContactTracingAppGUI(root)
    root.mainloop()
