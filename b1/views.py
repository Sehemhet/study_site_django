from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from b1.models import *
from b1.forms import AddPostForm, RegisterUserForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from b1.forms import LoginUserForm, ContactForm

# from aaa.b1.models import Women, Category

menu = [
    {'title':'О сайте','url_name':'about'},
    {'title':'Добавить статью','url_name':'add_page'},
    {'title':'Обратная связь','url_name':'contact'},
    {'title':'ПУТЬ','url_name':'brand'},
]

class home_page(ListView):
    paginate_by = 3
    model = Women
    context_object_name = 'posts'
    template_name = 'b1/index.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)      #То что будет читаться из модели




# def home_page(request):
#     posts = Women.objects.all()
#     data = {
#         'menu':menu,
#         'title':'Home page',
#         'posts':posts,
#         'cat_selected':0,
#     }
#     return render(request, 'b1/index.html', data)

class show_post(DetailView):
    model = Women
    template_name = 'b1/post.html'
    slug_url_kwarg = 'post_slug'
    # pk_url_kwarg = 'pk' # cat_id # post_id
    context_object_name = 'post'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['title'] = context['post']
        return context


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#
#     data = {
#         'post':post,
#         'menu':menu,
#         'title':post.title,
#         'cat_selected':post.cat_id,
#     }
#     return render(request, 'b1/post.html', data)

class show_category(ListView):
    paginate_by = 3
    model = Women
    context_object_name = 'posts'
    template_name = 'b1/index.html'
    allow_empty = False

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - '+ str(context['posts'][0].cat)
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#     # cats = Category.objects.annotate(Count('women'))
#     data = {
#         # 'cats':cats,
#         'menu':menu,
#         'title':'отображение по рубрикам',
#         'posts':posts,
#         'cat_selected': cat_id,
#     }
#     return render(request, 'b1/index.html', data)

def about(request):
    data = {
        'menu':menu
    }
    return render(request, 'b1/about.html', data)

class add_page(CreateView):
    form_class = AddPostForm            #
    template_name = 'b1/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        return context


# def add_page(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             try:
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления поста')
#
#     else:
#         form = AddPostForm()
#     data = {
#         'menu':menu,
#         'form':form,
#     }
#     return render(request, 'b1/addpage.html', data)

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'b1/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обратная связь'
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        return context


    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')
#
# def login(request):
#     data = {
#         'menu':menu
#     }
#     return render(request, 'b1/about.html', data)


# def register(request):
#     return HttpResponse('<h1>Регистрация</h1>')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'b1/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['title'] = 'Регистрация'
        context['cat_selected'] = 0
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'b1/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['title'] = 'Авторизация'
        context['cat_selected'] = 0
        return context

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return dict(list(context.items()) + list(c_def.items()))

# Create your views here.
