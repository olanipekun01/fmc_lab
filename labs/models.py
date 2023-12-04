from django.db import models

# Create your models here.
class Departments(models.Model):
    dept_name = models.CharField(max_length=500)
    dept_id = models.CharField(max_length=200)
    
    def __str__(self):
        return self.dept_name

class Wards(models.Model):
    ward_name = models.CharField(max_length=500)
    ward_id = models.CharField(max_length=200)
    
    def __str__(self):
        return self.ward_name

class Investigations(models.Model):
    investigation_name = models.CharField(max_length=500)
    investigation_id = models.CharField(max_length=200)
    
    def __str__(self):
        return self.investigation_name

class Specimens(models.Model):
    specimen_name = models.CharField(max_length=500)
    specimen_id = models.CharField(max_length=200)
    
    def __str__(self):
        return self.specimen_name

class Records(models.Model):
    record_id = models.UUIDField(primary_key=True, editable=False)
    date = models.DateTimeField(auto_now=True)
    receipt_num = models.IntegerField(unique=True, blank=True, null=True)
    patient_name = models.CharField(max_length=400)
    hospital_num = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=10)
    ward = models.ForeignKey(Wards, related_name='wards', 
                             on_delete=models.SET_NULL, null=True, 
                             blank=True)
    specimen = models.ForeignKey(Specimens, related_name='specimens', 
                                 on_delete=models.SET_NULL, null=True, 
                             blank=True)
    investigation = models.ForeignKey(Investigations, 
                                      related_name='investigations',
                                      on_delete=models.SET_NULL,
                                      null=True, blank=True)
    cost = models.DecimalField(max_digits=15, decimal_places=1, default=0.0)
    
    def __str__(self):
        return self.patient_name