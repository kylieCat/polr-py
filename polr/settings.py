import os
import sys

from .utils import print_error


# Required settings
try:
    POLR_API_KEY = os.environ.get("POLR_API_KEY", "1234")
    POLR_URL = os.environ.get("POLR_URL", "http://polr.example.com")
except KeyError as err:
    print_error(f"missing required env var: {err}")
    sys.exit(1)
