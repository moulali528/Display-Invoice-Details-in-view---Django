from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InvoiceSerializer
from .models import Invoice

# Create your views here.

@api_view(['GET'])
def invoiceList(name):
    invoice = Invoice.objects.all()
    serializer = InvoiceSerializer(invoice, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def invoiceDetails(name, pk):
    invoice = Invoice.objects.get(id=pk)
    context = {'task':invoice}
    serializer = InvoiceSerializer(invoice, many=False)
    return Response(serializer.data)