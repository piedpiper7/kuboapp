import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobleSettings(object):
    site_title = "跬步后台管理系统"
    site_footer = "跬步在线做题平台"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    pass


class BannerAdmin(object):
    pass


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobleSettings)