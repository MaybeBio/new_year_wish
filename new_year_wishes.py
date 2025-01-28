import cv2
import numpy as np
from moviepy.editor import VideoClip, TextClip, CompositeVideoClip
from moviepy.video.fx.all import fadein, fadeout

# 定义视频参数
width, height = 1920, 1080
fps = 30
duration = 2  # 每个文本显示的时间

# 定义祝福内容
messages = ["3", "2", "1", "除夕快乐！", "xxx师姐", "除去烦恼", "迎接希望", "福气新岁", "万事顺遂", "2025年", "也要", "充满热爱", "❤️"]

# 粒子效果函数
def particle_effect(t, text):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    num_particles = 100
    for _ in range(num_particles):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        cv2.circle(img, (x, y), 2, (255, 255, 255), -1)
    return img

# 创建视频剪辑
clips = []
for i, message in enumerate(messages):
    text_clip = TextClip(message, fontsize=100, color='white', size=(width, height), method='caption')
    text_clip = text_clip.set_duration(duration).set_position('center').set_fps(fps)
    text_clip = fadein(text_clip, 0.5).fadeout(0.5)
    
    particle_clip = VideoClip(lambda t: particle_effect(t, message), duration=duration)
    particle_clip = particle_clip.set_fps(fps)
    
    composite_clip = CompositeVideoClip([particle_clip, text_clip])
    clips.append(composite_clip)

# 合并所有剪辑
final_clip = CompositeVideoClip(clips)
final_clip.write_videofile("new_year_wishes.mp4", fps=fps)

