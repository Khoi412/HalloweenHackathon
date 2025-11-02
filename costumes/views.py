from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Costume, Like, Comment
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
def homepage(request):
    return render(request, 'costumes/index.html')


def tickets(request):
    return render(request, 'costumes/tickets.html')


def about(request):
    return render(request, 'costumes/about.html')


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


@login_required
def comment_costume(request, costume_id):
    if request.method == 'POST':
        try:
            costume = Costume.objects.get(pk=costume_id)
        except Costume.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Costume not found'}, status=404)

        try:
            data = json.loads(request.body)
            text = data.get('text', '').strip()
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)

        if not text:
            return JsonResponse({'status': 'error', 'message': 'Comment text cannot be empty'}, status=400)

        comment = Comment.objects.create(
            user=request.user,
            costume=costume,
            text=text
        )

        return JsonResponse({
            'status': 'success',
            'comment': {
                'user': comment.user.username,
                'text': comment.text,
                'timestamp': comment.timestamp.strftime('%Y-%m-%d %H:%M'),
            }
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

def get_comments(request, costume_id):
    try:
        costume = Costume.objects.get(pk=costume_id)
    except Costume.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Costume not found'}, status=404)

    comments = costume.comments.all().order_by('-timestamp')
    comments_data = [{
        'user': comment.user.username,
        'text': comment.text,
        'timestamp': comment.timestamp.strftime('%Y-%m-%d %H:%M'),
    } for comment in comments]

    return JsonResponse({'status': 'success', 'comments': comments_data})