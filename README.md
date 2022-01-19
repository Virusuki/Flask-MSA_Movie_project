# Flask-MSA_Movie_project

- MSA 및 Kubernetes 배포 기반 영화 정보 제공 웹 사이트 youtube 동영상 링크   
https://www.youtube.com/watch?v=cZxfBEjU6u8


### MSA 및 Kubernetes 배포 기반 영화 정보 제공 웹 사이트 

-	UI 컨테이너: UI의 틀을 구성하는 컨테이너
-	영화 정보 컨테이너: 영화 정보를 제공하는 컨테이너
-	영화 카드를 클릭하면 영화 관련 상세 정보를 나타남
    - 제목, 설명 등으로 이루어진 간소한 페이지로 구성

- Flask 기반 영화 정보 제공 웹 사이트 구축   

<img src="https://github.com/Virusuki/Flask-MSA_Movie_project/blob/main/Readme_img/%EB%A9%94%EC%9D%B8%ED%99%94%EB%A9%B4.png" width="550px" height="300px" title="px(픽셀) 크기 설정" alt="메인 "></img><br/>

1.	Home - 메인화면 
2.	about - 소개
3.	Upload Movies - 영화정보 등록 (title, jenre, year)
4.	Show – 등록된 영화 View 및 영화 타이틀 카드 클릭 후 상세정보 확인


### UI 컨테이너 구성
- main_app_source 폴더
   
<img src="https://github.com/Virusuki/Flask-MSA_Movie_project/blob/main/Readme_img/main%20%ED%8F%B4%EB%8D%94.png" width="100px" height="100px" title="px(픽셀) 크기 설정" alt="메인 소스 폴더"></img><br/>   

   
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

<img src="https://github.com/Virusuki/Flask-MSA_Movie_project/blob/main/Readme_img/Movie%20UI%20%EB%8F%84%EC%BB%A4%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88%20%EB%8F%84%EC%BB%A4%ED%8C%8C%EC%9D%BC%20%EC%83%9D%EC%84%B1.png" width="300px" height="260px" title="px(픽셀) 크기 설정" alt="Movie UI 도커 컨테이너 Dockerfile"></img><br/>

```
Docker build –t namuk2004/main_app .
Docker push namuk2004/main_app
```

#### Movie UI 컨테이너 이미지를 활용한 쿠버네티스 기반 배포 
[Movie UI 컨테이너 쿠버네티스 배포 그림]

<img src="https://github.com/Virusuki/Flask-MSA_Movie_project/blob/main/Readme_img/Movie%20UI%20%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88%20%EC%BF%A0%EB%B2%84yaml.png" width="620px" height="370px" title="px(픽셀) 크기 설정" alt="Movie UI 도커 컨테이너 쿠버네티스 yaml"></img><br/>

```
Kubernetes 배포 command
kubectl apply –f main_app.yaml
```


### 영화정보 제공 컨테이너 구성 
flask_restx를 이용하여 영화 정보 생성, 삭제, 변경 등 Rest API 기반으로 구성된 앱   


<img src="https://github.com/Virusuki/Flask-MSA_Movie_project/blob/main/Readme_img/New%20movie%20%ED%8F%B4%EB%8D%94.png" width="100px" height="90px" title="px(픽셀) 크기 설정" alt="영화정보 제공 폴더"></img><br/>



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
   
<img src="https://github.com/Virusuki/Flask-MSA_Movie_project/blob/main/Readme_img/%EC%98%81%ED%99%94%EC%A0%95%EB%B3%B4%EB%93%B1%EB%A1%9D%20CRUD.png" width="700px" height="750px" title="px(픽셀) 크기 설정" alt="영화정보 등록 CRUD"></img><br/>   


#### 영화정보 제공 컨테이너 Dockerfile, build 및 이미지 생성

<img src="https://github.com/Virusuki/Flask-MSA_Movie_project/blob/main/Readme_img/%EC%98%81%ED%99%94%EC%A0%95%EB%B3%B4%20%EC%A0%9C%EA%B3%B5%20%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88%20%EB%8F%84%EC%BB%A4%ED%8C%8C%EC%9D%BC.png" width="300px" height="260px" title="px(픽셀) 크기 설정" alt="영화정보 제공 도커파일 CRUD"></img><br/>


```
Docker build –t namuk2004/new_movie .
Docker push namuk2004/new_movie
```

#### 영화정보 제공 컨테이너 이미지를 활용한 쿠버네티스 기반 배포

<img src="https://github.com/Virusuki/Flask-MSA_Movie_project/blob/main/Readme_img/%EC%98%81%ED%99%94%EC%A0%95%EB%B3%B4%EB%93%B1%EB%A1%9D%20%EC%BF%A0%EB%B2%84%20yaml.png" width="620px" height="370px" title="px(픽셀) 크기 설정" alt="영화정보 제공 폴더"></img><br/>


```
Kubernetes 배포 command
kubectl apply –f new_movie.yaml
```

- 등록된 영화 정보 관련 특정 영화 상세 페이지 view
[등록된 영화정보의 특정 영화 상세페이지 그림]
<img src="https://github.com/Virusuki/Flask-MSA_Movie_project/blob/main/Readme_img/%EB%93%B1%EB%A1%9D%EB%90%9C%20%EC%98%81%ED%99%94%EC%A0%95%EB%B3%B4%EC%9D%98%20%ED%8A%B9%EC%A0%95%20%EC%98%81%ED%99%94%20%EC%83%81%EC%84%B8%ED%8E%98%EC%9D%B4%EC%A7%80.png" width="550px" height="300px" title="px(픽셀) 크기 설정" alt="영화정보 상세 페이지"></img><br/>










