from PIL import Image
from subprocess import Popen, PIPE
from time import time
import numpy as np

loop_time = time()
fps, duration = 24, 100000
p = Popen(['ffmpeg', '-y', '-f', 'image2pipe', '-vcodec', 'mjpeg', '-r', '24', '-i',
          '-', '-vcodec', 'mpeg4', '-qscale', '5', '-r', '24', 'video.avi'], stdin=PIPE)
for i in range(fps * duration):
    im = Image.new('RGB', (300, 300), (i, 1, 1))
    im.save(p.stdin, 'JPEG')
    arr = np.array(im)
    im = Image.fromarray(arr)
    im.save('lucas.jpg')
    timef = (time() - loop_time)
    timef = timef if timef else 1
    fps = 1 / timef
    print('FPS {}'.format(fps))
    loop_time = time()

p.stdin.close()
p.wait()
