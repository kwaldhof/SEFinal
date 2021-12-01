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

# print(check_aduser("Smitty101",123456))




