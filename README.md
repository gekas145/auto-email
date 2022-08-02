# auto-email
I once needed to send many mails with personalzed greetings and same contents. This repository contains code that automates this sending. It works with `gmail` host, in order to be able to log in to your gmail account you will have to define special password in your google account for 3rd party apps. 

How to use:

- put mail body text and subject to `main_text.txt` and `subject.txt` respectively,
- specify your mail address and password in `MailSender.py`,
- if needed you can set `attachment_path` to attach a file to your message(tested with pdfs only), let it be equal to `None` otherwise,
- run `MailSender.py`.

Note: Use code from this repository at your own risk, I am not responsible for any issues that may be caused by this code.
