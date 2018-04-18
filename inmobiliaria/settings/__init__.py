from inmobiliaria.settings.production import *

try:
    from inmobiliaria.settings.local import *
except expression as identifier:
    pass