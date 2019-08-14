from django.contrib import admin
from .models import Posttop
from .models import Posttopsecond
from .models import Post
from .models import Postlive
from .models import Postslot

admin.site.register(Posttop)
admin.site.register(Posttopsecond)
admin.site.register(Post)
admin.site.register(Postlive)
admin.site.register(Postslot)