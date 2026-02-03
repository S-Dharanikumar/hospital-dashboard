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
@app.get("/kpi/total-admissions")
def total_admissions():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM patients")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return {"total_admissions": count}
@app.get("/kpi/emergency-vs-scheduled")
def emergency_vs_scheduled():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT emergency, COUNT(*) 
        FROM patients 
        GROUP BY emergency
    """)
    data = cur.fetchall()
    cur.close()
    conn.close()

    result = {
        "emergency": 0,
        "scheduled": 0
    }

    for row in data:
        if row[0]:
            result["emergency"] = row[1]
        else:
            result["scheduled"] = row[1]

    return result
@app.get("/kpi/outcomes")
def patient_outcomes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT outcome, COUNT(*)
        FROM patients
        GROUP BY outcome
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return {outcome: count for outcome, count in rows}
@app.get("/kpi/cost-by-department")
def cost_by_department():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT department, SUM(cost)
        FROM patients
        GROUP BY department
    """)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return {dept: float(cost) for dept, cost in rows}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

