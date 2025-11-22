##  ✅ DONE

| Features         | Dependencies |  
|------------------|---------|
| **CRUD operation on books**          |  |  
| **User Authentication**       |  |  
| **Forgot username or password** | |

## 🚧 IN PROGRESS
| Features         | Dependencies |  
|------------------|---------|
| **Data validation for the DB**          |  | 

## ⏭ NEXT PHASES
| Feature                             | What It Adds                                       | Dependencies                   |
| ----------------------------------- | -------------------------------------------------- | ------------------------------ |
| **Notes and Quotes**          |  |
| **Logic for the logout**          |  |
| **Borrow & Return Books**           | Let users issue and return books; track due dates  | new `BorrowRecord` model       |
| **Book Reviews & Ratings**          | Users can post reviews and rate books              | link to `User` & `Book` models |
| **Recommendations API**             | Suggest books based on favorites, genre, or author | logic or small ML module       |
| **Recently Added / Trending Books** | Sort by date added or popularity                   | MongoDB queries                |
| **Search API**                      | Search by title, author, or genre                  | MongoDB text index             |
| **Lazy loader**          |  |

## 🔐 SECRITY LAYER

| Feature                                    | What It Adds                                    | Dependencies                   |
| ------------------------------------------ | ----------------------------------------------- | ------------------------------ |
|**SMTP on sign up or login** | |
| **JWT Middleware**                         | Protect routes like `/add-book` or `/favorites` | `jsonwebtoken`                 |
| **Role-based Access Control (RBAC)**       | Distinguish admin vs user                       | add `role` field in User model |
| **Password Reset / Forgot Password**       | Realistic user flow                             | email or OTP service           |
| **Rate Limiting / Brute Force Protection** | Prevent abuse                                   | `express-rate-limit`           |



