from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.db.models import Q
from .models import PinventoryContent, ItemImage, Item
from .forms import SubmitPin, SubmitPinSet, SelectType, SubmitImage
from django.contrib.auth import get_user_model
from django.contrib import messages
import random


User = get_user_model()

def landing(request):
    return render(request, 'main/landing.html')


def homepage(request):
    return render(request, 'main/home.html')

def home(request):
    all_items = list(Item.objects.all())
    sample_items = random.sample(all_items, 6)
    images_primary = ItemImage.objects.filter(item__in=sample_items, is_primary=True)

    return render(request, 'main/home.html',{
        'sample_items':sample_items,
        'images_primary':images_primary,
    })

def search_pindex(request):
    print('Hello')
    query = request.GET.get('query', '')
    items = Item.objects.filter(Q(name__icontains=query))
    query_item_images = ItemImage.objects.filter(item__in=items, is_primary=True)

    return render(request, 'main/pindex_search_results.html', {
        'items':items,
        'query':query,
        'query_item_images':query_item_images,
    })


@login_required
def pinventory(request):
    pinventory = request.user.pinventory
    v = PinventoryContent.objects.filter(pinventory=pinventory)
    v_items = Item.objects.filter(pinventorycontent__in=v)
    v_images = ItemImage.objects.filter(item__in=v_items, is_primary=True)

    return render(request, 'main/pinventory.html', {
        'v':v,
        'pinventory':pinventory,
        'v_items':v_items,
        'v_images':v_images,
    })


def item_detail(request, item_slug):
    item = get_object_or_404(Item, slug=item_slug)
    main_item_images = ItemImage.objects.filter(item=item)
    main_item_primary_image = main_item_images.get(is_primary=True)
    similar_item_images = list(ItemImage.objects.filter(is_primary=True).exclude(item=item.id))
    if len(similar_item_images) >= 6:
        similar_item_images = random.sample(similar_item_images, 6)
        for item_image in similar_item_images:
            individual_item = item_image.item

    return render(request, 'main/item_detail.html', {
        'item':item,
        'main_item_images':main_item_images,
        'main_item_primary_image':main_item_primary_image,
        'similar_item_images':similar_item_images,
        'item_image':item_image,
        'individual_item':individual_item,
    })

@login_required
def submit_item(request):
    form1 = SelectType()
    form2 = SubmitPinSet()
    form3 = SubmitPin()
    ImageFormSet = modelformset_factory(ItemImage, SubmitImage, extra=5)
    formset = ImageFormSet(queryset=ItemImage.objects.none())
    if request.method == 'POST' and form1:
        form1 = SelectType(request.POST or None)
        formset = ImageFormSet(request.POST, request.FILES, queryset=ItemImage.objects.none())
        if form1.is_valid():
            if request.POST['type'] == '1':
                form2 = SubmitPinSet(request.POST or None)
                if form2.is_valid() and formset.is_valid():
                    item = form2.save(commit=False)
                    item.type = 1
                    item.submitted_by = request.user
                    item.slug = slugify(item.name)
                    item.save()
                    for form in formset.cleaned_data:
                        if form:
                            image = form['image']
                            photo = ItemImage(item=item, image=image)
                            photo.save()
                    messages.add_message(request, messages.SUCCESS, 'Request sumbitted successfully.')
                    return redirect('submit')
            else:
                form3 = SubmitPin(request.POST or None)
                if form3.is_valid() and formset.is_valid():
                    item = form3.save(commit=False)
                    item.type = 0
                    item.submitted_by = request.user
                    item.slug = slugify(item.name)
                    item.save()
                    for form in formset.cleaned_data:
                        if form:
                            image = form['image']
                            photo = ItemImage(item=item, image=image)
                            photo.save()
                    messages.add_message(request, messages.SUCCESS, 'Request sumbitted successfully.')
                    return redirect('submit')
    else:
        form3 = SubmitPin()
        form2 = SubmitPinSet()
        formset = ImageFormSet(queryset=ItemImage.objects.none())
    return render(request, 'main/submit_item.html', {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'formset': formset,
    })

def contact_us(request):
    return render(request, 'main/contact.html')

