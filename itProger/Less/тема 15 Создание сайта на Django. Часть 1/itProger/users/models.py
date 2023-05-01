from django.db import models
from django.contrib.auth.models import User
from PIL import Image


CHOICES = (('male', 'мужской пол'), ('female', 'женский пол'))

# name = forms.MultipleChoiceField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя',
                            default='default.png',
                            upload_to='user_images'
                            )
    gender = models.CharField(
        'пол', default='male', max_length=10, choices=CHOICES)
    sender = models.BooleanField('подписка на рассылку',
                                 default=1)

    def __str__(self):
        return f'Профаил пользователя {self.user.username}'

        def save(self, *args, **kwargs):
            super().save()
            image = Image.open(self.img.path)
            if image.height > 256 or image.width > 256:
                resize = (256, 256)
                image.thumbnail(resize)
                image.save(self.img.path)

                class Meta:
                    verbose_name = 'Профаил'
                    verbose_name_plural = 'Профаилы'
