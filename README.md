# 🧾 Context Tracker – A Full-Stack Browser Activity Monitoring System

**Context Tracker** is a full-stack system that captures, processes, and visualizes real-time browser activity. From tracking tab behavior to AFK detection and scroll metrics, it delivers a comprehensive overview of digital engagement patterns. Ideal for personal productivity, wellness monitoring, or behavioral research.

---

## 🧠 Overview

Context Tracker seamlessly connects a browser extension with a scalable backend infrastructure to:

- Collect events like **page visits, scroll depth, time on page, and idle states**
- Process them through a **queue-backed ingestion pipeline**
- Store the data in a structured SQL database
- Present insights on an **interactive dashboard** using beautiful charts and tables

---

## 🔧 Core Features

| Module                | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| 🧭 Website Activity    | Logs URL, page title, scroll %, time spent, and inferred category           |
| 🛑 AFK Detection       | Tracks user inactivity using input events and flags idle periods            |
| 🧮 Data Aggregation    | Aggregates time spent per domain/category/page                              |
| 📈 Dashboard           | React-based visualizations for sessions, categories, and usage patterns     |
| 📦 Resilient Ingestion | Redis-backed job queue with async background workers                        |
| 🗄 PostgreSQL Storage  | Normalized schema for reliable long-term storage and querying               |
| 🔌 FastAPI Endpoints   | RESTful APIs to receive and retrieve activity events securely               |
| 🎛️ Modular Trackers   | Scroll tracking, idle state, and more — each built as pluggable modules     |
| 🧠 DSA Analytics       | Sliding window, top-K, and map-reduce patterns for efficient processing     |
| 🔐 Secure Extension    | Manifest v3 browser extension, HTTPS-only, CORS-restricted                  |

---

## 💻 Tech Stack

### 🧩 Frontend

- **Browser Extension**: JavaScript (ES6, Manifest v3)
- **Dashboard**: React + Vite (TSX)
- **Styling**: Tailwind CSS
- **Charts**: Chart.js / Recharts

### 🛠 Backend

- **API**: FastAPI + Pydantic
- **Ingestion**: Redis + Python background workers
- **ORM**: SQLAlchemy

### 🗃 Database

- **Storage**: PostgreSQL
- **Management**: pgAdmin / DBeaver

### 🧰 DevOps

- Python venv
- Git + GitHub
- Docker (planned)

---

## 📊 Dashboard Visuals

- Time Spent by Category (Bar Chart) ✅
- Scroll Behavior (Table) ✅
- AFK Timeline ✅
- Top Domains & Titles ✅
- Category Sunburst Chart
---

## 🚧 Roadmap

- Auth system + private dashboards
- App usage tracking outside the browser
- Email-based productivity reports
- Gamification features (XP, streaks, etc.)
- Custom alerts (e.g., "3+ hrs of YouTube")

---

## 📦 Use Cases

- Personal time auditing
- Digital wellbeing monitoring
- Online behavior research
- Freelance and remote work time tracking
