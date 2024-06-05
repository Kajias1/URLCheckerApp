from django.shortcuts import render, redirect
from requests.exceptions import MissingSchema
from requests.exceptions import InvalidURL
import requests

from .models import URLRecord
from .forms import URLRecordForm

def index(request):
    url_records = URLRecord.objects.all().order_by('date_added')
    url_add_success = False
    errors = {}
    messages = {}

    if request.method == 'POST':
        form = URLRecordForm(request.POST)
        if form.is_valid():
            new_url_record = form.save(commit=False)
            if not URLRecord.objects.filter(url=new_url_record.url).exists():
                try:
                    new_url_record.status = check_url(new_url_record.url)
                    new_url_record.save()
                    url_add_success = True
                except (MissingSchema, InvalidURL):
                    redirect('index')
                    errors['url_format_error_message'] = 'Введите правильный формат URL'
            else:
                messages['url_already_exists'] = 'Данный URL уже добавлен'
    form = URLRecordForm()
    return render(request, 'index.html', context={'url_records': url_records, 'url_add_form': form, 'url_add_success': url_add_success, 'errors': errors, 'messages': messages})

def check_all(request):
    for record in URLRecord.objects.all():
        record.status = check_url(record.url)
        record.save()
    return redirect('/')

def check_url(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def delete_url_record(request, id: int):
    URLRecord.objects.filter(id=id).delete()
    return redirect('/')

def check_url_record(request, id: int):
    record = URLRecord.objects.filter(id=id).first()
    if record != None:
        record.status = check_url(record.url)
        record.save()
    return redirect('/')