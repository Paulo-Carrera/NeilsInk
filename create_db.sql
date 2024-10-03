-- Create the database
CREATE DATABASE appointments_db;

-- Connect to the database
\c appointments_db;

-- Create the tables
CREATE TABLE availability (
    id SERIAL PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL
);

CREATE TABLE appointment (
    id SERIAL PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL,
    appointment_time TIMESTAMP NOT NULL,
    description TEXT,
    image_file VARCHAR(100),
    payment_method VARCHAR(50),
    payment_amount DECIMAL(10, 2)
);
