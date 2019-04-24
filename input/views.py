from django.shortcuts import render, redirect
from django.views import generic
from .forms import form000, form001
from .models import story000, story001

# Create your views here.
def input(request, story_num):
    if story_num == 's000':
        if request.method == 'POST':
            form = form000(request.POST, request.FILES)
            if form.is_valid():
                Bollywood_Actress_Name = form.cleaned_data.get('Bollywood_Actress_Name')
                Bollywood_Actor_Name = form.cleaned_data.get('Bollywood_Actor_Name')
                Body_Part_1 = form.cleaned_data.get('Body_Part1')
                Body_Part_2 = form.cleaned_data.get('Body_Part2')
                Old_Bollywood_Actor = form.cleaned_data.get('Old_Bollywood_Actor')
                Noun = form.cleaned_data.get('Noun')
                Country = form.cleaned_data.get('Country')
                Occupation_1 = form.cleaned_data.get('Occupation')
                Past_Tense_Verb = form.cleaned_data.get('Past_Tense_Verb')
                Occupation_2 = form.cleaned_data.get('Occupation')
                Adjective_1 = form.cleaned_data.get('Adjective1')
                Adjective_2 = form.cleaned_data.get('Adjective2')
                Adjective_3 = form.cleaned_data.get('Adjective3')
                Number_between_1_and_10 = form.cleaned_data.get('Number_between_1_and_10')

                form_save = form.save(commit=False)
                new_input = form.save()
                return redirect('/' + story_num + '/' + str(new_input.id) + '/output')
        else:
            form = form000()
        return render(request, 'input_words.html', {'form' : form})
    elif story_num == 's001':
        if request.method == 'POST':
            form = form001(request.POST, request.FILES)
            if form.is_valid():
                male_name = form.cleaned_data.get('male_name')
                verb_1 = form.cleaned_data.get('verb_1')
                adjective_1 = form.cleaned_data.get('adjective_1')
                girl_name = form.cleaned_data.get('girl_name')
                movement = form.cleaned_data.get('movement')
                number_1 = form.cleaned_data.get('number_1')
                adjective_2 = form.cleaned_data.get('adjective_2')
                number_2 = form.cleaned_data.get('number_2')
                number_3 = form.cleaned_data.get('number_3')
                bollywood_actor = form.cleaned_data.get('bollywood_actor')
                bollywood_film = form.cleaned_data.get('bollywood_film')
                adjective_3 = form.cleaned_data.get('adjective_3')

                form_save = form.save(commit=False)
                new_input = form.save()
                return redirect('/' + story_num + '/' + str(new_input.id) + '/output')
        else:
            form = form001()
        return render(request, 'input_words.html', {'form' : form})

database = {
  "s000": story000,
  "s001": story001
}

def output(request, story_num, pk):
    tuple = database[story_num].objects.get(id=pk)
    return render(request, 'output_'+story_num+'.html', {'tuple' : tuple, 'pk' : pk, 'current_path': request.get_full_path()})
