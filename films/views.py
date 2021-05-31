from django.shortcuts import render
from .forms import *
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.

def homepage(request):

    films = Film.objects.all()
    # for i in films:
    #     print(i.category)
   
    # print(films.category)

    return render(request,'homepage.html', {'films':films})

# def add_film(request):
#     new_film_form = FilmForm(request.POST)
#     if new_film_form.is_valid():
#         new_film = new_film_form.save()


class AddFilm(generic.CreateView):
    template_name = 'addFilm.html'
    model = Film
    fields = '__all__'
    success_url = reverse_lazy('homepage')
    

    def form_valid(self, form):
        post_to_add = form.cleaned_data
        print(post_to_add)
        return super().form_valid(form) 


class AddDirector(generic.CreateView):
    
    template_name = 'addDirector.html'
    model = Director
    fields = '__all__'
    success_url = reverse_lazy('homepage')


    def form_valid(self, form):
        post_to_add = form.cleaned_data
        print(post_to_add)
        return super().form_valid(form) 

class UpdateFilm(generic.UpdateView):
    
    template_name = 'update.html'
    model = Film
    fields = '__all__'
    success_url ='/homepage'

    # def get_object(self):
    #     film = self.Film.get('id')
    #     return get_object_or_404(Article, id=id)


    def form_valid(self, form):
        post_to_add = form.cleaned_data
        print(post_to_add)
        return super().form_valid(form) 