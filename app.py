import streamlit as st
from streamlit_option_menu import option_menu

from home import run_home
from order import run_order
from ml import run_ml



def main():
    st.title('Learned Flower 에서 학습된 꽃들을 만나요 :)')

    menu = ['메인화면','주문서','나의 꽃 확인하기']
    with st.sidebar :
        st.write('# 🌷 Learned Flower 🌼')
        choice = option_menu(' ', menu,
                             icons=['house','bi bi-clipboard-heart','bi bi-flower3'],
                             menu_icon='bi bi-list', default_index=0,
                             styles={
        "container": {"padding": "5!important", "background-color": "#ffffff"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fff"},
        "nav-link-selected": {"background-color": "#D05252"}})
    
   
    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_order()
    elif choice == menu[2] :
        run_ml()



if __name__ == '__main__' :
    main()