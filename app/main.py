from fastapi import FastAPI
from car import Car

app = FastAPI()


@app.get("/registered_cars")
async def registered_cars():
    a = Car()
    if a.registered_cars:
        registered_cars = "Registered cars: " + ", ".join(a.registered_cars)
    else:    
        registered_cars = "No registered cars at this moment"   
    return {"info": registered_cars}


@app.post("/add_car")
async def add_car(number: str):
    a = Car(number)
    return {"info": a.status}


@app.delete("/delete_car/{number}")
async def delete_car(number: str):
    a = Car() 
    a.delete_car_number(number)
    return {"info": a.status}
