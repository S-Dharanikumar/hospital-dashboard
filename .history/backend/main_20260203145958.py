from fastapi import FastAPI
import psycopg2

app = FastAPI(title="Hospital Resource Dashboard API")

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="hospital_db",
        user="postgres",
        password="postgres123"
    )

@app.get("/")
def root():
    return {"message": "Hospital API is running"}

@app.get("/patients")
def get_patients():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients ORDER BY patient_id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

@app.get("/kpi/alos")
def average_length_of_stay():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT AVG(discharge_date - admission_date)
        FROM patients
    """)
    alos = cur.fetchone()[0]
    cur.close()
    conn.close()
    return {"average_length_of_stay_days": float(alos)}
