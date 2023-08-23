"""

API endpoint for Kicad REST API library.

This plugin supplies the endpoints and data needed for KiCad to display selected categories and their
corresponding parts within the Kicad environment.

"""
import datetime
import os

from django.conf.urls import url
from django.http import JsonResponse, HttpResponse

from django.urls import include, re_path, path

from plugin import InvenTreePlugin
from plugin.mixins import UrlsMixin, AppMixin, SettingsMixin

from django.utils.translation import gettext_lazy as _

from plugins.inventree_kicad.viewsets import router_kicad, PartsPreViewList
from .version import KICAD_PLUGIN_VERSION
from . import views

# ---------------------------- KiCad API Endpoint Plugin --------------------------------------------------
class KiCadLibraryPlugin(UrlsMixin, AppMixin, InvenTreePlugin):
    AUTHOR = "Andre Iwers"

    DESCRIPTION = _(
        "KiCad EDA conform API endpoint for KiCad's parts library tool. This plugin provides metadata only "
        "and requires matching symbol and footprint libraries within the KiCad EDA.")

    VERSION = KICAD_PLUGIN_VERSION

    TITLE = "KiCad Library Endpoint"
    SLUG = "kicad-library-plugin"
    NAME = "KiCadLibraryPlugin"

    PUBLISH_DATE = datetime.date(2023, 6, 9)
    WEBSITE = "https://www.aioz.com.au"

    MIN_VERSION = '0.11.0'

    os.environ['KICAD_PLUGIN_GET_SUB_PARTS'] = 'True'

    def setup_urls(self):
        """Returns the URLs defined by this plugin."""

        return [
            re_path(r'settings.json', views.kicad_settings, name="kicad_Settings"),
            re_path('^parts/category/(?P<id>.+).json$', PartsPreViewList.as_view()),
            url(r'', include(router_kicad.urls)),
        ]