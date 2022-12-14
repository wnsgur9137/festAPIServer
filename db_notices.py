import mariadb
import sys

import db_conn


def set_notice(title, writer, content):
    conn = db_conn.db_connect()
    cur = conn.cursor()

    insert_query = "insert into notices(writer, title, content) values (?, ?, ?)"
    try:
        cur.execute(insert_query, (writer, title, content))
        conn.commit()
        return 'success'
    except mariadb.Error as e:
        print(f"Error: {e}")
        return 'fail'


def get_all_notices():
    return_list = []

    conn = db_conn.db_connect()
    cur = conn.cursor()

    select_all_query = 'select id, writer, title, content from notices'
    cur.execute(select_all_query)
    resultset = cur.fetchall()

    for result_id, result_writer, result_title, result_content in resultset:
        # print('result_id: ', result_id)
        # print('result_writer: ', result_writer)
        # print('result_title: ', result_title)
        # print('result_content: ', result_content)
        return_list.append({'id': result_id, 'title': result_title, 'writer': result_writer, 'content': result_content})
    # print('\nreturn_list: ', return_list)
    return {'noticeList': return_list}

def get_notice(id):
    writer = ''
    title = ''
    content = ''

    conn = db_conn.db_connect()
    cur = conn.cursor()

    select_get_query = 'select id, writer, title, content from notices where id=?'
    cur.execute(select_get_query, (id,))
    resultset = cur.fetchall()

    for result_id, result_writer, result_title, result_content in resultset:
        _ = result_id
        writer = result_writer
        title = result_title
        content = result_content

    return {"writer": writer, "title": title, "content": content}


def update_notice(id, title, content):
    conn = db_conn.db_connect()
    cur = conn.cursor()

    insert_query = "update notices set title=?, content=? where id=?"
    try:
        cur.execute(insert_query, (title, content, id))
        conn.commit()
        print("conn success")
        return 'success'
    except mariadb.Error as e:
        print(f"Error: {e}")
        return 'fail'


def delete_notice(id):
    conn = db_conn.db_connect()
    cur = conn.cursor()

    delete_query = "delete from notices where id=?"
    try:
        cur.execute(delete_query, (id,))
        conn.commit()
        return 'success'
    except mariadb.Error as e:
        print(f"Error: {e}")
        return 'fail'