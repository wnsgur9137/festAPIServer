import mariadb
import sys

import db_conn


def get_user_info(email):
    nickname = ''
    updateDate = ''

    conn = db_conn.db_connect()
    cur = conn.cursor()

    select_all_query = 'select email, nickname, updateDate from users where email=?'
    cur.execute(select_all_query, (email,))
    resultset = cur.fetchall()

    for result_email, result_nickname, result_updateDate in resultset:
        _ = result_email
        nickname = result_nickname
        updateDate = result_updateDate

    return {"email": email, "nickname": nickname, "updateDate": updateDate}


def get_nickname_check(nickname):
    email = ''
    updateDate = ''
    return_nickname = ''
    conn = db_conn.db_connect()
    cur = conn.cursor()

    select_all_query = 'select email, nickname, updateDate from users where nickname=?'
    cur.execute(select_all_query, (nickname,))
    result_set = cur.fetchall()
    for result_email, result_nickname, result_updateDate in result_set:
        email = result_email
        return_nickname = result_nickname
        updateDate = result_updateDate

    return {"email": email, "nickname": return_nickname, "updateDate": updateDate}


def set_user_info(email, nickname, updateDate):
    print(f"email: {email}")
    print(f"nickname: {nickname}")
    print(f"updateDate: {updateDate}")
    conn = db_conn.db_connect()
    cur = conn.cursor()

    insert_query = "insert into users(email, nickname, updateDate) values (?, ?, ?)"
    try:
        cur.execute(insert_query, (email, nickname, updateDate))
        conn.commit()
        return 'success'
    except mariadb.Error as e:
        print(f"Error: {e}")
        return 'fail'


def update_user_info(email, nickname, updateDate):
    conn = db_conn.db_connect()
    cur = conn.cursor()

    update_query = 'update users set nickname=?, updateDate=? where email=?'
    try:
        cur.execute(update_query, (nickname, updateDate, email))
        conn.commit()
        return 'success'
    except mariadb.Error as e:
        print(f"Error: {e}")
        return 'fail'


def delete_user_info(email):
    conn = db_conn.db_connect()
    cur = conn.cursor()

    delete_query = 'delete from users where email=?'
    try:
        cur.execute(delete_query, (email,))
        conn.commit()
        return 'success'
    except mariadb.Error as e:
        print(f"Error: {e}")
        return 'fail'
