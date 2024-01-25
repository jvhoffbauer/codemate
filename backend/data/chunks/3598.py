def create_dependency(name: str):
    def fun(deps: DepList):
        deps.append(name)

    return Depends(fun)