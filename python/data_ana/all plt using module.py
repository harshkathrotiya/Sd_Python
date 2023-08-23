import pandas as pd
import plt_module as pt

empdata=[(101,"harsh",100000,"1-03-04"),
         (102,"jenish",150000,"1-03-04"),
         (103,"jeel",120000,"1-03-04"),
         (104,"het",105000,"1-03-04")]
df=pd.DataFrame(empdata,columns=("empid","empname","empsal","empdob"))
pt.historigram(df.empsal)
# pt.piechart(df.empsal, df.empname)
# pt.scat(df.empid,df.empsal)