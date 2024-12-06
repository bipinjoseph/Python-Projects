accounts=[]
import datetime

#add email property and also add it to the accont registration place.

class Bankaccount:
    def __init__(self,accountnumber,name,password,email):
        self.accountnumber=accountnumber
        self.name=name
        self.balance=0
        self.history=[]
        self.password=password
        self.email=email

    
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"{amount} rupees is deposited succsesfully and current balance is{self.balance}")

    def withdraw(self,amount):
        self.balance=self.balance-amount
        print(f"{amount} rupees is withdrawed succsesfully and current balance is{self.balance}")

    def showbalance(self):
        print(f"The current balance is {self.balance}")
        
    
    def details(self):
        print(f"The account holder name is:{self.name}")
        print(f"The account  number  is:{self.accountnumber}")
        print(f"The account balance is:{self.balance}")

    def debit(self,amount):
        self.balance=self.balance-amount

    def credit(self,amount):
        self.balance=self.balance+amount

    def addlog(self,opr,des,accnt):
        idno=len(self.history)+1
        date=datetime.datetime.now()
        self.history.append([idno,opr,des,accnt,date])

    







def select():

    choice=int(input('''

                 1.Create Account
                 2.Log In
                 3.List All Account
                 4.Exit
                  
                Enter your choice:         '''))


 

    if(choice==1):

        print("Account Registration")

        na=input("Enter the name of the account holder: ") 
        accnum=int(input("Enter the account number: "))
        passw=input("Enter the password: ") 
        em=input("Enter your email: ")        
        n=Bankaccount(accnum,na,passw,em)
        accounts.append(n)
        n.details()

        #here we use google smtp to send email while account creation

        import smtplib
        from email.mime.text import MIMEText
        subject = "Your account is created"
        body = f'''Your account is created succsesfully
                   Your account deatils are: 
                   Account Number:{n.accountnumber}
                   Name: {n.name}
                   Email ID: {n.email}'''

        sender = "bipinjoseph2003@gmail.com"
        recipients = [n.email]
        password = "drfpqwhpyvdualib" # passwrod generated to use smtp service


        def send_email(subject, body, sender, recipients, password):
                msg = MIMEText(body)
                msg['Subject'] = subject
                msg['From'] = sender
                msg['To'] = ', '.join(recipients)
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                 smtp_server.login(sender, password)
                 smtp_server.sendmail(sender, recipients, msg.as_string())
                print("Message sent!")


        send_email(subject, body, sender, recipients, password)

        from twilio.rest import Client
        account_sid = 'AC2862d58c2efcf4a767aeae61bb31dce5'
        auth_token = 'c81b9b584878262f52224b71b26ed917'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        messaging_service_sid='MGda4b100daeee215fef5a4e14898ea299',
        body=f'''Your account is created succsesfully
                   Your account deatils are: 
                   Account Number:{n.accountnumber}
                   Name: {n.name}
                   Email ID: {n.email}''',
        to='+918590191091'
        )
        print(message.sid)
                
        print("Account created successfully")

        select()

    elif(choice==2):
        print("Logged In")

        l=int(input("Enter  your account number: "))
        p=input("Enter your password: ")
        for w in accounts:  #name of account is w
            if(w.accountnumber==l and w.password==p):
                print("Successfully Loged In")
                print(f"welcome{w.name} and your account number is{w.accountnumber} ")

                def sel():

                 d=int(input('''
                                21. Get Account Details
                                2. Deposit
                                3. Withdraw
                                4. Check Balance
                                5. Transfer
                                6.Payment history
                                7.Back To Main Menu
                            
                                Enter your Choice:      '''     ))
                 
                 if d==1:
                    print("Get account Details")
                    w.details()
                
                    sel()
                 elif d==2:
                    print("Deposit")
                    k=int(input("Enter the amount to deposit: "))
                    w.deposit(k)
                    import smtplib
                    from email.mime.text import MIMEText
                    subject = "Deposit success"
                    body = f'''Deposition is succesful and the details are as follows:
                            Amount of deposition:{k} 
                            Account Number:{w.accountnumber}
                            Name: {w.name}
                            Email ID: {w.email}'''

                    sender = "bipinjoseph2003@gmail.com"
                    recipients = [w.email]
                    password = "drfpqwhpyvdualib" # passwrod generated to use smtp service


                    def send_email(subject, body, sender, recipients, password):
                            msg = MIMEText(body)
                            msg['Subject'] = subject
                            msg['From'] = sender
                            msg['To'] = ', '.join(recipients)
                            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                             smtp_server.login(sender, password)
                             smtp_server.sendmail(sender, recipients, msg.as_string())
                            print("Message sent!")


                    send_email(subject, body, sender, recipients, password)
                    w.addlog ("deposit",f"deposited rupees {k} to your account by ","self")
                    sel()

                 elif d==3:
                    print("Withdraw")
                    wi=int(input("Enter the amount to withdraw: "))
                    w.withdraw(wi)
                    import smtplib
                    from email.mime.text import MIMEText
                    subject = "Withdrawal Success"
                    body = f'''Withdrawal is successful and the derails are as follows:
                            Amount: {wi} 
                            Account Number: {w.accountnumber}
                            Name: {w.name}
                            Email ID: {w.email}'''

                    sender = "bipinjoseph2003@gmail.com"
                    recipients = [w.email]
                    password = "drfpqwhpyvdualib" # passwrod generated to use smtp service


                    def send_email(subject, body, sender, recipients, password):
                            msg = MIMEText(body)
                            msg['Subject'] = subject
                            msg['From'] = sender
                            msg['To'] = ', '.join(recipients)
                            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                             smtp_server.login(sender, password)
                             smtp_server.sendmail(sender, recipients, msg.as_string())
                            print("Message sent!")


                    send_email(subject, body, sender, recipients, password) 
                    w.addlog("withdraw",f"withdrawed amount is{wi} from your account by","self")
                    sel()

                 elif d==4:
                     print("Check Balance")
                     w.showbalance()
                     sel()

                 elif d==5:
                     print("Transfer")
                     tr=int(input("Enter the account nmbr to transfer: "))
                     j=""
                     for account in accounts:
                         if(tr==account.accountnumber):
                             j=account
                             break
                     print(f"transfer to {j.name}")
                     amt=int(input("Enter the amount to transfer: "))
                     w.debit(amt)
                     w.addlog("debit",f"debited amount rupees{amt} from your account to",f"{j.name}--{j.accountnumber}")
                     j.credit(amt)
                     j.addlog("credit",f"credited amount rupees{amt} to your account from",f"{w.name}--{w.accountnumber}")
                     import smtplib
                     from email.mime.text import MIMEText
                     subject1 = "Amount is transfered successfully"
                     subject2= "Amount received successfully"
                     body1 = f'''Amount is transfered 
                            Transfered account deatils are: 
                            Account Number:{j.accountnumber}
                            Transfered Amount is: {amt}
                            Name: {j.name}
                            Email ID: {j.email}'''

                     body2 = f'''Amount is transfered 
                            Transfered account deatils are: 
                            Account Number:{j.accountnumber}
                            Transfered Amount is: {amt}
                            Name: {j.name}
                            Email ID: {j.email}'''

                     sender = "bipinjoseph2003@gmail.com"
                     recipients1 = [w.email]
                     recipients2 = [j.email]
                     password = "drfpqwhpyvdualib" # passwrod generated to use smtp service
 

                     def send_email(subject, body, sender, recipients, password):
                            msg = MIMEText(body)
                            msg['Subject'] = subject
                            msg['From'] = sender
                            msg['To'] = ', '.join(recipients)
                            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                             smtp_server.login(sender, password)
                             smtp_server.sendmail(sender, recipients, msg.as_string())
                            print("Message sent!")


                     send_email(subject1, body1, sender, recipients1, password)
                     send_email(subject2, body2, sender, recipients2, password)
                     print("Payment completed successfully")


                     sel()

                 elif d==6:
                     print("Payment History")
                     for tt in w.history:
                         print(tt[0],tt[1],tt[2],tt[3],tt[4])
                     sel()

                 elif d==7:
                     print("Back To Main Menu")
                     select()

                 else:
                     print("Invalid Input")
                     sel()

                sel()

            

    elif(choice==3):
     print("Listing  All Accounts")
     for account in accounts:
            print(account.accountnumber,account.name)
            select()
    elif(choice==4):
        print("Exited")
        
    else:
        print("Invalid Input")
        select()

select()




