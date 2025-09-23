from fastapi import FastAPI,HTTPException,Depends
from sqlalchemy.orm import Session
import models,schemas
from database import SessionLocal,engine,Base
Base.metadata.create_all(bind=engine)
app = FastAPI(debug=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/products/",response_model=schemas.ProductResponse)
async def create_product(product:schemas.ProductCreate,db:Session=Depends(get_db)):
    db_product =  models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products/{product_id}",response_model=schemas.ProductResponse)
def read_product(product_id:int,db:Session=Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404,detail="Product not found")
    return db_product

@app.get("/products/",response_model=list[schemas.ProductResponse])
def list_products(skip:int=0,limit:int=10,db:Session=Depends(get_db)):
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products

@app.put("/products/{product_id}",response_model=schemas.ProductResponse)
def update_product(product_id:int,product:schemas.ProductUpdate,db:Session=Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404,detail="Product not found")
    for var, value in vars(product).items():
        setattr(db_product, var, value) if value else None
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete("/products/{product_id}")
def delete_product(product_id:int,db:Session=Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404,detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"detail":"Product deleted"}