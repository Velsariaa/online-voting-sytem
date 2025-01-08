from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import (
    adminnform as AdminForm,
    registrationform as RegistrationForm,
    loginform as LoginForm,
    contactform as ContactForm,
    candidacyform as CandidacyForm,
    credentialsform as CredentialsForm,
    resetpass as ResetPass,
    comelecform as ComelecForm,
    voteform as voteform,
)
from .models import comelecform, adminnform, candidacy_form, Candidate, voteform

# admin
@login_required(login_url='loginform')
def admin_form_view(request):
    if request.session.get('role') != 'admin':
        return redirect('loginform')

    form = AdminForm()

    if request.method == 'POST':
        positions = request.POST.getlist('position')  # Extract selected positions
        others1 = request.POST.get('others1', '')  # Extract other 1 content
        others2 = request.POST.get('others2', '')  # Extract other 2 content
        others3 = request.POST.get('others3', '')  # Extract other 3 content
        others4 = request.POST.get('others4', '')  # Extract other 4 content
        others5 = request.POST.get('others5', '')  # Extract other 5 content

        # Populate the data dictionary for saving
        form_data = {
            'institute': request.POST.get('institute', ''),
            'startdate': request.POST.get('startdate', ''),
            'enddate': request.POST.get('enddate', ''),
            'positions': ', '.join(positions),  # Save positions as a comma-separated string
            'others1': others1,
            'others2': others2,
            'others3': others3,
            'others4': others4,
            'others5': others5,
        }

        form = AdminForm(form_data)

        # Check if the form is valid and save
        if form.is_valid():
            form.save()
            return redirect('adminnform')
        else:
            # Handle errors
            messages.error(request, "There was an error with the form submission.")

    return render(request, 'adminnform.html', {'form': form})



# Registration view
def registration_form_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confpass = form.cleaned_data.get('confpass')
            if password == confpass:
                # Save to registrationform
                new_user = form.save()

                # Create a Django user for authentication
                user = User.objects.create_user(
                    username=new_user.uid,  # Use User ID as the username
                    password=password,
                    first_name=new_user.fname,
                    last_name=new_user.lname,
                    email=new_user.emailadd,
                )

                # Save to comelecform
                comelecform.objects.create(
                    fname=new_user.fname,
                    mname=new_user.mname,
                    lname=new_user.lname,
                    age=new_user.age,
                    gender=new_user.gender,
                    suffix=new_user.suffix,
                    idtype=new_user.idtype,
                    idnum=new_user.idnum,
                    uid=new_user.uid,
                    emailadd=new_user.emailadd,
                    contact=new_user.contact,
                )
                messages.success(request, "Registration successful! Please log in.")
                return redirect('loginform')
            else:
                form.add_error('confpass', 'Passwords do not match')
    context = {'form': form}
    return render(request, 'registrationform.html', context)


# Login view for all users (Admin, COMELEC, User)
@never_cache
def login_form_view(request):
  
    if request.user.is_authenticated:
        return redirect('user')  

    form = LoginForm()

    if request.method == 'POST':
        uid = request.POST.get('uid')  # User ID from form
        password = request.POST.get('password')  # Password from form

        # Admin credentials
        if uid == "admin" and password == "admin":
            request.session['role'] = 'admin'  # Save role in session
            return redirect('adminnform')  # Redirect to Admin Main Page

        # COMELEC credentials
        elif uid == "comelec" and password == "comelec":
            request.session['role'] = 'comelec'  # Save role in session
            return redirect('comelec')  # Redirect to COMELEC Page

        # Authenticate regular user
        user = authenticate(request, username=uid, password=password)
        if user is not None:
            login(request, user)
            request.session['role'] = 'user'  # Save role in session
            return redirect('user')  # Redirect to User Dashboard

        # Invalid credentials
        messages.error(request, "Invalid User ID or Password.")
    else:
        form = LoginForm()  # Render empty form on GET requests

    return render(request, 'loginform.html', {'form': form})



# Logout view
def logoutUser(request):
    logout(request)
    request.session.flush()  # Clear session
    return redirect('loginform')


# Contact view
def contact_form_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'contactform.html', context)


