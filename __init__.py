from django.conf import settings
from .helpers import IonicPush

IonicPush.config(settings.IONICPUSH_APP_ID, settings.IONICPUSH_PRIVATE_KEY)