from django.shortcuts import get_object_or_404, render
from logger import logger
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling customer-related operations
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request):
        """Get all customers"""
        logger.info("Getting all customers")
        customers = self.get_queryset()
        logger.info(f"Found {len(customers)} customers")
        serializer = self.serializer_class(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Create a new customer"""
        logger.info(f"Creating customer: {request.data}")
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Customer created: {serializer.data}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f"Invalid customer data: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Get a specific customer by ID"""
        logger.info(f"Retrieving customer with ID: {pk}")
        customer = get_object_or_404(Customer, pk=pk)
        serializer = self.serializer_class(customer)
        logger.info(f"Customer retrieved: {serializer.data}")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        """Update a customer"""
        logger.info(f"Updating customer with ID: {pk}")
        customer = get_object_or_404(Customer, pk=pk)
        serializer = self.serializer_class(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Customer updated: {serializer.data}")
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(f"Invalid customer data: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete a customer"""
        logger.info(f"Deleting customer with ID: {pk}")
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        logger.info(f"Customer deleted: {pk}")
        return Response(status=status.HTTP_204_NO_CONTENT)
