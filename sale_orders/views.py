from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .serializers import SaleOrderSerializer, SaleOrderItemSerializer
from .models import SaleOrder, SaleOrderItem
from rest_framework.decorators import action, permission_classes
from  rest_framework.response import Response
from locations.models import ItemLocation

class SaleOrderViewSet(ModelViewSet):
    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def validate(self, request, pk):
        sale_order = SaleOrder.objects.get(pk=pk)
        if sale_order.completed:
            return Response({'message': 'Sale Order is already validated.'})
        location = sale_order.location

        for sale_item in sale_order.sale_items.all():
            item = sale_item.item
            qty = sale_item.qty
            location_item, created = ItemLocation.objects.get_or_create(item=item, location=location)

            if location_item.qty >= qty:
                location_item.qty -= qty
                print(location_item)
                location_item.save()
            else:
                return Response({'message': 'Not enough items.'})
        sale_order.completed = True
        sale_order.save()
        return  Response({'message': 'Order has been completed'})


class SaleOrderItemViewSet(ModelViewSet):
    queryset = SaleOrderItem.objects.all()
    serializer_class = SaleOrderItemSerializer
