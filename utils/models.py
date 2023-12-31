import datetime
import posixpath

from django.conf import settings


def get_image_upload_path(instance, filename):
    return posixpath.join(datetime.datetime.now().strftime(settings.SHELTERSEARCH_IMAGE_FOLDER), filename)
