import glob
from PIL import Image

photos = glob.glob("C:\\Users\\Alec Burslem\\Documents\\CAS 2019\\Data\\2019_09_08\\1_0745\\snaps\*.png")
n=1

for f in photos:
    print(n)
    im = Image.open(f)
    rgb_im = im.convert('RGB')
    rgb_im.save("snap_%s!.jpg" % n)
    n += 1