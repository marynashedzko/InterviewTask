import unittest
import requests
from unittest.mock import MagicMock, patch
from olsAPI.ols_api_functions import OntologyAPI  
 

class TestOntologyAPI(unittest.TestCase):

    def setUp(self):
        self.api = OntologyAPI()


    def test_fetch_ontology_details_wrong_id(self):
        # Mocking the response for a 404 error for a wrong ontology ID
        ontology_id = "wrong_id"
        expected_error_message = f"Ontology with ID '{ontology_id}' not found."
        self.api.session.get = MagicMock(return_value=MagicMock(status_code=404))

        result = self.api.fetch_ontology_details(ontology_id)

        self.assertEqual(result, expected_error_message)

    def test_fetch_ontology_details_connection_error(self):
        # Mocking a connection error
        ontology_id = "example_id"
        expected_error_message = "Failed to connect to the API. Please check your internet connection or try again later."
        
        # Create a MagicMock object to simulate the behavior of self.api.session.get
        self.api.session.get = MagicMock(side_effect=requests.exceptions.ConnectionError)

        result = self.api.fetch_ontology_details(ontology_id)

        self.assertEqual(result, expected_error_message)    

    

if __name__ == '__main__':
    unittest.main()
