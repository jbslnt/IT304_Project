# IT304_Project

Run the following commands in the terminal to install the necessary libraries:

bash
    pip install pycryptodome
    pip install pyodbc


pycryptodome: Used for AES encryption.
pyodbc: Used to connect Python to SQL Server.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Here are the direct steps to set up and run your pyodbc project in Visual Studio Code:

1. Install pyodbc
 - Open the terminal in Visual Studio Code (Ctrl + ~).
 - If using a virtual environment, create and activate it:
      python -m venv venv  # Create virtual environment
      venv\Scripts\activate  # For Windows
      source venv/bin/activate  # For macOS/Linux
   
 - Install pyodbc:
      pip install pyodbc

3. Select Python Interpreter
 -  Press Ctrl + Shift + P (or Cmd + Shift + P on macOS) to open the Command Palette.
 -  Search for and select Python: Select Interpreter.
 -  Choose the interpreter from your virtual environment (e.g., ./venv/bin/python or ./venv/Scripts/python.exe).

4. Install ODBC Driver
  Install ODBC Driver 17 for SQL Server.
 (Link: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16)

5. Setup SQL Server Connection
In your Python script, add the connection configuration:

import pyodbc

def get_connection():
return pyodbc.connect(
 'DRIVER={ODBC Driver 17 for SQL Server};'
 'SERVER=YOUR_SERVER_NAME;'  # Replace with actual server name
 'DATABASE=YOUR_DATABASE_NAME;'  # Replace with actual database name
 'Trusted_Connection=yes;'  # For Windows authentication
  )
      
6. Run Your Python Script
  - Run the Python script in the terminal:
        python your_script.py
  

