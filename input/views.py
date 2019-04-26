from django.shortcuts import render, redirect
from django.views import generic
from .forms import form000, form001, form002, form003
from .models import story000, story001, story002, story003

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
                action_word = form.cleaned_data.get('action_word')
                adjective_1 = form.cleaned_data.get('adjective_1')
                girl_name = form.cleaned_data.get('girl_name')
                movement = form.cleaned_data.get('movement')
                number_1 = form.cleaned_data.get('number_1')
                location = form.cleaned_data.get('location')
                adjective_2 = form.cleaned_data.get('adjective_2')
                number_2 = form.cleaned_data.get('number_2')
                location = form.cleaned_data.get('location')
                bollywood_actor = form.cleaned_data.get('bollywood_actor')
                bollywood_film = form.cleaned_data.get('bollywood_film')
                adjective_3 = form.cleaned_data.get('adjective_3')

                form_save = form.save(commit=False)
                new_input = form.save()
                return redirect('/' + story_num + '/' + str(new_input.id) + '/output')
        else:
            form = form001()
        return render(request, 'input_words.html', {'form' : form})
    elif story_num == 's002':
        if request.method == 'POST':
            form = form002(request.POST, request.FILES)
            if form.is_valid():
                male_name_1 = form.cleaned_data.get('male_name_1')
                male_name_2 = form.cleaned_data.get('male_name_2')
                male_name_3 = form.cleaned_data.get('male_name_3')
                girl_name = form.cleaned_data.get('girl_name')
                number = form.cleaned_data.get('number')
                relative_1 = form.cleaned_data.get('relative_1')
                relative_2 = form.cleaned_data.get('relative_2')
                animal_1 = form.cleaned_data.get('animal_1')
                mode_of_transportation = form.cleaned_data.get('mode_of_transportation')
                city = form.cleaned_data.get('city')
                noun_1 = form.cleaned_data.get('noun_1')
                noun_2 = form.cleaned_data.get('noun_2')
                slogan = form.cleaned_data.get('slogan')
                past_tense_verb_1 = form.cleaned_data.get('past_tense_verb_1')
                past_tense_verb_2 = form.cleaned_data.get('past_tense_verb_2')
                animal_2 = form.cleaned_data.get('animal_2')
                animal_3 = form.cleaned_data.get('animal_3')

                form_save = form.save(commit=False)
                new_input = form.save()
                return redirect('/' + story_num + '/' + str(new_input.id) + '/output')
        else:
            form = form002()
        return render(request, 'input_words.html', {'form' : form})
    elif story_num == 's003':
        if request.method == 'POST':
            form = form003(request.POST, request.FILES)
            if form.is_valid():
                adjective_1 = form.cleaned_data.get('adjective_1')
                color = form.cleaned_data.get('color')
                type_of_relative = form.cleaned_data.get('type_of_relative')
                adjective_2 = form.cleaned_data.get('adjective_2')
                adjective_3 = form.cleaned_data.get('adjective_3')
                city = form.cleaned_data.get('city')
                adjective_4 = form.cleaned_data.get('adjective_4')
                girl_name = form.cleaned_data.get('girl_name')
                noun = form.cleaned_data.get('noun')
                illness = form.cleaned_data.get('illness')
                adjective_5 = form.cleaned_data.get('adjective_5')
                adjective_6 = form.cleaned_data.get('adjective_6')
                adjective_7 = form.cleaned_data.get('adjective_7')

                form_save = form.save(commit=False)
                new_input = form.save()
                return redirect('/' + story_num + '/' + str(new_input.id) + '/output')
        else:
            form = form003()
        return render(request, 'input_words.html', {'form' : form})

database_list = {
  's000': story000,
  's001': story001,
  's002': story002,
  's003': story003,
}

def output(request, story_num, pk):
    tuple = database_list[story_num].objects.get(id=pk)
    return render(request, 'output_'+story_num+'.html', {'tuple' : tuple, 'pk' : pk, 'current_path': request.get_full_path()})

def output_img(request, story_num, pk):
    path = request.get_full_path()
    return render(request, 'output_'+story_num+'_img.html', {'current_path' : path[:len(path)-len('img')]})
