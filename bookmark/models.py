from django.db import models

# Create your models here.

# model = DB의 테이블
# Field = DB의 컬럼

# 북마크
# 이름 => varchar
# URL 주소 => varchar

class Bookmark(models.Model):
    name = models.CharField(max_length=100)
    # url = models.CharField('URL', max_length=100)
    url = models.URLField('URL')
    #장고 내 urlfield 사용
    created_at = models.DateTimeField('생성일시', auto_now_add=True)
    # 생성일자 = 모델.필드(자동추가)
    updated_at = models.DateTimeField('수정일시', auto_now=True)
    # 업데이트일자 = 모델.필드(자동설정)

    class Meta:
        verbose_name = '북마크'
        verbose_name_plural = '북마크 목록'

