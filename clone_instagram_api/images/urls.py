from django.conf.urls import url
from . import views

app_name = 'images'
urlpatterns = [
    url(
        regex=r"^$",
        view=views.Feed.as_view(),
        name='feed'
    ),
    url(  # id 에 해당하는 image 불러오기
        regex=r"^(?P<image_id>[0-9]+)/$",
        view=views.ImageDetail.as_view(),
        name='image'
    ),
    url( # id 에 해당하는 image 에 like
        regex=r"^(?P<image_id>[0-9]+)/like/$",
        view=views.LikeImage.as_view(),
        name='like_image'
    ),
    url( # id 에 해당하는 image 에 unlike
        regex=r"^(?P<image_id>[0-9]+)/unlike/$",
        view=views.LikeImage.as_view(),
        name='unlike_image'
    ),
    url( # id 에 해당하는 image 에 comment 달기
        regex=r"^(?P<image_id>[0-9]+)/comments/$",
        view=views.CommentOnImage.as_view(),
        name='comment_image'
    ),
    url( # id 에 해당하는 image 에서 comment_id 에 해당하는 comment 삭제
        regex=r"^(?P<image_id>[0-9]+)/comments/(?P<comment_id>[0-9]+)/$",
        view=views.ModerateComments.as_view(),
        name='comment_image'
    ),
    url( # id 에 해당하는 comment 삭제
        regex=r"comments/(?P<comment_id>[0-9]+)/$",
        view=views.Comment.as_view(),
        name='comment'
    ),
    url( # 검색
        regex=r"^search/$",
        view=views.Search.as_view(),
        name='search'
    )
]
