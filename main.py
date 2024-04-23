import smtplib
import datetime as dt
import random

import pandas as pd

PLACE_HOLDER = "[NAME]"


# --------------- Extra Hard Starting Project ------------------

def sendmail(mail, text):
    my_email = "d.arun672002@gmail.com"
    password = "fqxadmylptcrysgj"
    with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
        conn.starttls()
        conn.login(user=my_email, password=password)
        conn.sendmail(from_addr=my_email, to_addrs=f"{mail}",
                      msg=f"Subject:Happy Birthday\n\n{text}")
        conn.close()


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["day"]):data_row for (index, data_row) in data.iterrows()}
month = dt.datetime.now().month
day = dt.datetime.now().day
today_tuple =(month,day)
if today_tuple in birthdays_dict:
    friend = birthdays_dict[today_tuple]
    # today = dt.datetime(day=6,month=7,year=2002)
    file = random.randint(1, 3)
    file_path = f"letter_templates/letter_{file}.txt"
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

    with open(file_path) as f:
        ls = f.read()
    ls = ls.replace(PLACE_HOLDER, friend["name"])
    sendmail(friend["email"], ls)
