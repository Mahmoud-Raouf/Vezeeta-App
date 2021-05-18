from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth.models import User
from .forms import UserCreationForms ,Login_Form , UpdateUserForm ,UpdateProfileForm ,CommentForm , AppointmentForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .models import Profile , Comment , Category ,Appointment
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView , CreateView ,ListView
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponse



def doctors_list(request):
    post = User.objects.order_by('?')

    name = request.GET.get('name')
    address = request.GET.get('address')
    doctor = request.GET.get('doctor')

    if name :
        post = User.objects.filter(
        Q(profile__name__icontains=name)
    )
    if address :
        post = User.objects.filter(
        Q(profile__address__icontains=address)
    )
    if doctor :
        post = User.objects.filter(
        Q(profile__doctor__icontains=doctor)
    )
    
    return render(request , 'user/doctors_list.html',{
        'post' : post,
    })


def doctors_detail(request , slug):
    user_detail = Profile.objects.get(slug=slug)
    comments = Comment.objects.filter(comment=user_detail)#لمعرفه عدد الكومنات واظهار الكومنتات 
    image_category = Category.objects.filter(photo=user_detail )

    if request.method == "POST":
        forms_comment = CommentForm(request.POST)
        if forms_comment.is_valid():
            new_comment = forms_comment.save(commit=False)
            new_comment.comment = user_detail
            new_comment.save()
        forms_comment = CommentForm()

    else:
        forms_comment = CommentForm()
    return render(request , 'user/doctors_detail.html',{
        'user_detail' : user_detail,
        'forms_comment' : forms_comment,
        'comments' : comments,
        'image_category' : image_category,

    })



# Class-Based-View
# class ProfileDetails(DetailView):
#     model = Profile
#     form_class = CommentForm
#     template_name = 'user/doctors_detail.html'

#     def get_object(self, queryset=None):
#         return get_object_or_404(
#             Profile, 
#             slug=self.kwargs['slug'],
#         )

# class CommentCreateView(CreateView):
#     model = Comment
#     template_name = "user/createcomments.html"

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)


# class CommentListView(DetailView):
#     model = Comment
#     template_name = 'user/comments.html'


# user

def signup(request):
    if request.method == 'POST':
        form = UserCreationForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username , password=password)
            login(request, user)
            return redirect('accounts:doctors_list')
    else:
        form = UserCreationForms()
    
    return render(request , 'user/signup.html' , {
        'form' : form,
        'title' : 'إنشاء حساب'
    })



def user_login(request):
    if request.method == 'POST':
        form = Login_Form()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request ,username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('accounts:doctors_list')
        else:
            messages.error(request, "كلمه السر غير صحيحه")
    else:
        form = Login_Form()

    return render(request , 'user/login.html' , {
        'form' : form,
        'title' : 'تسجيل الدخول'
    })


@login_required(login_url='accounts:login')
def profile(request ):
    return render(request , 'user/profile.html' , {
        'title' : 'الصفحه الشخصيه', 
    })

def update_profile(request):
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user.profile)
    
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST , instance=request.user)
        profile_form = UpdateProfileForm(request.POST , request.FILES , instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            return redirect('accounts:profile')

    return render(request , 'user/updata_profile.html' , {
        'title' : 'الصفحه الشخصيه',
        'user_form' : user_form,
        'profile_form' : profile_form,
    })

def appointment(request , slug):
    doctor1 = get_object_or_404(Profile , slug=slug)
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.doctor = doctor1
            user_form.save()
            return redirect('accounts:profile')
        else:
            messages.error(request, "تأكيد من رقم الهاتف والاسم")

    else:
        form = AppointmentForm()
    return render(request , 'user/appointment.html' , {
        'form' : form
    })

def requests(request,slug):
    doctor = get_object_or_404(Profile , slug=slug)
    requests = Appointment.objects.filter(doctor=doctor)
    
    if request.method == 'POST':
        user_id = request.POST['user_id']
        print(user_id)
        r_read = get_object_or_404(Appointment, doctor_id=user_id)
        if r_read.read :
            r_read.read = False
            r_read.save()
        else:
            r_read.read = True
            r_read.save()

    return render(request , 'user/requests.html' , {
        'requests' : requests,
    })

def requests_delete(request , id):
    # user = User.objects.filter(id=request.user.id)
    requests_delete = Appointment.objects.get(id=id).delete()
    return redirect('accounts:requests', slug=request.user.profile.slug)
