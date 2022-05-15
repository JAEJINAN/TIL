# 데이터 베이스 모델링

DB모델링이란 어떤 Item에 속성 데이터를 사전에 정의하는 것

```
Jobs라는 Table에 각 Job의 정보를 저장
- 산업
- 연봉
- 근무지
- 수정일
- 생성일
```



Django에서는

- Django에서 id는 기본 값(primary key)을 정의 하지 않아도 자동으로 정의됨
- 외래키(foreign key)를 사용하면 뒤에 `xxxx_id`를 자동으로 생성
  - Job에 위치를 추가하고 싶은데 해당 위치가 다른 테이블에 있다면 location으로 정의해주면 location_id로 데이터 컬럼이 생성됨



Django DB 컬럼 타입 (django==3+)

```
- CharField (길이가 정해진 문자열, max_length)
- IntegerField (-2147483648 ~ 2147483647)
- PositiveIntegerField
- BigIntegerField (-9223372036854775808 ~ 9223372036854775807)
- PositiveBigIntegerField
- DateField (날짜)
- DatetimeField (날짜 + 시간)
- BooleanField (True/False)
- TextField (길이가 정해지지 않은 문자열)
- EmailField (이메일 포맷)
- JSONField (json 포멧)
- AutoField (Auto Increment 필드 with IntegerField)
- BigAutoField (Auto Increment 필드 with BigIntegerField)
- ForeignKey (다른 테이블 PK 참조 필드)
...
```



database modeling 1

```python
from django.db import models

class PayPlan(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)
```



슈퍼유저

```
python manage.py createsuperuser
```



UserData 추가

```
from django.contrib
```







