# Generated by Django 5.0.6 on 2024-05-25 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_classrooms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('announcement_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AnswersList',
            fields=[
                ('answer_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('attachment_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AttemptQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='AttemptTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('classroom_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('classroom_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Educator',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Learner',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('question_title', models.CharField(max_length=50)),
                ('right_answer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('starting_time', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('t_ype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('deadline', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='classrooms',
        ),
        migrations.DeleteModel(
            name='users_data',
        ),
        migrations.AddField(
            model_name='attachment',
            name='classroom_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.classroom'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='classroom_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.classroom'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='creator_email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.educator'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.educator'),
        ),
        migrations.AddField(
            model_name='enroll',
            name='classroom_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.classroom'),
        ),
        migrations.AddField(
            model_name='answerslist',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='classroom_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.classroom'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.educator'),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quiz'),
        ),
        migrations.AddField(
            model_name='attemptquiz',
            name='quiz_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quiz'),
        ),
        migrations.AddField(
            model_name='answerslist',
            name='quiz_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quiz'),
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('default_language', models.CharField(max_length=50)),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.user_data')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user_data'),
        ),
        migrations.AddField(
            model_name='enroll',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user_data'),
        ),
        migrations.AddField(
            model_name='attempttask',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user_data'),
        ),
        migrations.AddField(
            model_name='attemptquiz',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user_data'),
        ),
        migrations.AddField(
            model_name='task',
            name='classroom_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.classroom'),
        ),
        migrations.AddField(
            model_name='task',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.educator'),
        ),
        migrations.AddField(
            model_name='attempttask',
            name='task_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.task'),
        ),
        migrations.AlterUniqueTogether(
            name='request',
            unique_together={('email',)},
        ),
        migrations.AlterUniqueTogether(
            name='enroll',
            unique_together={('email', 'classroom_id')},
        ),
        migrations.AlterUniqueTogether(
            name='attemptquiz',
            unique_together={('email', 'quiz_id')},
        ),
        migrations.AlterUniqueTogether(
            name='attempttask',
            unique_together={('email', 'task_id')},
        ),
    ]
