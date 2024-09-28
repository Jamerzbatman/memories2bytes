from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import UserInfoForm, MediaDetailForm
from .models import MediaDetail , Quote
import json

def add_quote_view(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request
            data = json.loads(request.body)

            # Extract user info from the data
            user_form_data = {
                'first_name': data.get('firstName'),
                'last_name': data.get('lastName'),
                'email': data.get('email')
            }

            # Validate user form with extracted data
            user_form = UserInfoForm(user_form_data)

            if user_form.is_valid():
                # Access the cleaned data after validation
                email = user_form.cleaned_data['email']
                first_name = user_form.cleaned_data['first_name']
                last_name = user_form.cleaned_data['last_name']

                # Create or get the user
                user, created = User.objects.get_or_create(
                    email=email,
                    defaults={
                        'username': email,
                        'first_name': first_name,
                        'last_name': last_name
                    }
                )

                if created:
                    user.set_unusable_password()  # Create user without password
                    user.save()

                # Create a new Quote instance for the user
                quote = Quote(user=user)
                quote.save()  # Save the Quote to generate the hash

                # Process media details from the request
                media_entries = data.get('media', [])
                if not media_entries:
                    return JsonResponse({'success': False, 'message': 'No media entries provided'})

                # Save media information to the database
                for media in media_entries:
                    media_type = media.get('mediaType')
                    quantity = media.get('quantity')
                    condition = media.get('condition')

                    # Create MediaDetail instances associated with the Quote
                    MediaDetail.objects.create(
                        quote=quote,  # Associate with the created Quote
                        type=media_type,
                        quantity=quantity,
                        condition=condition
                    )

                # Return success as JSON response
                return JsonResponse({'success': True, 'message': 'Quote submitted successfully!'})

            else:
                # Return form errors if validation fails
                return JsonResponse({'success': False, 'errors': user_form.errors})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})