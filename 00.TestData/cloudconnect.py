import cx_Oracle

# conn =cx_Oracle.connect("ADMIN","Chltpfla890","etoiles2db_high")
# conn =cx_Oracle.connect("ora_user/1234@localhost:1521/xe")
cx_Oracle.init_oracle_client(lib_dir=r"C:\프로그램\Wallet_etoiles2db.zip")
conn = cx_Oracle.connect(user='ADMIN', password='Chltpfla890', dsn='etoiles2db_high')

cs=conn.cursor()


sql = "select * from member"
rows=cs.execute(sql)

for row in rows:
    print(row[0], row[1], row[2])


cs.close()
conn.commit()
conn.close()
    
    