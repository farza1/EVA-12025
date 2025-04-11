OSPF = 110
RIP = 120
EIGRP = 90
BGP = 20

pregunta =input("De cual protocolo se desea saber la distancia Administrativa"))
if pregunta ==str("OSPF"):
    print("Distancia administrativa del protocolo OSPF es ") + str(OSPF)
elif pregunta==str("RIP"):
    print("Distancia administrativa del protocolo RIP es")+ str(RIP))
elif pregunta==str("EIGRP"):
    print("Distancia administrativa de protocolo EIGRP es")+str(EIGRP))
elif pregunta==str("BGP"):
    print("Distancia administrativa del protocolo BGP es")+ str(BGP))
else:
    print("Porfavor escribe un nombre valido para el protocolo que desea consultar(como por ejemplo OSPF , RIP , EIGRP O BGP")
