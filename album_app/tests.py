from django.test import TestCase
from io import BytesIO
from PIL import Image

from album_app.models import Photo
 
# Create your tests here.
class PhotoTests(TestCase):
    def test_image_upload(self):
 # create an image file to upload
        file = BytesIO()
        image = Image.new('RGBA', size=(10, 10), color=(126, 6, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        data = {
            'title': file.name,
            'photo': file,
        }
        # submit the image to the server using a POST request
        response = self.client.post('/photo-upload/', data, format='multipart/form-data')
    
        self.assertEqual(response.status_code, 200) 

       