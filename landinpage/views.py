from .forms import EmailPostForm
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404 
from .models import MainSection, Sector, Stat, Service, Project, Team, BucoInfo
# Create your views here.

def index(request):
    sections = MainSection.objects.all()
    sectors = Sector.objects.order_by('title')
    stats = Stat.objects.all()
    services = Service.objects.all()
    teams = Team.objects.all()
    infos = BucoInfo.objects.first()
    sent = False
    # sending email setup
    if request.method == 'POST':
        # Form is submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form field pass validation
            cd = form.cleaned_data
            subject = f"Mail de :{cd['name']}" + f' Objet du message:' + cd['subject']
            message = cd['message']
            email = cd['email']
            send_mail(subject, message, email, ['buco@gmail.com'])
            sent = True
    else:
        form = EmailPostForm()

    data = {
            'sections': sections, 
            'sectors': sectors, 
            'stats': stats, 
            'services': services,
            'teams': teams,
            'infos': infos,
            'sent': sent,
            'form': form,
        }
    return render(request, 'landinpage/index.html', data)

def portofolio(request, title):

    service = get_object_or_404(Service, title=title)
    projects = Project.objects.filter(service=service.id)

    print(projects)
    # service = Service.objects.filter(servi)
    # projects = Project.objects.filter(service=id)
    # print(projects)
    data = {
        'projects': projects, 
        'service': service
        }

    return render(request, 'landinpage/portofolio.html', data)