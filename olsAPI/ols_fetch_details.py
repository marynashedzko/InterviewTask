"""
This module provides classes and functions for 
interacting with the EBI Ontology Lookup Service (OLS) API.

The main class in this module is OntologyAPI, which allows 
fetching ontology details in both human-readable and machine-readable formats.
"""

import sys
from os import system
import requests

class OntologyAPI:
    """
    A class for interacting with the EBI Ontology Lookup Service (OLS) API.

    This class provides methods to fetch ontology details, 
    both in human-readable and machine-readable formats.
    """
    def __init__(self):
        """
        Initializes the OntologyAPI object with the base URL and a session object.
        """
        self.base_url = "https://www.ebi.ac.uk/ols4"
        self.session = requests.Session()  # Initialize a session object

    def fetch_ontology_details(self, ontology_id):
        """
        Fetches details for a specific ontology in JSON format.

        Parameters:
        - ontology_id (str): The ID of the ontology to fetch details for.

        Returns:
        - dict or str: A dictionary containing ontology details if successful, 
        or an error message if unsuccessful.
        """
        try:
            # Fetch ontology details
            endpoint = f"/api/ontologies/{ontology_id}"
            url = self.base_url + endpoint
            response = self.session.get(url, timeout=5)

            if response.status_code == 200:
                ontology_details = response.json()
                required_details = {
                    "title": ontology_details['config']['title'],
                    "description": ontology_details['config']['description'],
                    "number_of_terms": ontology_details['numberOfTerms'],
                    "status": ontology_details['status']
                }
                return required_details
            if response.status_code == 404:
                return f"Ontology with ID '{ontology_id}' not found."
            else:
                return f"Error fetching details for ontology with ID '{ontology_id}'. Status code:{response.status_code}"
        except requests.exceptions.ConnectionError:
            return "Failed to connect to the API. Please check your internet connection or try again later."


    def fetch_ontology_details_hum(self, ontology_id):
        """
        Fetches ontology details in human-readable format.

        Parameters:
        - ontology_id (str): The ID of the ontology to fetch details for.

        Returns:
        - str: A human-readable string containing ontology details,
          or a message indicating no details found.
        """
        details = self.fetch_ontology_details(ontology_id)
        if details:
            return (
                f"Ontology Title: {details['title']}\n"
                f"Ontology Description: {details['description']}\n"
                f"Number of Terms: {details['number_of_terms']}\n"
                f"Current Status: {details['status']}"
            )
        return "No details found for the provided ontology ID."


def main():
    """
    Main function to interact with the user, handle inputs, and display ontology details.
    """
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <ontology_id> <output_format>")
        sys.exit(1)

    ontology_id = sys.argv[1]
    output_format = sys.argv[2]

    hum = api.fetch_ontology_details_hum(ontology_id)
    machine = api.fetch_ontology_details(ontology_id)
    # Based on the output format selected, print the ontology details
    if output_format == "hum":
        print(hum)  # Print in human-readable format
    elif output_format == "machine":
        print(machine)  # Print in machine-readable format
    else:
        print("Invalid output format. Please choose 'machine' or 'hum'.")
        sys.exit(1)



if __name__ == "__main__":
    # create an instance of ontology API
    api = OntologyAPI()
    main()
