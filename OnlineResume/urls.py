from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.urls import resolve
from django.conf import settings
from . import views
from OnlineResume.views import index_view
urlpatterns = [
	# ex: /
	url(r'index/',index_view,name='index_view'),
	# url(r'^charcha-serviceworker(.*.js)$', views.charcha_serviceworker, name='charcha_serviceworker'),
	# url(r'^$', login_view, name='login'),
 #    url(r'^signup/$', signup, name='signup'),
	# # url(r'^quizes/$', QuizView.as_view(), name='QuizView'),
	# url(r'^quizes/(\d+)/(\d+)$', QuizView.as_view(), name='QuizView'),
	# url(r'^results/$', ResultView.as_view(), name='results'),
	# url(r'^logout/$', auth_views.logout, {'next_page': 'locco:login'}, name='logout'),
	# url(r'^SessionCreate/$', SessionCreate.as_view(), name='SessionCreate'),
	# # url(r'^session_create/$', session_create, name='session_create'),

    ]