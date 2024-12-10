from django.urls import path
from . import views

app_name = 'demandes' 

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.dashboard_view, name='dashboard'),
    path('demande/ajouter/', views.create_request, name='create_request'),
    path('acces-rh/', views.dashboard_view, name='dashboard'),
    path('demandes/', views.demandes_list, name='demandes_list'),
    path('demande/<int:pk>/', views.demande_detail, name='demande_detail'),
    path('demande/<int:pk>/modifier/', views.update_request, name='update_request'),
    path('demande/<int:pk>/supprimer/', views.delete_request, name='delete_request'),
    path('mes-demandes/', views.mes_demandes, name='mes_demandes'),
    path('rh-access/', views.rh_access, name='rh_access'),
    # path('update_statut/<int:demande_id>/<str:statut>/', views.update_statut, name='update_statut'),
    path('toggle_statut/<int:demande_id>/', views.toggle_statut, name='toggle_statut'),



]

# urlpatterns = [
#     # path('', home, name='home'),
#     # path('dashboard/', dashboard, name='dashboard'),
#     # path('demande_list/', DemandeListView.as_view(), name='demande_list'),
#     # path('demande/add/<int:document_id>/', DemandeAddView.as_view(), name='demande_add'),
#     # path('banques/', BanqueListView.as_view(), name='banque_list'),
#     # path('banques/add/', BanqueAddView.as_view(), name='banque_add'),
#     # path('banques/edit/<int:pk>/', BanqueEditView.as_view(), name='banque_update'),
#     # path('departements/', DepartementListView.as_view(), name='departement_list'),
#     # path('departements/add/', DepartementAddView.as_view(), name='departement_add'),
#     # path('departements/edit/<int:pk>/', DepartementEditView.as_view(), name='departement_update'),
    
# ]
