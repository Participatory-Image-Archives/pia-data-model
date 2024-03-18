# Finding IIIF Image API URLs from the DaSCH Service Platform (DSP)

## Overview
The goal of this directory is to automate the process of amending and completing a target CSV file (`target.csv`) with data derived from two other CSV files (`queryResults.csv` and `brunner-mapping.csv`) and additional computations. It leverages a Python script (`fill-csv.py`) and a utility module (`base64url_check_digit.py`) to calculate IDs, match records, and populate missing information in the target CSV.

## Files Description
- **fill-csv.py**: The main Python script that reads data from `queryResults.csv` and `brunner-mapping.csv`, processes it, and updates `target.csv`.
- **base64url_check_digit.py**: A Python module used by `fill-csv.py` to calculate a check digit for IDs extracted from `queryResults.csv`.
- **queryResults.csv**: Contains results from a SPARQL query, including image information and URLs for IIIF Image API services.
- **brunner-mapping.csv**: Maps old numbers to signatures, assisting in the correlation of records in `target.csv`.
- **target.csv**: The CSV file to be amended with data from the other files. Contains columns for image IDs, URLs, signatures, and more.

## How It Works
The script matches records from `queryResults.csv` to `target.csv` based on image labels/signatures and updates the latter with DSP URLs, IIIF Image API info and full image URLs. It also uses `brunner-mapping.csv` to fill in the former numbers in `target.csv` based on the mappings provided.

## Running the Script
1. **Run Script**: Execute the `fill-csv.py` script with the command `python fill-csv.py`. This will read the necessary data from `queryResults.csv` and `brunner-mapping.csv`, process it, and update `target.csv` accordingly.
2. **Check Results**: Upon completion, the script will generate `target_amended.csv`, which contains the updated and completed data.