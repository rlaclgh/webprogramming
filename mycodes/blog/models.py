from django.db import models
from django.urls import reverse

# reverse 는 url 패턴을 만들어주는 장고의 내장 함수

# Create your models here.
class Post(models.Model):
    # charfield로 한 줄로 입력됩니다. 
    title = models.CharField(verbose_name="TITLE" , max_length=50)
    # unique 하므로 특정 포스트를 검색할 때 기본 키 대신 사용됩니다.
    slug = models.SlugField("SLUG" , unique=True , allow_unicode = True ,help_text='one word for title alias.')
    # 빈칸 blank 도 가능
    description = models.CharField("DESCRIPTION", max_length=100 ,blank = True , help_text = 'simple description text.')
    content = models.TextField('CONTENT')
    # 객체가 생성될 떄 자동으로 기록됨
    create_dt = models.DateTimeField("CREATE DATE" , auto_now_add = True)
    # 객체가 변경될 떄의 시각이 자동으로 기록됨
    modify_dt = models.DateTimeField("MODIFY DATE" , auto_now = True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        db_table = "blog_posts"
        ordering = ('-modify_dt',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args= (self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()