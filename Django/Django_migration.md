## 마이그레이션(migration)

데이터베이스에 적용시켜야 하는 변화에 대한 기록이다.

예)

- 댓글 기능이 없던 블로그에 댓글 작성 기능을 추가했다면 데이터 베이스에 댓글을 저장하기 위한 공간(테이블)이 필요할 것이다.
- 이를 db에 반영해야 서버를 실행했을 때 웹 사이트에 추가한 댓글 기능을 제대로 사용할 수 있다.



처음 장고 프로젝트를 만들면 추가한 기능이 아무것도 없는데 적용해야할 마이그레이션이 존재한다. 왜?

장고는 새 프로젝트를 생성할 때 데이터베이스에 기본적으로 필요한 테이블을 미리 마련해 두기 때문이다.



마이그레이션 만들기

```
python manage.py imgrations
```





```
python manage.py migrate
```

```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

db.sqlite3라는 파일이 생기고, 그 안에 마이그레이션을 반영한 데이터베이스가 생성된다.



### 왜 sqlite??

sqlite의 특징은 파일 하나로 데이터베이스를 관리함.

다른 DBMS는 설치하고 사용법을 알고 있어야 하는데 sqlite는 파일 하나만 관리하면 되기 때문에 편리하다. (백업은 그냥 파일을 어딘가에 복사해두면 그만)



그러나 단점도 존재.

파일 기반의 DB이기 때문에 I/O 작업이 많은 큰 프로젝트에서는 불리하다. 이럴 때는 다른 DB를 연동해서 써야한다.

