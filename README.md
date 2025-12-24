# Docker Compose – Multi-Container Application

This project demonstrates how to deploy a **multi-container microservice application** using **Docker Compose**, enabling seamless orchestration of application and database services with minimal configuration.

---

## 📌 Project Overview

The application consists of:
- A **Python-based web application**
- A **MongoDB database**
- Container orchestration handled by **Docker Compose**
- Persistent storage using Docker volumes
- Health checks and service dependency handling

This setup closely resembles real-world **DevOps and microservice deployment patterns** used in enterprise environments.

---

## 🧱 Architecture

Client → Web Application (Python / Flask) → MongoDB Database

---

## 🛠 Tech Stack

| Component | Technology |
|--------|------------|
| Containerization | Docker |
| Orchestration | Docker Compose |
| Backend | Python / Flask |
| Database | MongoDB |
| Image Registry | Docker Hub |
| OS | Linux |

---

## 📂 Project Structure

```
.
├── docker-compose.yml
├── app/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── ...
├── README.md
```

---

## ⚙️ Key Features

- Multi-container orchestration using Docker Compose
- Environment variable–based configuration
- Service dependency handling (`depends_on`)
- Health checks for application readiness
- Persistent MongoDB storage using volumes
- Application image pulled directly from Docker Hub
- One-command deployment

---

## 🚀 How to Run the Application

### 1️⃣ Prerequisites
- Docker installed
- Docker Compose installed

### 2️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd <repo-folder>
```

### 3️⃣ Start the Application
```bash
docker-compose up -d
```

### 4️⃣ Verify Running Containers
```bash
docker ps
```

### 5️⃣ Access the Application
```
http://localhost:5000
```

---

## 🧪 Health Check Verification

Docker Compose ensures the application starts **only after the database is healthy**, improving reliability and startup consistency.

---

## 🧹 Stop & Cleanup

```bash
docker-compose down
```

To remove volumes:
```bash
docker-compose down -v
```

---

## 📈 DevOps Best Practices Followed

- Infrastructure as Code (IaC)
- Environment isolation
- Minimal manual intervention
- Production-like local setup
- Clean container lifecycle management

---

## 🔮 Future Enhancements

- Add Nginx as a reverse proxy
- Integrate CI/CD pipeline (Jenkins / GitHub Actions)
- Kubernetes migration using Helm
- Observability with Prometheus & Grafana

---

## 👨‍💻 Author

**Senthil Kumar R**  
DevOps Engineer | Docker | Kubernetes | AWS | Terraform | CI/CD

---

⭐ If you find this project useful, please give it a star!