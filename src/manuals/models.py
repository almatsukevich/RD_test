from django.db import models
# from catalog.models import Employee


# class Level(models.Model):
#     name = models.CharField(
#         verbose_name = "Наименование уровня",
#         max_length=10)
            
#     class Meta:
#         verbose_name = "Уровень"
#         verbose_name_plural = "Уровни"

# class Chief(models.Model):
#     chief = models.ForeignKey(
#         Employee,
#         on_delete=models.PROTECT,
#         related_name='chief',
#         verbose_name = "Руководитель")
            
#     class Meta:
#         verbose_name = "Руководитель"
#         verbose_name_plural = "Руководители"