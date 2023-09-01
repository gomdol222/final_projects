# Generated by Django 4.2.4 on 2023-09-01 05:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('restaurant_name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('event', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SuggestionBoard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post_content', models.TextField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('review_text', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('rating', models.FloatField(blank=True, default=0)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('menu_name', models.CharField(max_length=150)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('restaurant', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
    ]