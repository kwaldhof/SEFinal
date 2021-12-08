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

def get_aduser(user_name,user_password):
    df = pd.read_excel("Data1.xlsx","Organizer")
    for i in range(len(df)):
        if user_name == df.at[i,"Username"] and user_password == df.at[i,"Password"]:
            return df.at[i,"Org_Name"]

def create_league(League_Name,Org_Name_input,Sport_input):
    fname = "Data1.xlsx"
    Sport = pd.read_excel (fname, 'Sport')
    Organizer = pd.read_excel (fname, 'Organizer')
    print(Organizer)
    for i in range(len(Sport)):
        if Sport_input == Sport.at[i,"Sport_Name"]:
            Sport_ID = Sport.at[i,"Sport_ID"]
    for j in range(len(Organizer)):
        if Org_Name_input == Organizer.at[j,"Org_Name"]:
            Organizer_ID = (Organizer.at[j,"Org_ID"])

    data = pd.read_excel(fname,"League") #read the excel file
    new_data = [[len(data),League_Name,Organizer_ID,Sport_ID,0]] #Fetching new record from the frontend (right now I am just set up a record)
    df2 = pd.DataFrame(new_data, columns=['League_ID',"League_Name","Organizer","Sport", "Games"])# Convert this new record to dataframe
    data = data.append(df2,ignore_index=True)#append to the data we got from the excel
    print(data)

    book = load_workbook(fname)
    writer = pd.ExcelWriter(fname,engine = 'openpyxl')
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)#trying to set up not overwrite the excel

    data.to_excel(writer,sheet_name="League",index=False)#push the data to the excel

    writer.save()

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







