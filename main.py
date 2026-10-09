
from fastapi import Depends,FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session


app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
     
 ) # Replace with your frontend URL

database_models.Base.metadata.create_all(bind= engine)   

@app.get("/")

def greet():
    return "Hello, welcome to the Sayan's World ............... I am devil of my world"

products = [
    Product(id=1, name="Phone", description="budget phone", price=10000, quantity=10),
    Product(id=2, name="Laptop", description="gaming laptop", price=50000, quantity=5),
    Product(id=3, name="Headphones", description="wireless headphones", price=2000, quantity=20),
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()

    count = db.query(database_models.Product).count()

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))

    db.commit()


init_db()  # Initialize the database with sample products # Initialize the database with sample products


@app.get("/products")  
def get_all_products(db: Session = Depends(get_db)):
  
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/products/{id}")  #Read
def get_product_by_id(id: int,db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return  "Product not found"


@app.post("/products") #Create
def add_product(product: Product,db: Session = Depends(get_db)):
      db.add(database_models.Product(**product.model_dump()))
      db.commit()
      return product

@app.put("/products/{id}")  #Update
def update_product(id: int, updated_product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = updated_product.name
        db_product.description = updated_product.description
        db_product.price = updated_product.price
        db_product.quantity = updated_product.quantity
        db.commit()
        return updated_product
    else:
      return {"error": "Product not found"}


@app.delete("/products/{id}")  #Delete
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted"}
    else:
     return {"error": "Product not found"}
