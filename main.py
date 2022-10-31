from fastapi import FastAPI
import uvicorn

import db_users

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# region users
@app.get("/getUserInfo/{email}")
async def get_user_info(email: str):
    result = db_users.get_user_info(email)
    print(result)
    return result


@app.post("/setUserInfo/{email, nickname, updateDate}")
async def set_user_info(email: str, nickname: str, updateDate: str):
    result = db_users.set_user_info(email, nickname, updateDate)
    return result


@app.post("/updateUserInfo/{email, nickname, updateDate}")
async def update_user_info(email: str, nickname: str, updateDate: str):
    result = db_users.update_user_info(email, nickname, updateDate)
    return result


@app.post("/deleteUserInfo/{email}")
async def delete_user_info(email: str):
    result = db_users.delete_user_info(email)
    return result


# endregion

# region notices
@app.get("/getNotice/{id}")
async def get_notice(id: int):
    pass


@app.post("/setNotice/{title, writer, content}")
async def set_notice(title: str, writer: str, content: str):
    pass


@app.post("/updateNotice/{id, title, content}")
async def update_notice(id: int, title: str, content: str):
    pass


@app.post("/deleteNotice/{id}")
async def delete_notice(id: int):
    pass


# endregion

if __name__ == "__main__":
    uvicorn.run("main:app")
