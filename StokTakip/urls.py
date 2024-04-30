"""
URL configuration for StokTakip project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as users_views
from ekipman import views as ekipman_views
from kategori import views as kategori_views
from konum import views as konum_views
from tedarikci import views as tedarikci_views
from makine import views as makine_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),

    #users app
    path('', users_views.LoginView, name='Login'),
    path('logout', users_views.LogoutView, name='Logout'),
    path('myProfile', users_views.MyProfileView, name='MyProfile'),
    
    #ekipman app
    path('home', ekipman_views.EkipmanIndex, name='Home'),
    path('detailsEkipman/<int:pk>/', ekipman_views.EkipmanDetailsView.as_view(), name='EkipmanDetails'),
    path('createEkipman', ekipman_views.EkipmanCreateView, name='CreateEkipman'),
    path('deleteEkipman/<int:pk>/', ekipman_views.EkipmanDeleteView, name="DeleteEkipman"),
    path('updateEkipman/<int:id>/', ekipman_views.EkipmanUpdateView, name="UpdateEkipman"),

    #kategori app
    path('kategoriIndex', kategori_views.KategoriListView, name='KategoriIndex'),
    path('createKategori', kategori_views.KategoriCreateView, name='CreateKategori'),
    path('updateKategori/<int:id>/', kategori_views.KategoriUpdateView, name='UpdateKategori'),
    path('deleteKategori/<int:id>/', kategori_views.KategoriDeleteView, name='DeleteKategori'),

    #tedarikci app
    path('tedarikciIndex', tedarikci_views.ListTedarikciVİew, name='TedarikciIndex'),
    path('createTedarikci', tedarikci_views.CreateTedarikciView, name='CreateTedarikci'),
    path('updateTedarikci/<int:id>/', tedarikci_views.UpdateTedarikciView, name='UpdateTedarikci'),
    path('deleteTedarikci/<int:pk>/', tedarikci_views.DeleteTedarikciView, name='DeleteTedarikci'),

    #makine app
    path('makineIndex', makine_views.ListMakineVİew, name='MakineIndex'),
    path('createMakine', makine_views.CreateMakineView, name='CreateMakine'),
    path('updateMakine/<int:id>/', makine_views.UpdateMakineView, name='UpdateMakine'),
    path('deleteMakine/<int:pk>/', makine_views.DeleteMakineView, name='DeleteMakine'),

    #konum app
    path('konumIndex', konum_views.ListKonumVİew, name='KonumIndex'),
    path('createKonum', konum_views.CreateKonumView, name='CreateKonum'),
    path('updateKonum/<int:id>/', konum_views.UpdateKonumView, name='UpdateKonum'),
    path('deleteKonum/<int:pk>/', konum_views.DeleteKonumView, name='DeleteKonum'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)