from django.db import models


class Employee(models.Model):
    name = models.CharField(
        verbose_name = "ФИО",
        max_length=40)

    position = models.ForeignKey(
        'Position',
        on_delete=models.PROTECT,
        verbose_name = "Должность",
        default=1)

    recruitment_date = models.DateField(
        verbose_name = "Дата приема на работу")
    
    salary = models.DecimalField(
        verbose_name = "Размер заработной платы", 
        max_digits=7, 
        decimal_places=2)

    payd_salary = models.DecimalField(
        verbose_name = "Выплаченная заработная плата", 
        max_digits=9, 
        decimal_places=2)

    level = models.ForeignKey(
        'Level',
        on_delete=models.PROTECT,
        related_name='employee',
        verbose_name = "Уровень",
        default=1)

    chief = models.ForeignKey(
        'Chief',
        on_delete=models.PROTECT,
        related_name='employee',
        verbose_name = "Начальник",
        blank=True,
        null=True)

    def __str__(self) ->str:
        return str(f"{self.position.name} - {self.name}")



    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"



class Position(models.Model):
    name = models.CharField(
        verbose_name = "Наименование должности",
        max_length=40)

    def __str__(self) ->str:
        return self.name    

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"



class Level(models.Model):
    name = models.CharField(
        verbose_name = "Наименование уровня",
        max_length=10)

    def __str__(self) ->str:
        return self.name   

    class Meta:
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"
    

class Chief(models.Model):
    chief = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        related_name='chiefs',
        verbose_name = "Руководитель")

    def __str__(self) ->str:
        return self.chief.__str__()  

    class Meta:
        verbose_name = "Руководитель"
        verbose_name_plural = "Руководители"