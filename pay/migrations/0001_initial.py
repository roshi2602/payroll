# Generated by Django 3.1.1 on 2020-09-26 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('overtime_pay', models.FloatField()),
                ('tax', models.FloatField()),
                ('gross_pay', models.FloatField()),
                ('net_pay', models.FloatField()),
                ('deduction', models.FloatField()),
                ('payment_method', models.CharField(choices=[('C', 'cash'), ('D', 'digital')], max_length=200)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp.employee')),
            ],
        ),
    ]
