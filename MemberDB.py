import pymysql

def loginId(inputId, inputPw):
    # STEP 2: MySQL Connection 연결
    con = pymysql.connect(host='localhost', user='pythonConn', password='1234',
                          db='python_db', charset='utf8')  # 한글처리 (charset = 'utf8')

    # STEP 3: Connection 으로부터 Cursor 생성
    cur = con.cursor()

    # STEP 4: SQL문 실행 및 Fetch
    sql = "SELECT * FROM members WHERE MID = %s AND MPW = %s"  # 파라미터 바인딩 사용
    cur.execute(sql, (inputId, inputPw))  # 튜플로 값을 전달

    # 데이타 Fetch
    rows = cur.fetchall()
    print(rows)  # 전체 rows

    # STEP 5: DB 연결 종료
    con.close()

    return rows