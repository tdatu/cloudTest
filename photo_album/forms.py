from django.forms import ModelForm

from cloudinary.forms import CloudinaryJsFileField, CloudinaryUnsignedJsFileField
# Next two lines are only used for generating the upload preset sample name
from cloudinary.compat import to_bytes
import cloudinary, hashlib
from cloudinary.forms import CloudinaryFileField

from .models import Photo

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

    image = CloudinaryFileField(
        options = {
            'tags': "TestInterview",
            'crop': 'limit',
            'width': 500, 
            'height': 500,
        })

class PhotoDirectForm(PhotoForm):
    image = CloudinaryJsFileField()

class PhotoUnsignedDirectForm(PhotoForm):
    upload_preset_name = "sample_" + hashlib.sha1(to_bytes(cloudinary.config().api_key + cloudinary.config().api_secret)).hexdigest()[0:10]
    image = CloudinaryUnsignedJsFileField(upload_preset_name)
