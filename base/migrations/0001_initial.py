# Generated by Django 5.1.4 on 2025-03-04 16:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('blog', 'BLOG'), ('ebook', 'EBOOK'), ('audio book', 'AUDIO BOOK'), ('explanation audio', 'EXPLANATION AUDIO'), ('event', 'EVENT')])),
                ('description', models.TextField()),
                ('price_in_etb', models.FloatField(default=0.0)),
                ('price_in_usd', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
