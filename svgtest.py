import svgwrite
from random import randrange as rr
def add_to_svg(filename, profile, index1, index2):
    dwg = svgwrite.Drawing(filename, profile = profile)
    dwg.add(dwg.line((501.21667, 559.25061), (471.80249, 559.25061), stroke=svgwrite.rgb(10, 10, 16, '%')))
    dwg.add(dwg.line((0.67352706, 0.05433017), (0.67352706, 0.05433017), stroke=svgwrite.rgb(10, 10, 16, '%')))
    dwg.add(dwg.line((471.80249, 588.93311), (501.21667,588.93311), stroke=svgwrite.rgb(10, 10, 16, '%')))

    #dwg.add(dwg.polyline([(10,10),index2,(310,390)], stroke=svgwrite.rgb(236,100,75, '%')))
    dwg.add(dwg.text('Test', insert=(10, 10.2), fill='red'))
    dwg.save()
add_to_svg('test.svg', 'tiny', (14,12), (83, 903))
