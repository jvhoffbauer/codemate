async def before_request(
    request: Request,
):
    if request.url.path not in ALLOW_LIST:
        try:
            authorization = request.headers.get("Authorization", None)
            if not authorization:
                raise NotAuthorized("Authorization Headers Required")
            token = authorization.split(" ")[1]
            content = decode_jwt(token)
            # staff = await adal.get_or_404(User, json.loads(content["sub"])["user"])
            # g.staff = staff
        except NotAuthorized as e:
            raise e
        except NotFound as e:
            raise NotAuthorized("no such staff")
        except Exception:
            # TODO: more specific error
            raise NotAuthorized("token not correct")