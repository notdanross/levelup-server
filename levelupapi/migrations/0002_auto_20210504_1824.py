# Generated by Django 3.2 on 2021-05-04 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gamer_event',
            new_name='GamerEvent',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='attending', through='levelupapi.GamerEvent', to='levelupapi.Gamer'),
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='number_of_players',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='skill_level',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
