from django.db import models

# Create your models here.


class Question(models.Model):
    subject = models.CharField(max_length=200)  # 제목 (최대 200자)
    # 글자수 제한이 있는 텍스트는 CharField를 쓴다.
    content = models.TextField()  # 내용 / 글자수 제한이 없으면 TextField를 쓴다.
    # 생성날짜 / 날짜, 시간과 관련 속성은 DateTimeField를 쓴다.
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 질문에 대한 답변이므로 Question모델의 속성을 가져와야한다. 이럴때 ForeignKey를 써준다.
    # on_delete=models.CASCADE 는 Question과 연결되어 질문 삭제시 답변들도 다 같이 사라진다.
    # 질문 하나에는 무수히 많은 답변이 등록될 수 있다. CASCADE 옵션은 질문을 삭제하면 그에 달린 답변들도 모두 함께 삭제한다.
    content = models.TextField()
    create_date = models.DateTimeField()
