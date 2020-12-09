from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

status_choices =(('draft', 'DRAFT'),
                 ('published', 'PUBLISHED'))


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    slug = models.SlugField(unique=True,max_length=150)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name="Tag")
    slug = models.SlugField(unique=True, max_length=150)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def get_absolute_url(self):
        return reverse('tag', args=[self.slug])

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=300, verbose_name="Title")
    slug = models.SlugField(unique=True)
    status = models.CharField(choices= status_choices, default='draft', max_length=10, verbose_name='Status')
    date_published = models.DateField(verbose_name='Created')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='uploads.%Y/%m/%d', verbose_name='Picture', blank=True, null=True)
    content = RichTextUploadingField(verbose_name='Content')
    author = models.CharField(default='anonymous', max_length=15, verbose_name='Author')
    tag = models.ManyToManyField(Tag)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def get_absolute_url(self):
        return reverse('post_details', args=[self.slug])

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    email = models.EmailField(max_length=200)
    message_date = models.DateField()
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.name + self.email








