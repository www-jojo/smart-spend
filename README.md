# SmartSpend

SmartSpend is a personal finance analytics platform built with Flask, SQLite,
and vanilla web technologies.

The project starts as a clean Flask application, then grows feature by feature
into a portfolio-ready system for expense tracking, analytics, and future
machine learning experiments.

## Current Milestone

- Flask application entry point
- Reusable base template
- Home page
- Static CSS and JavaScript folders
- Project folders for future backend, data, and testing work

## Project Structure

```text
smart-spend/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   └── home.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
├── models/
├── routes/
├── services/
├── utils/
├── tests/
└── instance/
```

## Run Locally

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```
