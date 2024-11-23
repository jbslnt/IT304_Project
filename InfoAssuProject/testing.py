import pyodbc

# Function to check database connection
def check_connection():
    try:
        # Attempt to establish a connection
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-L26QNKV;'  # Your SQL Server hostname or IP address
            'DATABASE=CapitalGuardDB;'  # Your database name
            'Trusted_Connection=yes;'  # Using Windows Authentication (no username/password)
        )
        print("Connection successful!")
        connection.close()
        return True  # Return True if the connection is successful
    except pyodbc.Error as e:
        print(f"Error connecting to database: {e}")
        return False  # Return False if there was an error

# Example usage of the check_connection function
def main():
    if check_connection():
        print("You can proceed with your database operations.")
    else:
        print("Please check your connection settings and try again.")

if __name__ == "__main__":
    main()
