import xadmin
from .models import PaperComment, UserLike, UserMessage, UserPaper


class PaperCommentAdmin(object):
    pass


class UserLikeAdmin(object):
    pass


class UserMessageAdmin(object):
    pass


class UserPaperAdmin(object):
    pass


xadmin.site.register(PaperComment, PaperCommentAdmin)
xadmin.site.register(UserLike, UserLikeAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserPaper, UserPaperAdmin)