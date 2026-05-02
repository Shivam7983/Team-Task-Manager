# 🚀 Team Task Manager (Full Stack Web App)

A full-stack Task Management System built using **FastAPI, SQLAlchemy, and Vanilla JS frontend**.  
It supports authentication, project management, task tracking, and dashboard analytics.

---

## ✨ Features
- 🔐 JWT Authentication (Login / Signup)
- 👥 Project & Team Management
- 📝 Task Creation & Assignment
- 📊 Dashboard Analytics
- ⏰ Overdue Task Tracking
- 🔒 Role-Based Access Control

---

## 🛠️ Tech Stack

**Backend**
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

**Frontend**
- HTML
- CSS
- JavaScript

**Database**
- SQLite (Dev)
- PostgreSQL (Prod)

---

## 📁 Project Structure

backend/
│── main.py
│── models.py
│── schemas.py
│── crud.py
│── database.py
│── config.py

frontend/
│── index.html
│── style.css
│── scripts.js

---

## ⚙️ Local Setup

### 1️⃣ Clone Repository
git clone https://github.com/your-username/task-manager.git
cd task-manager

---

### 2️⃣ Backend Setup

cd backend
pip install -r requirements.txt

Run server:
uvicorn main:app --reload

Backend runs at:
http://127.0.0.1:8000

API Docs:
http://127.0.0.1:8000/docs

---

### 3️⃣ Frontend Setup

Option 1:
Open index.html directly in browser

Option 2 (Recommended):
cd frontend
python -m http.server 5500

Open:
http://localhost:5500

---

## 🔐 Environment Variables

Create .env file:

SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///./test.db

---

## 📡 API Endpoints

Authentication:
- POST /signup
- POST /token

Projects:
- POST /projects/
- POST /projects/{id}/add-member

Tasks:
- POST /tasks/
- PATCH /tasks/{id}/status

Dashboard:
- GET /dashboard/

---

## 🚀 Deployment Guide

### 🔵 Backend Deployment (Render)

1. Push code to GitHub
2. Go to https://render.com
3. Create New Web Service
4. Connect GitHub repo

Build Command:
pip install -r requirements.txt

Start Command:
uvicorn main:app --host 0.0.0.0 --port 10000

Add Environment Variables:
- SECRET_KEY
- DATABASE_URL

---

### 🟣 Backend Deployment (Railway)

1. Go to https://railway.app
2. New Project → Deploy from GitHub
3. Add variables:
   - SECRET_KEY
   - DATABASE_URL

Start Command:
uvicorn main:app --host 0.0.0.0 --port $PORT

---

### 🌐 Frontend Deployment

Option 1: Netlify
- Drag & drop frontend folder

Option 2: Vercel
- Import GitHub repo

Option 3: GitHub Pages

---

## 🧠 Future Improvements
- React frontend upgrade
- WebSocket real-time updates
- Notifications system
- PostgreSQL production migration
- Docker support

---

## 👨‍💻 Author
Full Stack Developer Project

---

## ⭐ Support
If you like this project:
- ⭐ Star repo
- 🍴 Fork it
- 🚀 Share it
