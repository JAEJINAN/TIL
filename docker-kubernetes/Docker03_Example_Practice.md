# Docker Container Example

컨테이너는 항상 이미지를 기반으로 하기 때문에 이를 위해 먼저 이미지라 불리는 것을 생성해야 한다.

이런 이미지를 생성하기 위해 도커 파일을 생성하여 확장자 없이 `Dockerfile`이라 명명한다.



우선 Dockerfile을 만든다. 그 후 빌드를 해준다.

```dockerfile
docker build .
```

그러면 image 파일이 만들어진다.

```
writing image sha256:c828d4ddacfb0aa12858717ea9de32b9ac091cc2017b5b522ceeb5938dcec20d
```



그 후 image 컨테이너를 실행해보자. 
포트를 게시(publish)해줘야 하므로 -p 플래그를 사용하자.
3000포트에서 3000 포트로 실행되게 하자.

```
docker run -p 3000:3000 sha256:c828d4ddacfb0aa12858717ea9de32b9ac091cc2017b5b522ceeb5938dcec20d
```



이러면 포트가 열리면서 도커화 된 애플리케이션이 가동된다.

<img src="C:\Users\Jay\Desktop\git\DataEngneering\Docker\image\3000to3000.png" alt="3000to3000" style="zoom:60%;" align="Left"/>

이제 컨테이너를 중지시켜보자.

새로운 터미널을 열고 다음 명령을 실행하자

```
docker ps

>>
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS      NAMES
3f224df2c745   c828d1ddadfb   "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   3000/tcp   admiring_nobel
```

여기서 NAMES는 랜덤하게 부여된 컨테이너 이름이다. 이 이름을 이용해 컨테이너를 종료시키자.

```
docker stop admiring_nobel
```



이제 컨테이너가 종료되었고 localhost:3000을 통해 애플리케이션 접속이 안된다.





