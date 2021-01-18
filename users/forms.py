from django import forms

class IssueForm(forms.Form):
    title = forms.CharField(label='标题', 
                            widget=forms.TextInput(attrs={'placeholder':'请填写活动标题'}),
                            max_length=10,  help_text='取一个独一无二的标题吧')
    content = forms.CharField(label='内容',widget=forms.Textarea)

    
