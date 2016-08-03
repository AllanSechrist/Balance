from django.conf.urls import url
from . import views

app_name = 'file'

urlpatterns = [
    # /file/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /file/<folder_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /file/folders/
    url(r'^folders/$', views.MyFoldersView.as_view(), name='folders'),

    # /file/folders/add/
    url(r'folders/add/$', views.FolderCreate.as_view(), name='folder-add'),

    # /file/folders/<folder_id>
    url(r'folders/(?P<pk>[0-9]+)/$', views.FolderUpdate.as_view(), name='folder-update'),

    # file/folders/<folder_id>/delete
    url(r'folders/(?P<pk>[0-9]+)/delete/$', views.FolderDelete.as_view(), name='folder-delete')
]