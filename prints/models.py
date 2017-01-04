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
    publication_date = models.DateField(null=True, blank=True, verbose_name='data wydania')
    printing_place = models.CharField(max_length=32, blank=True, verbose_name='miejsce wydruku')
    printing_house_name = models.CharField(max_length=128, blank=True, verbose_name='drukarnia')
    printing_date = models.DateField(null=True, blank=True, verbose_name='data wydruku')
    number_of_pages = models.IntegerField(verbose_name='ilość stron')
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
    daten_from = models.DateField(null=True, blank=True, verbose_name='datan od')
    daten_to = models.DateField(null=True, blank=True, verbose_name='datan_do')

    @property
    def path(self):
        return os.path.join(settings.STATIC_ROOT, 'img', 'data', str(self.id))

    @property
    def static(self):
        return '/'.join(['img', 'data', str(self.id)])

    @property
    def dict(self):
        return {
            "id": self.id,
            "title_page": self.title_page.static if self.title_page else settings.DEFAULT_TITLE_PAGE,
            "title": self.title,
            "title_page_content": self.title_page_content,
            "title_variant": self.title_variant,
            "author_khw": self.author_khw,
            "author_doc": self.author_doc,
            "publication_place": self.publication_place,
            "publisher_name": self.publisher_name,
            "publication_date": self.publication_date,
            "printing_place": self.printing_place,
            "printing_house_name": self.printing_house_name,
            "printing_date": self.printing_date,
            "number_of_pages": self.number_of_pages,
            "designation_illustration": self.designation_illustration,
            "bibliography_format": self.bibliography_format,
            "ownership_entries": self.ownership_entries,
            "figerprint": self.figerprint,
            "other_information": self.other_information,
            "co_founder": self.co_founder,
            "keywords": self.key_words,
            "source_type": self.source_type,
            "resource_identifier": self.resource_identifier,
            "e_format": self.e_format,
            "source": self.source,
            "language_code": self.language_code,
            "language": self.language,
            "bookbinding_block": self.bookbinding_block,
            "signature": self.signature,
            "laws": self.laws,
            "daten_from": self.daten_from,
            "daten_to": self.daten_to,
        }

    @property
    def smart_dict(self):
        return {
            "id": self.id,
            "title_page": self.title_page.static if self.title_page else settings.DEFAULT_TITLE_PAGE,
            "title": self.title,
            # "title_page_content": self.title_page_content,
            "author_khw": self.author_khw,
            "publication_date": self.publication_date if self.publication_date else 'nieznana',
        }

    @property
    def key_words(self):
        return self.keywords.split(' ')

class Scan(models.Model):
    id = models.AutoField(primary_key=True)
    old_print = models.ForeignKey('OldPrint')
    page_number = models.IntegerField()
    format = models.CharField(max_length=8, )

    @property
    def file_name(self):
        return '.'.join([str(self.page_number), self.format])

    @property
    def static(self):
        return '/'.join([self.old_print.static, str(self.file_name)])

    @property
    def path(self):
        return os.path.join(self.old_print.path, str(self.file_name))

