from django.shortcuts import render, redirect
from .models import Costume, Like, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request, 'costumes/index.html')

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
    return render(request, 'costumes/view_costumes.html', {'costumes': costumes})