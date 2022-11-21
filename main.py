from fastapi import FastAPI
import uvicorn

import db_medicineList
import db_medicineInfoList
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
@app.get("/PillInfo/getAllNotices/")
async def get_all_notices():
    return db_notices.get_all_notices()


@app.get("/PillInfo/getNotice/")
async def get_notice(id: int):
    return db_notices.get_notice(id)


@app.post("/PillInfo/setNotice/")
async def set_notice(title: str, writer: str, content: str):
    print('setNotice: ', title, writer, content)
    return db_notices.set_notice(title, writer, content)
# PillInfo/setNotice/?title=공지사항&writer=Admin&content=공지%5Cn

@app.post("/PillInfo/updateNotice/")
async def update_notice(id: int, title: str, content: str):
    return db_notices.update_notice(id, title, content)


@app.post("/PillInfo/deleteNotice/")
async def delete_notice(id: int):
    return db_notices.delete_notice(id)


# endregion

# region medicineList

@app.post("/PillInfo/getMedicineListName")
async def get_medicine_list_name(medicineName: str):
    print(medicineName)
    print(db_medicineList.get_medicine_list_name(medicineName))
    return db_medicineList.get_medicine_list_name(medicineName)

@app.post("/PillInfo/getMedicineListShape")
async def get_medicine_list_shape(medicineName: str):
    return db_medicineList.get_medicine_list_shape(medicineName)

# endregion

# region medicineInfo

@app.post("/PillInfo/getMedicineInfo")
async def get_medicineInfo_list(medicineName: str):
    print(medicineName)
    return db_medicineInfoList.get_medicineInfo_list_name(medicineName)

# endregion

if __name__ == "__main__":
    uvicorn.run("main:app")
