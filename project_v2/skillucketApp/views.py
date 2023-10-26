from skillucketApp.forms.register import RegisterForm
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from skillucketApp.forms.skills_profile import ProfileForm
from skillucketApp.forms.skills_profile import SkillForm
from .models.profile import Profile
from .forms.user_and_profile import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from .models.user_skill import UserSkill
from .models.bucket_skill import BucketSkill
from .models.skill import Skill
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms.add_skill import BucketSkillForm


def home_view(request):
    """  the template contains image carousel, this function sends the info for thr template to loop on
    instead of repeating it in the html file """

    content = ["Welcome to Skillucket!",
               "The best place to acquire the skills you have always desired",
               "Our mission is to foster human connections through the joy of learning", "Simply create an account, "
               "populate your bucket list with skills you are eager to learn, and discover your matches. "]

    slides = [{
            'image': 'images/homepage/computer.png',
            'title': 'First slide',
            'content': content
        },
        {
            'image': 'images/homepage/diy.png',
            'title': 'Second slide',
            'content': content
        },
        {
            'image': 'images/homepage/painting.png',
            'title': 'Third slid',
            'content': content
        },
        {
            'image': 'images/homepage/programing.png',
            'title': 'Fourth slid',
            'content': content
        }
    ]
    return render(request, "home.html", {'slides': slides})


# Views related to user management


@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }
    return render(request, "profile_v2.html", context)


def register(request):
    """Register view handles get and post requests.
    Register new user to db and create automatically a profile for the user.
    If a profile pic was sent in the registration form, it is added to the profile.
    After successful registration, redirect to login.
    """

    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data
            try:
                user = User.objects.create_user(username=form_data["username"], password=form_data["password"], email=form_data["email"])
                if user:
                    if "image" in request.FILES:
                        image = request.FILES["image"]
                        profile = Profile.objects.get(user=user)
                        profile.image = image
                        profile.save()
                    return redirect("login")
                else:
                    return HttpResponse("Failed to create user")
            except IntegrityError:
                form.add_error(None, "Username or email already exists")
    else:
        form = RegisterForm()

    return render(request, "register_v4.html", {"form": form})


def login_view(request):
    """
    Login view uses Django built in AuthenticationForm, authenticate function and login function
    """

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("profile")
    else:
        form = AuthenticationForm()

    return render(request, "login_v4.html", {"form": form})


def logout_view(request):
    """
        Handle user logout.
        This view logs the user out and redirects them to the home page.
    """
    logout(request)
    return redirect("home")


# Views related to user_skills


@method_decorator(login_required, name='dispatch')
class UserSkillsListView(ListView):
    model = UserSkill
    template_name = 'user_skills_list.html'
    context_object_name = 'user_skills'

    def get_queryset(self):
        return UserSkill.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class UserSkillsCreateView(CreateView):
    model = UserSkill
    fields = ['skill', 'proficiency_level', 'notes']
    template_name = "user_skills_create.html"
    success_url = reverse_lazy('user_skills')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class UserSkillUpdateView(UpdateView):
    model = UserSkill
    fields = ['skill', 'proficiency_level', 'notes']
    template_name = 'user_skill_update.html'
    success_url = reverse_lazy('user_skills')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404("User Skill not found")
        return obj

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class UserSkillDeleteView(DeleteView):
    model = UserSkill
    template_name = 'userskill_confirm_delete.html'
    success_url = reverse_lazy('user_skills')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404("User Skill not found")
        return obj


# Views related to bucket_skills

@method_decorator(login_required, name='dispatch')
class BucketSkillsListView(ListView):
    model = BucketSkill
    template_name = 'bucket_skills_list.html'
    context_object_name = 'bucket_skills'

    def get_queryset(self):
        return BucketSkill.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class BucketSkillsCreateView(CreateView):
    model = BucketSkill
    form_class = BucketSkillForm
    template_name = "bucket_skills_create.html"
    success_url = reverse_lazy('bucket_skills')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class BucketSkillUpdateView(UpdateView):
    model = BucketSkill
    fields = ['skill', 'target_date', 'notes']
    template_name = 'bucket_skills_update.html'
    success_url = reverse_lazy('bucket_skills')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404("Bucket Skill not found")
        return obj

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class BucketSkillDeleteView(DeleteView):
    model = BucketSkill
    template_name = 'bucketskill_confirm_delete.html'
    success_url = reverse_lazy('bucket_skills')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404("Bucket Skill not found")
        return obj


#  matches related views:


@login_required
def list_matches_view(request):
    user = request.user
    wanted_skills = Skill.objects.filter(bucketskill__user=user)  # getting the skills object through bucket_skill
    matching_users = User.objects.filter(userskill__skill__in=wanted_skills).distinct().exclude(id=user.id)
    matching_data = {}
    for matching_user in matching_users:
        user_skills = UserSkill.objects.filter(user=matching_user, skill__in=wanted_skills)

        for user_skill in user_skills:
            skill = user_skill.skill.name

            if skill not in matching_data:
                matching_data[skill] = []

            matching_data[skill].append({"user": matching_user, "user_skill": user_skill})

    context = {"matching_data": matching_data}
    return render(request, "matching_users.html", context)


@login_required
def search_skill_view(request):
    params = request.GET.get('skill', '')
    if not params:
        messages.error(request, 'Please enter a search query.')
        return redirect('home')
    else:
        matching_skills = Skill.objects.filter(name__icontains=params)
        matching_users = User.objects.filter(userskill__skill__in=matching_skills).distinct().exclude(id=request.user.id)
        if not matching_users:
            messages.error(request, 'No matches for this search term.')
            redirect('home')
        matching_data = {}
        for matching_user in matching_users:
            user_skills = UserSkill.objects.filter(user=matching_user, skill__in=matching_skills)

            for user_skill in user_skills:
                skill = user_skill.skill.name

                if skill not in matching_data:
                    matching_data[skill] = []

                matching_data[skill].append({"user": matching_user, "user_skill": user_skill})

        context = {"matching_data": matching_data}
        return render(request, "search_skill.html", context)