import re

def get_global_service_mock(url, service_id):
    """ Creates a url for a global service with the given url and service """
    return re.compile(r'%s/%s/.*' % (url, service_id))
