from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class Validate_password_latin:
    def __init__(self):
        self.alphabet = set('abcdefghiklmnopqrstuvwxyz')
    
    def validate(self, password, user=None):
        if self.alphabet.isdisjoint(password.lower()):
            raise ValidationError(_('Пароль должен содержать только латинские буквы или цифры'), code='invalid_password')
    def get_help_text(self):
        return _("The password must contain only Latin letters or numbers")