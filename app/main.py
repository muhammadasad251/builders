# app/main.py
from fastapi import FastAPI
from app.db.session import engine, Base  # Import the engine and Base
from app.routers import auth, users, projects, documents, billing

# Create all database tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SaaS Portal for Builders API")

# Include routers for all endpoints
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(projects.router, prefix="/projects", tags=["Projects"])
app.include_router(documents.router, prefix="/documents", tags=["Documents"])
app.include_router(billing.router, prefix="/billing", tags=["Billing"])

@app.get("/")
def root():
    return {"message": "Welcome to the SaaS Portal for Builders API"}

# Loop over app.routes instead of app.routers
for route in app.routes:
    print(f"Path: {route.path} | Name: {route.name} | Methods: {route.methods}")
