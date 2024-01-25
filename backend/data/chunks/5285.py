    def handle(self, *args, **options):
        from IPython import embed
        import cProfile
        import pdb
        import django.apps

        models = {model.__name__: model for model in django.apps.apps.get_models()}
        main = importlib.import_module("__main__")
        ctx = main.__dict__
        ctx.update(
            {
                **models,
                "ipdb": pdb,
                "cProfile": cProfile,
            }
        )
        embed(user_ns=ctx, banner2="", colors="neutral", using="asyncio")