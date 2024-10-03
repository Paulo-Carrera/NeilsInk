-- Create the database
CREATE DATABASE appointments_db;

-- Connect to the database
\c appointments_db;

-- Create the tables

-- Table for availability time slots
CREATE TABLE availability (
    id SERIAL PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    -- Consider adding a description for clarity
    description TEXT
);

-- Table for storing appointment details
CREATE TABLE appointment (
    id SERIAL PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL,
    appointment_time TIMESTAMP NOT NULL,
    description TEXT,
    image_file VARCHAR(100),
    payment_method VARCHAR(50),
    payment_amount DECIMAL(10, 2),
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'confirmed', 'cancelled')) -- Default status for appointments
);

-- Create indexes for improved query performance
CREATE INDEX idx_appointment_time ON appointment(appointment_time);
CREATE INDEX idx_availability_time ON availability(start_time, end_time);
