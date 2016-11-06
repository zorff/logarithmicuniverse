import svgwrite
import math

def frange(x, y, jump):
    while x < y:
        yield x
        x += jump

def logg(val):
    return math.log(val, 10)

def drawObjectR(dwg, diam, r, dist, diff, text = ""):
    rad = (r / 12) * math.pi
    drawObjectRad(dwg, diam, rad, dist, diff, text)

def drawObjectRad(dwg, diam, rad, dist, diff, text = ""):
    yy = dist * math.cos(rad)
    xx = dist * math.sin(rad)
    drawObject(dwg, diam, xx, yy, diff, text)

def drawLineR(dwg, rad, dist):
    yy = dist * math.cos(rad)
    xx = dist * math.sin(rad)
    drawLine(dwg, 1, 1, xx, yy)

def drawLine(dwg, x, y, x2, y2):
    if (x != 0 or y != 0):
        dist=logg(math.sqrt((x*x) + (y*y)))
        if (y == 0):
            rr = math.pi / 2
        else: 
            rr = math.atan2(x, y)
        xx1 = dist*math.sin(rr)
        yy1 = dist*math.cos(rr)
    else:
        xx1 = 0
        yy1 = 0

    dist2=logg(math.sqrt((x2*x2) + (y2*y2)))
    if (y == 0):
        rr2 = math.pi / 2
    else:
        rr2 = math.atan2(x2, y2)
    xx2 = dist2*math.sin(rr2)
    yy2 = dist2*math.cos(rr2)
    dwg.add(dwg.line((cx+round(scal*xx1), cy+round(scal*yy1)), (cx+round(scal*xx2), cy+round(scal*yy2)), stroke=svgwrite.rgb(10, 10, 16, '%')))
        
    
def drawObject(dwg, diam, xpos, ypos, diff, text = ""):
    x=xpos + diam*math.cos(0)
    y=ypos + diam*math.sin(0)
    dist=logg(math.sqrt((x*x) + (y*y)))
    if (y == 0):
        rr = math.pi / 2
    else:
        rr = math.atan2(x, y)
    
        
    xx1 = dist*math.sin(rr)
    yy1 = dist*math.cos(rr)
    poly = []
    poly.append((cx+round(scal*xx1), cy+round(scal*yy1)))
    
    for r in frange(0.0, 6.4, diff):
        x=xpos + diam*math.cos(r)
        y=ypos + diam*math.sin(r)
        dist=logg(math.sqrt((x*x) + (y*y)))
        if (y == 0):
            rr = math.pi / 2
        else:
            rr = math.atan2(x, y)
            
        xx = dist*math.sin(rr)
        yy = dist*math.cos(rr)

        poly.append((cx+round(scal*xx), cy+round(scal*yy)))
        #dwg.add(dwg.line(, (cx+round(scal*xx1), cy+round(scal*yy1)), stroke=svgwrite.rgb(10, 10, 16, '%')))
        xx1=xx
        yy1=yy
    dwg.add(dwg.polygon(poly,stroke='black', fill='none'))
    #, stroke=svgwrite.rgb(10, 10, 16, '%')
    if (not text == ""):
        dwg.add(dwg.text(text, insert=(cx+round(scal*xx)+5, cy+round(scal*yy)), fill='black'))
    
    
cx = 600
cy = 420
scal = 18

dwg = svgwrite.Drawing('test2.svg', profile='tiny')

kmperly = 9460730472580
mpc = 3260000 * kmperly

drawLineR(dwg, 0, 152098232)
drawLineR(dwg, 0.1, kmperly*10)
drawLineR(dwg, 0.3, kmperly*1000)
drawLineR(dwg, 0.5, kmperly*100000)
drawLineR(dwg, 0.7, mpc)
drawLineR(dwg, 0.9, 100*mpc)

drawObject(dwg, 6371, 0, 6371, 0.01, "Earth")
drawObject(dwg, 6471, 0, 6371, 0.01)
drawObject(dwg, 100, 0, 6371, 0.01)

# Moon
drawObject(dwg, 1737*2, 0, -384399, 1, "Moon")

# Sun
drawObject(dwg, 1396840, 0, -152098232, 1, "Sun")
#drawObjectRad(dwg, 1396840, 2, 152098232, 1)
#drawObjectRad(dwg, 1396840, 3, 152098232, 1)


# orbit of Neptune
drawObject(dwg, 4503000000, 0, 152098232, 0.01, "Neptune Orbit")

drawObject(dwg, 249209300, 0, -152098232, 0.01, "Mars Orbit")
drawObject(dwg, 107477000, 0, -152098232, 0.01, "Venus Orbit")
drawObject(dwg, 69816900, 0, -152098232, 0.01, "Mercury Orbit")

