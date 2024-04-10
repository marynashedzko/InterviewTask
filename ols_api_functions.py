import requests
import sys
from os import system

def check_api_access():
    """
    Check the accessibility of the default API endpoint.

    Returns:
    - str: A message indicating whether the API is accessible or not.
    """

    # Define the default base URL and endpoint
    base_url = "https://www.ebi.ac.uk/ols4"
    endpoint = "/terms"

    # Construct the full URL
    url = base_url + endpoint

    # Make a GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        return "API is accessible!"
    else:
        return f"API is not accessible. Status code: {response.status_code}"
    

def fetch_ontology_details(ontology_id):
    """
    Fetch ontology details from the API.

    Parameters:
    - ontology_id (str): The ID of the ontology to fetch details for.

    Returns:
    - dict: A dictionary containing the required ontology details.
    """
    base_url = "https://www.ebi.ac.uk/ols4"
    endpoint = f"/api/ontologies/{ontology_id}"
    url = base_url + endpoint
    response = requests.get(url)

    if response.status_code == 200:
        ontology_details = response.json()
        # Extract only required details
        required_details = {
            "title": ontology_details['config']['title'],
            "description": ontology_details['config']['description'],
            "number_of_terms": ontology_details['numberOfTerms'],
            "status": ontology_details['status']
        }
        return required_details
    elif response.status_code == 404:
        return f"Ontology with ID '{ontology_id}' not found."
    else:
        return f"Error fetching details for ontology with ID '{ontology_id}'. Status code: {response.status_code}"
    


def hum_format(ontology_id):
    """
    Format ontology details in human-readable format.

    Parameters:
    - ontology_id (str): The ID of the ontology to fetch details for.

    Returns:
    - str: Formatted ontology details in human-readable format.
    """
    details = fetch_ontology_details(ontology_id)
    if details:
        return (
            f"Ontology Title: {details['title']}\n"
            f"Ontology Description: {details['description']}\n"
            f"Number of Terms: {details['number_of_terms']}\n"
            f"Current Status: {details['status']}"
        )
    

    
def display_menu():
    """
    Display the menu options.
    """
    print("Select output format:")
    print("1. Human-readable")
    print("2. Machine-readable")
    print("3. Exit")

def done():
    """
    Exit the program.
    """
    system('cls')  # clears stdout
    print("Goodbye")
    sys.exit()


def main():
    """
    Main function to interact with the user and handle selections.
    """
    ontology_id = input("Please enter ontology id: ")
    while True:
        display_menu()

        selection = int(input("Please select the format (1-3): "))

        if selection == 1:
            print("Fetching ontology details (human-readable)...")
            # Fetch and format ontology details in human-readable format
            formatted_details = hum_format(ontology_id)
            print(formatted_details)
            input("Press Enter to Continue\n")
            system('cls')  # clears stdout
        elif selection == 2:
            print("Fetching ontology details (machine-readable)...")
            # Fetch ontology details in machine-readable format
            ontology_details = fetch_ontology_details(ontology_id)
            print(ontology_details)
            input("Press Enter to Continue\n")
            system('cls')  # clears stdout
        elif selection == 3:
            system('cls')  # clears stdout
            print("Goodbye")
            sys.exit()
        else:
            print("Invalid selection. Please enter a number between 1 and 3.")


