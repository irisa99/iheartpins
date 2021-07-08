from rest_framework import serializers
from django.forms.models import model_to_dict
from trans.models import Listing, ListingImage
from main.models import ItemImage, Item, PinventoryContent


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ['id','image','is_primary']
        depth = 2

    def get_image_url(self,obj):
        return obj.image.url

    def to_representation(self, instance):
        image = super(ItemImageSerializer, self).to_representation(instance)
        return image


class ItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')
    class Meta:
        model = Item
        fields = [
            'name',
            'image',
            'is_accepted',
            'type',
            'descrip',
            'date_item_added',
        ]
        depth = 2

    def get_image(self, item):
        image = ItemImage.objects.filter(item=item.id)
        if not ItemImageSerializer(image, many=True, read_only=True, context=self.context).data:
            return None
        else:
            return ItemImageSerializer(image, many=True, read_only=True, context=self.context).data[0]


class PinventoryContentSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    class Meta:
        model = PinventoryContent
        fields = '__all__'
        depth = 3


class ListingImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = ListingImage
        fields = ['id','image','image_url','is_primary']
        depth = 2

    def get_image_url(self,obj):
        return obj.image.url

    def to_representation(self, instance):
        image = super(ListingImageSerializer, self).to_representation(instance)
        return image


class ListingSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')
    pinventory_content = PinventoryContentSerializer(read_only=True)
    class Meta:
        model = Listing
        fields = [
            'id',
            'pinventory_content',
            'for_sale',
            'for_trade',
            'qty_available',
            'condition',
            'descrip',
            'price',
            'date_listing_created',
            'is_inactive',
            'image',
        ]
        depth = 6

    def get_image(self, listing):
        image = ListingImage.objects.filter(listing=listing.id)
        if not ListingImageSerializer(image, many=True, read_only=True, context=self.context).data:
            return None
        else:
            return ListingImageSerializer(image, many=True, read_only=True, context=self.context).data[0]
