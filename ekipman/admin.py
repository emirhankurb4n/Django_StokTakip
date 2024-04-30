from django.contrib import admin
from ekipman.models import *
from kategori.models import *
from konum.models import *
from makine.models import *
from tedarikci.models import *
from users.models import *


admin.site.register(Ekipman)
admin.site.register(EkipmanTuru)
admin.site.register(Konum)
admin.site.register(Makine)
admin.site.register(Tedarikci)
admin.site.register(CustomUser)
admin.site.register(HataTalep)
