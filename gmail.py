import imaplib

# account cred
email = "yourlogin@gmail.com"
email_pass = "password"

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

status, message_id_list = imap.search(None, 'FROM', "address email or header")
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