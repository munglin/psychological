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
    well_being_summary_t1 = {'Stress': 104, 
                          'Depression': 67, 
                          'Anxiety': 100,
                          'Bullying': 87,
                          'Lacking Peer Support': 90}

    well_being_summary_t1_p1 = {'Stress': 24, 
                          'Depression': 10, 
                          'Anxiety': 20,
                          'bullying': 26,
                          'Lacking Peer Support': 18}
    
    well_being_summary_t2 = {'Stress': 124, 
                          'Depression': 87, 
                          'Anxiety': 120,
                          'Bullying': 107,
                          'Lacking Peer Support': 110}
    
    well_being_summary_t2_p1 = {'Stress': 34, 
                          'Depression': 34, 
                          'Anxiety': 20,
                          'bullying': 26,
                          'Lacking Peer Support': 18}

    cohort, term = cs_sidebar(cohort_size)

    header()
    if term == 'Term 1 Start':
        if cohort == 'School-wide':
            body(well_being_summary_t1, sum(cohort_size), term)
        else:
            body(well_being_summary_t1_p1, cohort_size[1], term)
    else:
        if cohort == 'School-wide':
            body(well_being_summary_t2, sum(cohort_size), term)
        else:
            body(well_being_summary_t2_p1, cohort_size[1], term)    
    
    return None

# Sidebar Functions

def cs_sidebar(cohort_size):

    st.sidebar.markdown("## Dashboard View")
    # Selector
    st.sidebar.markdown('__Cohort Selection__')

    cohort = st.sidebar.selectbox('__Cohort (Size)__',
                                    ['School-wide', 
                                     'Primary 1',
                                     #'Primary 2 (' + str(cohort_size[1]) + ')',
                                     #'Primary 3 (' + str(cohort_size[2]) + ')',
                                     #'Primary 4 (' + str(cohort_size[3]) + ')',
                                     #'Primary 5 (' + str(cohort_size[4]) + ')',
                                     #'Primary 6 (' + str(cohort_size[5]) + ')',
                                     ])

    st.sidebar.markdown('__Term Selection__')

    term = st.sidebar.selectbox('__Term__',
                                    ['Term 1 Start', 
                                     'Term 2 End',
                                     #'Term 3 Start',
                                     #'Term 4 End'
                                     ])
    
    return cohort, term

##########################
# Main body of cheat sheet
##########################

def plot(label, num_total, num_condition):
    
    fig, ax1 = plt.subplots()
    sizes = [num_condition, num_total - num_condition]
    ax1.pie(sizes, explode= [0.2, 0], labels = ['Signs of ' + label, 'No signs of ' + label], autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    return fig

def header():
    st.title('Student Well-being Dashboard')
    st.subheader('Bishan Primary School')
    st.text('Note: Information here is based on sample information and not representative of realistic scenarios.')
    return None

def body(well_being_summary, cohort_size, term):
    # Title the app

    st.subheader('Number of students: ' + str(cohort_size))
    
    col1, col2 = st.columns([0.5,0.5])
    
    col1.subheader('Sentiment analysis of student mental health responses')
    col1.text('The machine learning model parses information from')
    col1.text(' check-in forms, and decides how students are feeling.')

    #cohort_size = cohort_size[0]
    
    
    for condition, num_condition in well_being_summary.items():
        fig1 = plot(condition, cohort_size, num_condition)
        col1.pyplot(fig1)
    
    col2.subheader('Analytics of Check-in Forms')
    col2.text('Displays analytics of student responses from forms.')

    if term == 'Term 1 Start':
        col2.text('How do you feel about the new school year?')
        chart_data = pd.DataFrame({'Bored': 56, 'Sad': 50, 'Excited': 40}, index = ['Students']).T
        col2.bar_chart(chart_data, horizontal = True)
        
        col2.text('What are you worried about?')
        chart_data_2 = pd.DataFrame({'Difficulty making friends': 56, 
                                   'Sad': 50}, index = ['Students']).T
        col2.bar_chart(chart_data_2, horizontal = True)
    
    else:
        col2.subheader('How do you feel about this previous term?')
        chart_data = pd.DataFrame({'Difficult': 104, 'Not enough friends': 100}, index = ['Students']).T
        col2.bar_chart(chart_data, horizontal = True)    
    
    return None

def body_t2(well_being_summary, cohort_size):
    # Title the app
    
    col1, col2 = st.columns([0.4,0.6])
    
    col1.subheader('Analysis of student well-being')
    col1.text('Analysis for each category is conducted')

    #cohort_size = cohort_size[0]
    
    
    for condition, num_condition in well_being_summary.items():
        fig1 = plot(condition, cohort_size, num_condition)
        col1.pyplot(fig1)
    
    col2.subheader('Student Responses')
    col2.text('How do you feel about the new school year?')
    chart_data = pd.DataFrame({'Bored': 56, 'Sad': 50, 'Excited': 40}, index = ['Students']).T
    col2.bar_chart(chart_data, horizontal = True)
    
    col2.text('What are you worried about?')
    chart_data_2 = pd.DataFrame({'Difficulty making friends': 56, 
                               'Sad': 50}, index = ['Students']).T
    col2.bar_chart(chart_data_2, horizontal = True)
    
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
# Disable widgets to remove interactivity:
>>> st.slider('Pick a number', 0, 100, disabled=True)
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