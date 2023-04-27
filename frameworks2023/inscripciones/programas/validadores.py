from django.core.validators import FileExtensionValidator, RegexValidator

telefono_validador = RegexValidator(
    regex='^\d{10}$',
    message='El número de telefono tiene un formato inválido',
    code='telefono_invalido'
)