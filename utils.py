from models import Users, Carteira

def cria_conta(name, bithday):
    user = Users(nome=name, data_de_nascimento=bithday)
    user.save()
    carteira = Carteira(saldo=0, investido=0, user=user)
    carteira.save()

def consulta_usuarios(i):
    user = Users.query.filter_by(id=i).first()
    print(user)
    carteira = Carteira.query.filter_by(user=user).first()
    print(carteira)

def soma_saldo(i):
    user = Users.query.filter_by(id=i).first()
    carteira = Carteira.query.filter_by(user=user).first()
    carteira.saldo += 1
    carteira.save()
    print(carteira)

def subtrai_saldo(i):
    user = Users.query.filter_by(id=i).first()
    carteira = Carteira.query.filter_by(user=user).first()
    carteira.saldo -= 1
    carteira.save()
    print(carteira)

if __name__ == '__main__':
    # cria_conta('Luidgi', '24/01/2004')
    # consulta_usuarios(1)
    # soma_saldo(1)
    subtrai_saldo(1)