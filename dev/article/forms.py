from django import forms

class CreateArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    # publish_date = forms.DateField()

    def clean_title(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get("title").islower():
            raise forms.ValidationError("Title should be in ALL CAPS")
        title = cleaned_data.get("title").upper()
        return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data
