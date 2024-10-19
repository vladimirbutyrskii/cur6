# Generated by Django 5.1.2 on 2024-10-19 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_time",
                    models.DateTimeField(
                        blank=True,
                        help_text="Введите дату и время последней попытки",
                        null=True,
                        verbose_name="Дата и время последней попытки",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        help_text="Введите статус попытки",
                        max_length=10,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "server_response",
                    models.CharField(
                        help_text="Введите ответ почтового сервера",
                        verbose_name="Ответ почтового сервера",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ответ почтового сервера",
                "verbose_name_plural": "Ответы почтового сервера",
            },
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                (
                    "fio",
                    models.CharField(
                        help_text="Введите ФИО клиента",
                        max_length=100,
                        verbose_name="ФИО",
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        help_text="Введите комментарий", verbose_name="Комментарий"
                    ),
                ),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
            },
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_time",
                    models.DateTimeField(
                        blank=True,
                        help_text="Введите дату и время отправки",
                        null=True,
                        verbose_name="Дата и время отправки",
                    ),
                ),
                (
                    "periodicity",
                    models.CharField(
                        help_text="Введите периодичность рассылки",
                        max_length=10,
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        help_text="Введите статус рассылки",
                        max_length=10,
                        verbose_name="Статус",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subject",
                    models.CharField(
                        help_text="Введите тему письма",
                        max_length=10,
                        verbose_name="Тема письма",
                    ),
                ),
                (
                    "body",
                    models.TextField(
                        help_text="Введите текст письма", verbose_name="Тело письма"
                    ),
                ),
            ],
            options={
                "verbose_name": "Сообщение для рассылки",
                "verbose_name_plural": "Сообщения для рассылки",
            },
        ),
    ]