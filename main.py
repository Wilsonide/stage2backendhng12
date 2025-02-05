from fastapi import FastAPI, Response,status
from fastapi.middleware.cors import CORSMiddleware
import requests
import uvicorn
import app.helper as helper



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
def get_user(res:Response, number='',):
    if number == '':
        res.status_code = 400
        return {
            "number": "alphabet",
            "error": True,
        }

    if number.startswith('-'):
        if '.' in number:
            return {
            "number": "alphabet",
            "error": True,
        }
        mynumber = number[1:]
        if not mynumber.isnumeric():
             return {
            "number": "alphabet",
            "error": True,
        }
        else:
            num = abs(int(number))
            odd_even = ''
            sum = helper.getSum(num)
            isArmstrong = helper.isArmStrong(num)
            even = helper.is_even(num)
            isPrime = helper.is_prime(num)
            isPerfect = helper.is_perfect(num)
            fun_fact = helper.get_fun_fact(number)
        

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
    
    if number.isnumeric():
        num = int(number)
        odd_even = ''
        sum = helper.getSum(num)
        isArmstrong = helper.isArmStrong(num)
        even = helper.is_even(num)
        isPrime = helper.is_prime(num)
        isPerfect = helper.is_perfect(num)
        fun_fact = helper.get_fun_fact(num)

    

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
    
    if "." in number:
        res.status_code = 400
        return {
            "number": "alphabet",
            "error": True,
        }

    else:
        res.status_code = 400
        return {
            "number": "alphabet",
            "error": True,
        }



if __name__ == "__main__":
    uvicorn.run('main:app',port=8000, host='0.0.0.0')
