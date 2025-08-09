# Cashbook Flask App

A simple cashbook web application built with Flask and MySQL.  
It allows you to add, view, and delete cashbook entries.

## Features

- Add new cashbook entries (date, description, amount, type)
- View all entries
- Delete entries
- Input validation and error handling

## Requirements

- Python 3.x
- MySQL server
- `mysql-connector-python` package
- Flask

## Setup

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd cashbook
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install flask mysql-connector-python
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

5. **Configure database credentials**

   Update the credentials in `models.py` if needed:
   ```python
   host='localhost',
   user='root',
   password='your_mysql_password',
   database='cashbook_db'
   ```

6. **Run the application**

   ```bash
   python controllers.py
   ```

7. **Access the app**

   Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

## File Structure

- `models.py` — Database operations
- `controllers.py` — Flask routes and app logic
- `templates/index.html` — Main HTML template

## Usage

- Add entries using the form.
- View all entries on the homepage.
- Delete entries using the delete button.

## License

MIT License

---

**Note:**  
Make sure your MySQL server is running and accessible with the credentials provided in