            def select_maker(
                sel: Annotated[Select, Depends(self.get_select)],  # type: ignore
                link_clause: Annotated[Optional[Any], Depends(self.get_link_clause)] = None,  # type: ignore
            ) -> Select:
                if link_clause is not None:
                    sel = sel.where(link_clause)
                return sel