CREATE DATABASE IF NOT EXISTS company_revenue;
USE company_revenue;

CREATE TABLE company_revenue_data(
    `rank` int PRIMARY KEY,
    `name` varchar(255),
    industry varchar(255),
    revenue_usd_millions int,
    revenue_growth float,
    employees int,
    headquarters varchar(255)
);