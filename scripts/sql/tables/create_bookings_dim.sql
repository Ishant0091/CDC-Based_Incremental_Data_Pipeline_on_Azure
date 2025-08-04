CREATE TABLE airbnb.bookings_dim (
    booking_id NVARCHAR(100),
    property_id NVARCHAR(100),
    customer_id INT,
    owner_id NVARCHAR(100),
    check_in_date DATE,
    check_out_date DATE,
    booking_date DATETIME,
    amount FLOAT,
    currency NVARCHAR(10),
    city NVARCHAR(100),
    country NVARCHAR(100),
    full_address NVARCHAR(255),
    stay_duration BIGINT,
    booking_year INT,
    booking_month INT,
    time_stamp DATETIME
);

SELECT * FROM airbnb.bookings_dim;
