import pyodbc
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os

# AES Configuration
key = b'SecureKey1234567'  # 16 bytes key (ensure secure key management in production)

# Generate a random 16-byte IV
def generate_iv():
    return os.urandom(16)

# Functions for Encryption and Decryption
def encrypt_data(data):
    iv = generate_iv()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    return base64.b64encode(iv + encrypted).decode('utf-8')

def decrypt_data(encrypted_data):
    encrypted_data_bytes = base64.b64decode(encrypted_data)
    iv = encrypted_data_bytes[:16]  # Extract IV
    encrypted_message = encrypted_data_bytes[16:]  # Extract encrypted data
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted_message), AES.block_size)
    return decrypted.decode('utf-8')

# SQL Server Connection
def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-L26QNKV;'  # Change this to your server name
        'DATABASE=CapitalGuardDB;'
        'Trusted_Connection=yes;'  # Windows Authentication
    )

# Collect and Store Client and Banking Data
def collect_and_store_client_data():
    print("Enter Client and Banking Details:")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    contact_number = input("Contact Number: ")
    email_address = input("Email Address: ")
    address = input("Residential Address: ")
    national_id = input("National ID/SSN: ")
    bank_name = input("Bank Name: ")
    account_number = input("Account Number: ")
    account_type = input("Account Type (Savings/Checking): ")
    branch_name = input("Branch Name: ")
    ifsc_code = input("IFSC/SWIFT Code: ")
    account_balance = input("Account Balance: ")
    banking_pin = input("Banking PIN: ")

    # Encrypt sensitive data
    encrypted_data = {
        'first_name': encrypt_data(first_name),
        'last_name': encrypt_data(last_name),
        'dob': dob,
        'contact_number': encrypt_data(contact_number),
        'email_address': encrypt_data(email_address),
        'address': encrypt_data(address),
        'national_id': encrypt_data(national_id),
        'bank_name': encrypt_data(bank_name),
        'account_number': encrypt_data(account_number),
        'account_type': encrypt_data(account_type),
        'branch_name': encrypt_data(branch_name),
        'ifsc_code': encrypt_data(ifsc_code),
        'account_balance': account_balance,
        'banking_pin': encrypt_data(banking_pin),
    }

    # Store encrypted data in the database
    connection = get_connection()
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO ClientBankDetails (first_name, last_name, dob, contact_number, email_address, address, national_id, 
                                    bank_name, account_number, account_type, branch_name, ifsc_code, account_balance, banking_pin)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(insert_query, tuple(encrypted_data.values()))
    connection.commit()

    print("\nClient and banking details have been encrypted and stored successfully!")

    cursor.close()
    connection.close()

# Retrieve and Decrypt Client and Banking Data
def view_client_data():
    connection = get_connection()
    cursor = connection.cursor()

    select_query = """
    SELECT first_name, last_name, dob, contact_number, email_address, address, national_id,
           bank_name, account_number, account_type, branch_name, ifsc_code, account_balance, banking_pin
    FROM ClientBankDetails
    """
    cursor.execute(select_query)

    print("\nDecrypted Client and Banking Details:")
    for row in cursor.fetchall():
        decrypted_data = {
            'First Name': decrypt_data(row[0]),
            'Last Name': decrypt_data(row[1]),
            'Date of Birth': row[2],  # Not encrypted
            'Contact Number': decrypt_data(row[3]),
            'Email Address': decrypt_data(row[4]),
            'Address': decrypt_data(row[5]),
            'National ID/SSN': decrypt_data(row[6]),
            'Bank Name': decrypt_data(row[7]),
            'Account Number': decrypt_data(row[8]),
            'Account Type': decrypt_data(row[9]),
            'Branch Name': decrypt_data(row[10]),
            'IFSC/SWIFT Code': decrypt_data(row[11]),
            'Account Balance': row[12],  # Not encrypted
            'Banking PIN': decrypt_data(row[13]),
        }

        # Print decrypted data
        for key, value in decrypted_data.items():
            print(f"{key}: {value}")
        print("-" * 50)

    cursor.close()
    connection.close()

# Main Menu
def main():
    while True:
        print("\n--- Client Management System ---")
        print("1. Add New Client")
        print("2. View Clients")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            collect_and_store_client_data()
        elif choice == '2':
            view_client_data()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
