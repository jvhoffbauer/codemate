    def is_superuser(self, user: User) -> bool:
        return user.is_superuser