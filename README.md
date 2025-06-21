# Event Manager

A simple event management web application built with Flask (Python) for the backend and vanilla JavaScript for the frontend.

## Features

- Create, view, update, and delete events.
- RESTful API endpoints.
- SQLite database integration.
- Responsive Bootstrap UI.

## API Endpoints

| Method | Endpoint              | Description                | Request Body (JSON)                        | Response (JSON)                                      |
|--------|-----------------------|----------------------------|--------------------------------------------|------------------------------------------------------|
| GET    | `/api/events`         | List all events            | -                                          | `[{"id":1,"title":"...","description":"..."}]`       |
| POST   | `/api/events`         | Create a new event         | `{ "title": "...", "description": "..." }` | Created event object                                 |
| PUT    | `/api/events/<id>`    | Update an event by ID      | `{ "title": "...", "description": "..." }` | Updated event object                                 |
| DELETE | `/api/events/<id>`    | Delete an event by ID      | -                                          | 204 No Content                                       |

### Sample Requests

**Create Event**
```bash
curl -X POST http://localhost:5000/api/events \
  -H "Content-Type: application/json" \
  -d '{"title": "Meeting", "description": "Team sync at 10am"}'
```

**Get Events**
```bash
curl -X GET http://localhost:5000/api/events \
  -H "Content-Type: application/json"
```

**Update Event**
```bash
curl -X PUT http://localhost:5000/api/events/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Meeting", "description": "New time"}'
```

**Delete Event**
```bash
curl -X DELETE http://localhost:5000/api/events/1 \
  -H "Content-Type: application/json"
```

## Database

- **Type:** SQLite
- **Integration:** Using Flask-SQLAlchemy ([app/extensions.py](app/extensions.py))
- **File:** `instance/database.db` (auto-created)


## Requirements

- Python 3.7+
- Flask
- Flask-SQLAlchemy

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/keploy_2.git
    cd keploy_2
    ```
2. **Install dependencies:**
    ```bash
    pip install flask flask_sqlalchemy
    ```
3. **Run the server:**
    ```bash
    python run.py
    ```
4. **Open your browser:**  
   Visit [http://localhost:5000/](http://localhost:5000/)

## How to Run the Frontend Locally

The frontend is served automatically by Flask at the root URL (`/`).  
Open [http://localhost:5000/](http://localhost:5000/) in your browser.

## Project Structure

```
keploy_2/
├── run.py
├── instance/
│   └── database.db
├── templates/
│   └── index.html
├── static/
│   └── main.js
└── app/
    ├── config.py
    ├── routes.py
    ├── __init__.py
    ├── extensions.py
    └── models.py
```

## API Documentation

See [API.md](Api_documentation.md) for full API details.
