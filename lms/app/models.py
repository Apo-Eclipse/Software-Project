from django.db import models

class user_data(models.Model):
    email = models.EmailField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)


class Classroom(models.Model):
    classroom_id = models.CharField(max_length=50, primary_key=True)
    classroom_name = models.CharField(max_length=50)
    creator_email = models.ForeignKey(user_data, on_delete=models.CASCADE)

class Request(models.Model):
    email = models.ForeignKey(user_data, on_delete=models.CASCADE)
    classroom_id = models.CharField(max_length=50)
    class Meta:
        unique_together = ('email',)

class Enroll(models.Model):
    email = models.ForeignKey(user_data, on_delete=models.CASCADE)
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('email', 'classroom_id')

class Task(models.Model):
    task_id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=50)
    deadline = models.DateTimeField()
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    email = models.ForeignKey(user_data, on_delete=models.CASCADE)

class Quiz(models.Model):
    quiz_id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=50)
    starting_time = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    email = models.ForeignKey(user_data, on_delete=models.CASCADE)

class Question(models.Model):
    question_id = models.CharField(max_length=50, primary_key=True)
    question_title = models.CharField(max_length=50)
    right_answer = models.CharField(max_length=50)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)

class AnswersList(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_id = models.CharField(max_length=50, primary_key=True)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)

class Attachment(models.Model):
    attachment_id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)

class Announcement(models.Model):
    announcement_id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    email = models.ForeignKey(user_data, on_delete=models.CASCADE)

class Settings(models.Model):
    default_language = models.CharField(max_length=50)
    email = models.OneToOneField(user_data, on_delete=models.CASCADE, primary_key=True)

class AttemptTask(models.Model):
    email = models.ForeignKey(user_data, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    grade = models.FloatField()
    class Meta:
        unique_together = ('email', 'task_id')

class AttemptQuiz(models.Model):
    email = models.ForeignKey(user_data, on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    grade = models.FloatField()
    class Meta:
        unique_together = ('email', 'quiz_id')