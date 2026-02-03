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
df = pd.read_csv(
    r"C:\Users\dhara\OneDrive\Desktop\hospital-dashboard\sample_data\hospital_data.csv"
)



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
