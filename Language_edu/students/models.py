from django.db import models

from .validators import real_age


MAX_NAME_LENGTH = 20


class Teacher(models.Model):
    first_name = models.CharField('Name', max_length=MAX_NAME_LENGTH)
    last_name = models.CharField('Surname', max_length=MAX_NAME_LENGTH)

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        if self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.first_name


class Student(models.Model):
    first_name = models.CharField('Name', max_length=MAX_NAME_LENGTH)
    last_name = models.CharField(
        'Surname', blank=True, max_length=MAX_NAME_LENGTH
    )
    birthday = models.DateField('Date of birth', validators=(real_age,))
    image = models.ImageField(
        upload_to='students/photos/',
        null=True,
        blank=True,
        default=None,
        verbose_name='photo',
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students',
        verbose_name='Teacher',
    )

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )

    def __str__(self):
        if self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.first_name
