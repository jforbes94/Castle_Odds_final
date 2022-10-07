from django.contrib import admin
from .models import Odds
from .models import Games
from .models import MLB
from .models import NBA
from .models import NHL

admin.site.register(Odds)
admin.site.register(Games)
admin.site.register(MLB)
admin.site.register(NBA)
admin.site.register(NHL)