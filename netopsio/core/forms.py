"""Netops.io core app forms."""

from django import forms


class WhoisForm(forms.Form):
    """Whois form."""

    host = forms.CharField(label="domain or ip address", max_length=256)
