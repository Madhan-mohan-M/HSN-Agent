# src/validator.py

import pandas as pd
import re

# Load the dataset (once, on startup)
df = pd.read_csv(r'C:\Users\Administrator\Desktop\HSN\Data\HSN_MASTER_Data.csv')

# Format check: only 2, 4, 6, or 8 digits
def is_valid_format(code):
    return bool(re.fullmatch(r'\d{2}|\d{4}|\d{6}|\d{8}', str(code)))

# Main validation function
def validate_hsn(code):
    code = str(code).strip()
    if not is_valid_format(code):
        return {
            "code": code,
            "valid": False,
            "reason": "Invalid format (only 2, 4, 6, or 8 digits allowed)"
        }
    df.columns = df.columns.str.strip()  # remove whitespace from column names
    match = df[df['HSNCode'].astype(str) == code]
    if not match.empty:
        return {
            "code": code,
            "valid": True,
            "description": match.iloc[0]['Description']
        }
    else:
        return {
            "code": code,
            "valid": False,
            "reason": "HSN code not found in the dataset"
        }