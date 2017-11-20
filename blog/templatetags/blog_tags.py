from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe

from urllib.parse import urlparse

import markdown

register = template.Library()

from ..models import Post
@register.simple_tag
def total_posts():
	return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html', takes_context=True)
def show_latest_posts(context, count = 5):
	request = context['request']
	url = request.build_absolute_uri()
	path = urlparse(url).path
	classify = int(path.split('/')[2])
	latest_posts = Post.published.filter(classify = classify).order_by('-publish')[:count]
	return {'latest_posts' : latest_posts, 'request' : request, 'classify' : classify}


@register.assignment_tag(takes_context=True)
def get_most_commented_posts(context, count = 5):
	request = context['request']
	url = request.build_absolute_uri()
	path = urlparse(url).path
	classify = int(path.split('/')[2])
	return Post.published.filter(classify = classify).annotate(total_comments = Count('comments')).order_by('-total_comments')[:count]


@register.assignment_tag(takes_context=True)
def get_most_gambling_commented_posts(context, count = 2):
	return Post.published.filter(classify = 1).annotate(total_comments = Count('comments')).order_by('-total_comments')[:count]


@register.assignment_tag(takes_context=True)
def get_most_affiliate_posts(context, count = 2):
	return Post.published.filter(classify = 2).annotate(total_comments = Count('comments')).order_by('-total_comments')[:count]


@register.assignment_tag(takes_context=True)
def get_most_forex_posts(context, count = 2):
	return Post.published.filter(classify = 3).annotate(total_comments = Count('comments')).order_by('-total_comments')[:count]


@register.filter(name = 'markdown')
def markdown_format(text):
	return mark_safe(markdown.markdown(text))


@register.filter(name = 'klass')
def klass_format(obj):
    return obj.field.widget.__class__.__name__