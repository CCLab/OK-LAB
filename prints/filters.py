#!/usr/bin/python
# coding: utf-8
from collections import OrderedDict

from django_filters import FilterSet

from prints.models import OldPrint


class PrintsFilter(FilterSet):
    class Meta:
        model = OldPrint
        fields = OrderedDict((
            ("title", ['contains']),
            ("title_variant", []),
            ("title_page_content", []),
            ("author_khw", ['contains']),
            ("author_doc", []),
            ("publication_place", []),
            ("publisher_name", []),
            ("publication_date", ['lt', 'gt']),
            ("printing_place", []),
            ("printing_house_name", []),
            ("printing_date", []),
            ("number_of_pages", ['gt', 'lt']),
            ("designation_illustration", []),
            ("bibliography_format", []),
            ("ownership_entries", []),
            ("co_founder", []),
            ("keywords", ['contains']),
            ("source_type", []),
            ("resource_identifier", []),
            ("e_format", []),
            ("source", []),
            ("language_code", []),
            ("language", []),
            ("bookbinding_block", []),
            ("signature", []),
            ("laws", []),
        ))
