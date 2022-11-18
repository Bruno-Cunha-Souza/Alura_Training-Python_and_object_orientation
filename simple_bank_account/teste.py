def create_account(number, holder, balance, limit):
    account = {"number": number, "holder":  holder, "balance": balance, "limit": limit}
    return account

def deposit(account, valor):
    account["balance"] += valor
    
def withdraw(account, valor):
    account["balance"] -= valor
    
def extract(account):
    print("O seu saldo é de: {}".format(account["balance"]))