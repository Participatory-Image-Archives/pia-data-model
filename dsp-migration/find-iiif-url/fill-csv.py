import os
import pandas as pd
from base64url_check_digit import calculate_check_digit

# Load the CSV files
query_results_df = pd.read_csv("queryResults.csv")
brunner_mapping_df = pd.read_csv("brunner-mapping.csv")
target_df = pd.read_csv("target.csv")

# EKWS project settings
base_ark = "https://ark.dasch.swiss/ark:/72163/1/"
dsp_api = "https://api.dasch.swiss/v2/"
project = "0812"  # EKWS project identifier

# Process each row in queryResults.csv to update target.csv
for _, qr_row in query_results_df.iterrows():
    # Calculate complete ID with base64 check digit
    check_digit = calculate_check_digit(qr_row['internalLink'])
    complete_id = qr_row['internalLink'] + check_digit
    corrected_id = complete_id.replace('-', '=')
    dsp_url = f"{base_ark}{project}/{corrected_id}"

    # Find matching row in target.csv based on signature
    target_row = target_df[target_df['signature'] == qr_row['label']]

    # Update target.csv columns if match is found
    if not target_row.empty:
        index = target_row.index[0]
        target_df.at[index, 'dsp-url'] = dsp_url
        target_df.at[index, 'dsp-iiif-image-api-info'] = qr_row['ImageAPIinfo']
        target_df.at[index, 'dsp-iiif-image-api-full'] = qr_row['ImageAPIfull']

# Update former-number in target.csv based on brunner-mapping.csv
for _, bm_row in brunner_mapping_df.iterrows():
    target_rows = target_df[target_df['signature'] == bm_row['Signature']]
    for index, _ in target_rows.iterrows():
        target_df.at[index, 'former-number'] = bm_row['hasOldNr']

# Save the amended target.csv
target_df.to_csv("target_amended.csv", index=False)