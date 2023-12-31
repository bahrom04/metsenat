# Generated by Django 4.1 on 2023-10-30 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.sponsors')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.students')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
