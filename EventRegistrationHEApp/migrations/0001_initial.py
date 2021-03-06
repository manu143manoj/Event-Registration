# Generated by Django 3.0.6 on 2020-05-30 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErRegisteredUsers',
            fields=[
                ('user_id', models.IntegerField(db_column='User_ID', primary_key=True, serialize=False)),
                ('registration_id', models.CharField(db_column='Registration_ID', max_length=45)),
                ('full_name', models.CharField(db_column='Full_Name', max_length=250)),
                ('mobile', models.CharField(db_column='Mobile', max_length=20)),
                ('email', models.CharField(db_column='Email', max_length=100)),
                ('id_cards', models.ImageField(blank=True, upload_to='idCards')),
                ('registration_type', models.CharField(choices=[('Self', 'Self'), ('Group', 'Group'), ('Corporate', 'Corporate'), ('Others', 'Others')], db_column='Registration_type', max_length=100)),
                ('no_of_tickets', models.CharField(db_column='No_of_tickets', max_length=100)),
                ('registration_date', models.DateTimeField(db_column='Registration_Date', max_length=100)),
            ],
        ),
    ]
