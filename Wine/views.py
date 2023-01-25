from django.shortcuts import render
from django.http import HttpResponse
from .forms import TextInputForm


# Create your views here.
def my_view(request):
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            # do something with input_text
            return HttpResponse("Input text is : " + input_text)
    else:
        form = TextInputForm()
    return render(request, 'template.html', {'form': form})
