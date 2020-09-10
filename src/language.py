from django.utils.deprecation import MiddlewareMixin


class DefaultLanguageMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        if 'HTTP_ACCEPT_LANGUAGE' in request.META:
            del request.META['HTTP_ACCEPT_LANGUAGE']
