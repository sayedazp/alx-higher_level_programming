-- create database, use it, create a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS 
cities (id INT UNIQUE NOT NULL AUTO_INCREMENT,
name VARCHAR(256) NOT NULL,
state_id NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id));