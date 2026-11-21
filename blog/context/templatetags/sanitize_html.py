import nh3
from django import template
from django.utils.safestring import mark_safe


register = template.Library()

_ALLOWED_TAGS = nh3.ALLOWED_TAGS | {
    "img",
    "table",
    "thead",
    "tbody",
    "tfoot",
    "tr",
    "th",
    "td",
    "hr",
    "figure",
    "figcaption",
}
_ALLOWED_ATTRIBUTES = {
    tag: set(attributes)
    for tag, attributes in nh3.ALLOWED_ATTRIBUTES.items()
}
_ALLOWED_ATTRIBUTES.setdefault("img", set()).update(
    {"src", "alt", "title", "width", "height"}
)
_ALLOWED_ATTRIBUTES.setdefault("a", set()).add("target")
for tag in ("p", "div", "span", "img", "td", "th"):
    _ALLOWED_ATTRIBUTES.setdefault(tag, set()).add("style")

_CLEANER = nh3.Cleaner(
    tags=_ALLOWED_TAGS,
    attributes=_ALLOWED_ATTRIBUTES,
    url_schemes={"http", "https", "mailto"},
    filter_style_properties={
        "text-align",
        "color",
        "background-color",
        "font-weight",
        "font-style",
        "text-decoration",
        "font-size",
        "width",
        "height",
    },
    strip_comments=True,
)


@register.filter
def sanitize_html(value):
    """Return a safe subset of TinyMCE HTML for display."""
    return mark_safe(_CLEANER.clean(str(value or "")))
