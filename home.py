import streamlit as st
from PIL import Image

def run_home() :
    st.write('''
             ### Learned Flower 를 찾아주셔서 감사합니다. \n
             ##### 15년 경력의 플로리스트가 운영하는 꽃집입니다.''')

    st.write(' ')
    st.write("""데이터는 캐글에 있는 15가지의 꽃 사진 데이터 
             ( [https://www.kaggle.com/datasets/l3llff/flowers](https://www.kaggle.com/datasets/l3llff/flowers) ) 를 
             사용해서 꽃 사진 예측 모델을 만들었습니다.""")
    st.link_button('Kaggle 꽃 사진 데이터', url='https://www.kaggle.com/datasets/l3llff/flowers')



    img1 = Image.open('./image/home_img.jpg')
    st.image(img1, use_column_width=True)

    st.write("""
             #### 꽃과 나무가 주는 심신 치유 효과 \n
             꽃밭에서 걷기만 해도 기분이 좋아지는 현상은 뇌파와 관련이 있으며,
             아름다움 꽃과 녹색 식물을 보면 뇌에서 마음을 안정시키는 알파파가 활성화되어 
             스트레스가 해소되고 불안감이 줄어듭니다.\n
             씨앗을 뿌려 꽃이 필 때까지 보살피며 식물과 교감하는 과정에서 자존감이 높아지고,
             국내 연구 결과 우울감이 줄고 자존감이 높아졌습니다. \n
             건강한 성인은 집 베란단에서 꽃만 키워도 우울증 완화와 스트레스 해소 등의 
             효과를 볼 수 있으며, 플라워테라피용 꽃을 선택할 때는 계절, 촉감, 색깔 등을 고려하는 것이 좋습니다. \n
             다양한 색깔의 꽃을 가까이하면 마음이 안정되고 기분이 좋아지며, 
             색깔에 따라 다른 효과를 느낄 수 있다.
             """)