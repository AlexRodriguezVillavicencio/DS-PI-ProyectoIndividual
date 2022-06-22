import pandas as pd
import os 

ruta = os.path.abspath('../Datasets')

def carga(archivo, sep=',', encoding='utf-8'):
    df = pd.read_csv('/' +archivo, sep=sep, encoding=encoding)

    compra = ['IdCompra', 'Fecha', 'Fecha_Año', 'Fecha_Mes', 'Fecha_Periodo',
       'IdProducto', 'Cantidad', 'Precio', 'IdProveedor']
    
    if df.columns == compra :
        return 'es una tabla de compras'
    