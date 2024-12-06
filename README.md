# Banking System Project

This project is a Python-based Banking System application that allows users to:

- Create a bank account.
- Perform deposits, withdrawals, and transfers.
- View account details and transaction history.
- Receive email and SMS notifications for key transactions.

## Features

### 1. Account Management
- Users can register with their name, email, password, and account number.
- Secure login to access accounts.

### 2. Transactions
- **Deposit**: Add funds to your account.
- **Withdraw**: Withdraw funds from your account.
- **Transfer**: Transfer money between accounts.
- **Check Balance**: View current account balance.

### 3. Notifications
- Email notifications for account creation, deposits, withdrawals, and transfers.
- SMS notifications for account creation.

### 4. Transaction History
- Detailed logs of all transactions, including operation type, description, associated accounts, and timestamps.

---

## Technologies Used

- **Programming Language**: Python
- **Email Notifications**: Google SMTP
- **SMS Notifications**: Twilio API
- **Date and Time**: Python's `datetime` module

---

## Requirements

### Prerequisites

1. Python 3.6 or above.
2. Required libraries:
   - `smtplib` (built-in for email sending)
   - `email.mime` (for MIME-formatted email content)
   - `twilio` (for SMS notifications)
3. A Gmail account for sending emails (with "App Password" enabled).
4. A Twilio account for SMS notifications.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/banking-system.git
   cd banking-system
   ```
2. Install dependencies:
   ```bash
   pip install twilio
   ```
3. Set up environment variables for sensitive credentials:
   - Gmail Email and App Password
   - Twilio Account SID, Auth Token, and Messaging Service SID
   
   Example `.env` file:
   ```
   EMAIL_USER=your-email@gmail.com
   EMAIL_PASS=your-app-password
   TWILIO_SID=your-twilio-sid
   TWILIO_AUTH_TOKEN=your-auth-token
   TWILIO_MESSAGING_SID=your-messaging-sid
   ```
4. Run the script:
   ```bash
   python banking_system.py
   ```

---

## How to Use

1. **Run the Script**
   Start the program by running the script in your terminal:
   ```bash
   python banking_system.py
   ```

2. **Main Menu**
   Choose from the following options:
   - Create a new account.
   - Log in to an existing account.
   - List all accounts.
   - Exit the program.

3. **Account Actions**
   After logging in, perform actions like deposit, withdrawal, transfer, or viewing transaction history through a secondary menu.

---

## Code Structure

### Main Components
- **Bankaccount Class**: Encapsulates account operations such as deposits, withdrawals, and transaction history management.
- **Email Notifications**: Uses Google SMTP for sending emails.
- **SMS Notifications**: Implements Twilio API for SMS alerts.
- **Menus**: Provides an interactive CLI for account management and transactions.

---

## Security Notes

1. **Password Protection**
   - Passwords are currently stored in plaintext for simplicity. It is recommended to use a hashing algorithm like `bcrypt` for secure password storage.

2. **Credential Management**
   - Do not hardcode sensitive information (e.g., email password, Twilio tokens). Use environment variables for production.

3. **Error Handling**
   - Add robust error handling for invalid inputs, email/SMS failures, and account number mismatches.

---

## Future Enhancements

1. **Database Integration**
   - Use a database (e.g., SQLite, PostgreSQL) for persistent account and transaction storage.

2. **GUI**
   - Add a graphical user interface (GUI) for better user experience.

3. **Advanced Security**
   - Encrypt sensitive data and use secure authentication mechanisms.

4. **Extended Features**
   - Add support for recurring payments and account statements.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For any questions or feedback, feel free to contact:
- **Name**: Bipin Joseph
- **Email**: bipinjoseph2003@gmail.com

