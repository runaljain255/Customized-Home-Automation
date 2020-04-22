
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import usersviews
from . import areasviews
from . import switchviews
from . import actionview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users_view/',usersviews.userview),
    path('users_submit',usersviews.usersubmit),
    path('user_login/',usersviews.userlogin),
    path('check_login/',usersviews.checklogin),
    path('area_view/',areasviews.areaview),
    path('area_submit',areasviews.areasubmit),
    path('switch_view/',switchviews.switchview),
    path('switch_submit',switchviews.switchsubmit),
    path('action_view/',actionview.fetchallarea),
    path('switch_action/',actionview.fetchallswitchs),
    path('fetch_all_area/',areasviews.fetchallarea),
    path('display_by_id/',areasviews.displaybyid),
    path('edit_delete_area/',areasviews.editdeletearea),
    path('edit_picture',areasviews.editpicture),
    path('pubnub_action/',actionview.pubnubaction)
]

urlpatterns+=staticfiles_urlpatterns()
