import investpy as inv
import pandas as pd

class Data:
    def __init__(self,stock,country):
        self.stock = stock
        self.country = country
    
    def stock_recent_data(self):
        return inv.get_stock_recent_data(stock=self.stock,country=self.country,as_json=False)
        
    def stock_info(self):
        return inv.get_stock_informations(stock=self.stock,country=self.country,as_json=False)
    
    def stock_financial_summary(self):
        return inv.get_stock_financial_summary(stock=self.stock,country=self.country,summary_type="income_statement",period="anually")


        
