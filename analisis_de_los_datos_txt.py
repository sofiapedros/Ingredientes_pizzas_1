import pandas as pd

def analisis_dataFrame(df, file):
    '''
    Función que escribe en un fichero dado
    la información sobre la calidad de los
    datos de un dataframe
    '''
    # Número de NaN
    file.write("Número de NaN totales:\n")
    file.write(f"{str(df.isna().sum().sum())}\n")

    file.write("Número de NaN por columnas: \n")
    file.write(f'{str(df.isna().sum())}\n')
    file.write("\n")

    # Número de nulls
    file.write(f'Número de nulls totales: \n')
    file.write(f"{str(df.isnull().sum().sum())}\n")
    file.write(f'Número de nulls por columnas \n')
    file.write(f"{str(df.isnull().sum())} \n")
    file.write("\n")

    # Tipos de datos
    file.write("Los tipos de datos en las columnas son: \n")
    file.write(f'{str(df.dtypes)}\n')
        

if __name__ == "__main__":
    # ficheros que hay que analizar
    ficheros = ['data_dictionary.csv','order_details.csv','orders.csv','pizza_types.csv','pizzas.csv']

    # Fichero en el que se escribirá el análisis
    with open("Analisis_datos.txt","w") as file:
        for fichero in ficheros:
            # Escribe el análisis y una línea al final para separar visualmente los ficheros
            file.write(f"Análisis de {fichero}\n")
            analisis_dataFrame(pd.read_csv(fichero,sep=",",encoding="LATIN_1"),file)
            file.write("____________________________________________________________________\n")
