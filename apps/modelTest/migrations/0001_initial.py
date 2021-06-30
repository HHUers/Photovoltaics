# Generated by Django 3.2 on 2021-06-30 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='projectOverview',
            fields=[
                ('projectNo', models.IntegerField(primary_key=True, serialize=False, verbose_name='项目序号')),
                ('projectName', models.CharField(max_length=100, verbose_name='项目名称')),
                ('projectType', models.CharField(max_length=20, verbose_name='项目类型')),
                ('projectStage', models.CharField(max_length=20, verbose_name='项目阶段')),
                ('projectHost', models.CharField(max_length=30, null=True, verbose_name='项目业主')),
                ('projectHostGroup', models.CharField(max_length=50, null=True, verbose_name='项目业主集团')),
                ('projectDesign', models.CharField(max_length=50, verbose_name='设计单位')),
                ('projectDate', models.DateField(verbose_name='日期')),
            ],
        ),
        migrations.CreateModel(
            name='siteProfile',
            fields=[
                ('projectNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='modelTest.projectoverview', verbose_name='项目序号')),
                ('location', models.CharField(max_length=50, verbose_name='项目地址')),
                ('capacity', models.FloatField(verbose_name='安装容量')),
                ('area', models.FloatField(verbose_name='用地面积')),
                ('altitude', models.IntegerField(verbose_name='海拔高度')),
                ('longtitude', models.FloatField(verbose_name='经度')),
                ('latitude', models.FloatField(verbose_name='纬度')),
                ('radiationMJ', models.FloatField(verbose_name='水平太阳总辐射MJ')),
                ('radiationkwh', models.FloatField(verbose_name='水平太阳总辐射kwh')),
                ('dipAngle', models.IntegerField(verbose_name='最佳辐射量倾角')),
            ],
        ),
        migrations.CreateModel(
            name='temperature',
            fields=[
                ('projectNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='modelTest.projectoverview', verbose_name='项目序号')),
                ('avgTemperature', models.FloatField(verbose_name='多年平均气温')),
                ('maxTemperature', models.FloatField(verbose_name='多年极端最高气温')),
                ('minTemperature', models.FloatField(verbose_name='多年极端最低气温')),
                ('avgMonthTemperature', models.FloatField(verbose_name='最热月平均气温')),
                ('breakingGroundDepth', models.IntegerField(verbose_name='多年最大冻土深度')),
                ('avgSpeed', models.FloatField(verbose_name='多年平均风速')),
                ('maxSpeed', models.FloatField(verbose_name='多年最大风速')),
                ('rainyDays', models.FloatField(verbose_name='多年平均雷暴日数')),
                ('pollutionLevel', models.FloatField(null=True, verbose_name='污秽等级')),
            ],
        ),
    ]