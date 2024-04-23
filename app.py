import streamlit as st
import pandas as pd
from data_preprocessing import data_preprocessing
from prediction import prediction

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://media.licdn.com/dms/image/C560BAQHB5IJW-49lKw/company-logo_200_200/0/1630650405272/dicodingacademy_logo?e=1721260800&v=beta&t=4jBskQnN1ftNFQvfIrDXMWV6F6NNyukjkAbHD4YyT0M", width=130)
with col2:
    st.header('Jaya Jaya Institute (Prototype)')

data = pd.DataFrame()
 
col1, col2 = st.columns(2)

marital_status_options = {
    1: 'Single',
    2: 'Married',
    3: 'Widower',
    4: 'Divorced',
    5: 'Facto Union',
    6: 'Legally Separated'
}
gender_options = {
    0: 'Female',
    1: 'Male'
}
application_mode_options = {
    1: '1st phase - general contingent',
    2: 'Ordinance No. 612/93',
    5: '1st phase - special contingent (Azores Island)',
    7: 'Holders of other higher courses',
    10: 'Ordinance No. 854-B/99',
    15: 'International student (bachelor)',
    16: '1st phase - special contingent (Madeira Island)',
    17: '2nd phase - general contingent',
    18: '3rd phase - general contingent',
    26: 'Ordinance No. 533-A/99, item b2) (Different Plan)',
    27: 'Ordinance No. 533-A/99, item b3 (Other Institution)',
    39: 'Over 23 years old',
    42: 'Transfer',
    43: 'Change of course',
    44: 'Technological specialization diploma holders',
    51: 'Change of institution/course',
    53: 'Short cycle diploma holders',
    57: 'Change of institution/course (International)'
}

course_options = {
    33: 'Biofuel Production Technologies',
    171: 'Animation and Multimedia Design',
    8014: 'Social Service (evening attendance)',
    9003: 'Agronomy',
    9070: 'Communication Design',
    9085: 'Veterinary Nursing',
    9119: 'Informatics Engineering',
    9130: 'Equinculture',
    9147: 'Management',
    9238: 'Social Service',
    9254: 'Tourism',
    9500: 'Nursing',
    9556: 'Oral Hygiene',
    9670: 'Advertising and Marketing Management',
    9773: 'Journalism and Communication',
    9853: 'Basic Education',
    9991: 'Management (evening attendance)'
}


with col1:
    Application_mode = st.selectbox(label='Application Mode', options=list(application_mode_options.values()))
    data["Application_mode"] = [key for key, value in application_mode_options.items() if value == Application_mode]
with col2:
    Course = st.selectbox(label='Course', options=list(course_options.values()), index=1)
    data["Course"] = [key for key, value in course_options.items() if value == Course]

col1, col2 = st.columns(2)
with col1:
    Gender = st.selectbox(label='Gender', options=list(gender_options.values()), index=1)
    data["Gender"] = [key for key, value in gender_options.items() if value == Gender]
with col2:
    Marital_status = st.selectbox(label='Marital Status', options=list(marital_status_options.values()), index=1)
    data["Marital_status"] = [key for key, value in marital_status_options.items() if value == Marital_status]

col1, col2 = st.columns(2)

Daytime_evening_attendance_options = {
    0: 'Evening',
    1: 'Daytime',
}

previous_qualification_options = {
    1: 'Secondary education',
    2: "Higher education - bachelor's degree",
    3: 'Higher education - degree',
    4: "Higher education - master's",
    5: 'Higher education - doctorate',
    6: 'Frequency of higher education',
    9: '12th year of schooling - not completed',
    10: '11th year of schooling - not completed',
    12: 'Other - 11th year of schooling',
    14: '10th year of schooling',
    15: '10th year of schooling - not completed',
    19: 'Basic education 3rd cycle (9th/10th/11th year) or equiv.',
    38: 'Basic education 2nd cycle (6th/7th/8th year) or equiv.',
    39: 'Technological specialization course',
    40: 'Higher education - degree (1st cycle)',
    42: 'Professional higher technical course',
    43: 'Higher education - master (2nd cycle)'
}

mothers_qualification_options = {
    1: 'Secondary Education - 12th Year of Schooling or Eq.',
    2: "Higher Education - Bachelor's Degree",
    3: 'Higher Education - Degree',
    4: "Higher Education - Master's",
    5: 'Higher Education - Doctorate',
    6: 'Frequency of Higher Education',
    9: '12th Year of Schooling - Not Completed',
    10: '11th Year of Schooling - Not Completed',
    11: '7th Year (Old)',
    12: 'Other - 11th Year of Schooling',
    14: '10th Year of Schooling',
    18: 'General commerce course',
    19: 'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.',
    22: 'Technical-professional course',
    26: '7th year of schooling',
    27: '2nd cycle of the general high school course',
    29: '9th Year of Schooling - Not Completed',
    30: '8th year of schooling',
    34: 'Unknown',
    35: "Can't read or write",
    36: 'Can read without having a 4th year of schooling',
    37: 'Basic education 1st cycle (4th/5th year) or equiv.',
    38: 'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.',
    39: 'Technological specialization course',
    40: 'Higher education - degree (1st cycle)',
    41: 'Specialized higher studies course',
    42: 'Professional higher technical course',
    43: 'Higher Education - Master (2nd cycle)',
    44: 'Higher Education - Doctorate (3rd cycle)'
}

