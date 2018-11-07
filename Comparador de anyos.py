# coding:utf8
anyo_actual = int(input("Que anyo estyamos? "))
cualquier_anyo = int(input("Escriba un anyo cualquiera "))
if (anyo_actual == 2018) and (cualquier_anyo >=2018):
    print ("Para llegar al anyo",cualquier_anyo, "faltan", cualquier_anyo - anyo_actual,"anyos")
    
    
# coding:utf8
anyo_actual = int(input("Que anyo estamos? "))
cualquier_anyo = int(input("Escriba un anyo cualquiera "))
if (anyo_actual ==2018) and (cualquier_anyo <= 2018):
    print ("Desde el anyo",cualquier_anyo, "han pasado", anyo_actual - cualquier_anyo,"anyo")
    
    
# coding:utf8
anyo_actual = int(input("Que anyo estamos? "))
cualquier_anyo = int(input("Escriba un anyo cualquiera "))
if (anyo_actual ==2018) and (cualquier_anyo == 2018):
    print ("Son el mismo anyo")
