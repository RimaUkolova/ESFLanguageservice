from django.conf.urls import include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
from home.views import feedback1, feedback2, feedback3


# import esf

urlpatterns = [
    re_path(r'^django-admin/', admin.site.urls),

    re_path(r'^admin/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),

    # url(r'^search/$', search_views.search, name='search'),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    


    # the list:
    # url(r'', include(wagtail_urls)), Закомментировал т.к. ниже определено

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]

urlpatterns += i18n_patterns(
    # These URLs will have /<language_code>/ appended to the beginning

    re_path(r'', include(wagtail_urls)),
    re_path(r'^', include('home.urls')),
    re_path(r'^search/$', search_views.search, name='search'),

)


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
