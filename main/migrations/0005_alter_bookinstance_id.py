# Generated by Django 4.0.5 on 2022-06-14 10:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_author_second_name_alter_bookinstance_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.UUID('34d6b745-b24b-48d2-8e92-4e2432df502a'), primary_key=True, serialize=False),
        ),
    ]