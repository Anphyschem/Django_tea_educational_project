from django.shortcuts import render, redirect
from .models import Tea
from .forms import Tea_form
import random


def home(request):
    return render(request, "home_page.html")

def tea_table(request):
    teas = Tea.objects.all()
    return render(request, "tea_table.html",{"teas":teas})

def add_tea(request):
    if request.method == "POST":
        form = Tea_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tea_table")
    else:
        form = Tea_form()
    return render(request, "add_tea.html", {"form": form})


def tea_quiz(request):
    if 'quiz_teas' not in request.session:
        teas = list(Tea.objects.all())
        random.shuffle(teas)
        request.session['quiz_teas'] = [t.id for t in teas[:5]]
        request.session['current_index'] = 0
        request.session['score'] = 0

    tea_id = request.session['quiz_teas'][request.session['current_index']]
    tea = Tea.objects.get(id=tea_id)
    
    if request.method == 'POST':
        user_temp = int(request.POST.get('temperature', 0))
        user_spills = int(request.POST.get('spills', 0))
        
        if user_temp == tea.water_temperature and user_spills == tea.spillage_number:
            request.session['score'] += 1

        request.session['current_index'] += 1
        if request.session['current_index'] >= len(request.session['quiz_teas']):
            return redirect('quiz_results')
        
        return redirect('tea_quiz')
    
    return render(request, 'tea_quiz.html', {
        'tea': tea,
        'question_num': request.session['current_index'] + 1,
        'total_questions': len(request.session['quiz_teas'])
    })


def quiz_results(request):
    score = request.session.get('score', 0)
    total = len(request.session.get('quiz_teas', []))
   
    if 'quiz_teas' in request.session:
        del request.session['quiz_teas']

    
    return render(request, 'tea_quiz_results.html', {
        'score': score,
        'total': total,
        'is_low_score': score < 0.5 * total
    })