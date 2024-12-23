from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy.exc import SQLAlchemyError

# Initialize FastAPI application
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (adjust in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SQLAlchemy setup
DATABASE_URL = "mysql+mysqlconnector://admin:pswrd@mysql-db:3306/students_db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define database models
class StudentDB(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    grade = Column(Integer, nullable=False)

# Define the User table
class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(255), nullable=False)
    email= Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    
# Create tables in the database
Base.metadata.create_all(bind=engine)

# Dependency to get a session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define data models
class User(BaseModel):
    userName: str
    email: str
    password: str

class Student(BaseModel):
    name: str
    grade: int

# Sample user credentials
@app.post("/users/")
async def addUsers(user: User, db: Session = Depends(get_db)):
    try:
        # Check if the user already exists in the database
        existing_user = db.query(UserDB).filter(UserDB.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=409, detail="Email already exists")
        else:
            # Add new user if they don't exist
            new_user = UserDB(user_name=user.userName, email=user.email, password=user.password)
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            print(f"User {user.userName} added successfully.")
    except SQLAlchemyError as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Failed to create user")
    finally:
        db.close()  # Ensure the session is closed after the operation
      
    
# API Endpoints
@app.get("/users/{user_email}/{user_password}")
async def check_users(user_email:str,user_password:str, db: Session = Depends(get_db)):
    """Validate user credentials."""
    user_record = db.query(UserDB).filter(UserDB.email == user_email).first()
    if user_record:
        if user_record.password != user_password:
            raise HTTPException(status_code=401, detail="Password Incorrect")
        else:
            return [{"id": user_record.id, "name": user_record.user_name}]      
    else:
        raise HTTPException(status_code=401, detail="Email Not Exist")   
         
    

@app.get("/students/{id}")
def read_students(id:int, db: Session = Depends(get_db)):
    """Fetch all students from the database."""
    try:
        student = db.query(StudentDB).filter(StudentDB.id == id).first()
        return [{"id": student.id, "name": student.name, "grade": student.grade}]
    except SQLAlchemyError as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Failed to fetch students")
    


@app.get("/students/")
def read_students(db: Session = Depends(get_db)):
    """Fetch all students from the database."""
    try:
        students = db.query(StudentDB).all()
        return [{"id": student.id, "name": student.name, "grade": student.grade} for student in students]
    except SQLAlchemyError as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Failed to fetch students")



@app.post("/students/")
async def create_student(student: Student, db: Session = Depends(get_db)):
    """Add a new student to the database."""
    try:
        new_student = StudentDB(name=student.name, grade=student.grade)
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return {"message": "Student added successfully", "student": new_student}
    except SQLAlchemyError as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Failed to create student")

@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student, db: Session = Depends(get_db)):
    """Update an existing student's information."""
    try:
        student_record = db.query(StudentDB).filter(StudentDB.id == student_id).first()
        if not student_record:
            raise HTTPException(status_code=404, detail="Student not found")
        student_record.name = student.name
        student_record.grade = student.grade
        db.commit()
        db.refresh(student_record)
        return {"message": "Student updated successfully", "student": student_record}
    except SQLAlchemyError as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Failed to update student")

@app.delete("/students/{student_id}")
async def delete_student(student_id: int, db: Session = Depends(get_db)):
    """Delete a student from the database."""
    try:
        student_record = db.query(StudentDB).filter(StudentDB.id == student_id).first()
        if not student_record:
            raise HTTPException(status_code=404, detail="Student not found")
        db.delete(student_record)
        db.commit()
        return {"message": "Student deleted successfully"}
    except SQLAlchemyError as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Failed to delete student")

