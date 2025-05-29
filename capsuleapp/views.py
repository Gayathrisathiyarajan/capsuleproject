from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.urls import *
from django.http import JsonResponse
from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.management import call_command
from django.utils.timezone import now

def CapsuleInsertUpdateView(request):
    capsule_id = request.GET.get('capsule_id') or '0'
    capsule = TimeCapsule.objects.filter(id=capsule_id).first() if capsule_id != '0' else None
    if request.method == 'POST':
        form = TimeCapsuleForm(request.POST, request.FILES, instance=capsule)
        if form.is_valid():
            form.save()
            return redirect('CapsuleInsertUpdateView')
    else:
        form = TimeCapsuleForm(instance=capsule)
    today = now().date()
    unsent_capsules = TimeCapsule.objects.filter(unlock_date=today, email_sent=False)
    for cap in unsent_capsules:
        send_mail(
            subject=f"Your Time Capsule: {cap.title}",
            message=cap.message,
            from_email='yourcapsulemessage@gmail.com',
            recipient_list=[cap.email],
            fail_silently=True
        )
        cap.email_sent = True
        cap.save()
    capsules = TimeCapsule.objects.all()
    return render(request, 'capsule.html', {'form': form, 'capsules': capsules, 'capsule': capsule, 'page': 'edit' if capsule else 'create', 'capsule_id': capsule_id})


def CapsuleDeleteView(request):
    if request.method == 'POST':
        capsule_id = request.POST.get('id')
        capsule = TimeCapsule.objects.get(id=capsule_id).delete()
        return JsonResponse({'status': 'success'})

def run_capsule_email(request):
    call_command('send_email_capsule')
    return HttpResponse("✅ Time Capsule emails sent!")