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
        caption = request.POST.get('costume_caption')
        image = request.FILES.get('costume_image')
        # You would typically save the data to the database here
        # For now, we can just print it to the console (or handle as needed)
        print(f"Received caption: {caption}")
        print(f"Received image: {image.name if image else 'No image uploaded'}")
        # Redirect or render a success page as needed
        return redirect('view_costumes')  # Redirect to view costumes page after submission)
    
    return render(request, 'costumes/costumes_submission.html')

def view_costumes(request):
    # This view would typically fetch costume submissions from the database
    costumes = Costume.objects.all().order_by('-timestamp')  # Example: Fetch all costumes ordered by timestamp
    return render(request, 'costumes/view_costumes.html', {'costumes': costumes})