from django.shortcuts import render, redirect
from django.views import generic
from .forms import form000, form001, form002, form003
from .models import story000, story001, story002, story003

database_list = {
's000': story000,
's001': story001,
's002': story002,
's003': story003,
}

form_list = {
's000': form000,
's001': form001,
's002': form002,
's003': form003,
}

# Create your views here.
def input(request, story_num):
    story_form = form_list[story_num]

    if request.method == 'POST':
        form = story_form(request.POST, request.FILES)
        if form.is_valid():
            action_word = form.cleaned_data.get('action_word')
            adjective_1 = form.cleaned_data.get('adjective_1')
            adjective_2 = form.cleaned_data.get('adjective_2')
            adjective_3 = form.cleaned_data.get('adjective_3')
            adjective_4 = form.cleaned_data.get('adjective_4')
            adjective_5 = form.cleaned_data.get('adjective_5')
            adjective_6 = form.cleaned_data.get('adjective_6')
            adjective_7 = form.cleaned_data.get('adjective_7')
            animal_1 = form.cleaned_data.get('animal_1')
            animal_2 = form.cleaned_data.get('animal_2')
            animal_3 = form.cleaned_data.get('animal_3')
            body_part_1 = form.cleaned_data.get('body_part_1')
            body_part_2 = form.cleaned_data.get('body_part_2')
            bollywood_actress_name = form.cleaned_data.get('bollywood_actress_name')
            bollywood_actor_name = form.cleaned_data.get('bollywood_actor_name')
            bollywood_film = form.cleaned_data.get('bollywood_film')
            city = form.cleaned_data.get('city')
            color = form.cleaned_data.get('color')
            country = form.cleaned_data.get('country')
            girl_name = form.cleaned_data.get('girl_name')
            illness = form.cleaned_data.get('illness')
            location = form.cleaned_data.get('location')
            male_name = form.cleaned_data.get('male_name')
            male_name_1 = form.cleaned_data.get('male_name_1')
            male_name_2 = form.cleaned_data.get('male_name_2')
            male_name_3 = form.cleaned_data.get('male_name_3')
            mode_of_transportation = form.cleaned_data.get('mode_of_transportation')
            movement = form.cleaned_data.get('movement')
            noun = form.cleaned_data.get('noun')
            noun_1 = form.cleaned_data.get('noun_1')
            noun_2 = form.cleaned_data.get('noun_2')
            number = form.cleaned_data.get('number')
            number_between_1_and_10 = form.cleaned_data.get('number_between_1_and_10')
            number_1 = form.cleaned_data.get('number_1')
            number_2 = form.cleaned_data.get('number_2')
            occupation_1 = form.cleaned_data.get('occupation_1')
            occupation_2 = form.cleaned_data.get('occupation_2')
            old_Bollywood_actor = form.cleaned_data.get('old_Bollywood_actor')
            past_tense_verb = form.cleaned_data.get('past_tense_verb')
            past_tense_verb_1 = form.cleaned_data.get('past_tense_verb_1')
            past_tense_verb_2 = form.cleaned_data.get('past_tense_verb_2')
            relative_1 = form.cleaned_data.get('relative_1')
            relative_2 = form.cleaned_data.get('relative_2')
            slogan = form.cleaned_data.get('slogan')
            type_of_relative = form.cleaned_data.get('type_of_relative')

            form_save = form.save(commit=False)
            new_input = form.save()
            return redirect('/' + story_num + '/' + str(new_input.id) + '/output')
    else:
        form = story_form()
    return render(request, 'input_words.html', {'form' : form})

def output(request, story_num, pk):
    tuple = database_list[story_num].objects.get(id=pk)
    return render(request, 'output_'+story_num+'.html', {'tuple' : tuple, 'pk' : pk, 'current_path': request.get_full_path()})

def output_img(request, story_num, pk):
    path = request.get_full_path()
    return render(request, 'output_'+story_num+'_img.html', {'current_path' : path[:len(path)-len('img')]})
