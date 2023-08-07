DROP VIEW IF EXISTS product_sales CASCADE;

CREATE VIEW product_sales AS
SELECT c.sku, c.order_no, c.qty, (c.qty * p.price) AS total_price,
    extract(YEAR FROM o.date) AS year,
    extract(MONTH FROM o.date) AS month,
    extract(DAY FROM o.date) AS day_of_month,
    extract(DOW FROM o.date) AS day_of_week,
    split_part(cust.address, ',', -1) AS city
FROM contains c
JOIN pay py ON c.order_no = py.order_no
JOIN product p ON c.sku = p.sku
JOIN "order" o ON c.order_no = o.order_no
JOIN customer cust ON py.cust_no = cust.cust_no;
