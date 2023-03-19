from django.shortcuts import render
from discussion.forms import ContactForm
from django.contrib import messages
from discussion.models import Post


def home(request):
    form = ContactForm()
    if request.user.is_authenticated and request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request, "Thankyou for contact us!! Your message has been sent.",
                             extra_tags='alert alert-success alert-dismissible fade show')
        else:
            messages.error(request, "Oops something is missing!! Please try again",
                           extra_tags='alert alert-warning alert-dismissible fade show')
    elif request.method == "POST":
        messages.error(request, "Please login to send message!!",
                       extra_tags='alert alert-warning alert-dismissible fade show')
    try:
        posts = Post.objects.order_by('-pub_date')[:6]
    except:
        pass
    return render(request, 'home.html', {'form': form, 'posts': posts})
