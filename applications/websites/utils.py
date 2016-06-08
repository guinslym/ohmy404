import json
from .models import website404

def increment_the_total_views():
    websites = website404.objects.all()
    for sites in websites:
        pass

def write_to_a_file():
    pass
