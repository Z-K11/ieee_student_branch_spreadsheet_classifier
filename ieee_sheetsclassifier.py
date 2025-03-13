import pandas as pd 
import gspread 
from google.oauth2.service_account import Credentials
creds = Credentials.from_service_account_file("key/spreadsheet-classifier-7642139566a2.json",
                                              scopes=["https://www.googleapis.com/auth/spreadsheets",
                                                      "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(creds)
sheet_url="https://docs.google.com/spreadsheets/d/1VKMmCC1Hr2NaGF-MQk-BmcJSn3QFfMPELroygKstPCE/edit?gid=0#gid=0"
sheet=client.open_by_url(sheet_url)
worksheet = sheet.get_worksheet(0)
data=worksheet.get_all_records()
df = pd.DataFrame(data)
data_folder = "csv_file"
classified_files_save_path="classified_files"
import os 
os.makedirs(data_folder,exist_ok=True)
os.makedirs(classified_files_save_path,exist_ok=True)
print(f"Current files in the data folder = {os.listdir(data_folder)}")
sheets_name= input("Please provide name for the csv file if the file already exists it will be used or else a new file will be downloaded \n")
final_destination =os.path.join(data_folder,sheets_name) 
if os.path.exists(final_destination):
    print(f'Data already exists at {final_destination}')
else:
    df.to_csv(final_destination)
    print(f'Spreadsheet download succesfully')
print(f'The contents of the file are \n {df}')
print(f'Following columns are located in the spreadsheet {df.columns}')
team_list = df["Members "].unique()
print(f'All team name = {team_list}')
#ai_team = df[df['Members ']=="AI-Engineering Team"].reset_index(drop=True)
#print(ai_team)
#if 'Timestamp' in ai_team.columns:
#   ai_team=ai_team.drop(columns=['Timestamp'])
#print(ai_team)
for team in team_list:
    team_df = df[df["Members "]==team].reset_index(drop=True)
    team_df=team_df.drop(columns=['Timestamp'])
    if team=="":
        continue
    else:
        team_df.to_csv(os.path.join(classified_files_save_path,team+".csv"))
        print(f'Data fream create for team : {team} \n {team_df}')
