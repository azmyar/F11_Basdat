from django.shortcuts import render

def chart(request):
    context = {
        'name': 'Kelompok',
        'class': 'Basdat F'
    }

    return render(request, "chart.html", context)

def chart_detail(request):

    return render(request, 'chart_detail.html')