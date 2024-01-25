def get_account(
    # this will become the parameter of the json-rpc method that uses this dependency
    account_id: str = Body(..., example="1.1"),
    user: User = Depends(get_auth_user),
) -> Account:
    try:
        account = get_account_by_id(account_id)
    except KeyError:
        raise AccountNotFound

    if not account.owned_by(user):
        raise AccountNotFound

    return account