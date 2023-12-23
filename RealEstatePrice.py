import requests
import xmltodict
import pandas as pd
import streamlit as st


def get_apartment_trade_data(deal_ymd):
    url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?serviceKey=Qm%2FSxTC4k4vYtw5LKeqyTg%2FQ8vtQXBAP6PQFRjWClRCd7sFMNMlwW9x6%2BmsUEv0pObk76HsEYyhCueQU7RLfNQ%3D%3D'
    params = { 'pageNo':'1', 'numOfRows':'10', 'LAWD_CD':'11110', 'DEAL_YMD':deal_ymd }
    response = requests.get(url, params=params)

    data = xmltodict.parse(response.content)
    df = pd.DataFrame(data['response']['body']['items']['item'])

    return df[['년', '월', '거래유형', '거래금액', '건축년도', '전용면적', '도로명', '법정동']]


def main():
    st.title('아파트 거래 정보 조회')

    # Sidebar에 DEAL_YMD 선택 옵션 추가
    deal_ymd = st.sidebar.selectbox('거래 년월 선택',
                                    ['202301', '202302', '202303', '202304', '202305', '202306', '202307', '202308',
                                     '202309', '202310', '202311', '202312'])

    # 아파트 거래 데이터 가져오기
    apartment_data = get_apartment_trade_data(deal_ymd)

    # Streamlit에 데이터 표시
    st.table(apartment_data)


if __name__ == '__main__':
    main()