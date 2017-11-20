from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

# Create your models here.
class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status = 'published')


class Post(models.Model):
	STATUS_CODE = (
			('draft' , 'Draft'),
			('published' , 'Published'),
		)
	classify = models.IntegerField()
	image_affiliate = models.ImageField(upload_to = 'affiliate', blank = True)
	image_gambling = models.ImageField(upload_to = 'gambling', blank = True)
	image_forex = models.ImageField(upload_to = 'forex', blank = True)
	title = models.CharField(max_length = 250)
	slug = models.SlugField(max_length = 250, unique_for_date = 'publish')
	author = models.ForeignKey(User, related_name = 'blog_posts')
	body = models.TextField()
	publish = models.DateTimeField(default = timezone.now)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	status = models.CharField(max_length = 10, choices = STATUS_CODE, default = 'draft')
	objects = models.Manager()
	published = PublishedManager()
	tags = TaggableManager()
	top_banner_ads = models.TextField(blank = True)
	side_ads_fst = models.TextField(blank = True)
	side_ads_sec = models.TextField(blank = True)
	side_ads_thrd = models.TextField(blank = True)
	real_author = models.CharField(max_length = 100, blank = True)

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail', args = [self.classify,
													self.publish.year,
													self.publish.strftime('%m'),
													self.publish.strftime('%d'),
													self.slug])


class Comment(models.Model):
	post = models.ForeignKey(Post, related_name = 'comments')
	name = models.CharField(max_length = 80)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	active = models.BooleanField(default = True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return 'Comment by {} on {}'.format(self.name, self.post)