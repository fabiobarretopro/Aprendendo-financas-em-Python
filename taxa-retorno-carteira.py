import numpy
import pandas
from pandas_datareader import data
import matplotlib.pyplot

carteira_acoes = ["PETR4.SA", "BBDC4.SA", "OIBR4.SA", "AMAR3.SA", "GOLL4.SA"]
dados = pandas.DataFrame()
for t in carteira_acoes:
    dados[t] = data.DataReader(t, data_source="yahoo", start="2015-1-1")["Adj Close"]

print(dados.info())
print(dados.head())
print(dados.tail())
"""
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 1487 entries, 2015-01-02 to 2020-12-29
Data columns (total 5 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   PETR4.SA  1487 non-null   float64
 1   BBDC4.SA  1487 non-null   float64
 2   OIBR4.SA  1487 non-null   float64
 3   AMAR3.SA  1487 non-null   float64
 4   GOLL4.SA  1487 non-null   float64
dtypes: float64(5)
memory usage: 69.7 KB
None
            PETR4.SA   BBDC4.SA  OIBR4.SA   AMAR3.SA  GOLL4.SA
Date                                                          
2015-01-02  8.683293  12.811392      8.43  13.125690     14.99
2015-01-05  7.941135  12.844934      7.80  13.026185     14.85
2015-01-06  7.681378  13.267506      6.61  12.221085     15.21
2015-01-07  8.043181  13.794719      6.52  12.447261     14.55
2015-01-08  8.562695  13.865822      6.78  12.311535     14.27
             PETR4.SA   BBDC4.SA  OIBR4.SA  AMAR3.SA   GOLL4.SA
Date                                                           
2020-12-21  27.020000  26.166082      2.82      6.92  23.950001
2020-12-22  27.280001  26.698074      2.78      6.60  23.299999
2020-12-23  27.950001  27.308878      2.81      6.62  24.540001
2020-12-28  28.280001  27.584726      2.79      6.55  24.209999
2020-12-29  28.270000  27.530001      2.82      6.82  24.480000
"""

print(dados.iloc[0])
"""
PETR4.SA     8.683293
BBDC4.SA    12.811392
OIBR4.SA     8.430000
AMAR3.SA    13.125690
GOLL4.SA    14.990000
Name: 2015-01-02 00:00:00, dtype: float64
"""

(dados/dados.iloc[0]*100).plot(figsize=(20, 10))
matplotlib.pyplot.show()

dados.plot(figsize=(20, 10))
matplotlib.pyplot.show()

retorno = (dados/dados.shift(1)) - 1
print(retorno)
"""
Date                                                        
2015-01-02       NaN       NaN       NaN       NaN       NaN
2015-01-05 -0.085470  0.002618 -0.074733 -0.007581 -0.009340
2015-01-06 -0.032710  0.032898 -0.152564 -0.061806  0.024242
2015-01-07  0.047101  0.039737 -0.013616  0.018507 -0.043392
2015-01-08  0.064591  0.005154  0.039877 -0.010904 -0.019244
...              ...       ...       ...       ...       ...
2020-12-21 -0.043540 -0.031717 -0.040816 -0.029453 -0.064088
2020-12-22  0.009623  0.020331 -0.014184 -0.046243 -0.027140
2020-12-23  0.024560  0.022878  0.010791  0.003030  0.053219
2020-12-28  0.011807  0.010101 -0.007117 -0.010574 -0.013448
2020-12-29 -0.000354 -0.001984  0.010753  0.041221  0.011152

[1487 rows x 5 columns]

"""

pesos = pandas.array([.2, .2, .2, .2, .2])

retorno_anual = retorno.mean()*250
print(retorno_anual)
"""
PETR4.SA    0.343138
BBDC4.SA    0.201987
OIBR4.SA    0.095909
AMAR3.SA    0.066649
GOLL4.SA    0.406203
dtype: float64
"""

print(numpy.dot(retorno_anual, pesos))
"""
0.22277718656091167
"""
print(f"{(numpy.dot(retorno_anual, pesos)*100):.2f}%")
"""
22.28%
"""