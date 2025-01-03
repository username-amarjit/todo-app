# To-Do List API - Task List

## 1. **Set Up Project Structure**
   - Choose programming language and framework (e.g., Node.js with Express, Python with Flask/Django).
> I will use Django Rest Framework for this project. Done
   - Initialize a new project using your chosen framework.
> Done
   - Set up the basic folder structure (e.g., `src`, `controllers`, `models`, `routes`).
> Using django's url,view,service,serialzer,model strcuture. Done
   
## 2. **Install Dependencies**
   - Install necessary dependencies like `express` (for Node.js), `flask` (for Python), or equivalent for the chosen stack.
> Done
   - Install libraries for authentication (e.g., `jsonwebtoken`, `bcrypt` for Node.js).
> Encryption is already given by Django and using simpleJWT for authentication.
   - Install libraries for database interactions (e.g., `mongoose` for MongoDB or `sequelize` for SQL-based databases).
> Using SQLITE3 for this so by default no configuration needed in django.

## 3. **Database Setup**
   - Set up a database (e.g., MongoDB, PostgreSQL, MySQL).
> alerady set up SQLITE.
   - Design the schema for users and tasks:
     - **Users Table**: `id`, `username`, `password_hash`
> Using Default User model in Django.
     - **Tasks Table**: `id`, `title`, `description`, `status`, `created_at`, `updated_at`, `user_id`
> Created. Done

## 4. **Implement Authentication**
   - Create a user registration route to add users to the database.
> Done
   - Create a user login route that generates and returns a JWT token.
> Done
   - Implement a middleware to validate the JWT token for protected routes.
> Done

## 5. **CRUD Operations for Tasks**
   - **Create Task**: Implement a route to create a new task for a user.
> Done
   - **Get Tasks**: Implement a route to get all tasks (with optional filters by status).
> Done
   - **Get Task Details**: Implement a route to get details of a specific task.
> Done
   - **Update Task**: Implement a route to update the status of a task.
> Done
   - **Delete Task**: Implement a route to delete a task.
> Done

## 6. **Add Status Filters for Tasks**
   - Implement a feature to filter tasks based on their status (e.g., "completed", "pending", etc.).
> Done

## 7. **Validation and Error Handling**
   - Validate incoming data (e.g., check if task title is provided, if password meets criteria).
> Done
   - Implement error handling for common errors (e.g., invalid JWT, task not found, etc.).
> Done

<!-- ## 8. **Testing**
   - Write unit tests for authentication logic (e.g., registration, login).
   - Write integration tests for task CRUD operations.
   - Use tools like `jest` or `mocha` for testing.

## 9. **Documentation**
   - Write API documentation to explain available routes and authentication method.
   - Include examples of request bodies and responses.

## 10. **Deploy the API**
   - Deploy the API to a cloud provider (e.g., Heroku, AWS, DigitalOcean).
   - Set up environment variables (e.g., database URL, JWT secret) for production.
   
## 11. **Security Enhancements**
   - Ensure that passwords are securely hashed and salted.
   - Implement rate limiting or brute-force protection for login attempts.
   - Use HTTPS for secure communication in production.

## 12. **Optimize and Refactor Code**
   - Refactor the code for clarity and maintainability.
   - Optimize database queries to handle large amounts of data efficiently. -->
