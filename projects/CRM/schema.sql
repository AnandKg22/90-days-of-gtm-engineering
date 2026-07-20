-- PostgreSQL CRM Database Replica Schema
CREATE TABLE IF NOT EXISTS companies (
    id SERIAL PRIMARY KEY,
    crm_id VARCHAR(100) UNIQUE,
    name VARCHAR(255) NOT NULL,
    domain VARCHAR(255),
    employee_count INT,
    annual_revenue NUMERIC(12,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    crm_id VARCHAR(100) UNIQUE,
    company_id INT REFERENCES companies(id),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS deals (
    id SERIAL PRIMARY KEY,
    crm_id VARCHAR(100) UNIQUE,
    company_id INT REFERENCES companies(id),
    name VARCHAR(255) NOT NULL,
    stage VARCHAR(100) NOT NULL,
    amount NUMERIC(12,2),
    close_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
