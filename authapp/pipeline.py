from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode
from urllib.parse import urlunparse
from django.utils import timezone
from social_core.exceptions import AuthForbidden
import requests
from .models import ShopUserProfile