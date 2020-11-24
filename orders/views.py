from django.http import HttpResponse
from .models import Order

def index(request):
    latest_order_list = Order.objects.order_by('updated_at')[:5]
    output = ', '.join([o.code for o in latest_order_list])
    return HttpResponse(output)