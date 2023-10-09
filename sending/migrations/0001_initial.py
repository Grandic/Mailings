# Generated by Django 4.2.6 on 2023-10-09 17:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=50, verbose_name='Тема')),
                ('content', models.TextField(verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Sending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('next_run', models.DateTimeField(auto_now=True, verbose_name='Дата следующей рассылки')),
                ('interval', models.CharField(choices=[('раз в день', 'раз в день'), ('раз в неделю', 'раз в неделю'), ('раз в месяц', 'раз в месяц')], max_length=30, verbose_name='Периодичность')),
                ('status_sending', models.CharField(choices=[('Завершена', 'завершена'), ('Создана', 'создана'), ('Запущена', 'активирована')], max_length=30, verbose_name='Статус')),
                ('start_sending_date', models.DateField(default=datetime.datetime(2023, 10, 9, 17, 28, 42, 77069), verbose_name='Дата начала')),
                ('start_sending_time', models.TimeField(blank=True, default=datetime.time(17, 28, 42, 77079), null=True, verbose_name='время рассылки')),
                ('customer', models.ManyToManyField(to='customer.customer', verbose_name='Клиент')),
                ('message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sending.message', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
                'permissions': [('can_view_sending', 'Can view sending'), ('can_disable_sending', 'Can disable sending')],
            },
        ),
        migrations.CreateModel(
            name='TrySending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_attempt', models.DateTimeField(auto_now_add=True, verbose_name='Дата последней попытки')),
                ('status_attempt', models.CharField(choices=[('success', 'завершена'), ('failure', 'провалена'), ('in_progress', 'в процессе')], default='in_progress', max_length=30, verbose_name='Текущий статус')),
                ('answer_server', models.CharField(max_length=20, verbose_name='Ответ почтового сервера')),
                ('sending', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sending.sending', verbose_name='Письмо')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылок',
            },
        ),
    ]
