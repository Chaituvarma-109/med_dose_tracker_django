from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import MedicineForm
from .models import Medicine


def index(request):
    medicines = None

    if request.user.is_authenticated:
        medicines = Medicine.objects.filter(user=request.user)

    context = {'medicines': medicines}
    return render(request, 'tracker/index.html', context=context)


@login_required
def home(request):
    form = MedicineForm()

    if request.method == "POST":
        form = MedicineForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()

            return redirect('index')

    context = {"form": form,}

    return render(request, 'tracker/home.html', context=context)


@login_required
def edit_form(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk, user=request.user)
    form = MedicineForm(instance=medicine)

    if request.method == "POST":
        form = MedicineForm(data=request.POST, instance=medicine)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()

            return redirect('index')


    context = {'form': form}

    return render(request, 'tracker/edit_med.html', context=context)


@login_required
def delete_med(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk, user=request.user)
    medicine.delete()

    return redirect('index')
