# MovieApp — Backend API

FastAPI backend for **MovieApp**, a movie reviewing app built with Flutter. This service handles movies, user authentication, reviews, and watchlists.

Link to the frontend repo: [github repo link](https://github.com/jnanirudh/movie_app.git)

> 🚧 **Work in progress** — more services coming soon.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Validation | Pydantic v2 |
| Auth | JWT (PyJWT) |

---

## Project Structure

```
src/
├── startup/          # App entry point and database setup
├── routers/          # API route definitions
├── services/         # Business logic
├── repositories/     # Database queries
│   ├── models/       # SQLAlchemy table models
│   └── db/           # Base classes
├── contract/
│   ├── schemas/      # Pydantic request/response schemas
│   └── exceptions/   # Custom exceptions
├── config/           # Settings loaded from .env
└── migrations/       # Alembic migration files
```

---

## Getting Started

**1. Clone and set up environment**
```bash
git clone https://github.com/jnanirudh/MovieApp_backend.git
cd Backend
python3 -m venv venv
source venv/bin/activate
pip install -r src/requirements.txt
```

**2. Configure environment**
```bash
cp .env.example .env
# Fill in DATABASE_URL, TMDB_API_KEY, JWT_SECRET
```

**3. Run migrations**
```bash
cd src
alembic upgrade head
```

**4. Start the server**
```bash
# From Backend/
PYTHONPATH=src uvicorn startup.main:app --reload
```

API docs available at **http://localhost:8000/docs**

---

## Current Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/movies/homepage` | Paginated list of popular movies |
| `GET` | `/api/movies/search?query=` | Case-insensitive movie search |
| `GET` | `/api/movies/movie/{id}` | Movie details by ID |

---

## Planned Services

- [ ] User authentication (register, login, JWT)
- [ ] Movie reviews (create, read, update, delete)
- [ ] Watchlist management
- [ ] User profiles
