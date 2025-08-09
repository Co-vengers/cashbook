# Cashbook Flask App

A simple cashbook web application built with Flask and MySQL.  
It allows you to add, view, and delete cashbook entries.

## Features

- Add new cashbook entries (date, description, amount, type)
- View all entries
- Delete entries
- Input validation and error handling
- Flash messages for user feedback
- Environment variable support for configuration

## Requirements

- Python 3.x
- MySQL server
- `mysql-connector-python` package
- Flask
- `python-dotenv` package

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/Co-vengers/cashbook
   cd cashbook
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install flask mysql-connector-python python-dotenv
   ```

4. **Set up the MySQL database**

   ```sql
   CREATE DATABASE IF NOT EXISTS cashbook_db;

   USE cashbook_db;

   CREATE TABLE IF NOT EXISTS entries (
       id INT AUTO_INCREMENT PRIMARY KEY,
       date DATE NOT NULL,
       description VARCHAR(255) NOT NULL,
       amount DECIMAL(10, 2) NOT NULL,
       type ENUM('income', 'expense') NOT NULL
   );
   ```

5. **Configure environment variables**

   Create a `.env` file in the project root with the following content:

   ```
   db_host=localhost
   db_user=root
   db_password=your_mysql_password
   db_name=cashbook_db
   flask_secret_key=your_secret_key
   ```

6. **Run the application**

   ```bash
   python app.py
   ```

7. **Access the app**

   Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## File Structure

- `models.py` — Database operations
- `controllers.py` — Flask routes and app logic
- `templates/index.html` — Main HTML template
- `.env` — Environment variables for configuration

## Usage

- Add entries using the form.
- View all entries on the homepage.
- Delete entries using the delete button.

## License

MIT License

---

**Note:**  
Make sure your MySQL server is running and accessible with the credentials provided in your `.env