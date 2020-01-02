# Create your views here.
from django.http.response import JsonResponse
from django.views import View


class HelloView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"text": "Hello python!"})


class HelloQueryView(View):
    def get(self, request, *args, **kwargs):
        ids = request.GET.get('id', '')
        return JsonResponse({"text": f"Hello python, {ids}!"})
