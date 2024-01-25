def main():
    cookiecutter(
        template=str(ROOT_FOLDER),
        no_input=True,
        extra_context={
            "project_name": "minimal_project",
        },
    )