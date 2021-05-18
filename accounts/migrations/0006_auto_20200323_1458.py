# Generated by Django 2.2.7 on 2020-03-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200323_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.CharField(choices=[('نفسي', 'نفسي'), ('جراحة اورام', 'اورام'), ('مخ واعصاب', 'مخ واعصاب'), ('جلدية', 'جلدية'), ('نساء وتوليد', 'نساء وتوليد'), ('انف واذن وحنجرة', 'انف واذن وحنجرة'), ('قلب واوعية دموية', 'قلب واوعية دموية'), ('امراض دم', 'امراض دم'), ('اسنان', 'اسنان'), ('تخسيس وتغذية', 'تخسيس وتغذية'), ('جراحة اطفال', 'جراحة اطفال'), ('جراحة اورام', 'جراحة اورام'), ('جراحة اوعية دموية', 'جراحة اوعية دموية'), ('جراحة تجميل', 'جراحة تجميل'), ('جراحه سمنة ومناظير ', 'جراحه سمنة ومناظير '), ('عظام', 'عظام'), ('باطنه', 'باطنه'), ('جراحة اطفال', 'اطفال حديثي الولادة')], max_length=50, verbose_name='دكتور ؟'),
        ),
    ]