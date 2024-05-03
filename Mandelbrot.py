import pygame as pg
import numpy as np


resol = 300

WHITE=(255,255,255)
RED=(255,0,0)
SIZE=(1000,1000)

scale = 4
a=-2
b=-2
c_r, c_i = np.meshgrid(np.linspace(a,a+scale, SIZE[0]),np.linspace(b,b+scale, SIZE[1]))
def mandelbrot(ar, ai, cr,ci):
    return ar**2 -ai**2 +cr, 2 * ar * ai + ci
def gray(im):
    im = 255*im
    w, h = im.shape
    ret = np.empty((w, h, 3), dtype=np.uint8)
    ret[:, :, 2] = ret[:, :, 1] = ret[:, :, 0] = im
    return ret
def bicolor(imr,imb):
    imr, imb = 255*imr, 255*imb
    w, h = im.shape
    ret = np.empty((w, h, 3), dtype=np.uint8)
    ret[:, :, 2] = 0
    ret[:, :, 1] = imb
    ret[:, :, 0] = imr
    return ret


pg.init()
mouse_pos=np.array([0,0])
M = np.zeros((resol,resol)).astype(float)
scr = pg.display.set_mode((1000,1000))
running = True ; print("RUNNING")

S1 = np.zeros(SIZE)
S2 = np.zeros(SIZE)
R, I = np.zeros(SIZE), np.zeros(SIZE)
zoom = 0.5
i = 0
while running:
    scr.fill(WHITE)
    i+=1
    R, I = mandelbrot(R, I, c_r, c_i)
    N = np.sqrt(R**2 + I**2)
    bool = N==N
    S1 += bool
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False ; print("STOP")
    pg.display.set_caption("Mandelbrot's Set :  (" + str(np.round( a + scale * pg.mouse.get_pos()[0]/1000,3)) + " , " + str(np.round( b + scale * pg.mouse.get_pos()[1]/1000, 3)) + " ) ... step " + str(i) )

    if pg.mouse.get_pressed()[0]:
        print(i)
        if i > 10:
            S1 = np.zeros(SIZE)
            R, I = np.zeros(SIZE), np.zeros(SIZE)
            i = 0
            pos = pg.mouse.get_pos()
            a=a + scale * pos[0]/1000 * zoom
            b=b + scale * pos[1]/1000 * zoom
            print(a, b)
            scale *= 1-zoom
            c_r, c_i = np.meshgrid(np.linspace(a,a+scale, SIZE[0]),np.linspace(b,b+scale, SIZE[1]))
    scr.blit(pg.surfarray.make_surface(gray(S1.T/(S1.max()+1))), (0,0))

    pg.display.flip()

pg.quit()