# Generated by Django 4.1.5 on 2023-03-11 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('domainModel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalitiesLetters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e', models.DecimalField(decimal_places=2, max_digits=6)),
                ('i', models.DecimalField(decimal_places=2, max_digits=6)),
                ('s', models.DecimalField(decimal_places=2, max_digits=6)),
                ('n', models.DecimalField(decimal_places=2, max_digits=6)),
                ('t', models.DecimalField(decimal_places=2, max_digits=6)),
                ('f', models.DecimalField(decimal_places=2, max_digits=6)),
                ('j', models.DecimalField(decimal_places=2, max_digits=6)),
                ('p', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalitiesNames',
            fields=[
                ('personalityName', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentKnowledge', models.ManyToManyField(to='domainModel.theoreticaldata')),
            ],
        ),
        migrations.CreateModel(
            name='StudentProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('errorsNumber', models.IntegerField()),
                ('spentTime', models.DurationField()),
                ('solutionCode', models.TextField()),
                ('projectCodeCompletionLevel', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domainModel.project')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentModel.studentprofile')),
            ],
        ),
    ]
