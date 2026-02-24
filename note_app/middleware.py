import zoneinfo
from django.utils import timezone

class SimpleTimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Look for a cookie named 'django_timezone'
        tzname = request.COOKIES.get("django_timezone")
        if tzname:
            try:
                timezone.activate(zoneinfo.ZoneInfo(tzname))
            except Exception:
                pass 
        return self.get_response(request)