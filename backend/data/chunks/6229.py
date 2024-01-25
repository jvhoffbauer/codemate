@site.register_admin
class CategoryAdmin(admin.ModelAdmin):
    page_schema = "Category"
    # 配置管理模型
    model = Category