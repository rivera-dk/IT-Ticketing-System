# Generated by Django 4.0.2 on 2022-02-14 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketApp', '0002_ticket_date_updated_alter_ticket_ticket_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
