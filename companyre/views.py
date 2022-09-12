from django.http import Http404
from companyre.serializer import ComapanySerializer
from companyre.models import CompanyRecord
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class CompanyList(APIView):
    def get(self,request):
        rec=CompanyRecord.objects.all()
        serializer=ComapanySerializer(rec,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class CompanyDetails(APIView):
    def get_object(self,pk):
        try:
            return CompanyRecord.objects.get(pk=pk)
        except CompanyRecord.DoesNotExist:
            raise Http404

        
    def get(self,request,pk):
        rec=self.get_object(pk)
        serializer=ComapanySerializer(rec)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        rec=self.get_object(pk)
        serializer=ComapanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        rec=self.get_object(pk)
        rec.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
