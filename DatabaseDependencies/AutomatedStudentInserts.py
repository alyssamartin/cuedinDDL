import random
import names 
from faker import Faker
import string

def user_entity_insert (entity_username, entity_email, entity_type):

    user_entity_insert = " "

    user_entity_insert = "insert into userEntity (UserName, Email, EntityType)\n"
    user_entity_insert +="values ('" + entity_username + "', '" + entity_email + "', '"+ entity_type + "')"

    return user_entity_insert
def days_absent_generator (student_gpa):
    days_absent = 0 

    if student_gpa >= 3.5 and student_gpa <= 4.0:
        days_absent = random.randint(0,5)
    
    elif student_gpa < 3.0 and student_gpa >= 2.5:
        days_absent = random.randint(0,7)
    
    elif student_gpa < 2.5 and student_gpa >= 2.0:
        days_absent = random.randint(3,15)

    elif student_gpa < 2.0 and student_gpa >= 1.5:
        days_absent = random.randint(8,15)
    
    elif student_gpa < 1.5 and student_gpa >= 1.0:
        days_absent = random.randint(13,15)
    
    return days_absent

def hours_tracked_generator (student_grade_level, student_gpa):
    hours_tracked = 0

    if student_grade_level == "Freshmen":
        if student_gpa >= 3.5 and student_gpa <= 4.0:
            hours_tracked = random.randint(15,20)
        
        elif student_gpa < 3.0 and student_gpa >= 2.5:
            hours_tracked = random.randint(10,20)
        
        elif student_gpa < 2.5 and student_gpa >= 2.0:
            hours_tracked = random.randint(5,15)

        elif student_gpa < 2.0 and student_gpa >= 1.5:
            hours_tracked = random.randint(0,15)
        
        elif student_gpa < 1.5 and student_gpa >= 1.0:
            hours_tracked = random.randint(0,5)
    
    if student_grade_level == "Sophomore":
        if student_gpa >= 3.5 and student_gpa <= 4.0:
            hours_tracked = random.randint(20,25)
        
        elif student_gpa < 3.0 and student_gpa >= 2.5:
            hours_tracked = random.randint(15,25)
        
        elif student_gpa < 2.5 and student_gpa >= 2.0:
            hours_tracked = random.randint(10,20)

        elif student_gpa < 2.0 and student_gpa >= 1.5:
            hours_tracked = random.randint(5,10)
        
        elif student_gpa < 1.5 and student_gpa >= 1.0:
            hours_tracked = random.randint(0,10)

    if student_grade_level == "Junior":
        if student_gpa >= 3.5 and student_gpa <= 4.0:
            hours_tracked = random.randint(25,35)
        
        elif student_gpa < 3.0 and student_gpa >= 2.5:
            hours_tracked = random.randint(20,35)
        
        elif student_gpa < 2.5 and student_gpa >= 2.0:
            hours_tracked = random.randint(20,30)

        elif student_gpa < 2.0 and student_gpa >= 1.5:
            hours_tracked = random.randint(15,25)
        
        elif student_gpa < 1.5 and student_gpa >= 1.0:
            hours_tracked = random.randint(10,20)
    
    if student_grade_level == "Senior":
        if student_gpa >= 3.5 and student_gpa <= 4.0:
            hours_tracked = random.randint(35,45)
        
        elif student_gpa < 3.0 and student_gpa >= 2.5:
            hours_tracked = random.randint(30,45)
        
        elif student_gpa < 2.5 and student_gpa >= 2.0:
            hours_tracked = random.randint(25,40)

        elif student_gpa < 2.0 and student_gpa >= 1.5:
            hours_tracked = random.randint(20,35)
        
        elif student_gpa < 1.5 and student_gpa >= 1.0:
            hours_tracked = random.randint(15,30)

    return hours_tracked

def sat_scores_generator (student_gpa):
    sat_score = 0
    
      ### on a 1600 scale, ball parking stuff gauging
    if student_gpa >= 3.5 and student_gpa <= 4.0:
        sat_score = random.randint(1150,1600)
    
    elif student_gpa < 3.0 and student_gpa >= 2.5:
        sat_score = random.randint(900,1550)
    
    elif student_gpa < 2.5 and student_gpa >= 2.0:
        sat_score = random.randint(800,1400)

    elif student_gpa < 2.0 and student_gpa >= 1.5:
        sat_score = random.randint(700,1300)
    
    elif student_gpa < 1.5 and student_gpa >= 1.0:
        sat_score = random.randint(600,1250)

    return sat_score

