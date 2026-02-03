import pandas as pd
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="hospital_db",
    user="postgres",
    password="postgres123"
)

# Read CSV file



cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO patients (
            patient_id, age, gender, department,
            admission_date, discharge_date,
            outcome, cost, emergency
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        tuple(row)
    )

conn.commit()
cursor.close()
conn.close()

print("✅ Data loaded successfully into hospital_db")