mothers_occupations_options = {
    0: 'Student',
    1: 'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers',
    2: 'Specialists in Intellectual and Scientific Activities',
    3: 'Intermediate Level Technicians and Professions',
    4: 'Administrative staff',
    5: 'Personal Services, Security and Safety Workers and Sellers',
    6: 'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry',
    7: 'Skilled Workers in Industry, Construction and Craftsmen',
    8: 'Installation and Machine Operators and Assembly Workers',
    9: 'Unskilled Workers',
    10: 'Armed Forces Professions',
    90: 'Other Situation',
    99: '(blank)',
    122: 'Health professionals',
    123: 'Teachers',
    125: 'Specialists in information and communication technologies (ICT)',
    131: 'Intermediate level science and engineering technicians and professions',
    132: 'Technicians and professionals, of intermediate level of health',
    134: 'Intermediate level technicians from legal, social, sports, cultural and similar services',
    141: 'Office workers, secretaries in general and data processing operators',
    143: 'Data, accounting, statistical, financial services and registry-related operators',
    144: 'Other administrative support staff',
    151: 'Personal service workers',
    152: 'Sellers',
    153: 'Personal care workers and the like',
    171: 'Skilled construction workers and the like, except electricians',
    173: 'Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like',
    175: 'Workers in food processing, woodworking, clothing and other industries and crafts',
    191: 'Cleaning workers',
    192: 'Unskilled workers in agriculture, animal production, fisheries and forestry',
    193: 'Unskilled workers in extractive industry, construction, manufacturing and transport',
    194: 'Meal preparation assistants'
}

fathers_qualification_options = {
    1: 'Secondary Education - 12th Year of Schooling or Eq.',
    2: "Higher Education - Bachelor's Degree",
    3: 'Higher Education - Degree',
    4: "Higher Education - Master's",
    5: 'Higher Education - Doctorate',
    6: 'Frequency of Higher Education',
    9: '12th Year of Schooling - Not Completed',
    10: '11th Year of Schooling - Not Completed',
    11: '7th Year (Old)',
    12: 'Other - 11th Year of Schooling',
    13: '2nd year complementary high school course',
    14: '10th Year of Schooling',
    18: 'General commerce course',
    19: 'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.',
    20: 'Complementary High School Course',
    22: 'Technical-professional course',
    25: 'Complementary High School Course - not concluded',
    26: '7th year of schooling',
    27: '2nd cycle of the general high school course',
    29: '9th Year of Schooling - Not Completed',
    30: '8th year of schooling',
    31: 'General Course of Administration and Commerce',
    33: 'Supplementary Accounting and Administration',
    34: 'Unknown',
    35: "Can't read or write",
    36: 'Can read without having a 4th year of schooling',
    37: 'Basic education 1st cycle (4th/5th year) or equiv.',
    38: 'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.',
    39: 'Technological specialization course',
    40: 'Higher education - degree (1st cycle)',
    41: 'Specialized higher studies course',
    42: 'Professional higher technical course',
    43: 'Higher Education - Master (2nd cycle)',
    44: 'Higher Education - Doctorate (3rd cycle)'
}
fathers_occupations_options = {
    0: 'Student',
    1: 'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers',
    2: 'Specialists in Intellectual and Scientific Activities',
    3: 'Intermediate Level Technicians and Professions',
    4: 'Administrative staff',
    5: 'Personal Services, Security and Safety Workers and Sellers',
    6: 'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry',
    7: 'Skilled Workers in Industry, Construction and Craftsmen',
    8: 'Installation and Machine Operators and Assembly Workers',
    9: 'Unskilled Workers',
    10: 'Armed Forces Professions',
    90: 'Other Situation',
    99: '(blank)',
    101: 'Armed Forces Officers',
    102: 'Armed Forces Sergeants',
    103: 'Other Armed Forces personnel',
    112: 'Directors of administrative and commercial services',
    114: 'Hotel, catering, trade and other services directors',
    121: 'Specialists in the physical sciences, mathematics, engineering and related techniques',
    122: 'Health professionals',
    123: 'Teachers',
    124: 'Specialists in finance, accounting, administrative organization, public and commercial relations',
    131: 'Intermediate level science and engineering technicians and professions',
    132: 'Technicians and professionals, of intermediate level of health',
    134: 'Intermediate level technicians from legal, social, sports, cultural and similar services',
    135: 'Information and communication technology technicians',
    141: 'Office workers, secretaries in general and data processing operators',
    143: 'Data, accounting, statistical, financial services and registry-related operators',
    144: 'Other administrative support staff',
    151: 'Personal service workers',
    152: 'Sellers',
    153: 'Personal care workers and the like',
    154: 'Protection and security services personnel',
    161: 'Market-oriented farmers and skilled agricultural and animal production workers',
    163: 'Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence',
    171: 'Skilled construction workers and the like, except electricians',
    172: 'Skilled workers in metallurgy, metalworking and similar',
    174: 'Skilled workers in electricity and electronics',
    175: 'Workers in food processing, woodworking, clothing and other industries and crafts',
    181: 'Fixed plant and machine operators',
    182: 'Assembly workers',
    183: 'Vehicle drivers and mobile equipment operators',
    192: 'Unskilled workers in agriculture, animal production, fisheries and forestry',
    193: 'Unskilled workers in extractive industry, construction, manufacturing and transport',
    194: 'Meal preparation assistants',
    195: 'Street vendors (except food) and street service providers'
}

