def read_current_user(current_user: User = Depends(get_current_user)):
    if current_user is None:
        return {"msg": "Create an account first"}
    else:
        return current_user