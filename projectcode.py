accounts = {244123412: 1000.00, 244345656: 3000.00, 244456767: 5000.00, 244987676: 300.0}


def main() :
    print("Main Menu \n ----------- \n 1) Balance inquiry \n 2) Withdrawal \n 3) Deposit \n 4) Exit")
    option = int(input('Please enter an option (1 to 4): '))
    return option

def update(money):
    new_money = '${:,.2f}'.format(money)
    return new_money

while True:
    opt = main()
    if opt not in [1, 2, 3, 4]:
        print('No such option. Try again')
        continue
    elif opt == 4:
        break
    print(list(accounts.keys()))
    try:
        acc = int(input('Enter account number: '))
        balance = accounts[acc] #find amount of bal in bank
    except KeyError :
        print ('This account does not exist, try again')
        continue
    if opt == 1:
        f_bal = update(balance)
        print(f'Account Number: {acc} \nBalance: {f_bal}')
    elif opt == 2 :
        amt = float (input('Enter amount to be transacted: '))
        if amt > balance:
            print ('Sorry. There are insufficient funds for this transaction, please try again')
        elif amt < 0:
            print ('Amount to be transacted cannot be negative')
            continue
        elif isinstance(amt, complex):
            print('Amount to be transacted cannot be a complex number')
            continue
        else:
            remaining = balance - amt
            f_bal = update(remaining)
            print(f'Account Number: {acc} \nBalance: {f_bal}')
            accounts[acc] = remaining
    elif opt == 3:
        amt = float (input('Enter amount to be transacted: '))
        if amt < 0:
            print ('Amount to be transacted cannot be negative')
            continue
        elif isinstance(amt, complex):
            print('Amount to be transacted cannot be a complex number')
            continue
        updated = balance + amt
        accounts[acc] = updated
        f_bal = update(updated)
        print(f'Account Number: {acc} \nBalance: {f_bal}')
    else:
        break




