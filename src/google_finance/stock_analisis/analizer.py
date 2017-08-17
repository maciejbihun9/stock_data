
from src.google_finance.stock_analisis.stock_comparator import StockComparator
from numpy import *
from src.google_finance.stock_analisis.stock_data_manager import StockDataManager
from datetime import datetime
# plik nie powinien zawierać klasy
# poprostu metody

def analize():
    """
    Measure what is the value of the actions similarity.
    * by prices,
    * by volumens
    """
    stocks_corealtions = {}
    s_and_p_names = StockDataManager.get_s_and_p_names()
    for s_and_p_name_1 in s_and_p_names:
        try:
            stock_data_1 = StockDataManager.load_stock_data(s_and_p_name_1)
        except Exception:
            continue
        for s_and_p_name_2 in s_and_p_names:
            if s_and_p_name_1 == s_and_p_name_2:
                continue
            try:
                stock_data_2 = StockDataManager.load_stock_data(s_and_p_name_2)
            except:
                continue
            if len(stock_data_2) == 0:
                print(0)
            stocks_corr = StockComparator.cor_comp(stock_data_1, stock_data_2)
            vol_ratio = StockComparator.vol_ratio_comp(stock_data_1, stock_data_2)
            stocks_corealtions["{} : {}".format(s_and_p_name_1, s_and_p_name_2)] = stocks_corr
            print("corelations: {} : {} - value: {} ".format(s_and_p_name_1, s_and_p_name_2, stocks_corr))
            print("volumens: {} : {} - value: {} ".format(s_and_p_name_1, s_and_p_name_2, vol_ratio))
analize(None, None)
