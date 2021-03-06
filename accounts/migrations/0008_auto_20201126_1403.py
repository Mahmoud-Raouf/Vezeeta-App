# Generated by Django 3.0.7 on 2020-11-26 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201126_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='read',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='تمت القراءة'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.CharField(choices=[('مخ وأعصاب', 'مخ وأعصاب'), ('جراحة أطفال', 'جراحة أطفال'), ('جلدية', 'جلدية'), ('أسنان', 'أسنان'), ('جراحة أورام', 'جراحة أورام'), ('جراحة سمنة ومناظير ', 'جراحة سمنة ومناظير '), ('أورام', 'أورام'), ('جراحة تجميل', 'جراحة تجميل'), ('أمراض دم', 'أمراض دم'), ('أنف وأذن وحنجرة', 'أنف وأذن وحنجرة'), ('باطنة', 'باطنة'), ('نساء وتوليد', 'نساء وتوليد'), ('قلب وأوعيه دموية', 'قلب وأوعيه دموية'), ('تخسيس وتغذية', 'تخسيس وتغذية'), ('عظام', 'عظام'), ('نفسي', 'نفسي'), ('أطفال حديثي الولادة', 'أطفال حديثي الولادة'), ('جراحة أوعيه دموية', 'جراحة أوعيه دموية')], max_length=50, verbose_name='دكتور ؟'),
        ),
    ]
