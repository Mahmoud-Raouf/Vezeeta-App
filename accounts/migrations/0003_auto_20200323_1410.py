# Generated by Django 2.2.7 on 2020-03-23 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200323_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.CharField(choices=[('1', 'جلدية'), ('2', 'اسنان'), ('16', 'جراحة اورام'), ('15', 'جراحة اطفال'), ('5', 'مخ واعصاب'), ('3', 'نفسي'), ('6', 'عظام'), ('7', 'نساء وتوليد'), ('9', 'قلب واوعية دموية'), ('10', 'امراض دم'), ('18', 'جراحة تجميل'), ('13', 'باطنه'), ('12', 'اورام'), ('14', 'تخسيس وتغذية'), ('19', 'جراحه سمنة ومناظير '), ('4', 'اطفال حديثي الولادة'), ('8', 'انف واذن وحنجرة'), ('17', 'جراحة اوعية دموية')], max_length=50, verbose_name='دكتور ؟'),
        ),
    ]