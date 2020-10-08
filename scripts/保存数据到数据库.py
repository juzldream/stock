import mysql.connector


"""
- 安装Python操作MySQL数据库模块 mysql-connector ：pip install mysql-connector
"""
def main(config):
    output = []
    cnx = mysql.connector.connect(**config)
    cur = cnx.cursor()

    # Drop table if exists, and create it new
    stmt_drop = "DROP TABLE IF EXISTS names"
    cur.execute(stmt_drop)

    stmt_create = (
        "CREATE TABLE names ("
        "    id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT, "
        "    name VARCHAR(30) DEFAULT '' NOT NULL, "
        "    info TEXT DEFAULT '', "
        "    age TINYINT UNSIGNED DEFAULT '30', "
        "PRIMARY KEY (id))"
    )
    cur.execute(stmt_create)

    info = "abc" * 10000

    # Insert 3 records
    names = (('Geert', info, 30), ('Jan', info, 31), ('Michel', info, 32))
    stmt_insert = "INSERT INTO names (name, info, age) VALUES (%s, %s, %s)"
    cur.executemany(stmt_insert, names)
    cnx.commit()

    # Read the names again and print them
    stmt_select = "SELECT id, name, info, age FROM names ORDER BY id"
    cur.execute(stmt_select)

    for row in cur.fetchall():
        output.append("%d | %s | %d\nInfo: %s..\n" % (
            row[0], row[1], row[3], row[2][:20]))

    # Cleaning up, dropping the table again
    cur.execute(stmt_drop)

    cur.close()
    cnx.close()
    return output


if __name__ == '__main__':

    config = {
        'host': 'localhost',
        'port': 3306,
        'database': 'test',
        'user': 'root',
        'password': '',
        'charset': 'utf8',
        'use_unicode': True,
        'get_warnings': True,
    }

    out = main(config)
    print('\n'.join(out))