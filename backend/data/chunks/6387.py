@pytest.fixture(autouse=True)
def app_routes(app: FastAPI, models):
    user_schema = TableModelParser.get_table_model_schema(models.User)
    user_crud = SqlalchemyCrud(models.User, db.engine).register_crud(
        schema_read=user_schema
    )
    app.include_router(user_crud.router)