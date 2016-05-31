from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.template import loader, RequestContext, Context
import datetime

from books.models import Publisher, Author, Book

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html',
                {'books': books, 'query': q})
    return render(request, 'search_form.html', { 'errors': errors })


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'some initial vlauejkasdas'}
        )
    return render(request, 'contact_form.html', {'form': form})

#---------------------------------
def oldway(request):
    # ...
    t = loader.get_template('template2.html')
    c = Context({
        'app': 'My app',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR'],
        'message': 'I am the second view.'
    })
    return t.render(c)

def custom_proc(request):
    return {
        'app': 'My App',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR'],
    }

def view_1(request):
    t = loader.get_template('template1.html')
    c = RequestContext(request, {'message': 'view1 message'},
            processors=[custom_proc])
    return t.render(c)

def view_2(request):
    t = loader.get_template('template2.html')
    c = RequestContext(request, {'message': 'view2 message'},
            processors=[custom_proc])
    return t.render(c)


def view_3(request):
    return render(request, 'template3.html',
        {'message': 'hello world'},
        context_instance=RequestContext(request, processor=[custom_proc]))
