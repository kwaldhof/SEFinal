import pandas as pd

def check_aduser (user_name,user_password):
    df = pd.read_excel("Data1.xlsx","Organizer")
    df.head()
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
    writer = pd.ExcelWriter('Data1.xlsx', engine='xlsxwriter')
    df = pd.DataFrame({'League_ID': [1],
                   'League_Name': [League_name],
                   'Organizer':[2],
                   'Sport':[sport],
                   'Games':[2]})
    df.to_excel(writer, sheet_name="League", index=3)
    worksheet = writer.sheets['League']
    # Close writer
    writer.close()

# print(check_aduser("Smitty101",123456))

create_league("WAC","Football",1212,1212)




