from pyrsistent import s
import investpy as inv
import pandas as pd

class Data:
    def __init__(self,stock,country,start,stop):
        self.stock = stock
        self.country = country
        self.start= start
        self.stop = stop
    
    def stock_recent_data(self):
        temp= inv.get_stock_recent_data(stock=self.stock,country=self.country,as_json=False)
        temp['Name']=self.stock
        temp['Country']=self.country
        return temp
        
    def stock_info(self):
        return inv.get_stock_information(stock=self.stock,country=self.country,as_json=False)
    
    def stock_financial_summary(self):
        return inv.get_stock_financial_summary(stock=self.stock,country=self.country,summary_type="income_statement",period="annual")

    def historical_data(self):
        temp= inv.get_stock_historical_data(stock=self.stock,country=self.country,from_date=self.start,to_date=self.stop)
        temp['Name']=self.stock
        temp['Country']=self.country
        return temp

    def save_stock(self):
        self.historical_data().to_csv("stock.csv")

    def save_info(self):
        self.stock_info().to_csv("info.csv")


ONGC=Data("ONGC","India","01/01/2020","16/06/2022")
print("\nPrinting Stock information for ONGC Stock: \n")
print(ONGC.stock_info())
print("\n"+("-"*100)+"\n")
print("\nPrinting Stock Financial Summary for ONGC Stock: \n")
print(ONGC.stock_financial_summary())
print("\n"+("-"*100)+"\n")

BPCL=Data("BPCL","India","01/01/2020","16/06/2022")
print("\nPrinting Stock information for BPCL Stock: \n")
print(BPCL.stock_info())
print("\n"+("-"*100)+"\n")
print("\nPrinting Stock Financial Summary for BPCL Stock: \n")
print(BPCL.stock_financial_summary())
print("\n"+("-"*100)+"\n")

HPCL=Data("HPCL","India","01/01/2020","16/06/2022")
print("\nPrinting Stock information for HPCL Stock: \n")
print(HPCL.stock_info())
print("\n"+("-"*100)+"\n")
print("\nPrinting Stock Financial Summary for HPCL Stock: \n")
print(HPCL.stock_financial_summary())
print("\n"+("-"*100)+"\n")

GAIL=Data("GAIL","India","01/01/2020","16/06/2022")
print("\nPrinting Stock information for GAIL Stock: \n")
print(GAIL.stock_info())
print("\n"+("-"*100)+"\n")
print("\nPrinting Stock Financial Summary for GAIL Stock: \n")
print(GAIL.stock_financial_summary())
print("\n"+("-"*100)+"\n")

ADAN=Data("ADAN","India","01/01/2020","16/06/2022")
print("\nPrinting Stock information for ADAN Stock: \n")
print(ADAN.stock_info())
print("\n"+("-"*100)+"\n")
print("\nPrinting Stock Financial Summary for ADAN Stock: \n")
print(ADAN.stock_financial_summary())
print("\n"+("-"*100)+"\n")


