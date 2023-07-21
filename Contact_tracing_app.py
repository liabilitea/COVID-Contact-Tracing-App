# Create class and initialize empty list to put future contact entries
class ContactTracingApp:
    def __init__(self):
        self.entries = []

# Add method to add the entries and its parameters
    def add_entry(self, name, phone, email, date, vaccination_status, covid_test, contact_person_name_, contact_person_phone):
    # name, phone number, email, date, vaccination status, covid test, contact person name and number

# Write the entries in a file without overwriting other entries

# Add method to search for matching existing entries