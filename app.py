import streamlit as st
import requests
import json

# Thingspeak API Key 및 채널 ID

API_KEY = "ZWFPB90A2ITQUVNP"
CHANNEL_ID = "2232414"

# Thingspeak API를 통해 데이터 가져오기
def get_thingspeak_data():
    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={API_KEY}&results=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data["feeds"][0]["field1"]
    else:
        return None

# 대여 가능한 우산 개수를 확인하고 아이콘 표시 함수
def show_umbrella_icons(available_umbrellas):
    st.write(f"대여 가능한 우산 개수: {available_umbrellas}")

    if available_umbrellas >= 1:
        st.write("대여 가능한 우산")
        st.image("images/umbrella_available.png", width=100)
    else:
        st.write("대여 불가능한 우산")
        st.image("images/umbrella_unavailable.png", width=100)

def main():
    st.title("우산 대여 상태")

    available_umbrellas = get_thingspeak_data()
    if available_umbrellas is not None:
        show_umbrella_icons(int(available_umbrellas))
    else:
        st.error("데이터를 가져오는데 실패하였습니다. Thingspeak 설정을 확인해주세요.")

if __name__ == "__main__":
    main()
