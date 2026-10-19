-- Project 4: Executive E-Commerce & Regional Profitability Analytics
-- Description: Establishes a relational table schema matching the Python data pipeline output,
-- ensuring strict data typing for dimensions, financial metrics, and calculated ratios.

DROP TABLE IF EXISTS ecommerce_transactions;

CREATE TABLE ecommerce_transactions (
    order_id VARCHAR(50) PRIMARY KEY,
    order_date DATE NOT NULL,
    ship_date DATE NOT NULL,
    ship_mode VARCHAR(50),
    region VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    sub_category VARCHAR(50) NOT NULL,
    sales DECIMAL(10,2) NOT NULL,
    quantity INT NOT NULL,
    discount DECIMAL(4,2) NOT NULL,
    profit DECIMAL(10,2) NOT NULL,
    profit_margin_ratio DECIMAL(6,4),
    shipping_days INT
);
