from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.IndexPage.as_view(),name='index'),
    url(r'^contact/$',views.ContactPage.as_view(),name='contact'),
    url(r'^about/$',views.About.as_view(),name='about'),

    url(r'^article/all/$', views.AllArticleAPIView.as_view(), name='all_articles'),



]
