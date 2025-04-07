import streamlit as st
st.title("counter program using callback ")
if 'count' not in st.session_state:
    st.session_state['count'] =0

def increment():
    st.session_state.count +=1

button = st.button("click me",on_click=increment())

"Count = ",st.session_state.count


# # Example 3:"Use args and kwargs in Callbacks"
# # Callbacks also support passing arguments using the args parameter in a widget:
# st.title('Counter Example using Callbacks with args')
# if 'counter' not in st.session_state:
#     st.session_state.counter = 0
#
# increment_value = st.number_input('Enter a value', value=0, step=10)
#
# def increment_counter(increment_value):
#     st.session_state.counter += increment_value
#
# increment = st.button('Increment', on_click=increment_counter,
#     args=(increment_value, ))
#
# st.write('Count = ', st.session_state.count)





#
# Session State and Widget State association
# Session State provides the functionality to store variables across reruns. Widget state (i.e. the value of a widget) is also stored in a session.
#
# For simplicity, we have unified this information in one place. i.e. the Session State. This convenience feature makes it super easy to read or write to the widget's state anywhere in the app's code. Session State variables mirror the widget value using the key argument.
#
# We illustrate this with the following example. Let's say we have an app with a slider to represent temperature in Celsius. We can set and get the value of the temperature widget by using the Session State API, as follows:

if 'cel' not in st.session_state:
    st.session_state['cel'] =50.0

def change():
    print("changes has been done")

st.slider(label= "Temperature in Celsius",
          min_value=0.0,
          max_value=100.0,
          key='cel',
          on_change=change())

st.write(st.session_state.cel)