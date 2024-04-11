# EBI Ontology Lookup Service (OLS) API Module

## Introduction
This Python module facilitates interaction with the EBI Ontology Lookup Service (OLS) API. The module offers classes and functions to retrieve ontology details in both human-readable and machine-readable formats.

## Installation
There are no special installation instructions for this module. You can simply download the provided files and include them in your project directory.

## Usage
To use this module, follow these steps:

1. **Import the Module**: Import the `OntologyAPI` class from the module into your Python script or interactive session.
    ```python
    from ols_fetch_details import OntologyAPI
    ```

2. **Create an Instance of the `OntologyAPI` Class**: Instantiate the `OntologyAPI` class to access its methods.
    ```python
    api = OntologyAPI()
    ```

3. **Fetch Ontology Details**: Utilise the `fetch_ontology_details` method to retrieve ontology details in machine-readable format (JSON).
    ```python
    ontology_id = "your_ontology_id"
    details = api.fetch_ontology_details(ontology_id)
    print(details)
    ```

4. **Fetch Human-Readable Ontology Details**: Use the `fetch_ontology_details_hum` method to retrieve ontology details in human-readable format.
    ```python
    ontology_id = "your_ontology_id"
    details_hum = api.fetch_ontology_details_hum(ontology_id)
    print(details_hum)
    ```

5. **Main Functionality**: Alternatively, you can utilise the provided `main` function for command-line usage. Execute the script with the following command:
    ```bash
    python ols_fetch_details.py <ontology_id> <output_format>
    ```
    Replace `<ontology_id>` with the ID of the ontology you want to retrieve details for, and `<output_format>` with either `machine` or `hum` for machine-readable or human-readable output, respectively.

6. **Interactive Menu Functionality**: Alternatively, you can use the provided interactive menu from the command line to interactively fetch ontology details. Execute the following command:
    ```bash
    python olsAPI_menu.py
    ```
    The menu will guide you through the process of fetching ontology details interactively.


## Example
Here's an example demonstrating how to use the module:

```python
# Fetch ontology details in machine-readable format (JSON)
ontology_id = "efo"
details_machine = api.fetch_ontology_details_hum(ontology_id)
print(details_machine)

# Fetch ontology details in human-readable format
details_hum = api.fetch_ontology_details_hum(ontology_id)
print(details_hum)


```
  Output:
    
 ```python
# json
    {'title': 'Experimental Factor Ontology', 'description': 'The Experimental Factor Ontology (EFO) provides a systematic description of many experimental variables available in EBI databases, and for external projects such as the NHGRI GWAS catalogue. It combines parts of several biological ontologies, such as anatomy, disease and chemical compounds. The scope of EFO is to support the annotation, analysis and visualization of data handled by many groups at the EBI and as the core ontology for OpenTargets.org', 'number_of_terms': 52497, 'status': 'LOADED'}

# human-readable
    Ontology Title: Experimental Factor Ontology
    Ontology Description: The Experimental Factor Ontology (EFO) provides a systematic description of many experimental variables available in EBI databases, and for external projects such as the NHGRI GWAS catalogue. It combines parts of several biological ontologies, such as anatomy, disease and chemical compounds. The scope of EFO is to support the annotation, analysis and visualization of data handled by many groups at the EBI and as the core ontology for OpenTargets.org
    Number of Terms: 52497
    Current Status: LOADED
```
