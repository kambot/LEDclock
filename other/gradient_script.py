colors = {
"black":(0,0,0),
"white":(255,255,255),
"red":(255,0,0),
"lime":(0,255,0),
"blue":(0,0,255),
"yellow":(255,255,0),
"cyan":(0,255,255),
"magenta":(255,0,255),
"silver":(192,192,192),
"gray":(128,128,128),
"maroon":(128,0,0),
"olive":(128,128,0),
"green":(0,128,0),
"purple":(128,0,128),
"teal":(0,128,128),
"navy":(0,0,128)
}

def rounder(_number):
    d = _number - int(_number)
    if d >= .5:
        return int(_number) + 1
    else:
        return int(_number)
    
def from_to_lst(f,t):
    if t >= f:
        g = list(range(f,t+1))
    else:
        g = list(range(t,f+1))
        g = sorted(g,reverse=True)
    return g

to_color = "white"
rgbf = (0,100,0)
rgbt = colors[to_color]
rgbt = (0,0,255)

rf = rgbf[0]
gf = rgbf[1]
bf = rgbf[2]
rt = rgbt[0]
gt = rgbt[1]
bt = rgbt[2]
rd = abs(rt - rf)
gd = abs(gt - gf)
bd = abs(bt - bf)
maxd = max([rd,gd,bd])
sr = rd / maxd
sg = gd / maxd
sb = bd / maxd
r_grad = from_to_lst(rf,rt)
g_grad = from_to_lst(gf,gt)
b_grad = from_to_lst(bf,bt)
grad = []
sri = 0
sgi = 0
sbi = 0
for i in range(maxd+1):
    r = r_grad[rounder(sri)]
    g = g_grad[rounder(sgi)]
    b = b_grad[rounder(sbi)]
    grad.append((r,g,b))
    sri += sr
    sgi += sg
    sbi += sb
 
grad
