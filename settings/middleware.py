import socket
import logging
logger = logging.getLogger(__name__)

from django.http import HttpResponseBadRequest

class SuspiciousIPMiddleware(object): # pragma: no cover
    """
    Middleware that block certain remote access
    """
    def process_request(self, request):
        logger.info('process_request:')
        logger.info('Remote_address: '+ request.META['REMOTE_ADDR'])
        if request.META['REMOTE_ADDR'] in ['120.12.23.111']:
            return HttpResponseForbidden('<h1>Forbidden</h1>')
