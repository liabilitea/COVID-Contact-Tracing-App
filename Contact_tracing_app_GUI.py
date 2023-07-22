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
        self.root.resize(False, False)
        self.app = ContactTracingApp()

# Set elements per info
    # Info

    # Buttons for search add and checklist

# Function to retrieve data from gui

# Function to retrieve key term from gui