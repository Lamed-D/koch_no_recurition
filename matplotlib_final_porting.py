import matplotlib.pyplot as plt
import numpy as np

def add_vector(p, angle_deg, length):
    rad = np.radians(angle_deg)
    return (p[0] + length * np.cos(rad), p[1] + length * np.sin(rad))

def for_Koch_matplotlib(start_pos, dist, depth):
    if depth == 0:
        end_pos = add_vector(start_pos, 0, dist)
        return [start_pos, end_pos]

    length = dist / (3 ** depth)
    max_count = 4 ** (depth - 1) + 1
    flags = [0] * (depth - 1)
    angle = 0
    pos = start_pos
    path = [pos]

    for i in range(1, max_count):
        # 정확한 정삼각형 형태를 위해 4세그먼트로 분리
        segment_angles = [0, 60, -120, 60]
        for delta_angle in segment_angles:
            angle += delta_angle
            pos = add_vector(pos, angle, length)
            path.append(pos)

        turned = False
        for idx in reversed(range(depth - 1)):
            period = 4 ** (idx + 1)
            if i % period == 0:
                flags[idx] = 1 - flags[idx]
                for j in range(idx):
                    flags[j] = 0
                if flags[idx] == 1:
                    angle += 60
                else:
                    angle -= 120
                turned = True
                break

        if not turned:
            if i % 2 == 1:
                angle += 60
            else:
                angle -= 120

    return path

# 실행 및 시각화 (특히 depth=5 확인)
depth = 5
path = for_Koch_matplotlib(start_pos=(0, 0), dist=500, depth=depth)
x_vals, y_vals = zip(*path)

plt.figure(figsize=(10, 4))
plt.plot(x_vals, y_vals, color='blue')
plt.title(f"Koch Curve (depth={depth})")
plt.axis('equal')
plt.axis('off')
plt.tight_layout()
plt.show()