###Generates act Scores
def act_scores_generator (student_gpa):
    
    act_score = 0

    if student_gpa >= 3.5 and student_gpa <= 4.0:
        act_score = random.randint(25,35)
    
    elif student_gpa < 3.0 and student_gpa >= 2.5:
        act_score = random.randint(20,35)
    
    elif student_gpa < 2.5 and student_gpa >= 2.0:
        act_score = random.randint(15,30)

    elif student_gpa < 2.0 and student_gpa >= 1.5:
        act_score = random.randint(15,25)
    
    elif student_gpa < 1.5 and student_gpa >= 1.0:
        act_score = random.randint(10,20)
    
    return act_score

def student_income_generator(student_income_flag):

    student_income = " "
    
    if student_income_flag >= 1 and student_income_flag < 30:
        student_income = "Lower Income"
    
    elif student_income_flag >= 30 and student_income_flag < 80:
        student_income = "Middle Income"

    elif student_income_flag >= 80 and student_income_flag <=100:
        student_income = "Higher Income"

    return student_income

def student_ethnicity_generator(student_ethnicity_flag):
    
    student_ethnicity = " "

    if student_ethnicity_flag >=1 and student_ethnicity_flag < 65:
        student_ethnicity = "Caucasian"
    
    elif student_ethnicity_flag >=65 and student_ethnicity_flag <75:
        student_ethnicity = "African American"
    
    elif student_ethnicity_flag >= 75 and student_ethnicity_flag < 85:
        student_ethnicity = "Hispanic"
    
    elif student_ethnicity_flag >= 85 and student_ethnicity_flag < 90:
        student_ethnicity = "Asian"
    
    elif student_ethnicity_flag >= 90 and student_ethnicity_flag < 95:
        student_ethnicity = "Pacific Islander"
    
    elif student_ethnicity_flag >= 95 and student_ethnicity_flag <= 100:
        student_ethnicity = "Not selected or Other"
    
    return student_ethnicity

fake = Faker()

### This is where organization, and job inserts are going to be
org_name_list = ["withSimplicity", "Kanis Bakery & Catering", "Arconic", "Green Hummingbird", "Jack Browns", "Walmart Supercenter"]
###primarykeys for opportunities 
org_description_list = ["All Natural, Organic Makeup and Skincare", "Mediterranean Restaurant", "Materials Sciences for Building Products", "Clothing Store'", "Hamburger Restaurant", "Department Store"]
# org_street_address_list[] fuck it do random address
org_city_list = ["Harrisonburg", "Elkton", "Staunton", "Bridgewater", "Edinburg", "Mineral"]
org_state = "VA"
org_primary_keys = list(range(1,len(org_name_list) + 1))

for i in range (len(org_primary_keys)):
    print(org_primary_keys[i])
    print(org_name_list[i])

for i in range(len(org_primary_keys)):
    # org_entity_insert = "insert into userEntity (UserName, EmailAddress, EntityType)\n"
    # org_entity_insert += " values ('" + org_name_list[i].replace(" ", "")+ str(random.randint(1,100)) + "', '" + org_name_list[i].replace(" ", "") + "@gmail.com, 'ORG')"

    org_entity_insert = user_entity_insert(org_name_list[i].replace(" ", "")+ str(random.randint(1,100)), org_name_list[i].replace(" ", "") + "@gmail.com", "ORG")



    org_insert = "insert into Organization (OrganizationEntityID, OrganizationName, OrganizationDescription, StreetAddress, Country, City, State, ZipCode)\n"
    org_insert += " values (" + str(org_primary_keys[i]) + ", '" + org_name_list[i] + "', '" + org_description_list[i] + "', '" + fake.street_address() + "', '"
    org_insert += "USA', '" + fake.city() + "', 'VA', " + fake.zipcode() + ")"

    print(org_entity_insert)
    print(org_insert)

    with open('generatedinserts.txt', 'a') as input_file:
        input_file.write(org_entity_insert + "\n")
        input_file.write(org_insert + "\n")


# zip is going to be random


#Inserts for UserEntity for School HardCoding this
#School Inserts should be hardcoded in a pristine way
#List of schools we are going to use 
#parallel array!
#parallell arrays for hs and their emails for UserEntity

###fake information generator 

