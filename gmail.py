import imaplib
import argparse

# add possibility to add args in terminal
parser = argparse.ArgumentParser()
parser.add_argument('--login', type=str, default="anymail@wp.com",
                    help="What is your email address? ")
parser.add_argument('--passw', type=str, default="p@ssword",
                    help="What is password ?")
parser.add_argument('--sub', type=str, default="Header",
                    help="What is subject ?")
args=parser.parse_args()

# account cred
email = f"{args.login}"
email_pass = f"{args.passw}"

#initialize IMAP object for Gmail
imap = imaplib.IMAP4_SSL("imap.gmail.com")

#login to gmail with credentials
imap.login(email, email_pass)

# uncomment to check possible mailboxes
# for i in mail.list()[1]:
#     l = i.decode().split(' "/" ')
#     print(l[0] + " = " + l[1])

# select
imap.select(mailbox='Inbox')

status, message_id_list = imap.search(None, 'FROM', f"{args.sub}")
# return list of e-mails ids
messages = message_id_list[0].split(b' ')

try:
    print("Checking if there is any mail(s) to delete...")
    count =1
    for mail in messages:
        # mark the mail as deleted, delete mail by id
        imap.store(mail, "+FLAGS", "\\Deleted")
        print(count, "mail(s) deleted")
        count +=1
    print("All selected mails have been deleted")
except:
    print('No more mail(s) to delete')

# delete all the selected messages
imap.expunge()

# close the mailbox
imap.close()

# logout from the account
imap.logout()