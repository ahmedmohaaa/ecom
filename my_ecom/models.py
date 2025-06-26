from django.db import models

# Create your models here.
class Catcloth(models.Model):
    

    class C(models.TextChoices):
        Tshirt='Tshirt','Tshirt'
        Pants='pants','pants'
        jacket='jacket','jacket'
        shoes='shoes','shoes'
        blouse='blouse','blouse'
    cat=models.CharField(max_length=100,choices=C.choices)



class Category(models.Model):
    class N(models.TextChoices):
        man='man','man'
        woman='woman','woman'
        child='child','child'
    name=models.CharField(max_length=100,choices=N.choices)


    def __str__(self) -> str:
       return self.name
class Box(models.Model):
    class X(models.TextChoices):
       Available='available','Available'
       Sold='sold','Sold'
       
    class Y(models.TextChoices):
        Tshirt='Tshirt','Tshirt'
        Pants='pants','pants'
        jacket='jacket','jacket'
        shoes='shoes','shoes'
        blouse='blouse','blouse'

    class I(models.TextChoices):
        S='S','S'
        L='L','L'
        XL='XL','XL'
        M='M','M'           

    class C(models.TextChoices):
        black='black','black'
        white='white','white'
        blue='blue','blue'
        beige='beige','beige'

    STATUS_COLORS = {
                 'available': 'green',
                   'sold': 'red',
               }
    color=models.CharField(choices=C.choices)
    brice_before=models.IntegerField(null=True,blank=True)
    description=models.TextField(max_length=1000)
    size=models.CharField(max_length=100,choices=I.choices)
    brand=models.CharField(max_length=100)
    cloths = models.CharField(max_length=50, choices=Y.choices, default='Tshirt')
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='eback',null=True,blank=True)
    price=models.DecimalField(max_digits=6,decimal_places=3,null=True,blank=True)
    status = models.CharField(max_length=10, choices=X.choices,null=True,blank=True)
    active=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)



    def __str__(self) -> str:
       return self.title

    @property
    def status_color(self):
        if self.status:
            return self.STATUS_COLORS.get(self.status.lower(), 'black')
        return 'black'