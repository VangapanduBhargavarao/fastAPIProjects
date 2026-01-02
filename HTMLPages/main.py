from fastapi import FastAPI,Request,Depends,HTTPException,status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,UJSONResponse
from fastapi.staticfiles import StaticFiles
from scheams import RequestData,User
from sqlalchemy.orm import Session
from models import get_db
from models import Base,engine


app=FastAPI()
Base.metadata.create_all(bind=engine)

templates=Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/',response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse(
        "index.html",
        {"request":request}
        )


@app.post('/register')
async def login(request:Request,db:Session=Depends(get_db)):
    form__data= await request.form()
    data=dict(form__data)
    user_data=RequestData(**data)

    try:
        user=User(
        fname=user_data.fname,
        lname=user_data.lname,
        phone_number=user_data.phone_number,
        email=user_data.email,
        zipcode=user_data.zipcode)
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print("__________________ ERROR___________",e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Incorrect detials")
    
    return {"message":"data stored sucessfully."}

    