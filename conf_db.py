import datetime
from sqlalchemy import create_engine, Column, Integer, String, DATETIME, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///db.sqlite3', echo=True, pool_recycle=7200)
Base = declarative_base()

association_table = Table('ContactList', Base.metadata,
                          Column('owner_id', ForeignKey('Client.id'), primary_key=True),
                          Column('client_id', ForeignKey('Client.id'), primary_key=True)
                          )


class Client(Base):
    __tablename__ = 'Client'
    id = Column(Integer, primary_key=True)
    login = Column(String)
    info = Column(String)
    m2m = relationship('Client', secondary=association_table,
                       primaryjoin=association_table.c.client_id == id,
                       secondaryjoin=association_table.c.owner_id == id,
                       backref='children')

    def __init__(self, login, info):
        self.login = login
        self.info = info

    def __repr__(self):
        return "<Client('%s','%s')>" % (self.login, self.info)


class ClientHistory(Base):
    __tablename__ = 'ClientHistory'
    id = Column(Integer, primary_key=True)
    enter_time = Column(DATETIME, default=datetime.datetime.now(datetime.timezone.utc))
    ip_address = Column(String)

    def __init__(self, ip_address):
        self.ip_address = ip_address

    def __repr__(self):
        return "ClientHistory('%s', '%s')" % (self.enter_time, self.ip_address)


# clients_table = Client.__table__
# user = Client("Vasya", "Vasya Pupkin")
# c = Client('crazy11', 'so_crazy')
# o = Client('vegetable', 'veg')
# c.m2m.append(o)
# client_hist = ClientHistory('111.111.111.111')
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
# session.add(user)
# session.add(c)
# session.add(client_hist)
# session.commit()

if __name__ == "__main__":
    Base.metadata.create_all(engine)


