from django.conf.urls import url
from fishydishy import views

# setting up url patterns to be used
urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^fishmongermap/$', views.fish_map, name='fish_map'),
    url(r'^fishfinder/$', views.fish_finder, name='fish_finder'),
    url(r'^add_recipe/$', views.add_recipe, name='add_recipe'),
    url(r'^recipes/$', views.recipes, name='recipes'),
    url(r'^search/$', views.search, name='search'),

    # uses slug to get individual pages for recipes
    url(r'^recipe/(?P<recipe_name_slug>[\w\-]+)/$',
        views.show_recipe,
        name='show_recipe'),

    url(r'^register/$',
        views.register,
        name='register'),

    url(r'^login/$',
        views.user_login,
        name='login'),

    url(r'^user_profile/',
        views.user_profile,
        name='user_profile'),

    url(r'^logout/$',
        views.user_logout,
        name='logout'),

    url(r'^contact/$', views.contact, name='contact'),

    url(r'^site_map/$',
        views.site_map,
        name='site_map'),

]
