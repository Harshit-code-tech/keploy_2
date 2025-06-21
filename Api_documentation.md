## API Documentation

This API allows you to create, read, update, and delete events.

---

### 1. List All Events

- **Endpoint:** `/api/events`
- **Method:** `GET`
- **Request Body:** _None_
- **Response:**
    ```json
    [
      {
        "id": 1,
        "title": "Meeting",
        "description": "Team sync at 10am"
      },
      ...
    ]
    ```

---

### 2. Create a New Event

- **Endpoint:** `/api/events`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
      "title": "Meeting",
      "description": "Team sync at 10am"
    }
    ```
- **Response:**  
    ```json
    {
      "id": 2,
      "title": "Meeting",
      "description": "Team sync at 10am"
    }
    ```
- **Notes:**  
  - `title` is required.

---

### 3. Update an Event

- **Endpoint:** `/api/events/<id>`
- **Method:** `PUT`
- **Request Body:**
    ```json
    {
      "title": "Updated Meeting",
      "description": "New time"
    }
    ```
- **Response:**
    ```json
    {
      "id": 1,
      "title": "Updated Meeting",
      "description": "New time"
    }
    ```

---

### 4. Delete an Event

- **Endpoint:** `/api/events/<id>`
- **Method:** `DELETE`
- **Request Body:** _None_
- **Response:**  
    - HTTP Status: `204 No Content`

---

### Error Responses

- If a required field is missing (e.g., `title` on create), you will get:
    ```json
    {
      "error": "Title is required"
    }
    ```
    - HTTP Status: `400 Bad Request`

- If an event is not found, you will get:
    ```json
    {
      "message": "404 Not Found: Event not found"
    }
    ```
    - HTTP Status: `404 Not Found`

---

**Base URL:**  
`http://localhost:5000/`

---

**Example cURL Commands:**

- Create:  
    ```bash
    curl -X POST http://localhost:5000/api/events \
      -H "Content-Type: application/json" \
      -d '{"title": "Meeting", "description": "Team sync at 10am"}'
    ```
- List:  
    ```bash
    curl -X GET http://localhost:5000/api/events
    ```
- Update:  
    ```bash
    curl -X PUT http://localhost:5000/api/events/1 \
      -H "Content-Type: application/json" \
      -d '{"title": "Updated Meeting", "description": "New time"}'
    ```
- Delete:  
    ```bash
    curl -X DELETE http://localhost:5000/api/events/1
    ```
