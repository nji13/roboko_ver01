# SQLalchemyでコードを書くと、sqliteからmysqlに移行する時などにコードを書き換える必要がなくなる

import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost/test_mysql_database2', echo=True) # こちらのコード内でsqliteやmysqlなどを変更する

Base = sqlalchemy.ext.declarative.declarative_base()

class Person(Base):
    __tablename__ = 'tests'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=[True])
    addres = sqlalchemy.Column(sqlalchemy.Integer, nullable=[False])

Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

p1 = Person(name='Mike', age=20, addres=555)
session.add(p1)
# p2 = Person(name='Nancy')
# session.add(p2)
# p3 = Person(name='Jun')
# session.add(p3)
session.commit()

# p4 = session.query(Person).filter_by(name='Mike').first()
# p4.name = 'Michel'
# session.add(p4)
# session.commit()

# p5 = session.query(Person).filter_by(name='Nancy').first()
# session.delete(p5)
# session.commit()

persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name, person.age, person.addres)