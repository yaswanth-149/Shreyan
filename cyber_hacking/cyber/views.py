from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Sample initial data stored in memory for demonstration
ADD_DATA_RECORDS = []

@login_required(login_url='login')
def dashboard_view(request, tab_name='graphical_analysis', chart_type='bar'):
    global ADD_DATA_RECORDS
    
    # Handle form submission when user clicks Submit in "ADD DATA" tab
    if request.method == 'POST' and tab_name == 'add_data':
        entity = request.POST.get('entity')
        year = request.POST.get('year')
        records = request.POST.get('records')
        org_type = request.POST.get('org_type')
        methods = request.POST.get('methods')
        add_data_val = request.POST.get('add_data_val')
        time_val = request.POST.get('time_val')

        ADD_DATA_RECORDS.append({
            'entity': entity,
            'year': year,
            'records': records,
            'org_type': org_type,
            'methods': methods,
            'add_data_val': add_data_val,
            'time_val': time_val,
        })
        return redirect('dashboard_tab', tab_name='malware_data')

    context = {
        'active_tab': tab_name,
        'chart_type': chart_type,
        'records': ADD_DATA_RECORDS,
    }
    return render(request, 'cyber/dashboard.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cyber/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'cyber/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
