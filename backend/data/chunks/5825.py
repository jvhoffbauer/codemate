    def conv_row_to_dict(self, rows: List[Row]) -> List[Dict[str, Any]]:
        """sqlalchemy row to dict"""
        if not rows:
            return []
        keys = self.get_row_keys(rows[0])
        return [dict(zip(keys, row)) for row in rows]