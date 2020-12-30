import numpy
import pandas
from pandas_datareader import data
import matplotlib.pyplot

carteira_acoes = ["^DJI", "^GSPC", "^IXIC", "^BVSP"]

indice_dados = pandas.DataFrame()

for t in carteira_acoes:
    indice_dados[t] = data.DataReader(t, data_source="yahoo", start="2003-1-1")["Adj Close"]

print(indice_dados.head())
"""
                   ^DJI       ^GSPC        ^IXIC    ^BVSP
Date                                                     
2003-01-02  8607.519531  909.030029  1384.849976  11603.0
2003-01-03  8601.690430  908.590027  1387.079956  11600.0
2003-01-06  8773.570312  929.010010  1421.319946  12020.0
2003-01-07  8740.589844  922.929993  1431.569946  11876.0
2003-01-08  8595.309570  909.929993  1401.069946  11786.0
"""

print(indice_dados.tail())
"""
                    ^DJI        ^GSPC         ^IXIC          ^BVSP
Date                                                              
2020-12-22  30015.509766  3687.260010  12807.919922  116348.000000
2020-12-23  30129.830078  3690.010010  12771.110352  117857.000000
2020-12-24  30199.869141  3703.060059  12804.730469            NaN
2020-12-28  30403.970703  3735.360107  12899.419922  119051.000000
2020-12-29  30335.669922  3727.040039  12850.220703  119409.148438

"""

(indice_dados/indice_dados.iloc[0]*100).plot(figsize=(20, 15))
print(matplotlib.pyplot.show())

indice_retorno = (indice_dados/indice_dados.shift(1)) - 1

print(indice_retorno.tail)
"""
<bound method NDFrame.tail of                 ^DJI     ^GSPC     ^IXIC     ^BVSP
Date                                              
2003-01-02       NaN       NaN       NaN       NaN
2003-01-03 -0.000677 -0.000484  0.001610 -0.000259
2003-01-06  0.019982  0.022474  0.024685  0.036207
2003-01-07 -0.003759 -0.006545  0.007212 -0.011980
2003-01-08 -0.016621 -0.014086 -0.021305 -0.007578
...              ...       ...       ...       ...
2020-12-22 -0.006650 -0.002073  0.005132  0.002862
2020-12-23  0.003809  0.000746 -0.002874  0.012970
2020-12-24  0.002325  0.003537  0.002633       NaN
2020-12-28  0.006758  0.008723  0.007395       NaN
2020-12-29 -0.002246 -0.002227 -0.003814  0.003008

[4530 rows x 4 columns]>
"""

indice_retorno_anual = indice_retorno.mean()*250
print(indice_retorno_anual)
"""
[4530 rows x 4 columns]>
^DJI     0.086544
^GSPC    0.096323
^IXIC    0.145395
^BVSP    0.151526
dtype: float64
"""
carteira_acoes = ["PETR4.SA", "^BVSP", "ITUB4.SA"]

dados_2 = pandas.DataFrame()
for t in carteira_acoes:
    dados_2[t] = data.DataReader(t, data_source="yahoo", start="2007-1-1")["Adj Close"]

print(dados_2.tail())
"""
             PETR4.SA          ^BVSP   ITUB4.SA
Date                                           
2020-12-21  27.020000  116016.000000  31.100000
2020-12-22  27.280001  116348.000000  31.250000
2020-12-23  27.950001  117857.000000  31.940001
2020-12-28  28.280001  119051.000000  32.220001
2020-12-29  28.270000  119409.148438  32.099998
"""

(dados_2/dados_2.iloc[0]*100).plot(figsize=(15, 6))
print(matplotlib.pyplot.show())
