# Backend Authentication System

This project implements an authentication system using FastAPI, SQLModel, and JWT tokens. It includes features such as password hashing, token generation, middleware for token verification, and role-based access control.

## Project Structure

```
backend
├── auth
│   ├── __init__.py
│   ├── dependencies.py
│   ├── middleware.py
│   ├── password.py
│   ├── routes.py
│   ├── tokens.py
│   └── roles.py
├── .env.example
├── .gitignore
├── database.py
├── models
│   ├── __init__.py
│   └── user.py
├── main.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd backend
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Copy `.env.example` to `.env` (`Copy-Item .env.example .env` in PowerShell), then set your own database password and generate a secret with `python -c "import secrets; print(secrets.token_urlsafe(32))"`. Set `CORS_ORIGINS` to the comma-separated origins of your frontend.
   Keep `.env` private; Git ignores it. Share `.env.example`, never your populated `.env`.

5. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

## Usage

- **Sign Up**: Send `username`, `email`, and `password` as JSON to `/auth/signup`.
- **Login**: Send `username` and `password` as JSON to `/auth/login` to receive a JWT token.
- **Access Protected Routes**: Include the token in the `Authorization: Bearer <token>` header for `/auth/users/me` and `/auth/users/me/role`.

## Key Features

- **Password Hashing**: Securely hashes passwords using bcrypt.
- **JWT Tokens**: Generates and verifies JWT tokens for user sessions.
- **Middleware**: Protects routes by verifying JWT tokens.
- **Role-Based Access Control**: Manages user roles and permissions for accessing specific endpoints.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.