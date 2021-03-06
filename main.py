#AUTHORS: Fayez Mohammed & Rushabh Shah
#DATE: 7/16/22
#PURPOSE: Stock prediction and graphing

# open source framework that helps with GUI
import streamlit as st
# date api
import datetime as dt
# finance api
import yfinance as yf
# prediction api
from prophet import Prophet
# graph object trace api
from plotly import graph_objs as go
# plot api
from prophet.plot import plot_plotly

#Getting the last 10 years of historical data from the stock
TODAY = dt.datetime.now()
START = dt.datetime(TODAY.year - 10, TODAY.month, TODAY.day)

#Putting the title
st.title("Stockfest - Stock Prediction")

#Getting the stock from the user
stock_choice = st.text_input("Choose a stock")
st.write("The stock you chose is ", stock_choice)

#This function generates the plot graph for the stock's value in the past
def plot_generate_data():
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=data['Date'], y=data['Open'], name='opening_stock_value'))
    fig.add_trace(
        go.Scatter(x=data['Date'], y=data['Close'],
                   name='closing_stock_value'))
    fig.layout.update(title_text="History of Stock",
                      xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


#This saves the searches already made in cache to save memory
@st.cache
#This function gets the data for the stock from the yahoo api
def generate_data(stock):
    data = yf.download(stock, START, TODAY)
    data.reset_index(inplace=True)
    return data


data_loading = st.text("Loading....")
parsed = True
#only continues if there was input from the user
if stock_choice != "":
    # This calls the data for the stock the user chose
    data = generate_data(stock_choice)
    # This only loads once the data is called and formatted to be printed
    data_loading.text("....done!")

    st.subheader("Stock History")
    # This creates the table of values for thestock
    st.write(data.tail())
    # This creates a plot of values for the stock
    plot_generate_data()

    # Predictions
    # This is a slider for the user to choose the range they want to see their stock's prediction through
    t_days = st.slider("Days of prediction:", 1, 365)

    #initializes the prophet to be predicted
    model = Prophet()
    #resets the index of the table to be easier to handle
    data = data.reset_index()
    #adds in data columns with the names ds and y to allow the prophet to use the values for the prediction
    data[["ds", "y"]] = data[["Date", "Adj Close"]]
    #This code will only continue if the inputted stock was a valid stock inside the yahoo finance database
    try:
        prediction_loading = st.text("Loading....")
        model.fit(data)
        #Calculates the future values of the stock
        future = model.make_future_dataframe(periods=t_days)
        prediction = model.predict(future)
        model.plot(prediction)

        #plots the prediction
        st.write(prediction.tail())

        # The header for this section of the website
        st.write("Predicted Data")
        # This creates a plot graph for the predictions of the stock
        pred1 = plot_plotly(model, prediction)
        # This graphs the values
        st.plotly_chart(pred1)

        # This creates a vareity of graphs that represent dfferent types of predictions relative to the stock
        st.write("Prediction Components")
        # This graphs the values for those variety of predictions
        pred2 = model.plot_components(prediction)
        st.write(pred2)

        today_value = int(data['High'][2150])
        prediction_value = int(prediction['yhat_upper'][2150])
        difference = prediction_value - today_value
        percentage = round((difference / today_value) * 100, 1)
        st.write("The difference between the predicted value and today's value is " + str(difference))
        st.write("There is a percentage difference of " + str(percentage) + "%")
        #This only continues if the graphs and values are loaded and formatted for the user to view
        prediction_loading.text("....done!")
    except ValueError:
        #input was not inside the yahoo finance database
        st.write("INVALID INPUT!")

