from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
import models
from database import get_db, engine
from config import settings
from routers import user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(user.router)



#check database connection :
@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        # Test the database connection
        db.execute(text("SELECT 1")) 
        
        # ✅ SUCCESS: Prints to CMD terminal
        print("Database connection is connected")
        
        return {"status": "database connection is healthy"}
        
    except Exception as e:
        # ❌ FAILURE: Prints to CMD terminal if the connection fails
        print(f"Database connection failed! Error: {str(e)}")
        
        raise HTTPException(
            status_code=500, 
            detail=f"Database connection error: {str(e)}"
        )




@app.get("/")
def read_root():
    return {"Hello": "World"}
    