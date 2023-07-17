import pytesseract
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@csrf_exempt
def ocr_image(request):
    if request.method == 'POST' and 'image' in request.FILES:
        # Open the uploaded image file
        image = Image.open(request.FILES['image'])

        # Perform OCR using the custom traineddata
        text = pytesseract.image_to_string(image, lang='eng_bank_statement_1')

        # Return the extracted text as JSON response
        return JsonResponse({'text': text})

    # Return an error response for unsupported methods or missing image file
    return JsonResponse({'error': 'Invalid request'}, status=400)
