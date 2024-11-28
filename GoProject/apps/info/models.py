from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Tours(models.Model):
    image = models.ImageField(verbose_name='Фото тура')
    title = models.CharField(max_length=30, verbose_name='Название тура')
    description = models.CharField(max_length=250, verbose_name='Описание тура')
    price = models.FloatField(verbose_name='Цена тура')
    button_text = models.CharField(max_length=20, verbose_name='Текст кнопки')
    
    class Meta:
        verbose_name = 'Каталог туров'
        verbose_name_plural = 'Каталог туров'
        
        
    def __str__(self) -> str:
        return self.title
    
    
class VisaGo(models.Model):
    country_icon = models.ImageField(verbose_name='Иконка страны')
    time = models.CharField(max_length=250, verbose_name='Текст о сроке')
    price = models.FloatField(verbose_name='Цена визы')
    button_text = models.CharField(max_length=20, verbose_name='Текст кнопки')
    
    class Meta:
        verbose_name = 'Визовая поддержка VisaGo'
        verbose_name_plural = 'Визовая поддержка VisaGo'
        
    def __str__(self) -> str:
        return self.country_icon
    
    
class EasyGO(models.Model):
    image_icon = models.ImageField(verbose_name='Изображение')
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    button_more = models.CharField(max_length=15, verbose_name='Кнопка "Узнать подробнее"')
    
    class Meta:
        verbose_name = 'Доставка товаров из Китая EasyGo'
        verbose_name_plural = 'Доставка товаров из Китая EasyGo'
        
    def __str__(self) -> str:
        return self.title
    
    
class Reviews(models.Model):
    photo = models.ImageField(verbose_name='Фото клиентов')
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст отзыва')
    video = models.FileField(upload_to='', verbose_name='Видео')
    video_button = models.CharField(max_length=30, verbose_name='Кнопка "Смотреть видео"')
    
    class Meta:
        verbose_name = 'Отзывы клиентов'
        verbose_name_plural = 'Отзывы клиентов'
        
    def __str__(self) -> str:
        return self.title
    
    
class Contacts(models.Model):
    phone_number = PhoneNumberField(max_length=13, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта')
    address = models.CharField(max_length=50, verbose_name='Адрес')
    pictogram = models.ImageField(verbose_name='Пиктограмма', null=True,)
    map_link = models.URLField(verbose_name='Ссылка на карту')
    
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
        
    def __str__(self) -> str:
        return self.email
    
    
