from django.db import models

# Create your models here.

class Bookmark(models.Model):
    # title 컬럼은 공백을 가질 수 있다. 
    title = models.CharField('TITLE', max_length=100 , blank=True)
    url = models.URLField('URL' , unique = True)

    
    # 어드민 사이트나 장고 셀 등에서 테이블의 레코드명을 보여줘야함
    def __str__(self):
        return self.title

class Blog(models.Model):
    text = models.TextField()