with col1:
    Daytime_evening_attendance = st.selectbox(label='Daytime Evening Attendance', options=list(Daytime_evening_attendance_options.values()), index=1)
    data["Daytime_evening_attendance"] = [key for key, value in Daytime_evening_attendance_options.items() if value == Daytime_evening_attendance]
with col2:
    Previous_qualification = st.selectbox(label='Previous Qualification', options=list(previous_qualification_options.values()), index=1)
    data["Previous_qualification"] = [key for key, value in previous_qualification_options.items() if value == Previous_qualification]

col1, col2 = st.columns(2)

with col1:
    Mothers_qualification = st.selectbox(label='Mothers Qualification', options=list(mothers_qualification_options.values()), index=1)
    data["Mothers_qualification"] = [key for key, value in mothers_qualification_options.items() if value == Mothers_qualification]
with col2:
    Mothers_occupation = st.selectbox(label='Mothers Occupation', options=list(mothers_occupations_options.values()), index=1)
    data["Mothers_occupation"] = [key for key, value in mothers_occupations_options.items() if value == Mothers_occupation]

col1, col2 = st.columns(2)
with col1:
    Fathers_qualification = st.selectbox(label='Fathers Qualification', options=list(fathers_qualification_options.values()), index=1)
    data["Fathers_qualification"] = [key for key, value in fathers_qualification_options.items() if value == Fathers_qualification]
with col2:
    Fathers_occupation = st.selectbox(label='Fathers Occupation', options=list(fathers_occupations_options.values()), index=1)
    data["Fathers_occupation"] = [key for key, value in fathers_occupations_options.items() if value == Fathers_occupation]

col1, col2, col3, col4 = st.columns([1,1,2,2])
with col1:
    selected_option = st.checkbox("Displaced", value=False)
    data["Displaced"] = 1 if selected_option else 0

with col2:
    selected_option = st.checkbox("Debtor", value=False)
    data["Debtor"] = 1 if selected_option else 0

with col3:
    selected_option = st.checkbox("Tuition Fees Up to Date", value=False)
    data["Tuition_fees_up_to_date"] = 1 if selected_option else 0

with col4:
    selected_option = st.checkbox("Scholarship Holder", value=False)
    data["Scholarship_holder"] = 1 if selected_option else 0
 
col1, col2, col3 = st.columns(3)
 
with col1:
    Age_at_enrollment = int(st.number_input(label='Age At Enrollment', value=18))
    data["Age_at_enrollment"] = Age_at_enrollment

with col2:
    Previous_qualification_grade = int(st.number_input(label='Prev. Qualification Grade', min_value=0, max_value=200, value=100))
    data["Previous_qualification_grade"] = Previous_qualification_grade 

with col3:
    Admission_grade = int(st.number_input(label='Admission Grade', min_value=0, max_value=200, value=100))
    data["Admission_grade"] = Admission_grade 

col1, col2, col3, col4 = st.columns(4)
 
with col1:
    Curricular_units_1st_sem_enrolled = int(st.number_input(label='Curricular units 1st sem (enrolled)', value=5))
    data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled

with col2:
    Curricular_units_1st_sem_evaluations = int(st.number_input(label='Curricular units 1st sem (evaluation)', value=5))
    data["Curricular_units_1st_sem_evaluations"] = Curricular_units_1st_sem_evaluations 

with col3:
    Curricular_units_1st_sem_approved = int(st.number_input(label='Curricular units 1st sem (approved)', value=5))
    data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved     

with col4:
    Curricular_units_1st_sem_grade = int(st.number_input(label='Curricular units 1st sem (grade)', value=10))
    data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade

col1, col2, col3, col4 = st.columns(4)
 
with col1:
    Curricular_units_2nd_sem_enrolled = int(st.number_input(label='Curricular units 2nd sem (enrolled)', value=5))
    data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled

with col2:
    Curricular_units_2nd_sem_evaluations = int(st.number_input(label='Curricular units 2nd sem (evaluation)', value=5))
    data["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations 

with col3:
    Curricular_units_2nd_sem_approved = int(st.number_input(label='Curricular units 2nd sem (approved)', value=5))
    data["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved     

with col4:
    Curricular_units_2nd_sem_grade = int(st.number_input(label='Curricular units 2nd sem (grade)', value=10))
    data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade

with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    predicted_class, probability = prediction(new_data)        
    st.write("Status: {}".format(predicted_class))     
    st.write("Probabilitas: {:.2f}%".format(probability * 100))         