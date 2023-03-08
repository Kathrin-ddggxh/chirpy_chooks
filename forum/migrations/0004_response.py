# Generated by Django 3.2 on 2023-03-08 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_userprofile_default_county'),
        ('forum', '0003_entry_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('create_date', models.DateField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='profiles.userprofile')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response', to='forum.entry')),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
    ]
