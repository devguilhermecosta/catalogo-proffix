from django.db import models


class Information(models.Model):
    name = models.CharField(max_length=100, verbose_name='nome')
    phone = models.CharField(max_length=50, verbose_name='telefone')
    fax = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    about = models.TextField(verbose_name='sobre a empresa')

    def __str__(self):
        return 'Informações da Empresa'

    class Meta:
        verbose_name = 'informação'
        verbose_name_plural = 'informações'


class Docs(models.Model):
    local_upload = 'docs/'
    company = models.ForeignKey(Information, on_delete=models.CASCADE)
    afe = models.FileField(upload_to=local_upload,
                           blank=True,
                           null=True,
                           )
    cnpj = models.FileField(upload_to=local_upload,
                            blank=True,
                            null=True,
                            )
    crt = models.FileField(upload_to=local_upload,
                           blank=True,
                           null=True,
                           )

    def __str__(self):
        return f'Documentos de {self.company.name}'

    class Meta:
        verbose_name = 'documento'
        verbose_name_plural = 'documentos'
