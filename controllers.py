from flask import Flask, request, render_template, redirect, flash
from models import Database
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('flask_secret_key')  # Required for flashing messages
db = Database()

@app.route('/')
def index():
    entries = db.get_entries()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    date = request.form.get('date')
    description = request.form.get('description')
    amount = request.form.get('amount')
    entry_type = request.form.get('type')

    # Input validation
    if not date or not description or not amount or not entry_type:
        flash('All fields are required!')
        return redirect('/')

    try:
        # Assuming amount should be a float
        amount = float(amount)
        db.add_entry(date, description, amount, entry_type)
        flash('Entry added successfully!')
    except ValueError:
        flash('Invalid amount. Please enter a numeric value.')
    except Exception as e:
        flash(f'An error occurred: {str(e)}')

    return redirect('/')

@app.route('/delete/<int:entry_id>', methods=['POST'])
def delete_entry(entry_id):
    db.delete_entry(entry_id)
    return redirect('/')

@app.teardown_appcontext
def close_db(error):
    db.close()

if __name__ == '__main__':
    app.run(debug=True)