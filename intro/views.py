from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Person, Degrees
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'intro/index.html'
    context_object_name = 'all_person'

    def get_queryset(self):
        return Person.objects.all()


class DetailView(generic.DetailView):
    model = Person
    template_name = 'intro/detail.html'


class PersonCreate(CreateView):
    model = Person
    fields = ['name', 'gender', 'age', 'religion', 'status', 'image']


class PersonUpdate(UpdateView):
    model = Person
    fields = ['name', 'gender', 'age', 'religion', 'status', 'image']


class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('intro:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'intro/reg_form.html'

    # Display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Process the input data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # Returns user objbets if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('intro:index')
        return render(request, self.template_name, {'form': form})







'''
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Biodata, Education


def index(request):
    all_person = Biodata.objects.all()
    return render(request, 'intro/index.html', {'all_person': all_person})


def detail(request, data):
    person = get_object_or_404(Biodata, pk=data)
    return render(request, 'intro/detail.html', {'person': person})


def register(request, data):
    return HttpResponse("<h2> This page registers the information about the person named : " + str(data) + "</h2>")


def favourite(request, data):
    person = get_object_or_404(Biodata, pk=data)
    try:
        fav_degree = person.education_set.get(pk=request.POST['degrees'])
    except (KeyError, Education.DoesNotExist):
        return render(request, 'intro/detail.html', {'person': person,
                                                     'error': 'You did not select a degree',})
    else:
        print(fav_degree.is_favourite)
        fav_degree.is_favourite = True
        fav_degree.save()
        return render(request, 'intro/detail.html', {'person': person})

'''