# Candidacy form view
@login_required(login_url='loginform')
def candidacy_form_view(request):
    form = CandidacyForm()

    # Fetch all admin form entries
    admin_forms = adminnform.objects.all()
    position_list = []

    # Extract positions from each admin form entry
    for admin_form in admin_forms:
        if admin_form.positions:
            positions = admin_form.positions.split(',')  # Split positions by comma
            position_list.extend([pos.strip() for pos in positions])  # Add to the list

    # Collect the "OTHERS" positions from the admin form fields
    others_positions = []
    others_fields = [
        ('others1', admin_form.others1),
        ('others2', admin_form.others2),
        ('others3', admin_form.others3),
        ('others4', admin_form.others4),
        ('others5', admin_form.others5),
    ]

    # Append the content of the "OTHERS" fields to the list
    for _, other_value in others_fields:
        if other_value:
            others_positions.append(other_value.strip())  # Add to "OTHERS" list

    # Ensure "OTHERS" come first in the list, maintaining the order in which they were checked
    position_list = others_positions + position_list  # "OTHERS" come first

    # Remove duplicates if any
    position_list = list(set(position_list))

    # Pass the position list to the template context
    context = {'form': form, 'position_list': position_list}

    if request.method == 'POST':
        form = CandidacyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'candidacyform.html', context)

# Credentials form view
def credentials_form_view(request):
    form = CredentialsForm()
    if request.method == 'POST':
        form = CredentialsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('candidacyform')
    context = {'form': form}
    return render(request, 'credentialsform.html', context)


# Reset password view
def reset_form_view(request):
    form = ResetPass()
    if request.method == 'POST':
        uid = request.POST.get('uid')
        newpass = request.POST.get('newpass')
        confirmpass = request.POST.get('confirmpass')
        if newpass != confirmpass:
            messages.error(request, "Passwords do not match.")
            return render(request, 'resetpass.html', {'form': form})
        try:
            user = User.objects.get(username=uid)  # Use the Django User model
            user.set_password(newpass)
            user.save()
            messages.success(request, "Password has been successfully reset.")
            return redirect('loginform')
        except User.DoesNotExist:
            messages.error(request, "User ID not found.")
            return render(request, 'resetpass.html', {'form': form})
    return render(request, 'resetpass.html', {'form': form})


# Protected User Dashboard
@login_required(login_url='loginform')
def user(request):
    try:
        user_details = comelecform.objects.get(uid=request.user.username)
        context = {
            'user_details': user_details
        }
    except comelecform.DoesNotExist:
        messages.error(request, "User details not found")
        context = {}
    
    return render(request, 'usermain.html', context)


# Protected Voting View
@login_required(login_url='loginform')
def vote(request):
    return render(request, 'voteform.html')

#comelec
@login_required(login_url='loginform')
def user_management_view(request):
    if request.session.get('role') != 'comelec':
        return redirect('loginform')  # Restrict non-COMELEC access
    
    total_registered_users = comelecform.objects.count()
    total_candidates = candidacy_form.objects.count()
    total_votes = voteform.objects.count()
    
    users = comelecform.objects.all()
    form = ComelecForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('comelec')
    
    context = {'users': users,
               'form': form,
               'total_registered_users': total_registered_users,
               'total_candidates': total_candidates,
               'total_votes': total_votes,}
    return render(request, 'comelecform.html', context)


def user_management_update(request, pk):
    com = get_object_or_404(comelecform, id=pk)
    form = ComelecForm(instance=com)
    if request.method == "POST":
        form = ComelecForm(request.POST, instance=com)
        if form.is_valid():
            form.save()
            return redirect('comelec')
    context = {'form': form, 'com': com}
    return render(request, 'comelecform.html', context)


def user_management_delete(request, pk):
    comelecform.objects.filter(id=pk).delete()
    return redirect('comelec')


# View for displaying the voting form
def vote(request):
    candidates_position_1 = Candidate.objects.filter(position="Position 1")
    candidates_position_2 = Candidate.objects.filter(position="Position 2")
    candidates_position_3 = Candidate.objects.filter(position="Position 3")

    if request.method == "POST":
        # Collect the vote choices
        vote1_id = request.POST.get('vote1')
        vote2_id = request.POST.get('vote2')
        vote3_id = request.POST.get('vote3')
        
        # Save the vote
        vote.objects.create(
            voter_id=request.user.id,  # Assuming a logged-in user
            vote1_id=vote1_id,
            vote2_id=vote2_id,
            vote3_id=vote3_id
        )
        
        return redirect('submitted')  # Redirect to the thank you page

    return render(request, 'voteform.html', {
        'candidates_position_1': candidates_position_1,
        'candidates_position_2': candidates_position_2,
        'candidates_position_3': candidates_position_3,
    })



# Thank you page after vote submission
def voting_thank_you_view(request):
    return render(request, 'votesubmitted.html')

# User dashboard view
@login_required(login_url='loginform')
def dashboard(request):
    if request.session.get('role') != 'user':
        return redirect('loginform')  # Restrict non-user access
    return render(request, 'dashboard.html')


# Index (homepage) view
def index(request):
    return render(request, 'homepage.html')


# About view
def about(request):
    return render(request, 'about.html')

# Vote submitted confirmation view
def submitted(request):
    return render(request, 'votesubmitted.html')

#template
def inheritance(request):
    return render(request, 'inheritance.html')
