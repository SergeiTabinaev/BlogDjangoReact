from django.db import models


class BlogCategory(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class BlogPostManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset()

    def all(self):
        return self.get_queryset().filter(in_archive=False)


class BlogPost(models.Model):

    blog_category = models.ForeignKey(BlogCategory, verbose_name='Имя категории', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Название поста')
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_posts/', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True)
    in_archive = models.BooleanField(default=False)
    object = BlogPostManager

    def __str__(self):
        return f"{self.title} из категории \"{self.blog_category.name}\""
