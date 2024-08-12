# Importing pickle to unpickle pkl file
#and importing streamlit to deploy our model 
import pickle
import streamlit as st
model1 = pickle.load(open(r"C:\Data science project\price.pkl",'rb'))

# Defining a function for deployment
def func():

    # Makin a heading for webiste
    st.header("Prediction of Flight Price")

    # Making selecttion box for our string input and input box for our integer input
    airline = st.selectbox("Name of airline: ",['AirAsia','Air India','Go First','Indigo','Spicejet','Vistara'])
    source_city = st.selectbox("Source City: ",['Bangalore','Chennai','Delhi', 'Hyderabad', 'Kolkata','Mumbai'])
    departure_time = st.selectbox("Time of departure: ",['Afternoon','Early Morning', 'Evening', 'Late Night','Morning', 'Night'])
    stops = st.number_input("Enter number of stops")
    arrival_time = st.selectbox("Time of arrival: ",['Afternoon','Early Morning', 'Evening', 'Late Night','Morning', 'Night'])
    destination = st.selectbox("Destination City: ",['Bangalore','Chennai','Delhi', 'Hyderabad', 'Kolkata','Mumbai'])
    clss = st.selectbox("Class: ",['Business','Economy'])
    duration = st.number_input("Enter time taken by flight")
    days = st.number_input("Enter number of days left")

    # Making a predict button
    pred = st.button("Predict")

    # If predict button is clicked than this ‘if’ statement will run
    #converting string type input to integer type
    if pred:
        time =  {'Afternoon': 0,'Early Morning': 1, 'Evening': 2, 'Late Night': 3,'Morning': 4, 'Night': 5}
        arrival_t = time[arrival_time]
        departure_t = time[departure_time]
        cities = {'Bangalore': 0,'Chennai': 1, 'Delhi': 2, 'Hyderabad': 3, 'Kolkata': 4,'Mumbai': 5}
        destination_c = cities[destination]
        source = cities[source_city]
        cl = {'Business': 0, 'Economy': 1}
        cls = cl[clss]
        aline = {'AirAsia': 0,'Air India': 1,'Go First': 2,'Indigo': 3,'Spicejet': 4,'Vistara': 5}
        airl = aline[airline]

        # Predicting and writing the price of flight
        st.write("price of your flight is: ", model1.predict([[airl,source,departure_t,stops,arrival_t,destination_c,cls,duration,days]])[0])
func()
