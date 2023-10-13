from django.core.management import call_command
import pandas as pd
import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evaluation.settings')

django.setup()

from evaluation.models import ZipCode

excel_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'CPdescarga.xls')

try:
    excel_data = pd.read_excel(excel_path, sheet_name=None)

    extracted_data = []

    skip = True

    for sheet_name, df in excel_data.items():
        if skip:
            skip = False
            continue
        data_dict = df.to_dict(orient='records')
        extracted_data.extend(data_dict)

    ZipCode.objects.bulk_create([ZipCode(**item) for item in extracted_data])

    print("Data from excel inserted successfully")

except FileNotFoundError:
    print("file not found")
except pd.errors.ParserError:
    print(f'Error passing the excel file: {excel_path}')
