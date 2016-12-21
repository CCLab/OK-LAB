import os

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


# Create your models here.


class OldPrint(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User)
    title_page = models.ForeignKey('Scan', null=True)
    # author = models.CharField(max_length=2, blank=True)
    # lp = models.CharField(max_length=3, blank=True)
    title = models.CharField(max_length=1024, blank=True)
    title_page_content = models.TextField(blank=True)
    title_variant = models.CharField(max_length=256, blank=True)
    # ???
    author_khw = models.CharField(max_length=64, blank=True)
    # ???
    author_doc = models.CharField(max_length=64, blank=True)
    publication_place = models.CharField(max_length=32, blank=True)
    publisher_name = models.CharField(max_length=128, blank=True)
    publication_date = models.DateField(blank=True)
    printing_place = models.CharField(max_length=32, blank=True)
    printing_house_name = models.CharField(max_length=128, blank=True)
    printing_date = models.DateField(blank=True)
    number_of_pages = models.IntegerField(blank=True)
    designation_illustration = models.CharField(max_length=32, blank=True)
    bibliography_format = models.CharField(max_length=32, blank=True)
    # ???
    ownership_entries = models.CharField(max_length=512, blank=True)
    figerprint = models.CharField(max_length=64, blank=True)
    other_information = models.TextField(blank=True)
    co_founder = models.CharField(max_length=128, blank=True)
    keywords = models.CharField(max_length=256, blank=True)
    source_type = models.CharField(max_length=128, blank=True)
    resource_identifier = models.CharField(max_length=16, blank=True)
    e_format = models.CharField(max_length=16, blank=True)
    source = models.CharField(max_length=512, blank=True)
    language_code = models.CharField(max_length=16, blank=True)
    language = models.CharField(max_length=32, blank=True)
    bookbinding_block = models.CharField(max_length=16, blank=True)
    signature = models.CharField(max_length=16, blank=True)
    laws = models.CharField(max_length=16, blank=True)
    # ???
    daten_od = models.DateField(blank=True)
    daten_do = models.DateField(blank=True)

    @property
    def directory(self):
        return os.path.join(settings.STATIC_ROOT, 'img', 'data', str(self.id))


class Scan(models.Model):
    id = models.AutoField(primary_key=True)
    old_print = models.ForeignKey('OldPrint')
    page_number = models.IntegerField()
    format = models.CharField(max_length=8, )

    @property
    def file_name(self):
        return '.'.join([str(self.page_number), self.format])

    @property
    def path(self):
        return os.path.join(self.old_print.directory, str(self.file_name))

    def set_image(self, image):
        with open(self.path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)
