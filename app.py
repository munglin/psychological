import streamlit as st
import base64
import matplotlib.pyplot as plt
import pandas as pd

# Initial page config

st.set_page_config(
     page_title='Termly check-in',
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
    'About': "# This is a prototype of termly-check in information."
})

def main():
    
    # Define the size of student cohorts
    cohort_size = [200, 287, 323, 245, 223, 243]
    well_being_summary = {'stress': 45, 
                          'depression': 15, 
                          'anxiety': 24,
                          'bullying': 34,
                          'support': 28}
    
    cs_sidebar(cohort_size)
    real_body(well_being_summary,cohort_size)
    cs_body(well_being_summary)

    return None

# Thanks to streamlitopedia for the following code snippet

# Sidebar Functions

def cs_sidebar(cohort_size):

    st.sidebar.markdown("## Dashboard View")
    # Selector
    st.sidebar.markdown('__Cohort Selection__')

    cohort = st.sidebar.selectbox('__Cohort (Size)__',
                                    ['School-wide (' + str(sum(cohort_size)) + ')', 
                                     'Primary 1 (' + str(cohort_size[0]) + ')',
                                     'Primary 2 (' + str(cohort_size[1]) + ')',
                                     'Primary 3 (' + str(cohort_size[2]) + ')',
                                     'Primary 4 (' + str(cohort_size[3]) + ')',
                                     'Primary 5 (' + str(cohort_size[4]) + ')',
                                     'Primary 6 (' + str(cohort_size[5]) + ')',
                                     ])

    st.sidebar.markdown('__Term Selection__')

    term = st.sidebar.selectbox('__Term__',
                                    ['Term 1 Start', 
                                     'Term 2 End',
                                     'Term 3 Start',
                                     'Term 4 End'])

    return None

##########################
# Main body of cheat sheet
##########################

def plot(label, num_total, num_condition):
    
    fig, ax1 = plt.subplots()
    sizes = [num_condition, num_total - num_condition]
    ax1.pie(sizes, explode= [0.2, 0], labels = [label, 'Not ' + label], autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    return fig


def real_body(well_being_summary, cohort_size):
    # Title the app
    st.title('Student Well-being Dashboard')
    st.subheader('Bishan Primary School')
    
    col1, col2 = st.columns([0.4,0.6])
    
    col1.subheader('Well-being displays')

    
    cohort_size = cohort_size[0]
    
    
    for condition, num_condition in well_being_summary.items():
        fig1 = plot(condition, cohort_size, num_condition)
        col1.pyplot(fig1)
    
    col1.code('''
st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r\'\'\' e^{i\pi} + 1 = 0 \'\'\')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True

    ''')
    
    col2.subheader('Display interactive widgets')
    col2.code('''
st.button('Hit me')
st.data_editor('Edit data', data)
st.checkbox('Check me out')
st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.download_button('On the dl', data)
st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')
    ''')

    
    return None

def cs_body(well_being_summary):

    st.title('Gravitational Wave Quickview')
        
    col1, col2 = st.columns([0.4,0.6])

    col1.subheader(str(sum(well_being_summary.values())))

    #######################################
    # COLUMN 1
    #######################################
    
    # Display text

    col1.subheader('Display text')
    col1.code('''
st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r\'\'\' e^{i\pi} + 1 = 0 \'\'\')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True

    ''')

    # Display data

    col1.subheader('Display data')
    col1.code('''
st.dataframe(my_dataframe)
st.table(data.iloc[0:10])
st.json({'foo':'bar','fu':'ba'})
st.metric(label="Temp", value="273 K", delta="1.2 K")
    ''')


    # Display media

    col1.subheader('Display media')
    col1.code('''
st.image('./header.png')
st.audio(data)
st.video(data)
    ''')

    # Columns

    col1.subheader('Columns')
    col1.code('''
col1, col2 = st.columns(2)
col1.write('Column 1')
col2.write('Column 2')

# Three columns with different widths
col1, col2, col3 = st.columns([3,1,1])
# col1 is wider
              
# Using 'with' notation:
>>> with col1:
>>>     st.write('This is column 1')
              
''')

    # Tabs
    
    col1.subheader('Tabs')
    col1.code('''
# Insert containers separated into tabs:
>>> tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
>>> tab1.write("this is tab 1")
>>> tab2.write("this is tab 2")

# You can also use "with" notation:
>>> with tab1:
>>>   st.radio('Select one:', [1, 2])
''')

    # Control flow

    col1.subheader('Control flow')
    col1.code('''
# Stop execution immediately:
st.stop()
# Rerun script immediately:
st.experimental_rerun()

# Group multiple widgets:
>>> with st.form(key='my_form'):
>>>   username = st.text_input('Username')
>>>   password = st.text_input('Password')
>>>   st.form_submit_button('Login')
''')
    
    # Personalize apps for users

    col1.subheader('Personalize apps for users')
    col1.code('''
# Show different content based on the user's email address.
>>> if st.user.email == 'jane@email.com':
>>>    display_jane_content()
>>> elif st.user.email == 'adam@foocorp.io':
>>>    display_adam_content()
>>> else:
>>>    st.write("Please contact us to get access!")
''')


    #######################################
    # COLUMN 2
    #######################################

    # Display interactive widgets

    col2.subheader('Display interactive widgets')
    col2.code('''
st.button('Hit me')
st.data_editor('Edit data', data)
st.checkbox('Check me out')
st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.download_button('On the dl', data)
st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')
    ''')

    col2.code('''
# Use widgets\' returned values in variables
>>> for i in range(int(st.number_input('Num:'))): foo()
>>> if st.sidebar.selectbox('I:',['f']) == 'f': b()
>>> my_slider_val = st.slider('Quinn Mallory', 1, 88)
>>> st.write(slider_val)
    ''')
    col2.code('''
# Disable widgets to remove interactivity:
>>> st.slider('Pick a number', 0, 100, disabled=True)
              ''')

    # Build chat-based apps

    col2.subheader('Build chat-based apps')
    col2.code('''
# Insert a chat message container.
>>> with st.chat_message("user"):
>>>    st.write("Hello 👋")
>>>    st.line_chart(np.random.randn(30, 3))

# Display a chat input widget.
>>> st.chat_input("Say something")          
''')

    col2.markdown('<small>Learn how to [build chat-based apps](https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps)</small>', unsafe_allow_html=True)

    # Mutate data

    col2.subheader('Mutate data')
    col2.code('''
# Add rows to a dataframe after
# showing it.
>>> element = st.dataframe(df1)
>>> element.add_rows(df2)

# Add rows to a chart after
# showing it.
>>> element = st.line_chart(df1)
>>> element.add_rows(df2)
''')

    # Display code

    col2.subheader('Display code')
    col2.code('''
st.echo()
>>> with st.echo():
>>>     st.write('Code will be executed and printed')
    ''')

    # Placeholders, help, and options

    col2.subheader('Placeholders, help, and options')
    col2.code('''
# Replace any single element.
>>> element = st.empty()
>>> element.line_chart(...)
>>> element.text_input(...)  # Replaces previous.

# Insert out of order.
>>> elements = st.container()
>>> elements.line_chart(...)
>>> st.write("Hello")
>>> elements.text_input(...)  # Appears above "Hello".

st.help(pandas.DataFrame)
st.get_option(key)
st.set_option(key, value)
st.set_page_config(layout='wide')
st.experimental_show(objects)
st.experimental_get_query_params()
st.experimental_set_query_params(**params)
    ''')

  


    return None

# Run main()

if __name__ == '__main__':
    main()