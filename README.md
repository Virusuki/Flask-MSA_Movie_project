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


#### UI 컨테이너 구성
- main_app_source 폴더
[메인 앱 소스 폴더 그림]
-	그림과 같이 영화 정보 제공 웹 사이트는 flask 웹 프레임워크를 활용
	templates 폴더
	index.html은 Movie Server 메인 화면 페이지
	about.html는 Movie Server의 소개 페이지
	upload.html는 Movie 정보 등록 (CRUD기능) 페이지
	movie_info.html는 등록된 Movie 관련 정보의 상세 페이지
	app.py
	@app.route("/") decorator는 Rest API(get, put, pose, delete) 구성된 영화 정보를 제공하는 앱(컨테이너)으로부터 json 기반 영화 정보를 파싱
	@app.route("/movie_info/<string:dic>") decorator는 영화정보제공 컨테이너 앱을 통한 특정 영화 관련 정보를 movie_info.html에 전달
	@app.route("/about") decorator는 소개 페이지 view
	@app.route("/upload") decorator는 영화 등록을 위해 영화정보 컨테이너를 호출하며, iframe으로 페이지 구성 (참조: movie_informerip 변수에서 IP정보를 호스트 IP로 선언했지만, 유동적인 서버에서 도메인정보가 필요)


