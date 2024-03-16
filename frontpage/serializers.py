from rest_framework import serializers
from .models import Carosel


class frontpageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Carosel
        fields=['cid', 'cname', 'ctext', 'cimage']
        
            


'''class frontpageSerializer(serializers.Serializer):
    cid=serializers.IntegerField()
    cname=serializers.CharField(max_length=40)
    ctext=serializers.CharField(max_length=256)
    cimage=serializers.ImageField( )
    
    def create(self, validated_data):
        return Carosel.objects.create(**validated_data)'''
    
    