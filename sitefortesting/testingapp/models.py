from django.db import models

# Create your models here.
class Tests(models.Model):
    test_name = models.CharField(max_length=250,verbose_name='Название теста')
    WorkTime = models.IntegerField(verbose_name='Время выполнения (мин)')
    questions = models.ForeignKey('Questions', related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.Text

class Questions(models.Model):
    question = models.TextField(verbose_name='Текст вопроса')
    answer = models.BooleanField()

    def __str__(self):
        return self.Text