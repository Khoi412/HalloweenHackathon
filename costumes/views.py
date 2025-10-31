from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'costumes/index.html')

def costumes_submission_page(request):
    return render(request, 'costumes/costumes_submission.html')