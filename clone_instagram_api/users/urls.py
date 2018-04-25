from django.conf.urls import url
from . import views

app_name = "users"
urlpatterns = [
    url(
        regex=r"^explore/$",
        view=views.ExploreUsers.as_view(),
        name="explore_users"
    ),
    url(
        regex=r"^(?P<user_id>[0-9]+)/follow/$",
        view=views.FollowUser.as_view(),
        name='follow_user'
    ),
    url(
        regex=r"^(?P<user_id>[0-9]+)/unfollow/$",
        view=views.UnFollowUser.as_view(),
        name='unfollow_user'
    ),
    url(
        # regex=r"^(?P<username>\w+)/$",
        regex=r"^(?P<user_id>[0-9]+)/$",
        view=views.UserProfile.as_view(),
        name='user_profile'
    ),
    url(
        # regex=r"^(?P<username>\w+)/followers/$",
        regex=r"^(?P<user_id>[0-9]+)/followers/$",
        view=views.UserFollowers.as_view(),
        name='user_followers'
    ),
    url(
        # regex=r"^(?P<username>\w+)/following/$",
        regex=r"^(?P<user_id>[0-9]+)/following/$",
        view=views.UserFollowing.as_view(),
        name='user_following'
    ),
    url(
        regex=r"^search/$",
        view=views.Search.as_view(),
        name='user_search'
    )
]
