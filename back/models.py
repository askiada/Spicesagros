from django.db import models
from polymorphic.models import PolymorphicModel
import qrcode
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from mptt.models import MPTTModel, TreeForeignKey

from django.db.models import Q 
import operator  
from functools import reduce

from django.utils.safestring import mark_safe

from fontawesome.fields import IconField

# Create your models here.
class Category(MPTTModel):    
    name = models.CharField(max_length=200)
    alias_url = models.CharField(max_length=200)
    update_date = models.DateTimeField('Date de mise à jour', auto_now=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name = 'children',db_index=True)
    icon = IconField()
    def icon_display(self):
        return '<i class="fa fa-%s"  style="color:green"> </i>' % (self.icon)
    icon_display.allow_tags = True
    def __str__(self):
        return self.name
    
class Tag(MPTTModel):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7)
    parent = TreeForeignKey('self', blank=True, null=True, related_name = 'children',db_index=True)
    def __str__(self):
        return self.name
    # def get_queryset_descendants(nodes, include_self=False): 
       # if not nodes: 
           # return Tag.objects.none() 
       # filters = [] 
       # for n in nodes: 
           # lft, rght = n.lft, n.rght 
           # if include_self: 
               # lft -=1 
               # rght += 1 
           # filters.append(Q(tree_id=n.tree_id, lft__gt=lft, rght__lt=rght)) 
       # q = reduce(operator.or_, filters) 
       # return Tag.objects.filter(q)
        

class Document(PolymorphicModel):
    
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date d\'ajout', auto_now_add = True)
    update_date = models.DateTimeField('Date de mise à jour', auto_now=True)
    stat = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags= models.ManyToManyField(Tag)
    #upload = models.FileField(upload_to='uploads/')
   
    
    
    def get_absolute_url(self):
        return self.file.url
        
    def generate_qrcode(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=0,
        ) 
        qr.add_data(self.get_absolute_url())
        qr.make(fit=True)

        img = qr.make_image()

        buffer = io.BytesIO()
        img.save(buffer)
        filename = self.file.name
        filebuffer = InMemoryUploadedFile(
            buffer, None, filename, 'image/png', buffer.getbuffer().nbytes, None)
        self.qrcode.save(filename, filebuffer, False)
        
    def save(self, *args, **kwargs):
        self.generate_qrcode()
        super(Document, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
#Document privé uniquement visible par certains groupes d'utilisateurs 
class PrivateDocument(Document):
    class Meta:
        permissions = (
            ("view_public_document", "Peut télécharger le document publique"),
            ("view_private_document", "Peut télécharger le document privé"),
            ("add_class_note", "Peut ajouter une note au document")
        )
    file = models.FileField(upload_to='uploads/private/')
    qrcode = models.ImageField(upload_to = 'uploads/private/qrcode/')
    
        
        
#Document accessible à tous
class PublicDocument(Document):
    class Meta:
        permissions = (
            ("view_public_document", "Peut télécharger le document publique"),
            ("add_class_note", "Peut ajouter une note au document")
        )
    file = models.FileField(upload_to='uploads/public/')
    qrcode = models.ImageField(upload_to = 'uploads/public/qrcode/')
    
#Ajoute une note uniquement visible du créateur sur le document
#Intègre Latex comme format d'écriture mathématiques
#TODO : différentier avec notes de groupe ?

class Note(models.Model):
    name = models.CharField(max_length=200)
    content =  models.TextField(max_length=5000)
    TYPE_CHOICES = (('general', 'Note générale'), ('page', 'Note par page'))

    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='general')
 
    pub_date = models.DateTimeField('Date d\'ajout', auto_now_add = True)
    update_date = models.DateTimeField('Date de mise à jour', auto_now=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    
