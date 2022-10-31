import mariadb
import sys

import db_conn


def set_notice(title, writer, content):
    conn = db_conn.db_connect()
    cur = conn.cursor()

    insert_query = "insert into users(writer, title, content) values (?, ?, ?)"
    try:
        cur.execute(insert_query, (writer, title, content))
        conn.commit()
        return 'success'
    except mariadb.Error as e:
        print(f"Error: {e}")
        return 'fail'


def get_notice(id):
    writer = ''
    title = ''
    content = ''

    conn = db_conn.db_connect()
    cur = conn.cursor()

    select_all_query = 'select id, writer, title, content from users where id=?'
    cur.execute(select_all_query, (id,))
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

    insert_query = "update users set title=?, content=? where id=?"
    try:
        cur.execute(insert_query, (title, content, id))
        conn.commit()
        return 'success'
    except mariadb.Error as e:
        print(f"Error: {e}")
        return 'fail'


def delete_notice(id):
    conn = db_conn.db_connect()
    cur = conn.cursor()

    insert_query = "delete from users where id=?"
    try:
        cur.execute(insert_query, (id,))
        conn.commit()
        return 'success'
    except mariadb.Error as e:
        print(f"Error: {e}")
        return 'fail'