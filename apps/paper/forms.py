from django import forms


class UserAnswerForm(forms.Form):
    values = forms.CharField(required=True)