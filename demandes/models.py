from django.db import models
from django.forms import ValidationError

class RequestDocument(models.Model):
    reference = models.CharField(max_length=20, unique=True, editable=False,default='J12')
    nom = models.CharField(max_length=100, default='Joe')
    prenoms = models.CharField(max_length=100, default='Doe')
    email = models.EmailField(default='total@gmail.com')
    poste = models.CharField(max_length=100, default='Assistant IT')
    departement = models.CharField(
        max_length=100,
        choices=[
            ('direction_reseau', 'Direction Réseau'),
            ('direction_financiere', 'Direction Financière'),
            ('direction_commerciale', 'Direction Commerciale'),
            ('direction_hseq', 'Direction HSEQ'),
            ('direction_rhj', 'Direction des Ressources Humaines et Juridique'),
        ],
        default='direction_financière'
    )
    document_type = models.CharField(
        max_length=100,
        choices=[
            ('attestation_travail', 'Attestation de Travail'),
            ('attestation_conges', 'Attestation de Congés'),
            ('ordre_mission', 'Ordre de Mission'),
            ('accord_tripartite', 'Accord Tripartite'),
            ('pret_depannage', 'Prêt Dépannage'),
        ]
    )
    STATUT_CHOICES = [
        ('en_cours', 'En cours'),
        ('valide', 'Validé'),
        ('refuse', 'Refusé'),
    ]
    motif = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    resume_date = models.DateField(blank=True, null=True)
    mission_location = models.CharField(max_length=255, blank=True, null=True)
    mission_object = models.TextField(blank=True, null=True)
    invitation_letter = models.FileField(upload_to='invitations/', blank=True, null=True)
    ticket_copy = models.FileField(upload_to='tickets/', blank=True, null=True)
    bank_choice = models.CharField(max_length=100, blank=True, null=True)
    amortization_table = models.FileField(upload_to='amortizations/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_cours')
     # Champs spécifiques à Prêt Dépannage
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monthly_payment = models.IntegerField(blank=True, null=True)
    repayment_start_date = models.DateField(blank=True, null=True)
    repayment_duration_months = models.PositiveIntegerField(blank=True, null=True)  # < 12 mois

    def clean(self):
        """Validation supplémentaire pour les prêts dépannage."""
        if self.document_type == 'pret_depannage':
            if not self.loan_amount:
                raise ValidationError("Le montant demandé est obligatoire pour un prêt dépannage.")
            if not self.monthly_payment:
                raise ValidationError("La mensualité est obligatoire pour un prêt dépannage.")
            if not self.repayment_start_date:
                raise ValidationError("La date de début de remboursement est obligatoire pour un prêt dépannage.")
            if self.repayment_duration_months is None or self.repayment_duration_months > 12:
                raise ValidationError("La durée de remboursement doit être inférieure ou égale à 12 mois.")

    def __str__(self):
        return f"{self.nom} {self.prenoms} - {self.document_type}"
    
    def toggle_statut(self):
        if self.statut == 'en_cours':
            self.statut = 'valide'
        elif self.statut == 'valide':
            self.statut = 'refuse'
        else:
            self.statut = 'en_cours'
        self.save()
