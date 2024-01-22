import re
#Mapper by Matecitos
codigo = input("carga por aca el html de la web ")

coordenadas_matches = re.findall(r'style="left: ([-+]?\d*\.\d+|\d+)%; top: ([-+]?\d*\.\d+|\d+)%;', codigo)

if coordenadas_matches:
    coordenadas_resultantes = [f'/way {match[0]} {match[1]}' for match in coordenadas_matches]
    resultado_final = '\n'.join(coordenadas_resultantes)
    print(resultado_final)
else:
    print("Metiste mal el script papa, volve a cargarlo!")
    
