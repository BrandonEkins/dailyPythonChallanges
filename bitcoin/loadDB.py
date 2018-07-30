import subprocess
import os
import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
Base = declarative_base()
#schema:
class dbWallet(Base):
    __tablename__= "wallet"

    id = Column('id', Integer, primary_key=True)
    walletDate = Column('date', DateTime)
    btc = Column('btc', Integer)
    iot = Column('iot', Integer)
    ltc = Column('ltc', Integer)
    eth = Column('eth', Integer)
    ubtc = Column('ubtc', Integer)
    uiot = Column('uiot', Integer)
    ultc = Column('ultc', Integer)
    ueth = Column('ueth', Integer)

def initDatabase():
    engine = create_engine('sqlite:///wallet.db', echo=False)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def getAllWallets():
    session = initDatabase()
    wallets = session.query(dbWallet).all()
    session.close()
    return wallets

def getWallet():
    session = initDatabase()
    wallet = session.query(dbWallet).order_by(dbWallet.id.desc()).first()
    session.close()
    return wallet

def updateWallet(wallet, crypto):
    session = initDatabase()
    w = dbWallet()#creates wallet
    w.walletDate = datetime.now()
    w.btc = wallet['btc']
    w.iot = wallet['iot']
    w.ltc = wallet['ltc']
    w.eth = wallet['eth']
    w.ubtc = crypto['btc']['price']
    w.uiot = crypto['iot']['price']
    w.ultc = crypto['ltc']['price']
    w.ueth = crypto['eth']['price']
    session.add(w)
    session.commit()
    return w