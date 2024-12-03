import cv2

# 이미지 불러오기
img = cv2.imread(r"C:\Users\pegon\Desktop\codingsumin.png")


# 텍스트를 추가할 위치 (x, y) 좌표 지정
position = (50, 50)  # 텍스트가 시작할 위치 (왼쪽 위)

# 사용할 글꼴 설정 (기본적인 글꼴)
font = cv2.FONT_HERSHEY_SIMPLEX

# 텍스트 크기 (1은 기본 크기)
font_scale = 1

# 텍스트 색상 (여기서는 흰색)
color = (255, 255, 255)

# 텍스트 두께 (2픽셀)
thickness = 2

# 선 유형 (부드러운 선)
line_type = cv2.LINE_AA

# 이미지에 텍스트 추가
cv2.putText(img, 'Coding sumin', position, font, font_scale, color, thickness, line_type)

# 결과 이미지 보여주기
cv2.imshow('Image with Text', img)

# 키 입력을 기다린 후 종료
cv2.waitKey(0)
cv2.destroyAllWindows()
