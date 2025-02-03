from fastapi import FastAPI, Response,status
from fastapi.middleware.cors import CORSMiddleware
import httpx
import requests
import uvicorn
import helper

from pydantic import BaseModel

class UserResponse(BaseModel):
    number: int | str
    class Config:
        orm_mode = True


def init():
    async def lifespan(app:FastAPI):
        yield
    app = FastAPI(title='Fastapi',lifespan=lifespan)
    return app

app = init()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ['*']
)

@app.get('/')
def hello():
    return "Hello World"

@app.get('/api/classify-number',status_code=status.HTTP_200_OK)
def get_user(number,res: Response):


    try:
        headers = {'Accept': 'application/json'}
        response = requests.get(f'http://numbersapi.com/{number}/math',headers=headers)
        fun_fact = response._content
        num = int(number)
        odd_even = ''
        sum = helper.getSum(num)
        isArmstrong = helper.isArmStrong(num)
        even = helper.is_even(num)
        isPrime = helper.is_prime(num)
        isPerfect = helper.is_perfect(num)

    

        if not even:
            odd_even = "odd"
        else:
            odd_even = "even"

        properties = ["armstrong",odd_even]
        if not isArmstrong:
            properties.remove("armstrong")
            
        return {
                "number": number,
                "is_prime": isPrime,
                "is_perfect": isPerfect,
                "properties": properties,
                "digit_sum": sum,
                "fun_fact" : fun_fact,
                

        }
    except ValueError as e:
        print(e)
        res.status_code = 400
        return {
            "number": "alphabet",
            "error": True,
        }
    



if __name__ == "__main__":
    uvicorn.run('main:app',reload=True,port=8000)