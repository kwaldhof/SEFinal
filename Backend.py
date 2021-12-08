import pandas as pd
from openpyxl import load_workbook

def check_aduser (user_name,user_password):
    df = pd.read_excel("Data1.xlsx","Organizer")
    username_lsit = []
    username_lsit = df["Username"]
    userpw_list = []
    userpw_list = df["Password"]
    if user_name in list(username_lsit):
        if user_password in list(userpw_list):
            return True
        else:
            return False
    else:
        return False


def codeReturn(code):
    data = pd.read_excel ('Data1.xlsx', 'ViewLeagueName') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
    teamName = list(data['TeamName'])
    codeData = list(data['TeamCode'])
    for x in codeData:
        if code == x:
            return teamName[x-1]


def teamNames():
    data = pd.read_excel ('Data1.xlsx', 'ViewTeams')
    teamList = list(data['Team Name'])
    return teamList







