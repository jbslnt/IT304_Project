CREATE DATABASE CapitalGuardDB;

USE CapitalGuardDB;

CREATE TABLE ClientBankDetails (
    client_id INT IDENTITY(1,1) PRIMARY KEY,
    first_name NVARCHAR(255),  
    last_name NVARCHAR(255),   
    dob DATE,
    contact_number NVARCHAR(255),
    email_address NVARCHAR(255),
    address NVARCHAR(500),   
    national_id NVARCHAR(255),
    bank_name NVARCHAR(255),  
    account_number NVARCHAR(255),  
    account_type NVARCHAR(255),
    branch_name NVARCHAR(255),    
    ifsc_code NVARCHAR(255),      
    account_balance DECIMAL(15, 2),
    banking_pin NVARCHAR(255)
);
