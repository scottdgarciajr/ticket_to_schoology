#pip install schoolopy

import imaplib
from schoolopy import Schoology, Auth



def get_unread_emails():
    # Set up connection to IMAP server
    imap_server = imaplib.IMAP4_SSL('imap.gmail.com')
    imap_server.login('your_email_address@gmail.com', 'your_email_password')#set email here
    imap_server.select('inbox')

    # Search for unread messages
    status, email_ids = imap_server.search(None, 'UNSEEN')

    # Initialize empty string to store the email
    email_data_str = ''

    # Iterate over each unread message and append the email data to the string
    for email_id in email_ids[0].split():
        status, email_data = imap_server.fetch(email_id, '(RFC822)')
        email_data_str += str(email_data[0][1]) + '\n'

    # Close the connection to the IMAP server
    imap_server.close()
    imap_server.logout()

    # Return the email data string
    return email_data_str





# Replace with your Schoology API key and secret
api_key = 'your_api_key'#This is where I run into an issue... I need to find where to get an API key. I don't even know if I can get one since I'm a student
api_secret = 'your_api_secret'


username = 'put_username_here'#PUT SCHOOLOGY USERNAME HERE
password = 'put_password_here'#PUT SCHOOLOGY PASSWORD HERE

# Initialize the Schoology API client and authenticate with user credentials
client = Schoology(Auth(api_key, api_secret, username, password))

class_id = '6546201569'#put classID here... I think this is the right one

# Create a new Schoology update object with the specified text
new_update = client.update_me({'body': get_unread_emails(), 'section_id': class_id})

# Check if the update was successfully posted and print the update ID
if new_update:
    print(f'Update posted with ID {new_update.id}')
else:
    print('Failed to post update')


