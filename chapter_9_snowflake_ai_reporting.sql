SELECT
	product_name,
	SUM(revenue) AS total_sales,
	AVG(revenue) AS avg_sales,
	COUNT(order_id) AS total_orders
FROM sales_data
GROUP BY product_name
ORDER BY total_sales DESC;
