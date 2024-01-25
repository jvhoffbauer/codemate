    def _select_maker(self):
        if self.link_models:

            def select_maker(
                sel: Annotated[Select, Depends(self.get_select)],  # type: ignore
                link_clause: Annotated[Optional[Any], Depends(self.get_link_clause)] = None,  # type: ignore
            ) -> Select:
                if link_clause is not None:
                    sel = sel.where(link_clause)
                return sel

        else:
            select_maker = self.get_select
        return select_maker