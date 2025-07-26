from django.db import models


class Articles(models.Model):
    title = models.CharField("Title", max_length=50)
    intro = models.CharField('Intro', max_length=250)
    body = models.TextField('Full_text')
    date = models.DateTimeField("Date")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
