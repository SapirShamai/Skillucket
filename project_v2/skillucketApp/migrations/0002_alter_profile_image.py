# Generated by Django 4.2.4 on 2023-09-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("skillucketApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="profile_pics/jellyfisz.jpg", upload_to="profile_pics/"
            ),
        ),
    ]
