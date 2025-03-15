import pandas as pd
import gspread 
from google.oauth2.service_account import Credentials
key_path = input('Please provide the path to your api key down below \n')
print(f'Here is the provided key path = {key_path}')
creds = Credentials.from_service_account_file(key_path,
                                              scopes=["https://www.googleapis.com/auth/spreadsheets",
                                                      "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(creds)
sheet_url = input ("Please provide the url for the sheet\n")
sheet=client.open_by_url(sheet_url)
worksheet = sheet.get_worksheet(0)
data = worksheet.get_all_records()
df = pd.DataFrame(data)
import os 
data_folder = 'csv_file'
classified_files = 'classified_files'
os.makedirs(data_folder,exist_ok=True)
os.makedirs(classified_files,exist_ok=True)
sheet_name=input("Please provide the name for the google sheets file ")
dest = os.path.join(data_folder,sheet_name)
df.to_csv(dest)
print(f'File succesfully saved at path = {dest}')
print(f'Here is an overview of the spreadh shet \n {df.head()}')
print(f'Your file contains the following columns \n {df.columns}')