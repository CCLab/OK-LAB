#!/usr/bin/python
# coding: utf-8
from django_filters import FilterSet

from prints.models import OldPrint


class PrintsFilter(FilterSet):
    class Meta:
        model = OldPrint
        fields = [
            "title",
            "title_variant",
            "title_page_content",
            "author_khw",
            "author_doc",
            "publication_place",
            "publisher_name",
            "publication_date",
            "printing_place",
            "printing_house_name",
            "printing_date",
            "number_of_pages",
            "designation_illustration",
            "bibliography_format",
            "ownership_entries",
            "co_founder",
            "keywords",
            "source_type",
            "resource_identifier",
            "e_format",
            "source",
            "language_code",
            "language",
            "bookbinding_block",
            "signature",
            "laws",
        ]

