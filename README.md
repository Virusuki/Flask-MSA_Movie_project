# Flask-MSA_Movie_project

### MSA 및 Kubernetes 배포 기반 영화 정보 제공 웹 사이트 

-	UI 컨테이너: UI의 틀을 구성하는 컨테이너
-	영화 정보 컨테이너: 영화 정보를 제공하는 컨테이너
-	영화 카드를 클릭하면 영화 관련 상세 정보를 나타남
    - 제목, 설명 등으로 이루어진 간소한 페이지로 구성

- Flask 기반 영화 정보 제공 웹 사이트 구축
[메인그림]
<img src="https://github.com/Virusuki/Kubernetes/blob/main/k8s-develop/Pod-Container%20Design/files/img/Pod_service_action.PNG" width="550px" height="300px" title="px(픽셀) 크기 설정" alt="Pod service action"></img><br/>

1.	Home - 메인화면 
2.	about - 소개
3.	Upload Movies - 영화정보 등록 (title, jenre, year)
4.	Show – 등록된 영화 View 및 영화 타이틀 카드 클릭 후 상세정보 확인


### UI 컨테이너 구성
- main_app_source 폴더
[메인 앱 소스 폴더 그림]
- 그림과 같이 영화 정보 제공 웹 사이트는 flask 웹 프레임워크를 활용

- templates 폴더
   - index.html은 Movie Server 메인 화면 페이지
   - about.html는 Movie Server의 소개 페이지
   - upload.html는 Movie 정보 등록 (CRUD기능) 페이지
   - movie_info.html는 등록된 Movie 관련 정보의 상세 페이지

- app.py
```
	@app.route("/") decorator는 Rest API(get, put, pose, delete) 구성된 영화 정보를 제공하는 앱(컨테이너)으로부터 json 기반 영화 정보를 파싱
	@app.route("/movie_info/<string:dic>") decorator는 영화정보제공 컨테이너 앱을 통한 특정 영화 관련 정보를 movie_info.html에 전달
	@app.route("/about") decorator는 소개 페이지 view
	@app.route("/upload") decorator는 영화 등록을 위해 영화정보 컨테이너를 호출하며, iframe으로 페이지 구성 (참조: movie_informerip 변수에서 IP정보를 호스트 IP로 선언했지만, 유동적인 서버에서 도메인정보가 필요)
```

#### Movie UI 도커 컨테이너 Dockerfile, build 및 이미지 생성
[Movie UI 도커컨테이너 도커파일 생성.png 그림]

```
Docker build –t namuk2004/main_app .
Docker push namuk2004/main_app
```

#### Movie UI 컨테이너 이미지를 활용한 쿠버네티스 기반 배포 
[Movie UI 컨테이너 쿠버네티스 배포 그림]

```
Kubernetes 배포 command
kubectl apply –f main_app.yaml
```


### 영화정보 제공 컨테이너 구성 
flask_restx를 이용하여 영화 정보 생성, 삭제, 변경 등 Rest API 기반으로 구성된 앱
[New movie 폴더.png 그림]
```
@ns_Movie.route('/Movies')  # 영화
@ns_Movie.route('/Movies/<string:jenre>')   # 영화의 장르 종류
class movies_jenre(Resource): 
  - Get
  - Post
  - Delete
  - Put
@ns_Movie.route('/Movies/<string:jenre>/<int:jenre_id>') # 장르에 따른 영화
class movies_jenre_model(Resource):
  - Get
  - Post
  - Delete
  - Put
```

[ 영화정보등록 CRUD.png ]

#### 영화정보 제공 컨테이너 Dockerfile, build 및 이미지 생성
[영화정보 제공 컨테이너 도커파일 그림 ]

```
Docker build –t namuk2004/new_movie .
Docker push namuk2004/new_movie
```

#### 영화정보 제공 컨테이너 이미지를 활용한 쿠버네티스 기반 배포
[영화정보등록 쿠버 yaml.png 그림]

```
Kubernetes 배포 command
kubectl apply –f new_movie.yaml
```

- 등록된 영화 정보 관련 특정 영화 상세 페이지 view
[등록된 영화정보의 특정 영화 상세페이지 그림]









