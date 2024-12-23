# Generated by Django 3.2.16 on 2023-05-25 10:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0008_comment_pub_date"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={
                "default_related_name": "comments",
                "ordering": ("pub_date",),
                "verbose_name": "комментарий",
                "verbose_name_plural": "Комментарии",
            },
        ),
    ]
