    def requester(data, path_postfix=""):
        resp = raw_request(json_dumps(data), path_postfix=path_postfix)
        return resp.json()