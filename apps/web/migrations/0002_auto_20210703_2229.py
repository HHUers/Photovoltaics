# Generated by Django 3.2.4 on 2021-07-03 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectApplyForLog_log',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='编号')),
                ('record', models.CharField(max_length=30, verbose_name='记录')),
            ],
            options={
                'verbose_name': '申请审核',
                'verbose_name_plural': '申请审核',
                'db_table': 'projectApplyFor_log',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='projectApplyForLog',
        ),
    ]