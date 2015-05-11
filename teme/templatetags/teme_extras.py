from django import template

from teme.constants import MAX_RATING_STAR_VALUE


register = template.Library()


@register.simple_tag
def get_stars(stars):
    full_star = '<span class="glyphicon glyphicon-star"></span>'
    empty_star = '<span class="glyphicon glyphicon-star-empty"></span>'
    return stars * full_star + (MAX_RATING_STAR_VALUE - stars) * empty_star
