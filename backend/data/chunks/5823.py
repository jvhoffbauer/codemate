    def get_row_keys(self, row: Row) -> List[str]:
        """sqlalchemy row keys"""
        keymap = row._parent._keymap
        return [self.get_alias(keymap[field_name][2][1]) for field_name in row._fields]