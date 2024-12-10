from .models import RequestDocument
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RequestDocumentForm
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.http import JsonResponse



import uuid

def dashboard_view(request):
    if not request.session.get('rh_access'):
        messages.error(request, "Accès interdit. Veuillez entrer le mot de passe RH.")
        return redirect('demandes:rh_access')
    total_demandes = RequestDocument.objects.count()
    demandes_approuvees = RequestDocument.objects.filter(document_type='Attestation de Travail').count()
    demandes_refusees = RequestDocument.objects.filter(document_type='Accord Tripartite').count()

    context = {
        'total_demandes': total_demandes,
        'demandes_approuvees': demandes_approuvees,
        'demandes_refusees': demandes_refusees,
    }
    return render(request, 'demandes/pages/dashboard.html', context)


def home(request):
    return render(request, 'demandes/pages/home.html')

def generate_reference():
    return str(uuid.uuid4())[:8]

def create_request(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenoms = request.POST.get('prenoms')
        email = request.POST.get('email')
        poste = request.POST.get('poste')
        departement= request.POST.get('departement')
        document_type = request.POST.get('document_type')
        motif = request.POST.get('motif', '')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        resume_date = request.POST.get('resume_date')
        mission_location = request.POST.get('mission_location', '')
        mission_object = request.POST.get('mission_object', '')
        invitation_letter = request.FILES.get('invitation_letter')
        ticket_copy = request.FILES.get('ticket_copy')
        bank_choice = request.POST.get('bank_choice', '')
        other_bank = request.POST.get('other_bank', '')
        amortization_table = request.FILES.get('amortization_table')

        reference = generate_reference()

        # Si l'utilisateur a choisi "Autre", on utilise le champ other_bank
        if bank_choice == 'Autre':
            bank_choice = other_bank

        # Créer la demande
        RequestDocument.objects.create(
            reference=reference,
            nom=nom,
            prenoms=prenoms,
            email=email,
            poste=poste,
            departement=departement,
            document_type=document_type,
            motif=motif,
            start_date=start_date,
            end_date=end_date,
            resume_date=resume_date,
            mission_location=mission_location,
            mission_object=mission_object,
            invitation_letter=invitation_letter,
            ticket_copy=ticket_copy,
            bank_choice=bank_choice,
            amortization_table=amortization_table,
        )

        messages.success(request, "Demande soumise avec succès.")
        return redirect('demandes:home')

    return render(request, 'demandes/pages/create_request.html')

def toggle_statut(request, demande_id):
    try:
        demande = get_object_or_404(RequestDocument, pk=demande_id)
        demande.toggle_statut()
        return JsonResponse({'statut': demande.statut}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def demandes_list(request):
    if not request.session.get('rh_access'):
        return HttpResponseForbidden("Accès interdit. Veuillez entrer le mot de passe RH.")
    
    demandes = RequestDocument.objects.all()
    return render(request, 'demandes/pages/demandes_list.html', {'demandes': demandes})

def update_statut(request, demande_id, statut):
    demande = get_object_or_404(RequestDocument, pk=demande_id)
    if statut not in ['en_cours', 'valide', 'refuse']:
        messages.error(request, "Statut invalide.")
        return redirect('demandes:demandes_list')
    
    demande.statut = statut
    demande.save()
    messages.success(request, f"Le statut a été mis à jour : {statut.capitalize()}.")
    return redirect('demandes:demandes_list')

def demande_detail(request, pk):
    demande = get_object_or_404(RequestDocument, pk=pk)
    return render(request, 'demandes/pages/demande_details.html', {'demande': demande})

def update_request(request, pk):
    demande = get_object_or_404(RequestDocument, pk=pk)
    if request.method == 'POST':
        form = RequestDocumentForm(request.POST, request.FILES, instance=demande)
        if form.is_valid():
            form.save()
            messages.success(request, "Demande mise à jour avec succès.")
            return redirect('demandes:demandes_list')
    else:
        form = RequestDocumentForm(instance=demande)

    return render(request, 'demandes/pages/create_request.html', {'form': form})

def delete_request(request, pk):
    demande = get_object_or_404(RequestDocument, pk=pk)
    if request.method == 'POST':
        demande.delete()
        messages.success(request, "Demande supprimée avec succès.")
        return redirect('demandes/pages:demandes_list')

    return render(request, 'demandes/pages/demande_delete.html', {'demande': demande})

def mes_demandes(request):
    demandes = None
    email = request.GET.get('email')

    if email:
        # Rechercher les demandes par le champ `email` directement
        demandes = RequestDocument.objects.filter(email=email)

        if not demandes.exists():
            message = "Aucune demande trouvée pour cet email."
        else:
            message = None
    else:
        message = "Veuillez entrer votre email pour voir vos demandes."

    return render(request, 'demandes/pages/mes_demandes.html', {
        'demandes': demandes,
        'email': email,
        'message': message,
    })

RH_PASSWORD = "motdepasseRH"

def rh_access(request):
    if request.method == "POST":
        password = request.POST.get("password")
        if password == RH_PASSWORD:
            # Stocker l'état d'accès dans la session
            request.session['rh_access'] = True
            messages.success(request, "Accès accordé. Bienvenue dans la section RH.")
            return redirect('demandes:demandes_list')
        else:
            messages.error(request, "Mot de passe incorrect. Veuillez réessayer.")
            return redirect('demandes:rh_access')
    return render(request, 'demandes/pages/rh_access.html')

