import turtle as t

def for_Koch(dist, depth):

    # depth=0일 때 단순 직선
    if depth == 0:
        t.forward(dist)
        return

    #그려지는 모든 직선의 길이는 동일함
    #수식으로는 dist / 3의depth제곱
    length = dist / (3 ** depth)
    #max_count는 직선의 개수를 의미
    max_count = 4 ** (depth - 1) + 1
    flags = [0] * (depth - 1)  # 플래그 리스트: depth-1개 플래그 관리

    for i in range(1, max_count):
        # 4개 선 그리기 패턴
        t.forward(length)
        t.left(60)
        t.forward(length)
        t.right(120)
        t.forward(length)
        t.left(60)
        t.forward(length)

        # 플래그 및 회전 처리
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

# 초기 위치 왼쪽 -300, y=0 으로 이동
t.penup()
t.goto(-300, 0)
t.pendown()
##진짜 그리는 함수
t.speed(0)
for_Koch(500, 5)  # depth=6 포함 정상 동작 확인
t.done()
