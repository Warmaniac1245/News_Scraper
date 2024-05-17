from django import forms

class TopicForm(forms.Form):
    CHOICES = [
        ('cryptocurrency', 'Cryptocurrency'),
        ('business', 'Business'),
        ('entertainment', 'Entertainment'),
        ('sports', 'Sports'),
        ('science', 'Science'),
        ('technology', 'Technology'),
    ]
    topic = forms.ChoiceField(choices=CHOICES, label='Select Topic:')
