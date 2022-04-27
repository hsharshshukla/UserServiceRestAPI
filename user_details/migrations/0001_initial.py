# Generated by Django 4.0.2 on 2022-04-22 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('full_name', models.CharField(blank=True, max_length=40)),
            ],
            options={
                'ordering': ['-user_id'],
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_details.userdetail')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_details.userdetail')),
            ],
        ),
    ]