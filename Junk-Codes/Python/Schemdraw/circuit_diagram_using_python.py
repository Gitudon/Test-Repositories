import schemdraw
import schemdraw.elements as elm

d = schemdraw.Drawing()

V = d.add(elm.SourceV().up().label("V", loc="left"))
R = d.add(elm.Resistor().label("R").right())
C = d.add(elm.Capacitor().label("C").right())
L = d.add(elm.Inductor().label("L").down())

d.add(elm.Ground().at(V.start))
d.add(elm.Ground().at(L.end))
d.draw()
