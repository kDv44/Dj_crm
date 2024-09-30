import os
import pytest

from django.conf import settings

os.environ["DJANGO_SETTINGS_MODULE"] = "crm_service.settings"


@pytest.fixture(scope="session")
def django_db_setup():
    pass
