# Generated by Django 4.1.2 on 2023-06-08 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('by', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('descendants', models.IntegerField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=500, null=True)),
                ('deleted', models.BooleanField()),
                ('dead', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('by', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('deleted', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('dead', models.BooleanField()),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hacker_news.items')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hacker_news.comments')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
