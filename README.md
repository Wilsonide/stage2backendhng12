# Project documentation

## Description

this api takes a number and returns interesting mathematical properties about it, along with a fun fact.

- Endpoint -  GET <<https://surprising-shayne-wilsonide-3009276d.koyeb.app/api/classify-number>>

### Example Response

#### 200(ok) Response 

```bash
{
  "number": "6",
  "is_prime": false,
  "is_perfect": true,
  "properties": [
    "armstrong",
    "even"
  ],
  "digit_sum": 6,
  "fun_fact": "6 is the only number that is both the sum and the product of three consecutive positive numbers."
}
```
#### 400(Bad Request) Response

```bash
{ "number": "alphabet",
   "error" : "true'
}
```

## Project setup locally 
### clone repo
```bash
git clone <https://github.com/Wilsonide/stage2backendhng12.git>
```

## Compile and run the project

```bash
pip install -r requirements.txt
python main.py

```
