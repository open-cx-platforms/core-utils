from django.conf import settings
from django.core import wsgi
from django.core.handlers import exception

from .utils import *
from .loader import *
from .validation import *

default_app_config = 'core_utils.apps.DefaultConfig'


if getattr(settings, 'EE_AVAILABLE', False):
    for item in getattr(settings, 'VALIDATION_POINTS', []):
        md, fn = item.rsplit('.', 1)
        ValidationLoader().apply(import_path(md), fn)

    RequestLoader(ValidationContext(), LicenseRequestContext())\
        .apply(wsgi.WSGIHandler, 'get_response')
    ValidationResponseForException()\
        .apply(exception, 'response_for_exception')
