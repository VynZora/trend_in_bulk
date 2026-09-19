import os

from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse, JsonResponse
from django.urls import include, path, re_path
from django.views.static import serve

from trend_in_bulk_app.sitemap import StaticViewSitemap


# =====================================================
# ERROR HANDLERS
# =====================================================

handler404 = "trend_in_bulk_app.views.page_not_found"


# =====================================================
# SITEMAPS
# =====================================================

sitemaps = {
    "static": StaticViewSitemap,
}


# =====================================================
# HEALTH CHECK
# =====================================================

def health_check(request):
    return JsonResponse({
        "status": "ok"
    })


# =====================================================
# ROBOTS.TXT
# =====================================================

def robots_txt(request):
    file_path = os.path.join(
        settings.BASE_DIR,
        "trend_in_bulk_pro",
        "robots.txt",
    )

    with open(file_path, "r") as file:
        return HttpResponse(
            file.read(),
            content_type="text/plain",
        )


# =====================================================
# URL PATTERNS
# =====================================================

urlpatterns = [

    # Health check
    path(
        "health/",
        health_check,
        name="health_check",
    ),

    # Robots
    path(
        "robots.txt",
        robots_txt,
        name="robots_txt",
    ),

    # Sitemap
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="sitemap",
    ),

    # Main application
    # Keep this after the special URLs above
    path(
        "",
        include("trend_in_bulk_app.urls"),
    ),
]


# =====================================================
# TEMPORARY MEDIA SERVING ON RENDER
# =====================================================

urlpatterns += [
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.MEDIA_ROOT,
        },
    ),
]