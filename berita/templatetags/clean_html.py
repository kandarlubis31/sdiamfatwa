# berita/templatetags/clean_html.py

from django import template
from django.utils.safestring import mark_safe
import html

register = template.Library()

@register.filter
def clean_html(text):
    """
    Membersihkan HTML entities dan mengembalikan HTML yang valid
    """
    # Decode HTML entities
    decoded_text = html.unescape(text)
    return mark_safe(decoded_text)