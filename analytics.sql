
-- 6.1)

SELECT sku, city, year, month, day_of_month, day_of_week, SUM(qty) AS total_quantity, SUM(total_price) AS total_sales
FROM product_sales
WHERE year = 2022
GROUP BY ROLLUP(sku, city, year, month, day_of_month, day_of_week);


-- 6.2)

SELECT year, month, day_of_week, AVG(total_price) AS average_daily_sales
FROM product_sales
WHERE year = 2022
GROUP BY ROLLUP(year, month, day_of_week);
