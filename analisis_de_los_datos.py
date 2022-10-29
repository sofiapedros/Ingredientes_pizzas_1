import pandas as pd

def analisis_dataFrame(df):
    print('Número de NaN totales:')
    print(df.isna().sum().sum())
    print('Número de NaN por columnas')
    print(df.isna().sum())

    print("")

    print(f'Número de nulls totales:')
    print(df.isnull().sum().sum())
    print(f'Número de nulls por columnas')
    print(df.isnull().sum())

    print("")
    print("Los tipos de datos en las columnas son: ")
    print(df.dtypes)

if __name__ == "__main__":
    ficheros = ['data_dictionary.csv','order_details.csv','orders.csv','pizza_types.csv','pizzas.csv']
    for fichero in ficheros:
        print(f"Análisis de {fichero}")
        analisis_dataFrame(pd.read_csv(fichero,sep=",",encoding="LATIN_1"))
        print("____________________________________________________________________")
