# Decirle qué tiene que comprar para la semana que viene
import pandas as pd
import re

def ingredientes_de_una_pizza(nombre_tipo,pizza_types):
    '''
    Función que, dado un tipo de pizza te devuelve los ingredientes
    '''
    ingredientes = []
    for i in range(len(pizza_types.axes[0])):
        fila = pizza_types.iloc[i]
        if re.search(nombre_tipo,str(fila),re.IGNORECASE) != None:
            ingredientes = fila['ingredients']
            ingredientes_lista = ingredientes.split(",")
    print(ingredientes_lista)
    return ingredientes_lista

def cambiar_formato_nombre_pizza(nombre_tipo,pizzas):
    for i in range(len(pizzas.axes[0])):
        fila = pizzas.iloc[i]
        if re.search(nombre_tipo,str(fila),re.IGNORECASE) != None:
            nombre= fila['pizza_type_id']
            tamaño = fila['size']
            if tamaño == "S":
                cantidad = 1
            elif tamaño == "M":
                cantidad = 2
            elif tamaño == "L":
                cantidad = 3
            else:
                cantidad = 1
    return nombre, cantidad

def contar_pizzas_por_semana(order_details):
    numero_pizzas_año = 0
    for i in range(len(order_details)):
        fila = order_details.iloc[i]
        numero_pizzas_año += 1*int(fila['quantity'])
    print(numero_pizzas_año)
    numero_pizzas = numero_pizzas_año//52
    print(numero_pizzas)
    return numero_pizzas


def contar_pizzas_en_una_semana(order_details,pizzas):
    order_pizzas = pd.DataFrame(columns = ['pizza','numero'])
    for i in range(0,953):
        pizza_con_tam = order_details.loc[i,'pizza_id']
        quantity = order_details.loc[i,'quantity']
        pizza, tamaño = cambiar_formato_nombre_pizza(pizza_con_tam,pizzas)
        if len(order_pizzas) == 0:
            order_pizzas.loc[0] = (pizza,tamaño*int(quantity))
        else:
            añadido = False
            for j in range(len(order_pizzas)):
                fila2 = order_pizzas.iloc[j]
                if re.search(pizza,str(fila2)):
                    anterior = fila2['numero']
                    nuevo = anterior + quantity*tamaño
                    order_pizzas.loc[j,'numero'] = nuevo
                    añadido = True
                    break
            if añadido == False:
                order_pizzas.loc[len(order_pizzas)] = (pizza,tamaño*int(quantity))
    return order_pizzas

def calcular_ingredientes(order_pizzas,pizza_types):
    ingredientes = pd.DataFrame(columns = ['ingrediente','cantidad'])
    for i in range(len(order_pizzas)):
        ingredientes_de_esa_pizza = ingredientes_de_una_pizza(order_pizzas.loc[i,'pizza'],pizza_types)
        for ingrediente in ingredientes_de_esa_pizza:
            if len(ingredientes) == 0:
                ingredientes.loc[0] = (ingrediente,order_pizzas.loc[i,'numero'])
            else:
                añadido = False
                for j in range(len(ingredientes)):
                    fila2 = ingredientes.iloc[j]
                    if re.search(ingrediente,str(fila2)):
                        anterior = fila2['cantidad']
                        nuevo = anterior + order_pizzas.loc[i,'numero']
                        ingredientes.loc[j,'cantidad'] = nuevo
                        añadido = True
                        break
                if añadido == False:
                    ingredientes.loc[len(ingredientes)] = (ingrediente,order_pizzas.loc[i,'numero'])
    return ingredientes

        
if __name__=="__main__":

    pizza_types= pd.read_csv('pizza_types.csv',sep=",",encoding="LATIN_1") # Para ver los ingredientes de una pizza
    pedidos = pd.read_csv('order_details.csv',sep=",",encoding="LATIN_1") # Para calcular los pedidos
    pizzas = pd.read_csv('pizzas.csv',sep=",",encoding="LATIN_1") # Para ver el nombre de la pizza
    orders = pd.read_csv('orders.csv',sep=",",encoding="LATIN_1") # Para ver cuántos pedidos hay en una semana
    ingredientes_de_una_pizza("bbq_ckn",pizza_types)
    print(cambiar_formato_nombre_pizza("southw_ckn_l",pizzas))
    contar_pizzas_por_semana(pedidos)
    pr = contar_pizzas_en_una_semana(pedidos,pizzas)
    print(pr)
    print(calcular_ingredientes(pr,pizza_types))