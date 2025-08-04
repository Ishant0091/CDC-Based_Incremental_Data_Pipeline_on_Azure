CREATE TABLE airbnb.booking_customer_aggregation_fact
WITH (DISTRIBUTION = ROUND_ROBIN)
AS
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

SELECT * FROM airbnb.booking_customer_aggregation_fact;
