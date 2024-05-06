import serial
import requests

# 시리얼 포트 설정
ser = serial.Serial('COM6', 115200)

# 변수 초기화
position_x = [0.0] * 10
position_y = [0.0] * 10

# HTTP POST 요청을 보낼 주소 설정
url = "http://www.example.com/your-api-endpoint"

step = 0

while True:
    if ser.in_waiting > 0:
        if (step == 0):
            for i in range(0, 8):    
                data = ser.readline().decode().strip()
            ser.write(b'menu')
            step = step + 1
        if (step == 1):
            for i in range(0, 47):
                data = ser.readline().decode().strip()
            ser.write(b'b')
            step += 1
        if (step == 2):
            for i in range(0, 8):
                data = ser.readline().decode().strip()
            ser.write(b'10')
            step += 1
        if (step == 3):
            for i in range(0, 5):
                data = ser.readline().decode().strip()
            ser.write(b'123')
            step += 1
        
        # 시리얼 통신으로부터 데이터 읽기
        data = ser.readline().decode().strip()
        print("Received:", data)
