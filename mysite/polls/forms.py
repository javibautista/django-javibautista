from django import forms

class Question(forms.ModelForm):
    question_text = models.CharField('Question',max_length=255)
    pub_date = models.DateTimeField('fecha de publicacion')

    def __str__(self):
        return self.question_text


class Choice(forms.ModelForm):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
