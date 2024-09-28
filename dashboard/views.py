from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount
from django.shortcuts import render

@login_required
def dashboard_view(request):
    social_account = SocialAccount.objects.get(user=request.user, provider='google')
    extra_data = social_account.extra_data  # This contains all the profile info

    # Example: Access specific data
    email = extra_data.get('email')
    first_name = extra_data.get('given_name', '').capitalize()
    last_name = extra_data.get('family_name', '').capitalize()
    profile_picture = extra_data.get('picture')  # Profile picture URL

    context = {
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'profile_picture': profile_picture,
    }
    return render(request, 'dashboard/dashbaordpage.html', context)