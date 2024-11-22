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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '북마크'
        verbose_name_plural = '북마크 목록'

# makemigrations => migration.py 파일을 만듭니다. => 깃의 commit => github에 적용 x
# 실제 DB에는 영향 X => 실제 DB에 넣기 위한 정의를 하는 파일을 생성. => 깃의 push > github에 적용 o

# migrate => migrations/ 폴더 안에 있는 migration 파일들을 실제 DB에 적용을 합니다.
