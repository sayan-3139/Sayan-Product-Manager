# Sayan Product Manager

A full-stack product management application built to manage inventory and product information through a simple, interactive dashboard.

## Features

- View all products
- Add new products
- Search products by ID, name, or description
- Update product information
- Delete products
- Store product data in PostgreSQL
- Responsive React user interface

## Technology Stack

- **Frontend:** React.js, HTML, CSS, JavaScript
- **Backend:** Python, FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **API Documentation:** FastAPI Swagger UI

## Project Structure

```text
Sayan-Product-Manager/
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── TaglineSection.js
│   │   └── TaglineSection.css
│   └── package.json
├── main.py
├── database.py
├── database_models.py
├── models.py
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sayan-3139/Sayan-Product-Manager.git
cd Sayan-Product-Manager
```

### 2. Set up the Python backend

Create and activate a virtual environment, then install the required Python packages.

```bash
python -m venv myenv
```

On Windows PowerShell:

```powershell
.\myenv\Scripts\Activate.ps1
```

Install dependencies using your project's requirements file, once created:

```bash
pip install -r requirements.txt
```

Configure PostgreSQL and update the database connection settings before starting the backend.

### 3. Start the FastAPI server

```bash
python -m uvicorn main:app --reload
```

Backend API: http://127.0.0.1:8000

Interactive API documentation: http://127.0.0.1:8000/docs

### 4. Start the React frontend

Open a second terminal:

```bash
cd frontend
npm install
npm start
```

Frontend: http://localhost:3000

## Future Improvements

- User authentication and authorization
- Improved input validation and error handling
- Product categories and inventory alerts
- Deployment to a cloud platform

## Author

**Sayan Maiti**

GitHub: [sayan-3139](https://github.com/sayan-3139)

---

This project was developed for learning and practicing full-stack web development using React, FastAPI, and PostgreSQL.
