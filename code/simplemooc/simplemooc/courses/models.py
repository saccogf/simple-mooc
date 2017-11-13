from django.db import models

# Create your models here.


class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query)
            )


class Course(models.Model):

    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('Shortcurt')
    description = models.TextField('Description', blank=True)
    start_date = models.DateField('Start Date', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Image',
                              null=True, blank=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bitch'
        verbose_name_plural = 'Bitches'
        ordering = ['name']  # Use -name for descending order
