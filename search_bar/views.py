from django.shortcuts import render

# Create your views here.
def search_bar(request):
    context = {
    }
    return render(request, "search_bar.html", context)