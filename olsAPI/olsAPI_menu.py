import sys
from os import system
from ols_fetch_details import OntologyAPI


def display_menu():
    """
    Display the menu options.
    """
    print("Select output format:")
    print("1. Human-readable")
    print("2. Machine-readable")
    print("3. Exit")


def menu():
    """
    Handles user selections and interactions with the ontology API.
    """
    ontology_id = input("Please enter ontology id: ")
    while True:
        display_menu()

        selection = int(input("Please select the format (1-3): "))

        if selection == 1: # human readable
            print("Fetching ontology details (human-readable)...")
            # Fetch and format ontology details in human-readable format
            formatted_details = api.fetch_ontology_details_hum(ontology_id)
            print(formatted_details)
            input("Press Enter to Continue\n")
            system('cls')  # clears stdout
        elif selection == 2: # machinebreadable
            print("Fetching ontology details (machine-readable)...")
            # Fetch ontology details in machine-readable format
            ontology_details = api.fetch_ontology_details(ontology_id)
            print(ontology_details)
            input("Press Enter to Continue\n")
            system('cls')  # clears stdout
        elif selection == 3:
            system('cls')  # clears stdout
            print("Goodbye")
            sys.exit()
        else:
            print("Invalid selection. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    # create an instance of ontologu API
    api = OntologyAPI()
    menu()
