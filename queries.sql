--A)
SELECT c.cust_no, c.name FROM customer c
JOIN pay p ON c.cust_no = p.cust_no
GROUP BY c.cust_no, c.name
HAVING SUM(p.order_no) = (
     SELECT MAX(total_orders)
     FROM (
      SELECT SUM(pay.order_no) AS total_orders
      FROM customer
      JOIN pay ON customer.cust_no = pay.cust_no
      GROUP BY customer.cust_no
  ) as SUB
);


--B)
SELECT e.name FROM employee e
JOIN process pr ON e.ssn = pr.ssn
JOIN (
    SELECT order_no
    FROM "order"
    WHERE EXTRACT(YEAR FROM date) = 2022
) o ON pr.order_no = o.order_no
 GROUP BY e.name
 HAVING COUNT( pr.order_no) = (
     SELECT COUNT( order_no) FROM "order"
     WHERE EXTRACT(YEAR FROM date) = 2022
);

--C)
SELECT EXTRACT(MONTH FROM o.date) AS month, COUNT(*) AS unpaid_orders
FROM "order" o
LEFT JOIN pay p ON o.order_no = p.order_no
WHERE EXTRACT(YEAR FROM o.date) = 2022 AND p.order_no IS NULL
GROUP BY EXTRACT(MONTH FROM o.date)
ORDER BY EXTRACT(MONTH FROM o.date);