import pandas as pd
from openpyxl import load_workbook

def check_aduser (user_name,user_password):
    df = pd.read_excel("Data1.xlsx","Organizer")
    username_lsit = []
    username_lsit = df["Username"]
    userpw_list = []
    userpw_list = df["Password"]
    print(list(userpw_list))
    if user_name in list(username_lsit):
        if user_password in list(userpw_list):
            return True
        else:
            return False
    else:
        return False

def create_league(League_name,sport,user_name,user_password):
    # data = pd.DataFrame({'League_ID': [1],
    #                'League_Name': [League_name],
    #                'Organizer':[2],
    #                'Sport':[sport],
    #                'Games':[2]})
    fname = "Data1.xlsx"
    wb = load_workbook(fname)
    ws = wb.worksheets[0]
    ws_tables = []
    for table in ws_tables:
        ws_tables.append(table)
        print(table.name)
    
# print(check_aduser("Smitty101",123456))



def codeReturn(code):
    data = pd.read_excel ('Data1.xlsx', 'ViewLeagueName') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
    teamName = list(data['TeamName'])
    codeData = list(data['TeamCode'])
    for x in codeData:
        if code == x:
            return teamName[x-1]







