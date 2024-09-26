from django.db import models

class Campaña(models.Model):
    campaña = models.CharField(max_length=10)  # Proporcionar un valor por defecto
    mensaje = models.CharField(max_length=255)
    
    def __str__(self): 
        return f"Campaña: {self.campaña} - Mensaje: {self.mensaje}"
  
        
        
    # Create your models here.r
