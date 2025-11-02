from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Costume, Like, Comment
from django.contrib.auth.decorators import login_required


# Create your views here.
def homepage(request):
    return render(request, 'costumes/index.html')


def tickets(request):
    return render(request, 'costumes/tickets.html')


@login_required
def costumes_submission_page(request):

    if request.method == 'POST':
        # Handle form submission logic here
        try:
            caption = request.POST.get('costume_caption')
            image = request.FILES.get('costume_image')
            costume = Costume.objects.create(
                user=request.user,
                image=image,
                caption=caption
            )
            return redirect('view_costumes')  # Redirect to view costumes page after submission)
        except Exception as e:
            print(f"Error uploading costume: {e}")
            return redirect('costumes_submission_page')
            # Optionally, add error handling logic here (e.g., display an error message)

    return render(request, 'costumes/costumes_submission.html')


def view_costumes(request):
    # This view would typically fetch costume submissions from the database
    costumes = Costume.objects.all().order_by('-timestamp')  # Example: Fetch all costumes ordered by timestamp
    usersLiked = Like.objects.filter(user=request.user).values_list('costume_id', flat=True) if request.user.is_authenticated else []
    for costume in costumes:
        costume.user_has_liked = costume.id in usersLiked
    return render(request, 'costumes/view_costumes.html', {'costumes': costumes})


@login_required
def like_costume(request, costume_id):
    if request.method == 'POST':
        try:
            costume = Costume.objects.get(pk=costume_id)
        except Costume.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Costume not found'}, status=404)

        like, created = Like.objects.get_or_create(user=request.user, costume=costume)

        if created:
            # A new like was created (user just LIKED it)
            is_now_liked = True
        else:
            # The like already existed (user is UNLIKING it)
            like.delete()
            is_now_liked = False

        new_like_count = costume.likes.count() 

        return JsonResponse({
            'status': 'success',
            'likes_count': new_like_count,
            'is_liked': is_now_liked,  # 👈 PASS THIS BACK!
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
