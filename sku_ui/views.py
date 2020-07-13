# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def firstpage(request):
    """

    :param request:
    :return: Serves the index.html page
    """
    return render(request, template_name='index.html')