"""
Return custom error and success response.
"""
# python imports
import logging
from rest_framework.response import Response

log = logging.getLogger("test_log")


def custom_response(status, detail, data=None, **kwargs):
    """
    function is used for getting same global response for all api
    :param detail: success message
    :param data: data
    :param status: http status
    :return: Json response
    """
    return Response({"data": data, "detail": detail}, status=status, **kwargs)


def custom_error_response(status, detail, **kwargs):
    """
    function is used for getting same global error response for all api
    :param detail: error message .
    :param status: http status.
    :return: Json response
    """
    if not detail:
        detail = {}
    return Response({"detail": detail}, status=status, **kwargs)


def is_int(number):
    """
    validate number is integer or not.
    :param number: integer number
    :return: True/False
    """
    try:
        int(number)
        return True
    except ValueError:
        return False
