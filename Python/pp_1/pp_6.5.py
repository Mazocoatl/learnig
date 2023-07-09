#Promedio trimestras y anual de presupuesto
print("Bienvenido al programa de presupuesto")

print("Indique el presupuesto de cada mes")
p_ene = int(input("Enero = $"))
p_feb = int(input("Febrero = $"))
p_mar = int(input("Marzo = $"))
p_abr = int(input("Abril = $"))
p_may = int(input("Mayo = $"))
p_jun = int(input("Junio = $"))
p_jul = int(input("Julio = $"))
p_ago = int(input("Agosto = $"))
p_sep = int(input("Septiembre = $"))
p_oct = int(input("Octubre = $"))
p_nov = int(input("Noviembre = $"))
p_dic = int(input("Diciembre = $"))

p_1tri = [p_ene,p_feb,p_mar]
p_2tri = [p_abr,p_may,p_jun]
p_3tri = [p_jul,p_ago,p_sep]
p_4tri = [p_oct,p_nov,p_dic]
p_anu = [p_ene,p_feb,p_mar,p_abr,p_may,p_jun,p_jul,p_ago,p_sep,p_oct,p_nov,p_dic]

template = f"El presupuesto total del primer trimestre es de ${sum(p_1tri)} y el promedio es de ${round(sum(p_1tri)/len(p_1tri),2)}"
print(template)
template = f"El presupuesto total del primer trimestre es de ${sum(p_2tri)} y el promedio es de ${round(sum(p_2tri)/len(p_2tri),2)}"
print(template)
template = f"El presupuesto total del primer trimestre es de ${sum(p_3tri)} y el promedio es de ${round(sum(p_3tri)/len(p_3tri),2)}"
print(template)
template = f"El presupuesto total del primer trimestre es de ${sum(p_4tri)} y el promedio es de ${round(sum(p_4tri)/len(p_4tri),2)}"
print(template)
template = f"El presupuesto total anuela es de ${sum(p_anu)} y el promedio es de ${round(sum(p_anu)/len(p_anu),2)}"
print(template)