from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login



def home(request):

    
    return render (request, 'index.html')

def student_login(request):
    return render (request, 'student-login.html')

def management_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Check if the user is an admin
            if user.is_staff:  # Assuming admin users are marked as staff
                login(request, user)  # Log the user in
                return redirect('management_dashboard')  # Redirect to the admin dashboard
            else:
                # Handle non-admin user
                return render(request, 'management-login.html', {'error': 'You do not have admin privileges.'})
        else:
            return render(request, 'management-login.html', {'error': 'Invalid username or password.'})

    return render(request, 'management-login.html')


def management_dashboard(request):
    # You can add more context or data to be displayed on the dashboard here
    return render(request, 'management-dashboard.html')

def logout_view(request):
    logout(request)  # This will log out the current user
    return redirect('logout')