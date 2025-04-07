import streamlit as st
st.title("Counter program")
count =0
increment = st.button('Click me ')
if increment:
    count += 1
'Count= ',count
# """
# No matter how many times we press the Increment button in the above app, the count remains at 1. Let's understand why:
#
# Each time we press the Increment button, Streamlit reruns counter.py from top to bottom, and with every run, count gets initialized to 0 .
# Pressing Increment subsequently adds 1 to 0, thus count=1 no matter how many times we press Increment.
# As we'll see later, we can avoid this issue by storing count as a Session State variable. By doing so, we're indicating to Streamlit that it should maintain the value stored inside a Session State variable across app reruns.
# """

# if 'count' not in st.session_state:
#     st.session_state['count'] = 0
#
# # Read
# # st.write(st.session_state['key'])
# # Update
# st.session_state['key'] += 1;

"Using the session_state "

if 'count' not in st.session_state:
    st.session_state['count'] = 0
if increment:
    st.session_state['count'] += 1

'Count= ', st.session_state['count']



# Example 2: Session State and Callbacks
# Now that we've built a basic Counter app using Session State, let's move on to something a little more complex. The next example uses Callbacks with Session State.
#
# Callbacks: A callback is a Python function which gets called when an input widget changes. Callbacks can be used with widgets using the parameters on_change (or on_click), args, and kwargs.