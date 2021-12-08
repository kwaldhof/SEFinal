import pandas as pd

data = pd.read_excel ('Data1.xlsx', 'ViewTeams') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
teamName = list(data['Team Name'])
for x in teamName:
    print(x)
