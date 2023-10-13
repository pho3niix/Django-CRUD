import pandas as pd
import os
import django
from sqlalchemy import create_engine

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evaluation.settings')

django.setup()

db_url = 'mysql://root:@localhost/States'

excel_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'CPdescarga.txt')

try:
    data = pd.read_csv(excel_path, delimiter='|')

    engine = create_engine(db_url)

    data.to_sql('evaluation_zipcode', engine, if_exists='replace', index=False)

    print(f'Data transferred to MySQL table: evaluation')

except FileNotFoundError:
    print("file not found")
except pd.errors.ParserError:
    print(f'Error passing the excel file: {excel_path}')
