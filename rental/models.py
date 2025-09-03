from django.db import models

class Equipment(models.Model):
    name = models.CharField("Название", max_length=255)
    price = models.DecimalField("Цена за смену", max_digits=10, decimal_places=2)
    image = models.ImageField("Фото", upload_to="equipment/")
    description = models.TextField("Описание", blank=True)

    # Характеристики
    max_load = models.CharField("Максимальная грузоподъёмность", max_length=100, blank=True)
    boom_length = models.CharField("Максимальная длина стрелы", max_length=100, blank=True)
    max_height = models.CharField("Максимальная высота подъёма", max_length=100, blank=True)
    axles = models.CharField("Количество осей", max_length=50, blank=True)
    wheel_formula = models.CharField("Колёсная формула", max_length=50, blank=True)
    dimensions = models.CharField("Габариты", max_length=100, blank=True)

    # Дополнительно: свободный блок характеристик
    extra_specs = models.TextField("Дополнительные характеристики", blank=True,
                                   help_text="Можно вносить произвольный список характеристик в свободной форме")

    class Meta:
        verbose_name = "Техника"
        verbose_name_plural = "Техника"

    def __str__(self):
        return self.name


class Request(models.Model):
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("Email")
    phone = models.CharField("Телефон", max_length=20)
    message = models.TextField("Комментарий", blank=True)
    created_at = models.DateTimeField("Дата отправки", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"{self.name} ({self.phone})"
