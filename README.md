# Project documentation

## Description

this api takes a number and returns interesting mathematical properties about it, along with a fun fact.

- Endpoint -  GET <<https://backend-stage0.vercel.app/user>>

### Example Response

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

## Project setup

```bash
pip install -r requirements.txt
```

## Compile and run the project

```bash
python main.py

```
