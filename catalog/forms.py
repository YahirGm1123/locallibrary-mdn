import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RenewBookForm(forms.Form):
    """Formulario para que un bibliotecario renueve libros."""
    renewal_date = forms.DateField(help_text="Ingrese una fecha entre hoy y 4 semanas (predeterminado 3 semanas).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Verifica que la fecha no sea en el pasado
        if data < datetime.date.today():
            raise ValidationError(_('Fecha inválida: la renovación no puede ser en el pasado.'))

        # Verifica que la fecha no sea más de 4 semanas en el futuro
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Fecha inválida: no se puede renovar por más de 4 semanas.'))

        # Siempre debes devolver los datos limpios
        return data