# moon orbit
#drawObject(dwg, 384399, 0, 0, 0.1)

# Alpha Centauri / Proxima
drawObjectR(dwg, 224219312200, 14.55, 41305549243284, 0.1, "A Centauri")

drawObjectR(dwg, 224219312200, 17.9, 5.9630 * kmperly, 0.1, "Barnard's Star")
drawObjectR(dwg, 224219312200, 10.9, 7.7825 * kmperly, 0.1, "Wolf 359")
drawObjectR(dwg, 224219312200, 6.5, 8.5828 * kmperly, 0.1, "Sirius")
drawObjectR(dwg, 224219312200, 3.5, 10.522 * kmperly, 0.1, "Epsilon Eridani")
drawObjectR(dwg, 224219312200, 7.5, 11.402 * kmperly, 0.1, "Procyon")
drawObjectR(dwg, 224219312200, 22, 11.824 * kmperly, 0.1, "Epsilon Indi")
drawObjectR(dwg, 224219312200, 1.75, 11.887 * kmperly, 0.1, "Tau Ceti")
drawObjectR(dwg, 224219312200, 14.25, 36.7 * kmperly, 0.1 ,"Arcturus")

drawObjectR(dwg, 2242193122000, 6.47, 310 * kmperly, 0.1, "Canopus")
drawObjectR(dwg, 2242193122000, 18.55, 25 * kmperly, 0.1, "Vega")
drawObjectR(dwg, 224219312200, 5.25, 42.2 * kmperly, 0.1, "Capella")
drawObjectR(dwg, 2242193122000, 5.25, 860 * kmperly, 0.1, "Rigel")
drawObjectR(dwg, 2242193122000, 5.9, 643 * kmperly, 0.1, "Betelgeuse")
drawObjectR(dwg, 2242193122000, 1.5, 139 * kmperly, 0.1, "Achenar")
drawObjectR(dwg, 224219312200, 19.9, 16.73 * kmperly, 0.1, "Altair")
drawObjectR(dwg, 2242193122000, 4.5, 65 * kmperly, 0.1, "Aldebaran")

# Milky Way
drawObjectR(dwg, 5.20E+15, 17.75, 2.57E+17, 0.01, "Milky Way Centre")
drawObjectR(dwg, 5.20E+17, 17.75, 2.57E+17, 0.1, "Milky Way")

# Andromeda
drawObjectR(dwg, 1.32E+18, 0.6, 2.37E+19, 0.1,"Andromeda")
# Triangulum
drawObjectR(dwg, 50000 * kmperly, 1.6, 3000000*kmperly, 0.1, "Triangulum")

drawObjectR(dwg, 14000* kmperly, 5.4, 163000*kmperly, 0.1, "Greater Magellan")
drawObjectR(dwg, 7000* kmperly, 0.7,  200000*kmperly, 0.1, "Lesser Magellan")

drawObjectR(dwg, 6 * mpc, 12.7,  92 * mpc, 0.1, "Coma Supercluster")
drawObjectR(dwg, 15000000 * kmperly, 3.3,  73.6 * mpc, 0.1, "Perseus Cluster")
drawObjectR(dwg, 30 * mpc, 3.3,   185000000 * kmperly, 0.1, "Taurus Void")

# Bootes Void
drawObjectR(dwg, 2.37E+21, 14.8, 6.62E+21, 0.01, "Bootes Void")
#drawObjectR(dwg, 52 * mpc, 15, 61*mpc, 0.01, "Norhtern Local Void")
#drawObjectR(dwg, 56 * mpc, 15, 96*mpc, 0.01, "Southern Local Void")
drawObjectR(dwg, 550 * mpc, 3.25, 8000000000* kmperly, 0.01, "Eridanus Supervoid")

# Observable Universe
drawObject(dwg, 4.35E+23, 0, 0, 0.01, "Observable Universe")



# Local Void
drawObjectR(dwg, 22.5*mpc, 18.6, 23*mpc , 0.01, "Local Void")

# Virgo cluster
drawObjectR(dwg,  2.2*mpc, 12.5, 53800000*kmperly, 0.01, "Virgo cluster")

# Virgo Supercluster
#drawObject(dwg, 7175593*kmperly, 53800000*kmperly, 0, 0.01)
# Sloan Great Wall
#drawObject(dwg, 900000000*kmperly, 1000000000*kmperly, 0, 0.01 ,"Sloan Great Wall")

#Hercules-Corona Borealis Great Wall
#drawObject(dwg, 7300000000*kmperly, 0, 10000000000*kmperly, 0.01, "Hercules-Corona Borealis Great Wall")
#CfA2 Great Wall
#drawObject(dwg, 500000000*kmperly, 0, 200000000*kmperly, 0.01, "CfA2 Great Wall")



dwg.save()
print("done")
