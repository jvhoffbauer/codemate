    def new_print(*args):
        data = []
        for arg in args:
            if isinstance(arg, BaseModel):
                data.append(arg.model_dump())
            elif isinstance(arg, list):
                new_list = []
                for item in arg:
                    if isinstance(item, BaseModel):
                        new_list.append(item.model_dump())
                data.append(new_list)
            else:
                data.append(arg)
        calls.append(data)