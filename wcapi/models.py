from django.db import models

class Themes(models.Model):
    id_themes = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

class Category(models.Model):
    id_category = models.CharField(max_length=255)
    theme_name = models.CharField(max_length=255)
    icons = models.CharField(max_length=255)
    premium = models.CharField(max_length=255)

    def __str__(self):
        return self.theme_name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Theme(models.Model):
    id_theme = models.CharField(max_length=255)
    premium = models.CharField(max_length=255)
    preview = models.CharField(max_length=255)
    icons = models.CharField(max_length=255)
    wallpaper = models.CharField(max_length=255)
    widgets = models.CharField(max_length=255)

    def __str__(self):
        return self.premium

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Тема"

class Widgets(models.Model):
    id_Widgets = models.CharField(max_length=255)
    premium = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    preview = models.CharField(max_length=255)
    widgets = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Виджет"
        verbose_name_plural = "Виджеты"

class Icon(models.Model):
    id_Icon = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    preview = models.CharField(max_length=255)
    icons = models.CharField(max_length=255)
    wallpaper = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Иконка"
        verbose_name_plural = "Иконки"

class Wallpapers(models.Model):
    id_Wallpapers = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    wallpaper = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Обои"
        verbose_name_plural = "Обои"