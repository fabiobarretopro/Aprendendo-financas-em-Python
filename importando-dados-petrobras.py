import numpy
import pandas

serie = pandas.Series(numpy.random.random(7), name="Coluna 01")
print(serie)
"""
Gerou 7 números aleatórios dentre 0 e 1.
0    0.097430
1    0.572201
2    0.818129
3    0.170470
4    0.541471
5    0.179405
6    0.513266
Name: Coluna 01, dtype: float64
"""
from pandas_datareader import data
petrobras = data.DataReader("PETR4.SA", data_source="yahoo", start="2010-1-1")
print(petrobras)
"""
Resultando uma tabela com as 5 primeiras e 5 últimas altas, baixas e fechamento do dia de ações:

                 High        Low       Open      Close      Volume  Adj Close
Date                                                                         
2010-01-04  37.320000  36.820000  36.950001  37.320000  13303600.0  31.196165
2010-01-05  37.430000  36.799999  37.380001  37.000000  21396400.0  30.928682
2010-01-06  37.500000  36.799999  36.799999  37.500000  18720600.0  31.346632
2010-01-07  37.450001  37.070000  37.270000  37.150002  10964600.0  31.054062
2010-01-08  37.389999  36.860001  37.160000  36.950001  14624200.0  30.886881
...               ...        ...        ...        ...         ...        ...
2020-12-10  28.200001  27.129999  27.190001  27.820000  97537100.0  27.820000
2020-12-11  27.780001  27.280001  27.490000  27.410000  30843600.0  27.410000
2020-12-14  28.270000  27.620001  28.030001  27.620001  53159500.0  27.620001
2020-12-15  27.990000  27.620001  27.620001  27.850000  47208200.0  27.850000
2020-12-16  28.240000  27.469999  27.850000  28.190001  59399200.0  28.190001

[2680 rows x 6 columns]
"""
print(petrobras.info())
"""
Gerou um quadro de dados (Dataframe) para verificar se nada saiu errado!
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 2680 entries, 2010-01-04 to 2020-12-16
Data columns (total 6 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   High       2680 non-null   float64
 1   Low        2680 non-null   float64
 2   Open       2680 non-null   float64
 3   Close      2680 non-null   float64
 4   Volume     2680 non-null   float64
 5   Adj Close  2680 non-null   float64
dtypes: float64(6)
memory usage: 146.6 KB
"""

print(petrobras.head(10))  # Indica o número das primeiras linhas que eu quero extrair dos dados.
# no nosso caso foram 10 linha,

"""
                 High        Low       Open      Close      Volume  Adj Close
Date                                                                         
2010-01-04  37.320000  36.820000  36.950001  37.320000  13303600.0  31.196165
2010-01-05  37.430000  36.799999  37.380001  37.000000  21396400.0  30.928682
2010-01-06  37.500000  36.799999  36.799999  37.500000  18720600.0  31.346632
2010-01-07  37.450001  37.070000  37.270000  37.150002  10964600.0  31.054062
2010-01-08  37.389999  36.860001  37.160000  36.950001  14624200.0  30.886881
2010-01-11  37.340000  36.619999  37.209999  36.830002  15317700.0  30.786566
2010-01-12  36.680000  36.040001  36.590000  36.360001  14886200.0  30.393690
2010-01-13  36.740002  35.840000  36.560001  36.299999  23228200.0  30.343531
2010-01-14  36.459999  35.560001  36.279999  35.669998  20073400.0  29.816916
2010-01-15  36.099998  35.509998  35.570000  35.750000  21169000.0  29.883787
"""
print(petrobras.tail(10))  # Indica o número das últimas linhas que eu quero extrair dos dados.
# no nosso caso foram 10 linhas,

"""
Date                                                                         
2020-12-03  26.889999  26.049999  26.150000  26.639999  62424500.0  26.639999
2020-12-04  27.559999  27.059999  27.190001  27.410000  42316600.0  27.410000
2020-12-07  27.790001  26.670000  27.270000  27.000000  72664200.0  27.000000
2020-12-08  27.139999  26.459999  26.809999  26.660000  46276700.0  26.660000
2020-12-09  26.969999  26.400000  26.629999  26.940001  52448300.0  26.940001
2020-12-10  28.200001  27.129999  27.190001  27.820000  97537100.0  27.820000
2020-12-11  27.780001  27.280001  27.490000  27.410000  30843600.0  27.410000
2020-12-14  28.270000  27.620001  28.030001  27.620001  53159500.0  27.620001
2020-12-15  27.990000  27.620001  27.620001  27.850000  47208200.0  27.850000
2020-12-16   0.000000   0.000000   0.000000  28.190001         0.0  28.190001
"""

carteira_acoes = ["PETR4.SA", "GGBR4.SA", "MRVE3.SA", "CVCB3.SA"]
novos_dados = pandas.DataFrame()
for acoes in carteira_acoes:
    novos_dados[acoes] = data.DataReader(acoes, data_source="yahoo", start="2010-1-1")["Adj Close"]

print(novos_dados.tail())
"""
Geram dados de determinadas ações a serem escolhidas:

             PETR4.SA   GGBR4.SA   MRVE3.SA   CVCB3.SA
Date                                                  
2020-12-10  27.820000  23.000000  19.440001  21.000000
2020-12-11  27.410000  23.010000  19.389999  21.260000
2020-12-14  27.620001  22.809999  20.080000  21.860001
2020-12-15  27.850000  23.799999  20.410000  21.860001
2020-12-16  28.190001  23.780001  20.490000  21.860001
"""

novos_dados.info()

# Como salvar os arquivos:


print(novos_dados.to_csv("C:/Users/Fabio/Desktop/financas com python/arquivos/exemplo01.csv"))
print(novos_dados.to_excel("C:/Users/Fabio/Desktop/financas com python/arquivos/exemplo03.xlsx"))

novos_dados1 = pandas.read_csv("C:/Users/Fabio/Desktop/financas com python/arquivos/exemplo01.csv")
print(novos_dados1)

"""
Vai ler um arquivo Excel no Python:

            Date   PETR4.SA   GGBR4.SA   MRVE3.SA   CVCB3.SA
0     2010-01-04  31.196165  25.257845   7.326664        NaN
1     2010-01-05  30.928682  25.684504   7.230773        NaN
2     2010-01-06  31.346632  25.855158   7.353333        NaN
3     2010-01-07  31.054062  25.274918   7.086936        NaN
4     2010-01-08  30.886881  25.206648   6.879096        NaN
...          ...        ...        ...        ...        ...
2675  2020-12-10  27.820000  23.000000  19.440001  21.000000
2676  2020-12-11  27.410000  23.010000  19.389999  21.260000
2677  2020-12-14  27.620001  22.809999  20.080000  21.860001
2678  2020-12-15  27.850000  23.799999  20.410000  21.860001
2679  2020-12-16  28.190001  23.780001  20.490000  21.860001

[2680 rows x 5 columns]
Process finished with exit co
"""