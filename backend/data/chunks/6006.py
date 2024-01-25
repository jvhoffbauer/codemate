    def error_no_page_permission(self, request: Request):
        raise HTTPException(
            status_code=status.HTTP_307_TEMPORARY_REDIRECT,
            detail="No page permissions",
            headers={
                "location": f"{self.site.router_path}{self.site.router.url_path_for('login')}?redirect={request.url.path}",
            },
        )