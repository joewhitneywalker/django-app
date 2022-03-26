from ast import Delete
from sre_constants import SUCCESS
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Character, CharacterPowers



# Create your views here.

class Home(TemplateView): #HANDLES GET REQUEST
    template_name = "home.html"
   # def get(self, request): #SIMILAR TO RES.SEND
    #    return HttpResponse("App Home")


class About(TemplateView):
    template_name = "about.html"
   # def get(self, request):
   #     return HttpResponse("About")






'''
BEGINNING OF FAKEABASE
class Character: 

    def __init__(self, name, age, gender, attribute):
        self.name = name
        self.age = age
        self.gender = gender
        self.attribute = attribute

characters = [
    Character("Circe", 100000, "Female", "Transfiguration, Fearlessness, Wit"),
    Character("Pasiphaë", 80000, "Female", "Poisons, Trickery, Malevolence"),
    Character("Aeetes", 50000, "Male", "Pharmacaia, Hubris, Stubborness"),
    Character("Perses", 78890, "Male", "Raising The Dead, Veiling The Sky, Trickery"),
    Character("Helios", 100000000, "Male", "Lord of the Sun, Counters, Fire"),
]
COMMENTING OUT FAKEABASE
'''


class Character_List(TemplateView):
    template_name = 'characterlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #name query parameter
        name = self.request.GET.get("name") #name request getting request from object of self
        if name != None:
             context["characters"] = Character.objects.filter(name__icontains=name)#filters name 
             context["header"] = f"Searching for {name}"
        else:
            context['characters'] = Character.objects.all()
            context["header"] = "Our Cast Of Characters"
        return context

#create a new character
@method_decorator(login_required, name='dispatch')
class Character_Create(CreateView):
  model = Character
  fields = ['name', 'img', 'age', 'attribute', 'gender', 'characterpowers']
  template_name ="character_create.html"
  #success_url = '/characters/'
  def get_success_url(self):
        return reverse('character_detail', kwargs={'pk': self.object.pk})

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect('/characters/')
 

#view details of character
class Character_Detail(DetailView):
    model = Character
    template_name = "character_detail.html"

#update view
@method_decorator(login_required, name='dispatch')
class Character_Update(UpdateView):
    model = Character
    fields = ['name', 'img', 'age', 'attribute', 'gender', 'characterpowers']
    template_name = "character_update.html"
    #success_url = "/characters/"
    def get_success_url(self):
        return reverse('character_detail', kwargs={'pk': self.object.pk})

#delete view
@method_decorator(login_required, name='dispatch')
class Character_Delete(DeleteView):
    model = Character
    template_name = "character_delete_confirmation.html"
    success_url = "/characters/"

#user function
@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    characters = Character.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'characters': characters})


#characterpowers
def characterpowers_index(request):
    characterpowers = CharacterPowers.objects.all()
    return render(request, 'characterpowers_index.html', {'characterpowers': characterpowers})

def characterpowers_show(request, characterpowers_id):
    characterpowers = CharacterPowers.objects.get(id=characterpowers_id)
    return render(request, 'characterpowers_show.html', {'characterpowers': characterpowers})

@method_decorator(login_required, name='dispatch')
class CharacterPowersCreate(CreateView):
    model = CharacterPowers
    fields = '__all__'
    template_name = "characterpowers_form.html"
    success_url = '/characterpowers'

@method_decorator(login_required, name='dispatch')
class CharacterPowersUpdate(UpdateView):
    model = CharacterPowers
    fields = '__all__'
    template_name = "characterpowers_update.html"
    success_url = '/characterpowers'   

@method_decorator(login_required, name='dispatch')
class CharacterPowersDelete(DeleteView):
    model = CharacterPowers
    template_name = "characterpowers_confirm_delete.html"
    success_url = '/characterpowers'

#django auth
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            HttpResponse('<h1>Try Again</h1>')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/characters')

def login_view(request):
     # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')
    else: # it was a get request so send the emtpy login form
        # form = LoginForm()
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form}) 