import pandas as pd
import os
from databases import Database
from send_email import send_email

subject = "Email Subject"
#body = "This is the body of the text message"
sender = "rodriguestest1234@gmail.com"
recipients = ["rodriguestest1234@gmail.com"]
PASSWORD = os.environ.get('GMAIL_PASSWORD')

def main():
    body = pd.read_excel(r'/home/adam_rodrigues/NEST259/book1.xlsx')
    if body[body.Last_Login > 5]:
        print(body.Last_Login)
    #body = body.to_string()
    #send_email(subject, body, sender, recipients, password)

if __name__ == '__main__':
    print(main())
    




#with open('init2.sql', 'r') as sql_file:
    #sql_script = sql_file.read()
#conn = sqlite3.connect('test.db')
#database = Database("sqlite:///test.sqlite")
#cur = conn.cursor()
#cur.executescript(sql_script)
#cur.close()
#conn.close()
