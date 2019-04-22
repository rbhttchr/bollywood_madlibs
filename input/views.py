from django.shortcuts import render, redirect
from django.views import generic
from .forms import story1
from .models import story

# Create your views here.
def input(request, story_num):
    if request.method == 'POST':
        form = story1(request.POST, request.FILES)
        if form.is_valid():
            Bollywood_Actress_Name  = form.cleaned_data.get('Bollywood_Actress_Name')
            Bollywood_Actor_Name  = form.cleaned_data.get('Bollywood_Actor_Name')
            Body_Part_1  = form.cleaned_data.get('Body_Part1')
            Body_Part_2  = form.cleaned_data.get('Body_Part2')
            Old_Bollywood_Actor  = form.cleaned_data.get('Old_Bollywood_Actor')
            Noun  = form.cleaned_data.get('Noun')
            Country  = form.cleaned_data.get('Country')
            Occupation_1  = form.cleaned_data.get('Occupation')
            Past_Tense_Verb  = form.cleaned_data.get('Past_Tense_Verb')
            Occupation_2  = form.cleaned_data.get('Occupation')
            Adjective_1  = form.cleaned_data.get('Adjective1')
            Adjective_2  = form.cleaned_data.get('Adjective2')
            Adjective_3  = form.cleaned_data.get('Adjective3')
            Number_between_1_and_10  = form.cleaned_data.get('Number_between_1_and_10')

            form_save = form.save(commit=False)
            new_input = form.save()
            print(new_input.id)
            return redirect('/s000/' + str(new_input.id) + '/output')
    else:
        form = story1()
    return render(request, 'input_words.html', {'form' : form})

database = {
  "s000": story
}

def output(request, story_num, pk):
    tuple = database[story_num].objects.get(id=pk)
    return render(request, 'output.html', {'tuple' : tuple, 'pk' : pk, 'current_path': request.get_full_path()})
