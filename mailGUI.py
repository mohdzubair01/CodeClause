import tkinter as tk
from tkinter import messagebox
import smtplib

def send_mail():
    try:
        global sender_entry, sender_password_entry

        sender_email = sender_entry.get()
        sender_password = sender_password_entry.get()

        recipient_email = recipient_entry.get()

        subject = subject_entry.get()

        body = body_entry.get('1.0', tk.END)

        if not sender_email or not sender_password or not recipient_email or not subject or not body:
            messagebox.showerror('Error', 'Please fill in all fields.')
            return

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(sender_email, sender_password)

        smtp.sendmail(sender_email, recipient_email, f'Subject: {subject}\n\n{body}')

        messagebox.showinfo('Success', 'Your email has been sent!')

        smtp.quit()

    except smtplib.SMTPAuthenticationError:
        messagebox.showerror('Error', 'Failed to authenticate with the email server. '
                                      'Please check your email and password.')
    except smtplib.SMTPException:
        messagebox.showerror('Error', 'An error occurred while sending the email. '
                                      'Please try again later.')
    except Exception as e:
        messagebox.showerror('Error', f'An unexpected error occurred: {str(e)}')

root = tk.Tk()
root.title('Mail Sender')

sender_label = tk.Label(root, text='Sender\'s Email Address:')
sender_password_label = tk.Label(root, text='Sender\'s Password:')
recipient_label = tk.Label(root, text='Recipient\'s Email Address:')
subject_label = tk.Label(root, text='Subject:')
body_label = tk.Label(root, text='Body:')

sender_entry = tk.Entry(root)
sender_password_entry = tk.Entry(root, show='*')
recipient_entry = tk.Entry(root)
subject_entry = tk.Entry(root)
body_entry = tk.Text(root)

send_button = tk.Button(root, text='Send', command=send_mail)

sender_label.grid(row=0, column=0)
sender_entry.grid(row=0, column=1)
sender_password_label.grid(row=1, column=0)
sender_password_entry.grid(row=1, column=1)
recipient_label.grid(row=2, column=0)
recipient_entry.grid(row=2, column=1)
subject_label.grid(row=3, column=0)
subject_entry.grid(row=3, column=1)
body_label.grid(row=4, column=0)
body_entry.grid(row=4, column=1, columnspan=2)
send_button.grid(row=5, column=0, columnspan=2)

root.mainloop()
