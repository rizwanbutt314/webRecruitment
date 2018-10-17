from django.db import models

class Test(models.Model):

    testTime = models.TimeField(null=False, db_column='TestTime', default=10)
    name = models.TextField(default='Singleton Test')
    description = models.TextField(default='One Test for All.')
    passingMarks = models.IntegerField(default='0')


class Question(models.Model):

    description = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.DO_NOTHING)

class Options(models.Model):

    def question_default():
        return Question(description='Default question')

    description = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.SET_DEFAULT, default=question_default)
    is_Answer = models.BooleanField(default=False)