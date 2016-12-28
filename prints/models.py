import os

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


# Create your models here.


class OldPrint(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, verbose_name='właściciel')
    title_page = models.ForeignKey('Scan', null=True, verbose_name='strona tytułowa')
    # author = models.CharField(max_length=2, blank=True)
    # lp = models.CharField(max_length=3, blank=True)
    title = models.CharField(max_length=1024, blank=True, verbose_name='tytuł')
    title_page_content = models.TextField(blank=True, verbose_name='zawartość strony tytułowej')
    title_variant = models.CharField(max_length=256, blank=True, verbose_name='wariant tytułu')
    # ???
    author_khw = models.CharField(max_length=64, blank=True, verbose_name='autor khw')
    # ???
    author_doc = models.CharField(max_length=64, blank=True, verbose_name='autor dokumentu')
    publication_place = models.CharField(max_length=32, blank=True, verbose_name='miejsce wydania')
    publisher_name = models.CharField(max_length=128, blank=True, verbose_name='wydawca')
    publication_date = models.DateField(blank=True, verbose_name='data wydania')
    printing_place = models.CharField(max_length=32, blank=True, verbose_name='miejsce wydruku')
    printing_house_name = models.CharField(max_length=128, blank=True, verbose_name='drukarnia')
    printing_date = models.DateField(blank=True, verbose_name='data wydruku')
    number_of_pages = models.IntegerField(blank=True, verbose_name='ilość stron')
    designation_illustration = models.CharField(max_length=32, blank=True, verbose_name='oznaczenia ilustracji')
    bibliography_format = models.CharField(max_length=32, blank=True, verbose_name='format bibliografii')
    # ???
    ownership_entries = models.CharField(max_length=512, blank=True, verbose_name='wpisy własnościowe')
    figerprint = models.CharField(max_length=64, blank=True, verbose_name='fingerprint')
    other_information = models.TextField(blank=True, verbose_name='inne informacje')
    co_founder = models.CharField(max_length=128, blank=True, verbose_name='współtwórca')
    keywords = models.CharField(max_length=256, blank=True, verbose_name='słowa kluczowe')
    source_type = models.CharField(max_length=128, blank=True, verbose_name='typ źródła')
    resource_identifier = models.CharField(max_length=16, blank=True, verbose_name='identyfikator zasobu')
    e_format = models.CharField(max_length=16, blank=True, verbose_name='elektroniczny format')
    source = models.CharField(max_length=512, blank=True, verbose_name='źródło')
    language_code = models.CharField(max_length=16, blank=True, verbose_name='kod języka')
    language = models.CharField(max_length=32, blank=True, verbose_name='język')
    bookbinding_block = models.CharField(max_length=16, blank=True, verbose_name='blok introligatorski')
    signature = models.CharField(max_length=16, blank=True, verbose_name='sygnatura')
    laws = models.CharField(max_length=16, blank=True, verbose_name='prawa')
    # ???
    daten_from = models.DateField(blank=True, verbose_name='datan od')
    daten_to = models.DateField(blank=True, verbose_name='datan_do')

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