school_list = ["Louisa County High School", "East Rockingham County High School", "Spotswood High School", "Turner Ashby High School", "Broadway High School" , "Harrisonburg High School"]
school_email_list = ["Louisa@Louisa.edu" , "erhsattendance@rockingham.k12.va.us", "SpotsWood@spotswood.edu" , "TurnerAshby@turnerAshby.edu", "Broadway@broadway.edu" ,"Harrisonburg@harrisonburg.edu"]
school_street_address_list = ["757 Davis Hwy", "250 Eagle Rock Road", "368 Blazer Drive","800 N Main St","269 Gobbler Drive", "1001 Garber Church Rd" ]
school_country = "United States"
school_city_list = ["Mineral", "Elkton", "Penn Laird", "Bridgewater", "Broadway", "Harrisonburg"]
school_state = "VA"
school_county_list = ["Louisa County", "Rockingham County", "Rockingham County", "Rockingham County", "Rockingham County", "Harrisonburg City Public Schools"]
school_zipcode_list = ["23117","22827","22846","22812","22815", "22801"]
school_primary_key_list = list(range(len(org_primary_keys) + 1, len(org_primary_keys) + len(school_list) + 1))

for i in range (0,len(school_primary_key_list)):
    print(school_primary_key_list[i])
    print(school_list[i])

#No password for these guys. just here for associations
#only the schoolemployees should have thier own passwords

for i in range (len(school_list)): 
    ###insert into user entity first then we can go into school
    school_entity_insert = "insert into userEntity (UserName, EmailAddress, EntityType)\n" 
    school_entity_insert += " values  ('"+ school_list[i].replace(" ","") +"', '"+school_email_list[i] + "'" + "SCHL" + "')"
  
    school_entity_insert = user_entity_insert(school_list[i].replace(" ","") + str(random.randint(1,100)), school_email_list[i], "SCHL")
    ###inserting into the school entity
    school_insert = "insert into school (schoolEntityID, schoolName, StreetAddress, Country, City, State, SchoolCounty, ZipCode)\n"
    school_insert += " values (" + str(school_primary_key_list[i])+ ", '" + school_list[i] + "','" + school_street_address_list[i] + "','"
    school_insert += school_country+ "','"+ school_city_list[i] + "','"+ school_state + "','" +  school_county_list[i] + "'," + school_zipcode_list[i] + ")"

    with open('generatedinserts.txt', 'a') as input_file:
        input_file.write(school_entity_insert + "\n")
        input_file.write(school_insert + "\n")

#Whatever the amount of userEntity ID's there are
#this is the amount of schools there are 
#amount_of_schools = userEntityID 

###Array of grade levels students can be
student_grade_level_list = ["Freshmen", "Sophomore", "Junior", "Senior"]

###Array of the student income levels
student_income_level_list = ["Low Income" ,"Middle Income", "High Income"]

###Array of Interest
interest_list = ["Agreculture, Food and Natural Resources","Business and Marketing", "Hospitality and Human Services", "Public Safety"]
interest_list.extend (["Architecture and Construction", "Education and Training", "Information Technology", "STEM"])
interest_list.extend(["Arts, A/V, Technology, and Communications", "Health Science", "Manufacturing", "Transportation"])
interest_list_id = list(range(1, 13))

### insert into list

for i in range (len(interest_list_id)):

    interest_group_insert = "insert into InterestGroups (InterestGroupName)\n"
    interest_group_insert += "values ('" + interest_list[i] + "')"

    with open('generatedinserts.txt', 'a') as input_file:
        input_file.write(interest_group_insert + "\n")





