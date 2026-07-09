# AI Tools Directory - Backend

FastAPI + SQLAlchemy + MySQL backend for the AI Tools Directory project.

## Setup

1. Create a virtual environment:
   python -m venv venv

2. Activate it:
   - Windows: venv\Scripts\activate
   - Mac/Linux: source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Create your local env file:
   cp .env.example .env
   (then edit .env with your real MySQL password)

5. Start the server:
   uvicorn app.main:app --reload

API will run at: http://localhost:8000
Interactive docs: http://localhost:8000/docs
