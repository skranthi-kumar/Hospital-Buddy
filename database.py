import sqlite3

# Create connection and cursor
conn = sqlite3.connect('hospital.db')
c = conn.cursor()

# Create tables if not exist
def create_tables():
    c.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT
        )
    ''')
    conn.commit()

# Add a new patient
def add_new_patient(name, age, gender):
    c.execute('''
        INSERT INTO patients (name, age, gender) VALUES (?, ?, ?)
    ''', (name, age, gender))
    conn.commit()

# Get all patients
def get_all_patients():
    c.execute('SELECT * FROM patients')
    return c.fetchall()
