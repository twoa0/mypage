from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^about/', include('introduction.urls', namespace='about')),
    url(r'^admin/', admin.site.urls),

]

urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)