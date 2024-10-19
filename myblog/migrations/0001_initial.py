# Generated by Django 5.1 on 2024-08-31 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Myblog",
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
                    "title",
                    models.CharField(
                        help_text="Введите заголовок",
                        max_length=150,
                        verbose_name="Заголовок поста",
                    ),
                ),
                ("slug", models.CharField(max_length=150, verbose_name="Slug")),
                (
                    "body",
                    models.TextField(
                        help_text="Введите текст поста", verbose_name="Содержимое"
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение",
                        null=True,
                        upload_to="myblog/photo",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        blank=True,
                        help_text="Введите дату создания поста",
                        null=True,
                        verbose_name="Дата создания",
                    ),
                ),
                (
                    "public",
                    models.BooleanField(
                        default=False,
                        help_text="Введите признак публикации поста",
                        verbose_name="Признак публикации",
                    ),
                ),
                (
                    "views_counter",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Укажите количество просмотров",
                        verbose_name="Счетчик просмотров",
                    ),
                ),
            ],
            options={
                "verbose_name": "Блог",
                "verbose_name_plural": "Блоги",
            },
        ),
    ]