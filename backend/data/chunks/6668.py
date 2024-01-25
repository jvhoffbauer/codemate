@api_v1.method(errors=[NotEnoughMoney])
def withdraw(
    account: Account = Depends(get_account),
    amount: int = Body(..., gt=0, example=10),
) -> Balance:
    if account.amount - amount < 0:
        raise NotEnoughMoney(data={"balance": get_balance(account)})
    account.amount -= amount
    return get_balance(account)