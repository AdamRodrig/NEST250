import sqlite3
import os
import pandas as pd
from send_email import send_email
from get_hash import calculate_file_hash, check_file_for_changes

subject = "Email Subject"
body = "This is the body of the text message"
sender = "rodriguestest1234@gmail.com"
password = os.environ.get("GMAIL_PASSWORD")

def main():

    file_path = os.path.abspath("./Book1.xlsx")

    initial_hash = calculate_file_hash(file_path)
    stored_hash = os.environ.get("EXCEL_HASH")
    if not stored_hash:
        stored_hash = initial_hash

    has_changed = not check_file_for_changes(file_path, stored_hash)

    if has_changed:
        print("--->The file has been changed.")
        body = pd.read_excel(file_path)
        value = body[body['Last_Login'] > 30]
        for _, row in value.iterrows():
            last_login = row['Last_Login']
            message = f"Subject: Reminder: Your last login was {last_login} ago."
            body = value.to_string()
            send_email(subject, body, sender, row["Email_Address"], password)
    else:
        print("---> The file has not been changed.")
        print("---> Waiting for 10s before checking again")
    return

if __name__ == '__main__':
    main()
