    def test_scalar_type_choices(self):
        class UserStatus(IntegerChoices):
            NORMAL = 1, "正常"
            DISABLED = 2, "禁用"

        assert annotation_outer_type(UserStatus) == UserStatus