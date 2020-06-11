# Generated by Django 2.2.4 on 2020-02-21 18:30

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_remove_course_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('L', 'Lacunas'), ('ME', 'Múltipla Escolha'), ('VF', 'Verdadeiro ou Falso')], max_length=100, verbose_name='Tipo')),
                ('pergunta', models.TextField(verbose_name='Pergunta')),
                ('resposta', djongo.models.fields.ListField(verbose_name='Resposta')),
                ('pontuacao', models.IntegerField(verbose_name='Pontuação')),
                ('visibilidade', models.CharField(max_length=100, verbose_name='Visibilidade')),
                ('nivel_de_dificuldade', models.CharField(max_length=100, verbose_name='Nivel de Dificuldade')),
                ('tempo_resposta', models.CharField(max_length=100, verbose_name='Tempo de Resposta')),
                ('explicacao_resposta', models.TextField(blank=True, verbose_name='Explicação da Resposta')),
            ],
        ),
        migrations.CreateModel(
            name='Questao_Multipla_Escolha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100, verbose_name='Tipo')),
                ('pergunta', models.TextField(verbose_name='Pergunta')),
                ('resposta', models.TextField(verbose_name='Resposta')),
                ('pontuacao', models.IntegerField(verbose_name='Pontuação')),
                ('visibilidade', models.CharField(max_length=100, verbose_name='Visibilidade')),
                ('nivel_de_dificuldade', models.CharField(max_length=100, verbose_name='Nivel de Dificuldade')),
                ('tempo_resposta', models.CharField(max_length=100, verbose_name='Tempo de Resposta')),
                ('explicacao_resposta', models.TextField(blank=True, verbose_name='Explicação da Resposta')),
            ],
        ),
        migrations.CreateModel(
            name='Questao_Verdadeiro_Falso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100, verbose_name='Tipo')),
                ('pergunta', models.TextField(verbose_name='Pergunta')),
                ('resposta', models.TextField(verbose_name='Resposta')),
                ('pontuacao', models.IntegerField(verbose_name='Pontuação')),
                ('visibilidade', models.CharField(max_length=100, verbose_name='Visibilidade')),
                ('nivel_de_dificuldade', models.CharField(max_length=100, verbose_name='Nivel de Dificuldade')),
                ('tempo_resposta', models.CharField(max_length=100, verbose_name='Tempo de Resposta')),
                ('explicacao_resposta', models.TextField(blank=True, verbose_name='Explicação da Resposta')),
            ],
        ),
        migrations.RemoveField(
            model_name='atividade',
            name='curso_id',
        ),
        migrations.RemoveField(
            model_name='atividade',
            name='exibicao_resp_corretas_ao_final',
        ),
        migrations.RemoveField(
            model_name='atividade',
            name='exibicao_resp_corretas_durante',
        ),
        migrations.RemoveField(
            model_name='course',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='course',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='atividade',
            name='exibicao_resp_corretas',
            field=models.BooleanField(default=True, verbose_name='Respostas Corretas:'),
            preserve_default=False,
        ),
    ]