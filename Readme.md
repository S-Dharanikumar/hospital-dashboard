# Hospital Resource Utilization & Patient Outcomes Dashboard

## 📌 Problem Statement
Hospitals often face challenges in optimizing resource utilization due to lack of real-time insights into admissions, emergency cases, costs, and patient outcomes. This project provides a data-driven analytics solution to support hospital administrators in decision-making.

---

## 🧠 Solution Overview
This project implements an end-to-end analytics system that:
- Stores hospital data in a relational database
- Computes key performance indicators (KPIs)
- Visualizes insights using an interactive dashboard

---

## 🏗 Architecture
CSV Data → PostgreSQL → FastAPI Backend → Power BI Dashboard

---

## 📊 Key Features
- Admissions analysis by department
- Emergency vs scheduled case tracking
- Patient outcome distribution
- Cost analysis by department
- Average Length of Stay (ALOS) KPI
- Interactive filters for department and outcome

---

## 📈 KPIs Implemented
- Average Length of Stay (ALOS)
- Total Admissions
- Emergency vs Scheduled Cases
- Cost per Department
- Patient Outcomes Distribution

---

## 🛠 Tech Stack
- **Database:** PostgreSQL  
- **Backend:** FastAPI (Python)  
- **BI Tool:** Power BI Desktop  
- **Language:** Python  
- **Data Source:** CSV (simulated hospital data)

---

## 🚀 Backend API Endpoints
| Endpoint | Description |
|--------|------------|
| `/` | API health check |
| `/patients` | Get all patient records |
| `/kpi/alos` | Average Length of Stay |
| `/kpi/total-admissions` | Total admissions |
| `/kpi/emergency-vs-scheduled` | Emergency vs scheduled cases |
| `/kpi/outcomes` | Patient outcomes |
| `/kpi/cost-by-department` | Cost by department |

---

## 📊 Dashboard
The dashboard is built using **Power BI Desktop** and demonstrates:
- Department-wise admissions
- Emergency load
- Cost distribution
- Patient outcomes
- Average Length of Stay

> Dashboard is demonstrated via screen-recorded demo video.

---

## 🎥 Demo Video
Google Drive link (public):

---

👤 Author

Dharanikumar S
