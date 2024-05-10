<img src="https://capsule-render.vercel.app/api?type=shark&color=f1c0c0&height=150&section=header" />

# streamlit_flowers_noMl 

### 꽃 사진을 이용한 꽃 이름 예측 인공지능

#### 15가지 종류의 꽃 사진 데이터를 바탕으로 학습하여 꽃의 종류를 예측하는 인공지능을 경험할 수 있는 웹 페이지 입니다.

[꽃 사진 예측 앱 URL](http://ec2-43-203-208-63.ap-northeast-2.compute.amazonaws.com:8503/)



✏️ 작업순서
-

데이터 주제 선정 ➡︎ 데이터 가공(Teachable Machine, 주피터노트북) 
➡︎ Streamlit 프레임워크 웹 대시보드 개발 ➡︎ AWS EC2 배포




✏️ 데이터 가공
-

컴퓨터가 허용할 수 있는 용량으로 각 사진 별 데이터를 정리
- 기본 데이터인 15가지 꽃에서 꽃집에서 활용하기 좋은 꽃 10가지로 줄였습니다.
- 티처블머신에서 지속적인 오류 발생으로 꽃 종류별 사진 수를 정리했습니다.
- 주피터 노트북에서 티처블 머신에서 학습된 모델로 실제로 잘 예측되는지 확인했습니다.
- labels.txt 에 작성되어 있는 예측 명을 영어에서 한글로 변경하여 예측 값 한글로 나올 수 있도록 데이터 가공했습니다.




✏️ Streamlit 웹 대시보드 개발
-

파일명으로 정리했습니다.

✉︎ APP.PY
- 사이드바를 통해서 나의 웹 대시보드의 목록을 보여줍니다.
- 사이드바를 streamlit_option_menu 를 이용해서 업그레이드했습니다.

✉︎ HOME.PY
- 사용한 데이터 출처 표시 했습니다.
- 데이터 출처 : [kaggle의 🌸 | Flowers 데이터](https://www.kaggle.com/datasets/l3llff/flowers)
- 사진과 글을 넣어 웹 대시보드 메인 화면 만들었습니다.

✉︎ ODER.PY
- streamlit의 사전을 이용해서 고객에게 정보를 받을 수 있도록 코드를 만들었습니다.
- 학습된 꽃들로만 선택을 해야 나중에 꽃을 받은 사람이 예측 또한 할 수 있기 때문에 st.multiselect() 으로 꽃의 종류를 선택할 수 있게 했습니다.
- 받은 정보는 변수로 저장하고, 추가된 금액들은 총합하여 최종 데이터프레임에 변수와 총합이 계산되어 들어갈 수 있도록 개발했습니다.
- 주문 정보를 저장할 때, datetime을 이용해서 각각 다른 파일명으로 저장될 수 있도록 개발했습니다.

✉︎ ML.PY
- AWS 프리 티어로는 EC2에 탠서플로우 2.15.0 버전 설치가 어려워, 탠서플로우 버전을 2.12.0으로 다운그레이드해서 설치하여 서버에서 예측프로그램 실행 시켰습니다.
- 티처블 머신으로 꽃 사진 학습하였고 에포크는 50, 배치 사이즈는 16 으로 지정하여 학습 시켰습니다.
- 주피터 노트북에서 코드가 잘 예측되는지 확인(tensorflow==2.15.0)한 후, Visual Studio Code에서 가상환경에 주피터노트북과 같은 탠서플로우 버전으로 설치한 뒤 예측 코드를 입력받은 파일로 예측할 수 있게 수정하여 입력하였습니다.(EC2 리눅스 서버에서는 tensorflow==2.12.0 사용했습니다.)
- 각 꽃 별 사진과 설명을 변수로 저장하여 텍스트 수정에 용의하도록 정리했습니다.




✏️ 배포
-

AWS EC2에 리눅스 프리 티어를 사용해서 배포했습니다.
- Git 설치 과정과 AWS 배포 과정 블로그 정리했습니다.
- [minseonchoi의 블로그 AWS 카테고리](https://msdev-st.tistory.com/category/AWS)
  
github Actions로 EC2 리눅스에 git pull 자동화했습니다.

현재 사용하고 있는 사용자도 새로운 버전의 화면을 볼 수 있도록 서버 실행 명령어에 --server.runOnSave true를 추가했습니다.


✏️ 사용한 프로그램
-

<a href="https://jupyter.org/"><img src="https://img.shields.io/badge/jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white"/></a>
<a href="https://streamlit.io/"><img src="https://img.shields.io/badge/streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white"/></a>
<a href="https://code.visualstudio.com/"><img src="https://img.shields.io/badge/visualstudiocode-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white"/></a>
<a href="https://aws.amazon.com/ko/console/"><img src="https://img.shields.io/badge/amazonec2-FF9900?style=flat-square&logo=amazonec2&logoColor=000000"/></a>




✏️ 사용한 언어
-

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=minseonchoi&langs_count=8)](https://github.com/minseonchoi/github-readme-stats)


<img src="https://capsule-render.vercel.app/api?type=shark&color=f1c0c0&height=150&section=footer" />
