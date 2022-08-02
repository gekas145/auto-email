import smtplib
import ssl
from email.message import EmailMessage
import pandas as pd


class MailSender:

    def __init__(self):
        self.mails = []
        self.greetings = []
        tmp = pd.read_excel('database.xlsx',
                            header=None,
                            names=['greeting', 'mail'],
                            index_col=None,
                            engine='openpyxl')
        database = tmp.values.tolist()
        for record in database:
            self.greetings.append(record[0])
            self.mails.append(record[1])

        with open('main_text.txt', 'r', encoding='utf8') as f:
            self.main_text = f.read()
            f.close()

        with open('subject.txt', 'r', encoding='utf8') as f:
            self.subject = f.read()
            f.close()

    def send_mails(self, sender, password, attachment_path):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:

            if attachment_path is not None:
                attachment_file = open(attachment_path, 'rb')
                attachment_content = attachment_file.read()
            else:
                attachment_file = None
                attachment_content = None

            server.login(sender, password)
            for i in range(len(self.mails)):
                msg = EmailMessage()
                msg['Subject'] = self.subject
                msg['From'] = sender
                msg['To'] = self.mails[i]
                msg.set_content(self.greetings[i] + ',\n' + self.main_text)
                if attachment_content is not None:
                    msg.add_attachment(attachment_content,
                                       maintype='application',
                                       subtype='pdf',
                                       filename='attachment.pdf')
                server.send_message(msg)

            if attachment_path is not None:
                attachment_file.close()
            server.quit()
            print('Mails sent successfully!')


if __name__ == '__main__':
    login = 'some@mail'
    password = 'password'
    attachment_path = None

    mailSender = MailSender()
    mailSender.send_mails(login, password, attachment_path)
