# Import
import tkinter as tk
from Contact_tracing_app_GUI import ContactTracingAppGUI

# Create root window and main module
if __name__ == "__main__":
    root = tk.Tk()  
    app_gui = ContactTracingAppGUI(root)
    root.mainloop()
