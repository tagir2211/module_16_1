from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Главная страница."

@app.get("/user/admin")
async def root():
    return "Вы вошли как админ."

@app.get("/user/{user_id}")
async def read_user_id(user_id: int = 1):
    return  f'Вы вошли как пользователь {user_id}'

@app.get("/user/")
async def info_user(username: str = 'Иван', age: int = 0):
    return  f'информация о пользователе. Имя - {username}. Возраст - {age}'
