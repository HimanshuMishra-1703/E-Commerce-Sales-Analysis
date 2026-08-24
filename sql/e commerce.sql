SELECT *
FROM `order details`;


SELECT COUNT(*) AS total_records
FROM `order details`;


SELECT DISTINCT Category
FROM `order details`;


SELECT DISTINCT `Sub-Category`
FROM `order details`;



SELECT
    SUM(Amount) AS total_sales,
    SUM(Profit) AS total_profit,
    SUM(Quantity) AS total_quantity
FROM `order details`;



SELECT
    Category,
    SUM(Amount) AS total_sales,
    SUM(Profit) AS total_profit,
    SUM(Quantity) AS total_quantity
FROM `order details`
GROUP BY Category
ORDER BY total_sales DESC;


SELECT
    `Sub-Category`,
    SUM(Amount) AS total_sales,
    SUM(Profit) AS total_profit,
    SUM(Quantity) AS total_quantity
FROM `order details`
GROUP BY `Sub-Category`
ORDER BY total_sales DESC;


SELECT
    `Sub-Category`,
    SUM(Amount) AS total_sales
FROM `order details`
GROUP BY `Sub-Category`
ORDER BY total_sales DESC
LIMIT 3;



SELECT
    `Sub-Category`,
    SUM(Profit) AS total_profit
FROM `order details`
GROUP BY `Sub-Category`
ORDER BY total_profit DESC
LIMIT 3;



SELECT
    `Sub-Category`,
    SUM(Profit) AS total_profit
FROM `order details`
GROUP BY `Sub-Category`
ORDER BY total_profit DESC;



SELECT
    `Sub-Category`,
    SUM(Amount) AS total_sales,
    SUM(Profit) AS total_profit
FROM `order details`
GROUP BY `Sub-Category`
HAVING SUM(Profit) < 0
ORDER BY total_profit ASC;



SELECT
    `Sub-Category`,
    SUM(Amount) AS total_sales
FROM `order details`
GROUP BY `Sub-Category`
HAVING SUM(Amount) > 30000
ORDER BY total_sales DESC;


SELECT
    `Sub-Category`,
    SUM(Amount) AS total_sales,
    SUM(Profit) AS total_profit
FROM `order details`
GROUP BY `Sub-Category`
HAVING SUM(Amount) > 30000
   AND SUM(Profit) < 0
ORDER BY total_sales DESC;


SELECT
    `Sub-Category`,
    SUM(Amount) AS total_sales,
    SUM(Profit) AS total_profit,
    (SUM(Profit) / NULLIF(SUM(Amount), 0)) * 100 AS profit_margin
FROM `order details`
GROUP BY `Sub-Category`
ORDER BY profit_margin DESC;



SELECT
    Category,
    SUM(Amount) AS total_sales,
    SUM(Profit) AS total_profit,
    (SUM(Profit) / NULLIF(SUM(Amount), 0)) * 100 AS profit_margin
FROM `order details`
GROUP BY Category
ORDER BY profit_margin DESC;


SELECT
    `Sub-Category`,
    SUM(Amount) AS total_sales,
    SUM(Quantity) AS total_quantity,
    SUM(Amount) / NULLIF(SUM(Quantity), 0) AS sales_per_unit
FROM `order details`
GROUP BY `Sub-Category`
ORDER BY sales_per_unit DESC;