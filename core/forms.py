from django import forms
class Generate_image(forms.Form):
    
    # latitude=forms.DecimalField(required= True ,)
    # logitude=forms.DecimalField(required= True ,)
    zoom_start=forms.IntegerField(required= True,initial='13' ,min_value=1,max_value=20,label='zoom ')
    width=forms.IntegerField(required= True, initial='1100' ,min_value=100,max_value=2000,label='width Of Map')
    height=forms.IntegerField(required= True,initial='610' ,help_text='',min_value=20,max_value=20,label='hight Of Map')