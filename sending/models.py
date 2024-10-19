from django.db import models


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email")
    fio = models.CharField(
        max_length=100,
        verbose_name="ФИО",
        help_text="Введите ФИО клиента",
    )
    comment = models.TextField(
        verbose_name="Комментарий", help_text="Введите комментарий"
    )

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.fio


class Mailing(models.Model):
    date_time = models.DateTimeField(
        verbose_name="Дата и время отправки",
        help_text="Введите дату и время отправки",
        blank=True,
        null=True,
    )

    periodicity = models.CharField(
        max_length=10,
        verbose_name="Периодичность",
        help_text="Введите периодичность рассылки",
    )

    status = models.CharField(
        max_length=10,
        verbose_name="Статус",
        help_text="Введите статус рассылки",
    )

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

    def __str__(self):
        return self.status


class Message(models.Model):
    subject = models.CharField(
        max_length=10,
        verbose_name="Тема письма",
        help_text="Введите тему письма",
    )

    body = models.TextField(
        verbose_name="Тело письма",
        help_text="Введите текст письма",
    )

    class Meta:
        verbose_name = "Сообщение для рассылки"
        verbose_name_plural = "Сообщения для рассылки"

    def __str__(self):
        return self.subject


class Attempt(models.Model):
    date_time = models.DateTimeField(
        verbose_name="Дата и время последней попытки",
        help_text="Введите дату и время последней попытки",
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=10,
        verbose_name="Статус",
        help_text="Введите статус попытки",
    )

    server_response = models.CharField(
        verbose_name="Ответ почтового сервера",
        help_text="Введите ответ почтового сервера",
    )

    class Meta:
        verbose_name = "Ответ почтового сервера"
        verbose_name_plural = "Ответы почтового сервера"

    def __str__(self):
        return self.status
