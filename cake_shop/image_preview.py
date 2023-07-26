from django.utils.html import format_html


def image_preview(cake):
    height = 300
    return format_html(
        "<img src={} height={} />",
        cake.picture.url,
        height,
    )
