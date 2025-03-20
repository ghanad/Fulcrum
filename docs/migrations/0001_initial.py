# Generated by Django 4.0 on 2025-03-20 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertDocumentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Alert name (must match the alertname)', max_length=255)),
                ('description', models.TextField(help_text='Description of the alert and problem')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_documentations', to='auth.user')),
            ],
            options={
                'verbose_name': 'Alert Documentation',
                'verbose_name_plural': 'Alert Documentation',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='DocumentationAlertGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linked_at', models.DateTimeField(auto_now_add=True)),
                ('alert_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documentation_links', to='alerts.alertgroup')),
                ('documentation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alert_groups', to='docs.alertdocumentation')),
                ('linked_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documentation_links', to='auth.user')),
            ],
            options={
                'verbose_name': 'Documentation-Alert Link',
                'verbose_name_plural': 'Documentation-Alert Links',
                'unique_together': {('documentation', 'alert_group')},
            },
        ),
    ]
