#/usr/bin/python
import pandas as pd
import numpy as np

##1) ¿Cómo dividir una columna de texto en dos columnas separadas?

df = pd.DataFrame(["STD, City State",
"33, Kolkata-West Bengal",
"44, Chennai-Tamil Nadu",
"40, Hyderabad Telengana",
"80, Bangalore Karnataka"], columns=['row'])

print(pd.DataFrame(dict(zip(range(3), [df['row'].apply(lambda x : x.split(' ')[i]) for i in range(3)]))).head())


##3) ¿Cómo obtener las posiciones donde coinciden los valores de dos columnas

df = pd.DataFrame({'fruit1': np.random.choice(['apple', 'orange', 'banana'], 10),
                   'fruit2': np.random.choice(['apple', 'orange', 'banana'], 10)})
arr=[]

for idx, row in df.iterrows():
    if row['fruit1'] == row['fruit2']:
        arr.extend(str(idx))

print(df)
print(arr)

##5) Genere 3 columnas con 5 elementos cada uno. Cree una función para eliminar los N primeras o N últimas filas
df = pd.DataFrame({'fruit1': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit2': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit3': np.random.choice(['apple', 'orange', 'banana'], 5)})
print (df)
def n_primeras(df,n):
    print(df.iloc[n:])
def n_ultimas(df,n):
    print(df.iloc[:n])

n_primeras(df,2)
n_ultimas(df,2)


##7) Genere 4 columnas con 5 elementos cada uno. Cree una función para obtener los N primeros o N ultimos registros.
df = pd.DataFrame({'fruit1': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit2': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit3': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit4': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit5': np.random.choice(['apple', 'orange', 'banana'], 5)})
def get_n_primeras(df,n):
    print(df.iloc[:n])
def get_n_ultimas(df,n):
    print(df.iloc[n+1:])
get_n_primeras(df,2)
get_n_ultimas(df,2)


    
##9) Genere 6 columnas con 5 elementos cada uno. Cree una función para obtener un nuevo DataFrame sin la columna X
df = pd.DataFrame({'fruit1': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit2': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit3': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit4': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit5': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit6': np.random.choice(['apple', 'orange', 'banana'], 5)})
def del_column(df,column_name):
    print(df.drop(column_name, 1))

del_column(df,"fruit4")


##11) Genere 2 columnas con 20 elementos cada uno. La primera columna debe de tener uno de los siguientes valores:
##C1, C2, C3 y C4. Estos valores se pueden repetir. La segunda columna tiene valores de números cualesquiera. Cree una función para
##agrupar por la Primera Columna y que se listen los valores agrupados de la segunda Columna
df = pd.DataFrame({'column': np.random.choice(['C1', 'C2', 'C3', 'C4'], 20),
                   'number': np.random.choice(['1','2','3','4','5','6','7','8','9','0'], 20)})
print(df)
print(df.groupby(['column'])['number'].apply(lambda x:','.join(list(x))))

##13) Escriba una funcion que inserte en un indice especifico una nueva columna de datos en un DataFrame. Cree un DataFrame de ejemplo para probar su funcion.
df = pd.DataFrame({'column': np.random.choice(['C1', 'C2', 'C3', 'C4'], 5)})
def insert_column(df,name,new_col,index):
    df.insert(loc=index, column=name, value=new_col)
    print(df)

insert_column(df,'new_col',np.random.choice(['apple', 'orange', 'banana'], 5),0)


##15) Cree una funcion para cambiar strings o flotantes a tipo de dato entero de una columna y booleanos a 0 si es falso o 1 si es verdadero
##(tambien debe de quedar cambiada la columna a tipo entero). Cree un DataFrame de ejemplo para probar su funcion. Aqui un posible ejemplo:
df = pd.DataFrame({'score': np.random.choice(['12.50', '14.50', '12.77', '9.21'], 20),
                   'qualify': np.random.choice([True,False], 20)})
print(df)
print(df.dtypes)

def change_dtypes(df,column_name):
    print(pd.to_numeric(df[column_name], errors='ignore'))

    print(df.dtypes)
    
print(df)
print(df.dtypes)

    
##17) Escriba una funcion para buscar en que columnas se repite cierto valor y cuales no. Cree un DataFrame de ejemplo para probar su funcion.

df = pd.DataFrame({'fruit1': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit2': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit3': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit4': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit5': np.random.choice(['apple', 'orange', 'banana'], 5),
                   'fruit6': np.random.choice(['apple', 'orange', 'banana'], 5)})

def find_value(df,valor):
    print ((df == valor).all(1))

find_value(df,'apple')
    







