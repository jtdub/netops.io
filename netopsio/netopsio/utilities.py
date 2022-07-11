"""Netops.io utilities."""


def get_ip_address(request):
    """Get the IP Address from a request."""
    host = request.GET.get("host")

    if host is None:
        if "HTTP_X_FORWARDED_FOR" in request.META:
            host = request.META["HTTP_X_FORWARDED_FOR"]
        else:
            host = request.META["REMOTE_ADDR"]

    return host
