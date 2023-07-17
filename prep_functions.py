import pandas as pd

def calculate_processing_time(df):
    df['ORDER_DATE'] = pd.to_datetime(df['ORDER_DATE'])
    df['SHIP_DATE'] = pd.to_datetime(df['SHIP_DATE'])
    df['PROCESSING_TIME'] = (df['SHIP_DATE'] - df['ORDER_DATE']).dt.days
    df['ORDER_DATE'] = df['ORDER_DATE'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df['SHIP_DATE'] = df['SHIP_DATE'].dt.strftime('%Y-%m-%d %H:%M:%S')
    return df

def categorize_processing_time(df):
    df['PROCESSING_TIME_CATEGORY'] = pd.cut(df['PROCESSING_TIME'], bins=[-1, 3, 7, 14, float('inf')], labels=['Fast', 'Moderate', 'Slow', 'Very Slow'])
    return df

def calculate_profit_margin(df):
    df['PROFIT_MARGIN'] = (df['PROFIT'] / df['SALES']) * 100
    return df

def calculate_unit_price_sale(df):
    df['UNIT_PRICE_SALE'] = df['SALES'] / df['QUANTITY']
    return df

def calculate_unit_profit(df):
    df['UNIT_PROFIT'] = df['PROFIT'] / df['QUANTITY']
    return df

def calculate_unit_cost(df):
    df['UNIT_COST'] = (df['SALES'] - df['PROFIT']) / df['QUANTITY']
    return df

def calculate_cost(df):
    df['COST'] = df['SALES'] - df['PROFIT']
    return df