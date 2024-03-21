from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm



def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your account has been created successful, please login to continue')
            return redirect('auth:login')
        else:
            messages.warning(request, 'Something went wrong check you inputs')
            return redirect('auth:signup')
    else:
        form = SignUpForm()
    return render(request, 'authentication/signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.info(request, 'Login successfull enjoy session')
            return redirect('home')
        else:
            messages.warning(request, 'Something went wrong check you inputs')
            
    else:
        return render(request, 'authentication/login.html')


def logout_user(request):
    logout(request)
    messages.info(request, 'Your session has expired, login to continue')
    return redirect('auth:login')

        

# class SignUpView(CreateView):
#     template_name = 'signup.html'
#     form_class = SignUpForm
#     success_url = '/login/'

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         messages.success(self.request, 'Account created successfully. You can now log in.')
#         return response

# class CustomLoginView(LoginView):
#     template_name = 'login.html'
#     authentication_form = AuthenticationForm

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         messages.success(self.request, 'Logged in successfully.')
#         return response

# class CustomLogoutView(LogoutView):
#     next_page = '/login/'

#     def get(self, request, *args, **kwargs):
#         messages.success(self.request, 'Logged out successfully.')
#         return super().get(request, *args, **kwargs)

# class CustomPasswordResetView(PasswordResetView):
#     template_name = 'password_reset.html'
#     form_class = CustomPasswordResetForm
#     success_url = '/password-reset/done/'

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         messages.success(self.request, 'Password reset email sent successfully.')
#         return response

# class CustomPasswordResetConfirmView(PasswordResetConfirmView):
#     template_name = 'password_reset_confirm.html'
#     success_url = '/password-reset/complete/'

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         messages.success(self.request, 'Password reset successful. You can now log in with your new password.')
#         return response
