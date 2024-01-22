# Trecho Padrão para criar banco de dados com SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

#Tabelas

class Users(Base):
    __tablename__ = 'users' # Nome da tabela

    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    data_de_nascimento = Column(String(10))

    def __repr__(self):
        return f'<User {self.nome}>'
    
    def save(self):
        db_session.add(self)
        db_session.commit()
    
    def exclui(self):
        db_session.delete(self)
        db_session.commit()

class Carteira(Base):
    __tablename__ = 'carteira' # Nome da tabela
    id = Column(Integer, primary_key=True)
    saldo = Column(Integer)
    investido = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("Users")

    def __repr__(self): # Representação do Objeto
        return f'<Saldo {self.saldo}>'
    
    def save(self):
        db_session.add(self)
        db_session.commit()

# Função para criar o banco de dados
def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
