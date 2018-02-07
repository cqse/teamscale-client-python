import re

def get_project_service_mock(url, service_id):
    return re.compile(r'%s/p/foo/%s/.*' % (url, service_id))


def get_global_service_mock(url, service_id):
    return re.compile(r'%s/%s/.*' % (url, service_id))
