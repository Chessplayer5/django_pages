import sqlalchemy as db

engine = db.create_engine("sqlite:///census.sqlite")
connection = engine.connect()
results = connection.execute("select * from census")
for row in results:
    print(row)

connection.close()
