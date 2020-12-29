import numpy
from pandas_datareader import data
import matplotlib.pyplot

PETR4 = data.DataReader("PETR4.SA", data_source="yahoo", start="2020-1-1")
print(PETR4.head())
print(PETR4.tail())
"""
                 High        Low       Open      Close      Volume  Adj Close
Date                                                                         
2020-01-02  30.700001  30.309999  30.510000  30.700001  37774500.0  30.697731
2020-01-03  31.240000  30.450001  30.879999  30.450001  71595600.0  30.447748
2020-01-06  30.940001  29.950001  30.430000  30.809999  81844000.0  30.807720
2020-01-07  30.879999  30.469999  30.820000  30.690001  32822000.0  30.687731
2020-01-08  30.770000  30.240000  30.690001  30.500000  48215600.0  30.497744
                 High        Low       Open      Close      Volume  Adj Close
Date                                                                         
2020-12-21  27.490000  26.520000  27.190001  27.020000  99988800.0  27.020000
2020-12-22  27.469999  27.049999  27.200001  27.280001  46513200.0  27.280001
2020-12-23  28.250000  27.350000  27.430000  27.950001  49038900.0  27.950001
2020-12-28  28.520000  28.200001  28.360001  28.280001  26661400.0  28.280001
2020-12-29  28.430000  27.990000  28.379999  28.270000  29891100.0  28.270000
"""

# (Preço final / Preço inicial) - 1
PETR4["Retorno_simples"] = (PETR4["Adj Close"] / PETR4["Adj Close"].shift(-1)) - 1
print(PETR4["Retorno_simples"])
"""
Date
2020-01-02    0.008210
2020-01-03   -0.011684
2020-01-06    0.003910
2020-01-07    0.006230
2020-01-08    0.003289
                ...   
2020-12-21   -0.009531
2020-12-22   -0.023971
2020-12-23   -0.011669
2020-12-28    0.000354
2020-12-29         NaN
Name: Retorno_simples, Length: 246, dtype: float64
"""

PETR4["Retorno_simples"].plot(figsize=(15, 7))
matplotlib.pyplot.show()

retorno_diario = PETR4["Retorno_simples"].mean()  # .mean => taxa de retorno média diária
print(retorno_diario)
retorno_anual = PETR4["Retorno_simples"].mean()*250  # .mean => taxa de retorno média diária
print(retorno_anual)
print(f"{retorno_anual*100:.2f} %")
"""
0.0014121355361144795
0.3530338840286199
35.30 %
"""
print(PETR4.head())
"""
                 High        Low  ...  Adj Close  Retorno_simples
Date                              ...                            
2020-01-02  30.700001  30.309999  ...  30.697731         0.008210
2020-01-03  31.240000  30.450001  ...  30.447748        -0.011684
2020-01-06  30.940001  29.950001  ...  30.807720         0.003910
2020-01-07  30.879999  30.469999  ...  30.687731         0.006230
2020-01-08  30.770000  30.240000  ...  30.497744         0.003289

[5 rows x 7 columns]
"""

PETR4["retorno_log"] = numpy.log(PETR4["Adj Close"] / PETR4["Adj Close"].shift(1))
print(PETR4["retorno_log"])
"""
Date
2020-01-02         NaN
2020-01-03   -0.008177
2020-01-06    0.011753
2020-01-07   -0.003902
2020-01-08   -0.006210
                ...   
2020-12-21   -0.044516
2020-12-22    0.009577
2020-12-23    0.024263
2020-12-28    0.011738
2020-12-29   -0.000354
Name: retorno_log, Length: 246, dtype: float64
"""
PETR4["retorno_log"].plot(figsize=(18, 10))
matplotlib.pyplot.show()

retorno_diario02 = PETR4["retorno_log"].mean()
print(retorno_diario02)
"""
-0.0003362757377854689
"""
retorno_anual02 = PETR4["retorno_log"].mean()
print(retorno_anual02)
"""
-0.0003362757377854689
"""
print(f"{retorno_anual02*100} %")
"""
-0.033627573778546895 %
"""