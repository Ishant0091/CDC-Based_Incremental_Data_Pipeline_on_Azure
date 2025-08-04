CREATE PROCEDURE airbnb.sp_aggregate_booking_data
AS
BEGIN
    TRUNCATE TABLE airbnb.booking_customer_aggregation_fact;

    INSERT INTO airbnb.booking_customer_aggregation_fact
    SELECT 
        c.country,
        COUNT_BIG(*) AS total_bookings,
        SUM(ISNULL(b.amount, 0)) AS total_amount,
        MAX(b.booking_date) AS last_booking_date
    FROM 
        airbnb.bookings_dim b
    JOIN 
        airbnb.customer_dim c ON b.customer_id = c.customer_id
    GROUP BY 
        c.country;
END;

EXEC [airbnb].[sp_aggregate_booking_data];

SELECT * FROM airbnb.booking_customer_aggregation_fact;
