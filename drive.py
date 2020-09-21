import gspread
from oauth2client.service_account import ServiceAccountCredentials 
# from pprint import pprint
import pandas as pd 

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

#coment
credentials = ServiceAccountCredentials.from_json_keyfile_name('drive.json', scope)

client = gspread.authorize(credentials)

sheet = client.open('PurchaseData').sheet1
sheet.format('A1:L1', {'textFormat': {'bold': True}})
sheet.update('121','125')
data = sheet.get_all_records()
df = pd.DataFrame(data)
print(df)