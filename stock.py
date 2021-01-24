import datetime 
import pandas_datareader.data as web 
import dash 
import dash_core_components as dcc     
import dash_html_components as html 
from dash.dependencies import Input, Output 

# UI 
app = dash.Dash() 
app.title = "Stock Visualisation"
app.layout = html.Div(children =[ 
    html.H1("Stock Visualisation App"), 
      
    html.H3("Please enter the stock name"), 
  
    dcc.Input(id ='input', value ='', type ='text'), 
  
    html.Div(id ='output-graph') 
]) 

def update_value(input_data): 
    # Reads stock prices from January 1st, 2010 
    start = datetime.datetime(2010, 1, 1)  
    end = datetime.datetime.now() 
  
    # Read stock data from yahoo's finance API from start to end  
    df = web.DataReader(input_data, 'yahoo', start, end) 
        
    return dcc.Graph(id ="example", 
        figure ={ 
            'data':[{'x':df.index, 'y':df.Close, 'type':'line', 'name':input_data}, 
            ], 
            'layout':{ 
                'title':input_data 
            } 
        } 
    ) 

if __name__ == '__main__': 
    app.run_server() 