#Student Inserts 
amount_of_students = 5
studentID = len(org_primary_keys) + len(school_list) 
for i in range (amount_of_students):
    studentID = studentID + 1
    print(studentID)
    ###Determining Gender over here
    ###Determining names based off of genders
    ###kids will have boy or girl names. but 10% chance someone is a third party gender
    gender_flag = random.randint(0,1) 
    third_party_gender_flag = random.randint(1,100)

    ###0 means female 
    if gender_flag == 0:

        ##The if block that determines if they want to be a third gender (no choice, it's python's choice)
        if third_party_gender_flag <= 10:
            student_gender = "third party"
        else:
        ##Female
            student_gender = "female"
        student_first_name = names.get_first_name(gender='female')
        student_last_name = names.get_last_name()

    ###1 means male
    elif gender_flag == 1:

        ##The if block that determines if they want to be a third gender
        if third_party_gender_flag <= 10:
            student_gender = "third party"
        else:
            student_gender  = "male"

        student_first_name = names.get_first_name(gender='male')
        student_last_name = names.get_last_name()


    student_middle_initial = random.choice(string.ascii_uppercase)
    
    student_full_name = student_first_name + student_last_name
    ##Generate student username
    student_user_name = student_full_name + student_middle_initial + str(random.randint(0,1000))

    ###Generate student's school for email and further use...
    student_school_index = random.randint(0,len(school_list) -1)
    student_school = school_list[student_school_index]

    ###foreign key for student school. have to add 1 because
    student_school_id = school_primary_key_list[student_school_index]
    
    ##generate student emailAddress
    student_email_domain = school_email_list[student_school_index].split("@")[1]
    student_email = student_user_name + "@" + student_email_domain

    ###Generate student Address
    #disregard the red lines. took me 30 minutes to figure it dynamically goes away hahahahahahaha
    student_street_address = fake.street_address()
    student_city = fake.city()
    student_state = "VA"
    student_zip = fake.postcode_in_state(state_abbr="VA")

    ###dynamically assigns grade level
    student_grade_level = student_grade_level_list[random.randint(0,3)]

    ###Generate GPA, This is going to be a key metric for a lot of test scores, and absences.
    student_gpa = round(random.uniform(1.0,4.0), 2)

    if student_grade_level == "Senior" or student_grade_level == "Junior":
        ###generate student SAT scores
        student_sat = sat_scores_generator(student_gpa)

        take_act_flag = random.randint(1,100)
        
        if take_act_flag >=1 or take_act_flag <=75:
            ###generate student act scores
            student_act = act_scores_generator(student_gpa)
        
        else:
            #### do a nullif if it is 0
            student_act = 0
    
    else:
        student_sat = 0
        student_act = 0
        
    ##
    ##In terms of the system, I don't know if income is in our scope
    ##I'll add it anyways! just in case!


    ### Assigns student income level
    ### do we want to just do it randomly? 
    ### majority are going to be middle 50%
    ### lower going to be  30%
    ### higher going to be around 20%
    student_income_flag = random.randint(1,100)
    student_income_level = student_income_generator(student_income_flag)

    student_athlete_flag = random.randint (1,100)
    

    if student_athlete_flag >= 1 and student_athlete_flag <=62:
        student_athlete_status = "Y"
    
    else:
        student_athlete_status = "N"
        
    student_ethnicity_flag = random.randint(1,100) 
    student_ethnicity = student_ethnicity_generator(student_ethnicity_flag)


###Interest Group data
    ###Shuffle the list of interest groups
    random.shuffle(interest_list_id)

    ###initialize an empty list of potential primary keys
    student_interest_group_linkages = []

    ###random number of how many groups they wanna be apart of
    student_amount_of_interested = random.randint(1,8)

    for i in range (0,student_amount_of_interested):
        student_interest_group_linkages.append(interest_list_id[i])

    hours_tracked = hours_tracked_generator (student_grade_level,student_gpa)

    days_absent = days_absent_generator(student_gpa)
    
    student_dict = {
        
        "StudentEmailAddress": student_email,
        "StudentUserName": student_user_name,
        "StudentEntityID": studentID,
        "FirstName": student_first_name,
        "LastName": student_last_name,
        "MiddleInitial": student_middle_initial,
        "StreetAddress": student_street_address,
        "Country": "USA",
        "City": student_state, 
        "State": "VA",
        "ZipCode": student_zip,
        "StudentGradeLevel":student_grade_level,
        "StudentGPA": student_gpa,
        "StudentACTScore": student_act,
        "StudentSATScore": student_sat,
        "StudentEthnicity": student_ethnicity,
        "StudentGender": student_gender,
        "IncomeLevel": student_income_level,
        "DaysAbsent": days_absent,
        "HoursOfWorkPlaceExp": hours_tracked,
        "SchoolEntityID": student_school_id,
        "StudentInterest": student_interest_group_linkages

    }

    print(student_dict)

    ###student/user Entity Insert
    student_entity_insert = user_entity_insert(student_dict["StudentUserName"], student_dict["StudentEmailAddress"], "STUD")

    print(student_entity_insert)
    ###student Insert 

    # student_insert



        ####student Interest Group Insert
    

###student comments and org comment insert
###going to utilize a list of student ID's and all that stuff 
###all by chance

    

