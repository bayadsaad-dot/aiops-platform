# 🚀 AIOps Platform

An AI-powered IT Operations (AIOps) platform built to monitor infrastructure, servers, applications, and websites in real time.

The platform provides a centralized dashboard for monitoring system health, resource utilization, network performance, running processes, and incidents, helping IT teams detect issues before they become critical.

---

# 📸 Screenshots

> Add screenshots here after uploading them.

- Dashboard
- Assets
- Asset Details
- Alerts
- Website Monitoring

---

# ✨ Features

## 📊 Dashboard

- System overview
- CPU usage
- Memory usage
- Disk usage
- Active alerts
- Performance charts

## 🖥 Asset Management

- View all monitored assets
- Asset details
- Asset status
- Hardware information

## 📈 Performance Monitoring

- CPU History
- Memory History
- Disk History
- Network Speed
- Network Traffic
- Network Packets

## ⚙ Process Monitoring

- Top CPU Processes
- Top Memory Processes
- Running Processes Table

## 🌐 Website Monitoring

- Website availability
- HTTP status
- Response time
- Uptime monitoring

## 🚨 Alert Management

- Active alerts
- Alert severity
- Alert history

## 🔐 Authentication

- JWT Authentication
- Secure API access

---

# 🏗 System Architecture

```
Frontend (React + TypeScript)
            │
            ▼
      FastAPI Backend
            │
            ▼
      PostgreSQL Database
```

---

# 🛠 Tech Stack

## Frontend

- React
- TypeScript
- Material UI
- React Query
- Recharts
- React Router

## Backend

- FastAPI
- SQLAlchemy
- Alembic
- JWT Authentication
- PostgreSQL

## DevOps

- Docker
- Docker Compose

---

# 📂 Project Structure

```
aiops-platform/

├── backend/
│   ├── app/
│   ├── alembic/
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── Dockerfile
│
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/aiops-platform.git

cd aiops-platform
```

---

## Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 🐳 Run with Docker

```bash
docker compose up --build
```

---

# 📖 API Documentation

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# 📊 Main Dashboard

The dashboard provides:

- CPU Monitoring
- Memory Monitoring
- Disk Monitoring
- Network Monitoring
- Asset Overview
- Process Monitoring
- Alerts

---

# 🔮 Future Improvements

- Real-time WebSocket Monitoring
- Email Notifications
- Role-Based Access Control
- Dark Mode
- Export Reports
- CI/CD Pipeline

---

# 👨‍💻 Contributors

- Saad Byad
- Project Team

---

# 📄 License

This project is developed for educational and portfolio purposes.