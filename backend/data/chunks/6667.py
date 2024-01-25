def get_balance(
    account: Account = Depends(get_account),
) -> Balance:
    return Balance(
        amount=account.amount,
        currency=account.currency,
    )