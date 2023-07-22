# Create class and initialize empty list to put future contact entries
class ContactTracingApp:
    def __init__(self):
        self.entries = []

    # Add method to add the entries and its parameters
    def add_entry(self, name, phone, email, date, vaccination_status, covid_test, contact_person_name, contact_person_phone):
        if not phone.isdigit() or not contact_person_phone.isdigit():
            raise ValueError("Phone number should only contain digits.")

        entry = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nDate of Visit: {date}\nVaccination Status: {vaccination_status}\nTested for Covid-19 in the last 14 days: {covid_test}\nContact Person Name: {contact_person_name}\nContact Person Phone Number: {contact_person_phone}\n"

    # Write the entries in a file without overwriting other entries
        with open("c19_contact_tracing_data.txt", "a") as file:
            file.write(entry)

    # Add method to search for matching existing entries
    def search_entry(self, key_term):
        try:
            with open("c19_contact_tracing_data.txt", "r") as file: 
                entries = file.read().split("\n")
                match = []
        
            for entry in entries:
                entry_fields = entry.split("\n")
                if any(key_term.lower() in field.lower() for field in entry_fields):
                    match.append(entry)
            
            return match
        except FileNotFoundError:
            return None
        except Exception as e:
            print("Error searching entry:", e)
            return None

        