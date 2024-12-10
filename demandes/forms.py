from django import forms
from .models import RequestDocument


class RequestDocumentForm(forms.ModelForm):
    class Meta:
        model = RequestDocument
        fields = '__all__'

    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        if isinstance(start_date, str) and (not start_date.strip() or start_date.isspace()):
            return None
        return start_date

    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        if isinstance(end_date, str) and (not end_date.strip() or end_date.isspace()):
            return None
        return end_date

    def clean_resume_date(self):
        resume_date = self.cleaned_data.get('resume_date')
        if isinstance(resume_date, str) and (not resume_date.strip() or resume_date.isspace()):
            return None
        return resume_date







# from django import forms

# from .models import *


# # class CollaborateurForm(forms.ModelForm):
# #     class Meta:
# #         model = Demande
# #         fields = ['collaborateur', 'document']

# class CollaborateurForm(forms.ModelForm):
#     departement = forms.ModelChoiceField(
#         queryset=Departement.objects.all(), 
#         empty_label="Sélectionnez un département",
#         widget=forms.Select(attrs={'class': 'form-control'})
        
#     )

#     class Meta:
#         model = Collaborateur
#         fields = ['nom', 'prenoms', 'email', 'poste', 'departement']
           
# class AttestationTravailForm(forms.ModelForm):
#     class Meta:
#         model = Demande
#         fields = ['motif']

# class AttestationCongesForm(forms.ModelForm):
#     class Meta:
#         model = Demande
#         fields = ['periode_conge_debut', 'periode_conge_fin', 'date_reprise_service']

# class OrdreMissionForm(forms.ModelForm):
#     class Meta:
#         model = Demande
#         fields = ['lieu_mission', 'objet_mission', 'lettre_invitation', 'billet']

# class AccordTripartiteForm(forms.ModelForm):
#     banque = forms.ModelChoiceField(
#      queryset=Banque.objects.all(),
#     )
#     class Meta:
#         model = Demande
#         fields = ['banque', 'tableau_amortissement']

# class BanqueForm(forms.ModelForm):
#     class Meta:
#         model = Banque
#         fields = ['nom']
#         widgets = {
#             'nom': forms.TextInput(attrs={'class': 'form-control'}),
#         }

# class DepartementForm(forms.ModelForm):
#     class Meta:
#         model = Departement
#         fields = ['nom']
#         widgets = {
#             'nom': forms.TextInput(attrs={'class': 'form-control'}),
#         }
