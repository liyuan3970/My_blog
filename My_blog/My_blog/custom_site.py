from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = '小飞侠'
    site_title = '我的博客后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')