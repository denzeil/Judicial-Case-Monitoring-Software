from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from tkinter import *

def send_email():
    # Get the values from the Entry widgets
    sender = sender_entry.get()
    password ="1caleb2denzeil"
    recipient = recipient_entry.get()
    subject = subject_entry.get()
    body = body_text.get(1.0, END)

    # Create a MIME multipart message and set its headers
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject

    # Attach the body of the message as a MIME text object
    msg.attach(MIMEText(body, 'plain'))

    # Send the message using a SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        # Log in to your email account
        smtp.login(sender, password)

        # Send the email
        smtp.sendmail(sender, recipient, msg.as_string())

    # Clear the Entry and Text widgets
    sender_entry.delete(0, END)
    recipient_entry.delete(0, END)
    subject_entry.delete(0, END)
    body_text.delete(1.0, END)

    # Display a message indicating that the email has been sent
    message_label.config(text='Email sent successfully!')

# Create the GUI window
root = Tk()
root.title('Send Email')

# Create the labels and Entry widgets for the sender, password, recipient, and subject
sender_label = Label(root, text='Sender:')
sender_label.grid(row=0, column=0)
sender_entry = Entry(root)
sender_entry.grid(row=0, column=1)


recipient_label = Label(root, text='Recipient:')
recipient_label.grid(row=2, column=0)
recipient_entry = Entry(root)
recipient_entry.grid(row=2, column=1)

subject_label = Label(root, text='Subject:')
subject_label.grid(row=3, column=0)
subject_entry = Entry(root)
subject_entry.grid(row=3, column=1)

# Create the Text widget for the body of the email
body_label = Label(root, text='Body:')
body_label.grid(row=4, column=0)
body_text = Text(root, height=10, width=50)
body_text.grid(row=4, column=1)

# Create the button for sending the email
send_button = Button(root, text='Send Email', command=send_email)
send_button.grid(row=5, column=0)

# Create the label for displaying messages
message_label = Label(root, text='')
message_label.grid(row=5, column=1)

# Run the GUI loop
root.mainloop()
