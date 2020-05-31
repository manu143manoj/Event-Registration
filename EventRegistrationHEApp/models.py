from django.db import models

# Create your models here.
Registration_Type_Choices = (
    ('Self', 'Self'),
    ('Group', 'Group'),
    ('Corporate', 'Corporate'),
    ('Others', 'Others')
)


# Users Table model start here
class ErRegisteredUsers(models.Model):
    user_id = models.IntegerField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    registration_id = models.CharField(db_column='Registration_ID', max_length=45)  # Field name made lowercase.
    full_name = models.CharField(db_column='Full_Name', max_length=250)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
    id_cards = models.ImageField(upload_to='idCards', blank=True)  # Field name made lowercase.
    registration_type = models.CharField(db_column='Registration_type', max_length=100,
                                         choices=Registration_Type_Choices)  # Field name made lowercase.
    no_of_tickets = models.CharField(db_column='No_of_tickets', max_length=100)  # Field name made lowercase.
    registration_date = models.DateTimeField(db_column='Registration_Date', max_length=100)  # Field name made lowercase.

# Users Table model end here