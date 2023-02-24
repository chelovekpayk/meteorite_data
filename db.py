from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData, ForeignKey


#Метадата таблицы
meta = MetaData()

meteorites = Table('Meteorites', meta, 
    Column('id_meteor', Integer, primary_key=True),
    Column('')
)
