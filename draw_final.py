import turtle as t

# ===============================================
# 1. 'for' 루프 기반 코흐 함수 (수정본)
# (이 함수는 시작과 끝의 각도가 0도로 동일하게 유지됩니다)
# ===============================================
def for_Koch(dist, depth):

    # depth=0일 때 단순 직선
    if depth == 0:
        t.forward(dist)
        return

    length = dist / (3 ** depth)
    max_count = 4 ** (depth - 1) + 1
    flags = [0] * (depth - 1)  # 플래그 리스트

    for i in range(1, max_count):
        # 4개 선 그리기 기본 패턴
        t.forward(length)
        t.left(60)
        t.forward(length)
        t.right(120)
        t.forward(length)
        t.left(60)
        t.forward(length)

        # [수정된 핵심]
        # 맨 마지막 반복에서는 회전 로직을 실행하지 않음
        if i < max_count - 1:
            
            # 플래그 및 회전 처리 (한 단계 들여쓰기 됨)
            turned = False
            for idx in reversed(range(depth - 1)):
                period = 4 ** (idx + 1)
                if i % period == 0:
                    flags[idx] = 1 - flags[idx]  # 토글
                    for j in range(idx):
                        flags[j] = 0  # 이전 플래그 초기화
                    if flags[idx] == 1:
                        t.left(60)
                    else:
                        t.right(120)
                    turned = True
                    break

            if not turned:
                if i % 2 == 1:
                    t.left(60)
                else:
                    t.right(120)

# ===============================================
# 2. 전역 변수 및 단계별 설정
# ===============================================

current_depth = -1  # -1에서 시작, 첫 클릭에 0이 됨
MAX_DEPTH = 4

# 각 단계별 (한 변의 길이, 시작 X좌표, 시작 Y좌표)
# 요청대로 단계가 오르면 길이(distance)도 조금씩 늘어납니다.
settings = [
    # (distance, start_x, start_y)
    (300, -150, 100), # Depth 0
    (300, -150, 100), # Depth 1
    (350, -175, 120), # Depth 2
    (400, -200, 140), # Depth 3
    (450, -225, 160)  # Depth 4
]

# ===============================================
# 3. 그리기 및 이벤트 처리 함수
# ===============================================

# 전체 눈송이를 그리는 메인 함수
def draw_snowflake():
    # 1. 현재 단계에 맞는 설정값 가져오기
    distance, start_x, start_y = settings[current_depth]
    
    # 2. 화면 초기화 및 거북이 설정
    t.clear()         # 이전 그림 모두 지우기
    t.hideturtle()    # 거북이 숨기기
    t.penup()
    t.goto(start_x, start_y) # 설정된 시작 위치로 이동
    t.pendown()
    t.setheading(0)   # 항상 오른쪽(0도)을 바라보고 시작
    
    # 3. 화면에 현재 단계 표시
    t.penup()
    t.goto(0, -280) # 화면 하단 중앙
    t.write(f"Depth: {current_depth} (화면을 클릭하면 다음 단계)", 
            align="center", font=("Arial", 16, "normal"))
    
    # 4. 눈송이 그리기 (시작 위치로 복귀)
    t.goto(start_x, start_y)
    t.pendown()
    
    for i in range(3):
        for_Koch(distance, current_depth)
        t.right(120)

# "버튼" 역할: 화면을 클릭할 때마다 실행되는 함수
def next_step(x, y): # (x, y) 매개변수가 필수
    global current_depth
    
    # 1. 다음 단계로 이동 (4 초과 시 0으로 순환)
    current_depth += 1
    if current_depth > MAX_DEPTH:
        current_depth = 0
        
    # 2. 애니메이션 끄고 즉시 그리기
    #t.tracer(0, 0)      # 애니메이션 즉시 끔 (0, 0)
    draw_snowflake()    # 메인 그리기 함수 호출
    t.update()          # 화면 업데이트 (한번에 보여주기)

# ===============================================
# 4. 프로그램 실행
# ===============================================

# 1. 스크린 객체 설정
screen = t.Screen()
screen.setup(width=600, height=600)

# 2. 초기 안내 메시지
t.hideturtle()
t.write("화면을 클릭하여 0단계부터 시작하세요", 
        align="center", font=("Arial", 16, "normal"))

# 3. 화면 클릭 이벤트 연결
screen.onscreenclick(next_step)

# 4. 프로그램 종료 대기
t.done()
