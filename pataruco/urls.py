from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

"""
	from rest_framework.urlpatterns import format_suffix_patterns,
	le agregamos el soporte para que el usuario pueda pedir el formato
	de la informacion ya sea .api o .json
"""
urlpatterns = format_suffix_patterns(urlpatterns)