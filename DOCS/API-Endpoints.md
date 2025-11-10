# 📚 Library Management API Routes

This document lists all current API endpoints for **User Authentication** and **Book CRUD Operations**.

---

## 🧑‍💻 User Authentication Routes

| Endpoint         | Method | Description              | Request Body Example |
|------------------|---------|--------------------------|----------------------|
| `/signup`        | POST    | Register a new user      | `{ "username": "JohnDoe", "email": "john@example.com", "password": "123456" }` |
| `/login`         | POST    | Authenticate user login  | `{ "email": "john@example.com", "password": "123456" }` |
| `/users`         | GET     | Get list of all users    | — |

---

## 📘 Book Management Routes

| Endpoint         | Method | Description                | Request Body Example / Query Params |
|------------------|---------|----------------------------|-------------------------------------|
| `/add-book`      | POST    | Add a new book             | `{ "title": "The Great Gatsby", "author": "F. Scott Fitzgerald" }` |
| `/get-books`     | GET     | Get list of all books      | — |
| `/get-book`      | GET     | Get a single book by title | Query: `/get-book?title=The%20Great%20Gatsby` |

---

### 🧠 Notes

- All routes are prefixed by their respective blueprints:  
  - **User routes** → handled by `user_bp`  
  - **Book routes** → handled by `book_bp`
- If you ever add more operations (update/delete), continue following this structure for consistency.

