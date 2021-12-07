import pandas as pd

def codeReturn(code):
    data = pd.read_excel ('Data1.xlsx', 'ViewLeagueName') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
    teamName = list(data['TeamName'])
    codeData = list(data['TeamCode'])
    code = 1
    for x in codeData:
        if code == x:
            return teamName[x]

