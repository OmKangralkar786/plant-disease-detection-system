
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from .prediction import predict_leaf
from .models import PredictionHistory


def home(request):
    return JsonResponse({
        "message": "Plant Disease Detection API Running"
    })


class PredictDiseaseView(APIView):

    def post(self, request):

        if "image" not in request.FILES:
            return Response(
                {"error": "No image uploaded"},
                status=400
            )

        image = request.FILES["image"]

        image_path = f"media/{image.name}"

        with open(image_path, "wb+") as destination:
            for chunk in image.chunks():
                destination.write(chunk)

        disease, confidence = predict_leaf(image_path)

        descriptions = {
            "Potato___healthy":
                "The potato plant shows no visible signs of disease and is growing normally.",

            "Potato___Late_blight":
                "A serious disease caused by Phytophthora infestans that produces dark lesions on leaves and tubers.",

            "Potato___Early_blight":
                "A fungal disease characterized by brown spots with concentric rings on older leaves.",

            "Tomato___healthy":
                "The tomato plant is healthy and free from visible disease symptoms.",

            "Tomato___Late_blight":
                "A destructive disease that causes dark water-soaked lesions on leaves, stems, and fruits.",

            "Tomato___Early_blight":
                "A fungal disease causing dark spots with concentric rings on leaves.",

            "Tomato___Leaf_Mold":
                "A fungal disease that appears as yellow patches on upper leaf surfaces and mold underneath.",

            "Pepper__bell___healthy":
                "The bell pepper plant is healthy and showing normal growth.",

            "Pepper__bell___Bacterial_spot":
                "A bacterial disease that causes dark spots on leaves and fruits."
        }

        treatments = {
            "Potato___healthy":
                "Plant is healthy. Continue regular watering, balanced fertilization, weed control, and routine monitoring for pests and diseases.",

            "Potato___Late_blight":
                "Apply copper-based fungicide, remove infected leaves, avoid overhead irrigation, and ensure proper field drainage.",

            "Potato___Early_blight":
                "Use recommended fungicides, remove infected plant debris, and practice crop rotation.",

            "Tomato___healthy":
                "Plant is healthy. Maintain proper watering, fertilization, and regular monitoring.",

            "Tomato___Late_blight":
                "Apply fungicide immediately, remove infected leaves, and avoid excessive moisture around plants.",

            "Tomato___Early_blight":
                "Remove affected leaves, improve air circulation, and apply fungicide if necessary.",

            "Tomato___Leaf_Mold":
                "Improve ventilation, reduce humidity, remove infected leaves, and apply appropriate fungicides.",

            "Pepper__bell___healthy":
                "Plant is healthy. Continue good irrigation and nutrient management practices.",

            "Pepper__bell___Bacterial_spot":
                "Remove infected leaves, avoid overhead watering, and apply copper-based bactericides."
        }

        # Save prediction history
        PredictionHistory.objects.create(
            image=image,
            disease=disease,
            confidence=round(confidence, 2)
        )

        return Response({
            "disease": disease,
            "confidence": round(confidence, 2),
            "description": descriptions.get(
                disease,
                "No description available."
            ),
            "treatment": treatments.get(
                disease,
                "No treatment information available."
            )
        })


class DashboardView(APIView):

    def get(self, request):

        total_scans = PredictionHistory.objects.count()

        healthy_plants = PredictionHistory.objects.filter(
            disease__icontains="healthy"
        ).count()

        diseased_plants = (
            total_scans - healthy_plants
        )

        return Response({
            "total_scans": total_scans,
            "healthy_plants": healthy_plants,
            "diseased_plants": diseased_plants
        })


class PredictionHistoryView(APIView):

    def get(self, request):

        predictions = PredictionHistory.objects.all().order_by(
            "-timestamp"
        )

        data = []

        for item in predictions:

            data.append({
                "id": item.id,
                "disease": item.disease,
                "confidence": item.confidence,
                "image": item.image.url if item.image else "",
                "timestamp": item.timestamp.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            })

        return Response(data)
