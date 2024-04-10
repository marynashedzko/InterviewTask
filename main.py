import sys
import ols_api_functions as ols

if __name__ == "__main__":

    print(ols.check_api_access())
    ols.main()

    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <ontology_id> <output_format>")
        sys.exit(1)

    # Extract command-line arguments
    ontology_id = sys.argv[1]
    output_format = sys.argv[2]

    # Fetch ontology details
    ontology_details = ols.fetch_ontology_details(ontology_id)

    # Based on the output format selected, print the ontology details
    if output_format == "hum":
        print(ols.hum_format(ontology_id))  # Print in human-readable format
    elif output_format == "machine":
        print(ontology_details)  # Print in machine-readable format
    else:
        print("Invalid output format. Please choose 'machine' or 'hum'.")
        sys.exit(1)
