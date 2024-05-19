import streamlit as st
from PIL import Image

# from keras.models import load_model  # TensorFlow is required for Keras to work
# from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def run_ml() :
    st.write('''
             ### 내가 들고 있는 꽃의 사진을 찍어보세요.
             ### 꽃을 예측하고 예측한 꽃의 꽃말을 알 수 있어요!''')
    
    file = st.file_uploader('이미지 파일을 업로드하세요.', type=['jpg','png','jpeg','webp'])

    img0 = Image.open('./image/노루오줌.jpg')
    img1 = Image.open('./image/루드베키아.jpg')
    img2 = Image.open('./image/금잔화.jpg')
    img3 = Image.open('./image/카네이션.jpg')
    img4 = Image.open('./image/데이지.jpg')
    img5 = Image.open('./image/금계국.jpg')
    img6 = Image.open('./image/수선화.jpg')
    img7 = Image.open('./image/장미.jpg')
    img8 = Image.open('./image/해바라기.jpg')
    img9 = Image.open('./image/튤립.jpg')

    writ0 = '''
                > ##### 노루오줌/아스틸베 의 꽃말 💐
                > 이름과 다르게 사랑스러운 노루오줌의 꽃말은, \n
                > 우리나라에서는 쑥스러움, 기약 없는 사랑, 정열, 연정이고 \n
                > 외국에서는 조심스러운 사랑, 소극적인 접근, 자유, 밝은 기분 등이 있습니다. \n
                > 꽃말들이 전체적으로 밝고 사랑스러운 꽃이라는 느낌을 들게 합니다. \n
                > 노루오줌과 함께 사랑하는 마음을 전달하고, 
                오늘 하루 주는 사람과 받는 사람 모두 
                행복과 사랑이 가득하길 바랍니다 :)'''
    writ1 = '''
                > ##### 루드베키아 의 꽃말 💐
                > 작은 해바라기 같은 루드베키아 꽃말은 영원한 행복이라고 합니다. \n
                > 루드베키아와 함께 사랑하는 마음을 전달하고, 
                오늘 하루 주는 사람과 받는 사람 모두 
                행복과 사랑이 가득하길 바랍니다 :)'''
    writ2 = '''
                > ##### 금잔화 의 꽃말 💐
                > 금잔화는 로마어로 칼렌듈라(달의 초하루) 라고 부릅니다. \n
                > 꽃말은 겸손과 인내이고, 이별의 슬픔이라는 또 다른 꽃말도 있습니다. \n
                > 금잔화는 어두워지면 꽃잎을 닫고 아침 햇빛에 꽃잎을 피는데 이것이 꽃말의 이유라고 합니다. \n
                > 금잔화와 함께 사랑하는 마음을 전달하고, 
                오늘 하루 주는 사람과 받는 사람 모두 
                행복과 사랑이 가득하길 바랍니다 :)'''
    writ3 = '''
                > ##### 카네이션 의 꽃말 💐
                > 분홍색은 감사와 아름다움, \n
                > 빨간색은 사랑에 대한 믿음 또는 건강를 비는 사랑, 존경, \n
                > 주황색은 순수한 사랑, \n
                > 파랑색은 행복을 뜻합니다. \n
                > 카네이션과 함께 사랑하는 마음을 전달하고, 
                오늘 하루 주는 사람과 받는 사람 모두 
                행복과 사랑이 가득하길 바랍니다 :)'''
    writ4 = '''
                > ##### 데이지 의 꽃말 💐
                > 데이지의 꽃말은 순결, 미인, 평화, 희망 과 같이 귀여운 꽃말을 가지고 있습니다. \n
                > 이탈리아에서는 국민적인 사랑을 받는 꽃이며, \n
                > 해가 뜨면 고개를 들고 해가 지면 다시 고개를 내린다고 해서
                    '태양의 눈'이라고도 부른다고 합니다. \n
                > 데이지와 함께 사랑하는 마음을 전달하고, 
                오늘 하루 주는 사람과 받는 사람 모두 
                행복과 사랑이 가득하길 바랍니다 :)'''
    writ5 = '''
                > ##### 금계국의 꽃말 💐
                > 금계국은 꽃의 모습처럼 '상쾌한 기분' 이라는 꽃말을 가지고 있습니다. \n
                > 여름의 코스모스라고도 불리며 피어난 자리에는 항상 군락을 이루고 있어, 
                멀리서 바라봐도 상쾌한 기분을 느끼게 해주는 꽃입니다. \n
                > 금계국과 함께 사랑하는 마음을 전달하고, 
                오늘 하루 주는 사람과 받는 사람 모두 
                행복과 사랑이 가득하길 바랍니다 :)'''
    writ6 = '''
                > ##### 수선화 의 꽃말 💐
                > 수선화는 나르시소스라고도 부르며,  \n
                > 자기 사랑과 고결, 신비와 자존심 그리고 내면의 외로움이라는 꽃말을 가지고 있습니다.\n
                > 하지만 노란색의 수선화의 꽃말은 '사랑해 주세요', '내 곁으로 돌아와 주세요' 라는 
                    상대방에게 사랑받고 싶은 간절한 뜻을 지니고 있습니다. \n
                > 수선화와 함께 사랑하는 마음을 전달하고, 
                오늘 하루 주는 사람과 받는 사람 모두 
                행복과 사랑이 가득하길 바랍니다 :)'''
    writ7 = '''
                > ##### 장미 의 꽃말 💐
                > 붉은색은 열렬한 사랑, 불타는사랑, 아름다움  \n
                > 노란색은 질투, 시기와 완벽한 성취 \n
                > 주황색은 수줍음, 첫사랑의 고백 \n
                > 분홍색은 행복한 사랑, 맹세   \n
                > 흰색은 존경, 순결, 매력 \n
                > 여러 색의 장미와 함께 사랑하는 마음을 전달하고, 
                오늘 하루 주는 사람과 받는 사람 모두 
                행복과 사랑이 가득하길 바랍니다 :)'''
    writ8 = '''
                > ##### 해바라기 의 꽃말 💐
                > 한송이는 일편단심, \n
                > 4송이는 어디서라도 당신만을 바라볼게요, \n
                > 999송이는 몇번을 다시 태어나도 당신만을 바라볼게요 를 의미합니다. \n
                > 또한 희망의 상징으로 자주 쓰입니다. \n
                > 해바라기와 함께 사랑하는 마음을 전달하고, 
                오늘 하루 주는 사람과 받는 사람 모두 
                행복과 사랑이 가득하길 바랍니다 :)'''
    writ9 = '''
                > ##### 튤립 의 꽃말 💐
                > 빨간색은 영원한 사랑의 고백, \n
                > 분홍색은 애정, 배려, 사랑의 시작, \n
                > 노란색은 헛된 사랑, 사랑의 표시(혼자하는 사랑), \n
                > 망고/자몽 은 수줍은 사랑의 표시, 매혹적인 사랑, \n
                > 흰색은 추억, 실연, 용서, 과거의 우정, 새로운 시작을 뜻합니다.  \n
                > 다양한 색의 튤립과 함께 사랑하는 마음을 전달하고, 
                오늘 하루 주는 사람과 받는 사람 모두 
                행복과 사랑이 가득하길 바랍니다 :)'''

    st.error('''
             ##### AWS 프리티어로는 탠서프로우 설치가 어렵습니다. 
             ##### 그래서 로컬에서 실행한 화면으로 대체합니다.''')
    
    video_file = open('./image/ML.mkv', 'rb')
    st.video(video_file)


    if file is not None :

        st.image(file)
        
        '''
        머신 러닝 부분 주석 처리
        np.set_printoptions(suppress=True)

        # Load the model
        model = load_model("./model/keras_model.h5", compile=False)

        # Load the labels
        class_names = open("./model/labels.txt", "r", encoding='utf-8').readlines()

        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # Replace this with the path to your image
        image = Image.open(file).convert("RGB")

        # resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        # turn the image into a numpy array
        image_array = np.asarray(image)

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        # Load the image into the array
        data[0] = normalized_image_array

        # Predicts the model
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        # Print prediction and confidence score
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", confidence_score)

        st.info('이 꽃은 ' + class_name[2:] + ' 입니다. 예측 정확도는 '
                + str(round(confidence_score*100)) + '% 입니다.')
        
        
        
        data_pred = index

        if data_pred == 0 :
            st.image(img0, use_column_width=True)
            st.write(writ0)
        elif data_pred == 1 :
            st.image(img1, use_column_width=True)
            st.write(writ1)
        elif data_pred == 2 :
            st.image(img2, use_column_width=True)
            st.write(writ2)
        elif data_pred == 3 :
            st.image(img3, use_column_width=True)
            st.write(writ3)
        elif data_pred == 4 :
            st.image(img4, use_column_width=True)
            st.write(writ4)
        elif data_pred == 5 :
            st.image(img5, use_column_width=True)
            st.write(writ5)
        elif data_pred == 6 :
            st.image(img6, use_column_width=True)
            st.write(writ6)
        elif data_pred == 7 :
            st.image(img7, use_column_width=True)
            st.write(writ7)
        elif data_pred == 8 :
            st.image(img8, use_column_width=True)
            st.write(writ8)
        elif data_pred == 9 :
            st.image(img9, use_column_width=True)
            st.write(writ9)
        '''
    
    st.write('')
    st.write('')
    st.write('')

    st.write('''
             ##### 혹시 원하는 꽃이 나오지 않으셨나요?
             ##### 매장에 있는 다른 꽃들의 꽃말을 알고 싶다면 체크 박스를 눌러주세요!''')
    if st.checkbox('다른 꽃의 꽃말도 궁금해요'):
        flowers = ['노루오줌/아스틸베','루드베키아','금잔화/카렌듈라','카네이션','데이지','금계국','수선화','장미','해바라기','튤립']
        select_flowers = st.selectbox('알고싶은 꽃을 선택하세요', flowers)
        if select_flowers == flowers[0] :
            st.image(img0, use_column_width=True)
            st.write(writ0)
        elif select_flowers == flowers[1] :
            st.image(img1, use_column_width=True)
            st.write(writ1)
        elif select_flowers == flowers[2] :
            st.image(img2, use_column_width=True)
            st.write(writ2)
        elif select_flowers == flowers[3] :
            st.image(img3, use_column_width=True)
            st.write(writ3)
        elif select_flowers == flowers[4] :
            st.image(img4, use_column_width=True)
            st.write(writ4)
        elif select_flowers == flowers[5] :
            st.image(img5, use_column_width=True)
            st.write(writ5)
        elif select_flowers == flowers[6] :
            st.image(img6, use_column_width=True)
            st.write(writ6)
        elif select_flowers == flowers[7] :
            st.image(img7, use_column_width=True)
            st.write(writ7)
        elif select_flowers == flowers[8] :
            st.image(img8, use_column_width=True)
            st.write(writ8)
        elif select_flowers == flowers[9] :
            st.image(img9, use_column_width=True)
            st.write(writ9)

    else :
        st.write('')

