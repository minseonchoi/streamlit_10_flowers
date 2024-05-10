import streamlit as st
import pandas as pd
import os
import datetime
from PIL import Image

def run_order() :
    st.write('### 러드 플라워를 찾아주셔서 감사합니다. ')
    st.write('##### 런드 플라워 주문서')
    
    st.write('###### 🌷 예약자분 성함')
    name = st.text_input('성함을 입력하세요.', max_chars=20)

    st.write(' ')
    st.write(' ')

    st.write('###### 🌷 예약자분 연락처')
    tel_num = st.text_input('연락처를 입력하세요. 주문이 들어가면 안내 문자 드립니다.')
    
    st.write(' ')
    st.write(' ')

    st.write('###### 🌷 예약 방문 날짜')
    re_date = st.date_input('방문 날짜를 선택해주세요', min_value=datetime.date(2024,5,8), max_value=datetime.date(2024,9,30) )
    st.info(f'방문 예약 날짜는 {re_date} 입니다.')
    
    st.write(' ')
    st.write(' ')

    st.write('###### 🌷 예약 방문 시간')
    st.write('''방문 예약 시간은 따로 없이 예약 당일 영업시간에 오시면 됩니다. \n
             tel : 032-000-0000 영업시간 : 매일 AM 09:00 - PM 06:00''')
    
    st.write(' ')
    st.write(' ')

    flowers = ['노루오줌/아스틸베','루드베키아','금잔화/카렌듈라','카네이션','데이지','금계국','수선화','장미','해바라기','튤립']
    
    st.write('###### 🌷 메인 꽃의 종류를 선택 해주세요. (메인 꽃을 여러개 선택하시면 추가 비용 있습니다. 기본가격은 1 종류 입니다.)')
    main_flo = st.multiselect('이번주에 준비되어 있는 꽃 입니다. 최대 3 종류까지 가능합니다.', flowers, max_selections=3)
    if len(main_flo) == 0:
        return
    elif len(main_flo) == 1:
        st.info(f'선택하신 메인 꽃은 {main_flo[0]} 입니다.')
        main_pr = 0
    elif len(main_flo) == 2 :
        st.info(f"선택하신 메인 꽃은 '{main_flo[0]}' , '{main_flo[1]}' 입니다.")
        st.write('추가 비용 5,000원 입니다.')
        main_pr = 5000
    elif len(main_flo) == 3 :
        st.info(f"선택하신 메인 꽃은 '{main_flo[0]}', '{main_flo[1]}', '{main_flo[2]}' 입니다.")
        st.write('추가 비용 9,000원 입니다.')        
        main_pr = 9000
    st.caption('메인 꽃이 아닌 다른 식물은 시장 상황에 따라 예쁜 소재들을 데려와서 같이 만들고 있습니다.')
    
    st.write(' ')
    st.write(' ')

    st.write('###### 🌷 포장 종류를 선택해주세요.')
    pack = ['꽃다발','화병 +5,000','꽃바구니 +5,000']
    pack_flo = st.radio('꽃다발 외의 화병, 꽃바구니로 할 경우 추가 비용있습니다.', pack)
    # 라디오 버튼 가로로 열세우기
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if pack_flo == pack[1] :
        st.info('예쁘게 화병으로 포장해드릴게요 :) 이동 시 움직이지 않게 고정되어 있습니다.')
        plus_5 = 5000
    elif pack_flo == pack[2] :
        st.info('예쁘게 꽃바구니로 포장해드릴게요 :) 이동 시 움직이지 않게 고정되어 있습니다.')
        plus_5 = 5000
    elif pack_flo == pack[0] :
        st.info('꽃다발로 예쁘게 포장해드릴게요 :)')
        plus_5 = 0

    st.write(' ')
    st.write(' ')

    st.write('###### 🌷 꽃의 크기를 선택해주세요.')
    size = ['mini','Small','Medium','large','다른 사이즈는 전화 문의 부탁드립니다.']
    size_price = [15000, 20000, 25000, 30000]
    size_flo = st.selectbox('크기를 선택해주세요.', size)

    img0 = Image.open('./image/mi.png')
    img1 = Image.open('./image/sm.png')
    img2 = Image.open('./image/med.png')
    img3 = Image.open('./image/lar.png')
      
    if size_flo == size[0] :
        st.image(img0, use_column_width=(20,20))
        st.info(f'선택하신 사이즈는 {size[0]} 이며, 기본 가격은 {size_price[0]}원 입니다.')
        base_flo = size_price[0]
    elif size_flo == size[1] :
        st.image(img1, use_column_width=(20,20))
        st.info(f'선택하신 사이즈는 {size[1]} 이며, 기본 가격은 {size_price[1]}원 입니다.')
        base_flo = size_price[1]
    elif size_flo == size[2] :
        st.image(img2, use_column_width=(20,20))
        st.info(f'선택하신 사이즈는 {size[2]} 이며, 기본 가격은 {size_price[2]}원 입니다.')
        base_flo = size_price[2]
    elif size_flo == size[3] :
        st.image(img3, use_column_width=(20,20))
        st.info(f'선택하신 사이즈는 {size[3]} 이며, 기본 가격은 {size_price[3]}원 입니다.')
        base_flo = size_price[3]
    else :
        st.info('''전화 문의 부탁드립니다. \n
                 tel : 032-000-0000 영업시간 : 매일 AM 09:00 - PM 06:00''')
        return
    
    st.write(' ')
    st.write(' ')
    
    st.write('###### 🌷 주문 정보를 확인해주세요.')
    final_price = main_pr + plus_5 + base_flo
    data = {
        '성함':[name],
        '연락처':[tel_num],
        '예약일':[re_date],
        '메인꽃 종류':[main_flo],
        '포장방법':[pack_flo],
        '사이즈':[size_flo],
        '예정가격(원)':[final_price]
    }
     # 고객 주문서 데이터 프레임으로 만들기
    st.dataframe(pd.DataFrame(data))
    df = pd.DataFrame(data)

    check = ['예', '아니오']
    per_check= st.radio('주문 정보가 맞으신가요?', check)
    if per_check[0] == check[0]:
        st.write('주문 정보를 저장합니다. 저희가 주문정보 확인 후 연락드립니다.')
        st.caption('- 영업시간 중 주문 정보 작성 시, 당일 영업시간 이내에 연락드립니다.')
        st.caption('- 영업시간 외 주문 정보 작성 시, 다음날 영업시간에 연락드립니다.')
        st.caption('- 이 부분 참고하시어 주문 부탁드립니다. ')
        # 주문 정보 저장하기 버튼
        if st.button('주문정보 저장하기') :
           filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
           file_path = os.path.join('./', 'customer_data', filename + '.csv')
           df.to_csv(file_path)
           st.success('주문 정보가 저장 되었습니다. 빠른 시간 내에 확인 연락드리겠습니다. 감사합니다 :)')
    else :
        # 처음 홈페이지로 돌아가는 버튼 만들기
        st.write('''
                 > 입력 값을 수정하고 싶으신가요? \n
                 > 처음 부터 다시 입력하시고 싶으시면 버튼을 눌러주세요.
                 ''')
        st.link_button('첫 시작 페이지로 돌아갑니다. 새로운 창으로 이동', url='http://43.203.208.63:8503/')