CREATE TABLE airbnb.customer_dim (
    customer_id INT, 
    first_name NVARCHAR(100),
    last_name NVARCHAR(100),
    email NVARCHAR(255),
    phone_number NVARCHAR(50),
    address NVARCHAR(255),
    city NVARCHAR(100),
    state NVARCHAR(100),
    country NVARCHAR(100),
    zip_code NVARCHAR(20),
    signup_date DATE,
    last_login DATETIME,
    total_bookings INT,
    total_spent DECIMAL(10, 2),
    preferred_language NVARCHAR(50),
    referral_code NVARCHAR(50),
    account_status NVARCHAR(50)
);

SELECT * FROM airbnb.customer_dim;
