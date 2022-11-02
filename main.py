from fastapi import FastAPI
import uvicorn

import db_notices
import db_users

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# region users
@app.get("/PillInfo/getUserInfo/")
async def get_user_info(email: str):
    result = db_users.get_user_info(email)
    print(result)
    return result


@app.get("/PillInfo/getNicknameCheck/")
async def get_nickname_check(nickname: str):
    result = db_users.get_nickname_check(nickname)
    print(result)
    return result


@app.post("/PillInfo/setUserInfo/")
async def set_user_info(email: str, nickname: str, updateDate: str):
    result = db_users.set_user_info(email, nickname, updateDate)
    return result


@app.post("/PillInfo/updateUserInfo/")
async def update_user_info(email: str, nickname: str, updateDate: str):
    result = db_users.update_user_info(email, nickname, updateDate)
    return result


@app.post("/PillInfo/deleteUserInfo/")
async def delete_user_info(email: str):
    result = db_users.delete_user_info(email)
    return result


# endregion

# region notices
@app.get("/PillInfo/getNotice/")
async def get_notice(id: int):
    pass


@app.post("/PillInfo/setNotice/")
async def set_notice(title: str, writer: str, content: str):
    print('setNotice: ', title, writer, content)
    db_notices.set_notice(title, writer, content)


@app.post("/PillInfo/updateNotice/")
async def update_notice(id: int, title: str, content: str):
    pass


@app.post("/PillInfo/deleteNotice/")
async def delete_notice(id: int):
    pass


# endregion

if __name__ == "__main__":
    uvicorn.run("main:app")
