import random
from random import randrange
import names 
from faker import Faker
import string
from datetime import datetime
from datetime import timedelta
import datetime

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """

    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def user_entity_insert (entity_username, entity_email, entity_type,twitter_handle,twitter_link):

    user_entity_insert = " "

    user_entity_insert = "insert into userEntity (UserName, EmailAddress, EntityType, TwitterHandle, TwitterLink, LastUpdated)\n"
    user_entity_insert +="values ('" + entity_username + "', '" + entity_email + "', '"+ entity_type +"'," + "Nullif('"+twitter_handle +"', ' '), " + "Nullif('"+ twitter_link + "',' '), GETDATE());"

    return user_entity_insert
def days_absent_generator (student_gpa):
    days_absent = 0 

    if student_gpa >= 3.5 and student_gpa <= 4.0:
        days_absent = random.randint(0,5)
    
    elif student_gpa < 3.5 and student_gpa >= 3.0:
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

        elif student_gpa < 3.5 and student_gpa >= 3.0:
            hours_tracked = random.randint(13,20)
            
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
        
        elif student_gpa < 3.5 and student_gpa >= 3.0:
            hours_tracked = random.randint(18,25)
        
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
        
        elif student_gpa < 3.5 and student_gpa >= 3.0:
            hours_tracked = random.randint(23,35)

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
        
        elif student_gpa < 3.5 and student_gpa >= 3.0:
            hours_tracked = random.randint(32,45)
        
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
    
    elif student_gpa < 3.5 and student_gpa >= 3.0:
        sat_score = random.randint(1100,1550)

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

    elif student_gpa < 3.5 and student_gpa >= 3.0:
        act_score = random.randint(23,35)
    
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
org_name_list = ["withSimplicity", "Kanis Bakery & Catering", "Arconic", "Green Hummingbird", "Jack Browns", "Walmart Supercenter", "Food Lion", "Merck", "Jenzabar", "Health and Rehabilitation Center", "ConvergentAI"]
###primarykeys for opportunities 
org_description_list = ["All Natural, Organic Makeup and Skincare", "Mediterranean Restaurant", "Materials Sciences for Building Products", "Clothing Store", "Hamburger Restaurant", "Department Store", "Grocery Store", "Pharmaceuticals", "Software Development", "Rehabilitation Center", "Software Company"]
org_street_address_list = ["108 South Main Street","182 Neff Avenue","2031 Dyerle Ave", "320 South Main Street", "80 South Main Street", "171 Burgess Road", "1021 Port Republic Rd", "2778 SE Side Hwy", "181 S Liberty St","1225 Reservoir St", "2 S Main St #501"]
org_state = "VA"
org_zip_code_list = ["22801", "22801", "22801", "22801", "22801", "22801", "22801", "22827","22801","22801","22802"] 
org_city_list = ["Harrisonburg","Harrisonburg","Harrisonburg","Harrisonburg", "Harrisonburg", "Harrisonburg", "Harrisonburg", "Elkton", "Harrisonburg", "Harrisonburg", "Harrisonburg"] 
org_image_list = ["img/withSimplicity.jpg", "img/kanis.jpg", "img/arconic.jpg","img/greenhummingbird.jpg", "img/jackbrowns.jpg", "img/walmart.jpg", "img/foodlion.jpg", "img/merck.jpg", "img/jenzabar.jpg", "img/healthandrehab.jpg", "img/convergentAI.jpg"]
org_url_list = ["https://www.withsimplicityllc.com", "https://www.kandiscakesandbakeshop.com/", "https://www.arconic.com/global/en/home.asp","http://www.greenhummingbird.net/","https://www.jackbrownsjoint.com/", "https://www.walmart.com/","https://foodlion.com", "https://www.merck.com", "https://jenzabar.com", "https://www.mfa.net/center/harrisonburg-health-rehabilitation-center", "http://convergentai.com/"]
org_twitter_handle = [" ", " ", "Arconicexeter", " ", "JackBrownsJoint","Walmart", "FoodLionNews", "Merck", " ", " ","ConvergentAI"]
org_twitter_link = [" ", " ", "https://twitter.com/Arconicexeter?ref_src=twsrc%5Etfw"," ", "https://twitter.com/JackBrownsJoint?ref_src=twsrc%5Etfw", "https://twitter.com/Walmart?ref_src=twsrc%5Etfw","https://twitter.com/FoodLionNews?ref_src=twsrc%5Etfw","https://twitter.com/Merck?ref_src=twsrc%5Etfw"," "," ","https://twitter.com/ConvergentAI?ref_src=twsrc%5Etfw"]

org_primary_keys = list(range(1,len(org_name_list) + 1))



for i in range(len(org_primary_keys)):
    org_entity_insert = user_entity_insert(org_name_list[i].replace(" ", "")+ str(random.randint(1,100)), org_name_list[i].replace(" ", "") + "@gmail.com", "ORG",org_twitter_handle[i], org_twitter_link[i])
    print(org_entity_insert)


    org_insert = "insert into Organization (OrganizationEntityID, OrganizationName, OrganizationDescription, StreetAddress, Country, City, State, ZipCode, Image, ExternalLink, LastUpdated)\n"
    org_insert += " values (" + str(org_primary_keys[i]) + ", '" + org_name_list[i] + "', '" + org_description_list[i] + "', '" + org_street_address_list[i] + "', '"
    org_insert += "USA', '" + org_city_list[i]+ "', 'VA', " + str(org_zip_code_list[i]) + ",'"+org_image_list[i] +"','"+org_url_list[i]+"',GETDATE());"

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


school_list = ["Louisa County High School", "East Rockingham County High School", "Spotswood High School", "Turner Ashby High School", "Broadway High School" , "Harrisonburg High School"]
school_email_list = ["Louisa@Louisa.edu" , "erhsattendance@rockingham.k12.va.us", "SpotsWood@spotswood.edu" , "TurnerAshby@turnerAshby.edu", "Broadway@broadway.edu" ,"Harrisonburg@harrisonburg.edu"]
school_street_address_list = ["757 Davis Hwy", "250 Eagle Rock Road", "368 Blazer Drive","800 N Main St","269 Gobbler Drive", "1001 Garber Church Rd" ]
school_country = "United States"
school_city_list = ["Mineral", "Elkton", "Penn Laird", "Bridgewater", "Broadway", "Harrisonburg"]
school_state = "VA"
school_county_list = ["Louisa County", "Rockingham County", "Rockingham County", "Rockingham County", "Rockingham County", "Harrisonburg City Public Schools"]
school_zipcode_list = ["23117","22827","22846","22812","22815", "22801"]
school_twitter_handle =  ["LouisaCountyVA","ERHS_PTSA","SHSChargers","TA_FCA"," ","hhsmedianow"]
school_twitter_link = ["https://twitter.com/LouisaCountyVA?ref_src=twsrc%5Etfw","https://twitter.com/ERHS_PTSA?ref_src=twsrc%5Etfw","https://twitter.com/SHSChargers?ref_src=twsrc%5Etfw","https://twitter.com/TA_FCA?ref_src=twsrc%5Etfw", " ", "https://twitter.com/hhsmedianow?ref_src=twsrc%5Etfw"]
school_primary_key_list = list(range(len(org_primary_keys) + 1, len(org_primary_keys) + len(school_list) + 1))


for i in range (0,len(school_primary_key_list)):
    print(school_primary_key_list[i])
    print(school_list[i])

#No password for these guys. just here for associations
#only the schoolemployees should have thier own passwords

for i in range (len(school_list)): 
    ###insert into user entity first then we can go into school
    
    school_entity_insert = user_entity_insert(school_list[i].replace(" ","") + str(random.randint(1,100)), school_email_list[i], "SCHL",school_twitter_handle[i],school_twitter_link[i])
    ###inserting into the school entity
    school_insert = "insert into school (schoolEntityID, schoolName, StreetAddress, Country, City, State, SchoolCounty, ZipCode, LastUpdated)\n"
    school_insert += " values (" + str(school_primary_key_list[i])+ ", '" + school_list[i] + "','" + school_street_address_list[i] + "','"
    school_insert += school_country+ "','"+ school_city_list[i] + "','"+ school_state + "','" +  school_county_list[i] + "'," + school_zipcode_list[i] + ",GETDATE());"

    with open('generatedinserts.txt', 'a') as input_file:
        input_file.write(school_entity_insert + "\n")
        input_file.write(school_insert + "\n")


###Paralell Array of Interest Groups
interest_list = ["Agriculture, Food and Natural Resources","Business and Marketing", "Hospitality and Human Services", "Public Safety"]
interest_list.extend (["Architecture and Construction", "Education and Training", "Information Technology", "STEM"])
interest_list.extend(["Arts, A/V, Technology, and Communications", "Health Science", "Manufacturing", "Transportation"])
###Generate the primary keys for these guys
interest_list_id = list(range(1, 13))

###Interest Group Inserts 
for i in range (len(interest_list_id)):

    interest_group_insert = "insert into InterestGroups (InterestGroupName)\n"
    interest_group_insert += "values ('" + interest_list[i] + "');"

    with open('generatedinserts.txt', 'a') as input_file:
        input_file.write(interest_group_insert + "\n")



###Student Grade Level Generation
###Array of grade levels students can be
student_grade_level_list = ["Freshmen", "Sophomore", "Junior", "Senior"]

###Array of the student income levels
student_income_level_list = ["Low Income" ,"Middle Income", "High Income"]

###Store all primary keys of students in here for later usage (comments and log hours).
student_id_list = [] 


###Student Inserts 
###Amount of students we want to have
amount_of_students = 2263

studentID = len(org_primary_keys) + len(school_list) 
for i in range (amount_of_students):
    studentID = studentID + 1
    student_id_list.append(studentID)

    print(studentID)
    ###Determining Gender over here
    ###Determining names based off of genders
    ###kids will have boy or girl names. but 10% chance someone is an other gender
    gender_flag = random.randint(0,1) 
    third_party_gender_flag = random.randint(1,100)

    ###0 means female 
    if gender_flag == 0:

        ##The if block that determines if they want to be an other gender 
        if third_party_gender_flag <= 10:
            student_gender = "Other"
        else:
        ##Female
            student_gender = "Female"
        student_first_name = names.get_first_name(gender='female')
        student_last_name = names.get_last_name()

    ###1 means male
    elif gender_flag == 1:

        ##The if block that determines if they want to be an other gender
        if third_party_gender_flag <= 10:
            student_gender = "Other"
        else:
        ###Male
            student_gender  = "Male"

        student_first_name = names.get_first_name(gender='male')
        student_last_name = names.get_last_name()

    ###Get middle initial here
    student_middle_initial = random.choice(string.ascii_uppercase)
    
    ###full name for testing and debugging purposes
    student_full_name = student_first_name + student_last_name

    ###Generate student username
    student_user_name = student_full_name + student_middle_initial + str(random.randint(0,1000))

    ###Generate student's school for email and further use...
    student_school_index = random.randint(0,len(school_list) -1)
    student_school = school_list[student_school_index]

    ###Foreign key for student school
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
    student_gpa = float(random.randrange(100, 400))/100

    ###Only Upper Level Classmen take the SAT.
    if student_grade_level == "Senior" or student_grade_level == "Junior":

        ###Generate student SAT scores
        student_sat = sat_scores_generator(student_gpa)

        ###not all but some students take the ACT 
        take_act_flag = random.randint(1,100)
        
        if take_act_flag >=1 or take_act_flag <=75:
            ###Generate student act scores
            student_act = act_scores_generator(student_gpa)
        
        else:
           
            student_act = 0
    
    else:
        student_sat = 0
        student_act = 0
        
    ### Assigns student income level
    ### majority are going to be middle 50%
    ### lower going to be  30%
    ### higher going to be around 20%
    student_income_flag = random.randint(1,100)
    student_income_level = student_income_generator(student_income_flag)

    student_athlete_flag = random.randint (1,100)

    ###62% of students are usually student athletes. 
    if student_athlete_flag >= 1 and student_athlete_flag <=62:
        student_athlete_status = "Y"
    
    ###Not a Student Athlete
    else:
        student_athlete_status = "N"
    
    ###Etnicity generator. 
    student_ethnicity_flag = random.randint(1,100) 
    student_ethnicity = student_ethnicity_generator(student_ethnicity_flag)


    ###Interest Group data
    ###Shuffle the list of interest groups
    random.shuffle(interest_list_id)

    ###initialize an empty list of potential primary keys
    student_interest_group_linkages = []

    ###random number of how many groups they wanna be apart of
    student_amount_of_interested = random.randint(1,8)

    ###Students can have 1-8 interest, and they are randomly generated. 
    for i in range (0,student_amount_of_interested):
        student_interest_group_linkages.append(interest_list_id[i])

    ###Hours of work based learning is based on their GPA, and grade level
    hours_tracked = hours_tracked_generator (student_grade_level,student_gpa)

    ###Just based on GPA
    days_absent = days_absent_generator(student_gpa)

    ###Randomly picked if students are currently employed or not.
    student_employment_flag = random.randint(1,100)
    student_employment = " "

    ###40% chance that students are employed 
    if student_employment_flag <=40:
        student_employment = "Y"
    else:
        student_employment = "N"
    

    ###Initialize a graduation track var
    student_graduation_track = " "

    ###if student has below a 2.00 assume they are not on track.
    if student_gpa <2.00:
        student_graduation_track = "N"
    else:
        student_graduation_track = "Y"


    ###Student ELL and First Generation Students

    ###Student ELL
    student_ell_flag = random.randint(1,100)
    student_ell_status = " "

    if student_ell_flag <= 80:
        student_ell_status = "N"
    else:
        student_ell_status = "Y"
    
    ###Student First Generation Students
    student_first_gen_flag = random.randint (1,100)
    student_first_gen_status = " "

    if student_first_gen_flag <= 75:
        student_first_gen_status = "N"
    else:
        student_first_gen_status = "Y"


    
    ###putting data into a dictionary for organization and ease of use.
    student_dict = {
        "StudentEmailAddress": student_email,
        "StudentUserName": student_user_name,
        "StudentEntityID": studentID,
        "FirstName": student_first_name,
        "LastName": student_last_name,
        "MiddleInitial": student_middle_initial,
        "StreetAddress": student_street_address,
        "Country": "USA",
        "City": student_city, 
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
        "StudentAthleteFlag": student_athlete_status,
        "StudentGraduationTrack": student_graduation_track,
        "StudentEmploymentFlag": student_employment,
        "SchoolEntityID": student_school_id,
        "StudentImage" : "img/student.jpg",
        "StudentInterest": student_interest_group_linkages,
        "StudentELLStatus": student_ell_status,
        "StudentFirstGeneration": student_first_gen_status

    }

    print(student_dict)


    ###student/user Entity Insert
    student_entity_insert = user_entity_insert(student_dict["StudentUserName"], student_dict["StudentEmailAddress"], "STUD", " ", " ")

    ###insert the string into a textfile
    with open('generatedinserts.txt', 'a') as input_file:
        input_file.write(student_entity_insert + "\n")

    ###student Insert 
    student_insert = "insert into student (StudentEntityID, FirstName, LastName, MiddleInitial, StreetAddress, Country,City, State,"
    student_insert += "ZipCode, StudentGradeLevel, StudentGPA, StudentACTScore, StudentSATScore, StudentEthnicity, StudentGender,"
    student_insert += " IncomeLevel, DaysAbsent, HoursOfWorkPlaceExp, StudentAthleteFlag, StudentGraduationTrack, StudentEmploymentFlag, StudentImage,SchoolEntityID, LastUpdated, StudentELLStatus, StudentFirstGenerationCollege)\n"
    student_insert += "values (" + str(student_dict["StudentEntityID"]) + ", '" + student_dict["FirstName"] + "', '"
    student_insert += student_dict["LastName"] +"', '" + student_dict["MiddleInitial"] + "', '" + student_dict["StreetAddress"] + "', '"
    student_insert += student_dict["Country"] + "','" + student_dict["City"] + "','" + student_dict["State"] + "','" + student_dict["ZipCode"] + "','"
    student_insert += student_dict["StudentGradeLevel"] +"', " + str(student_dict["StudentGPA"]) + ", " + str(student_dict["StudentACTScore"]) + ", " + str(student_dict["StudentSATScore"]) + ",'"
    student_insert += student_dict["StudentEthnicity"] +"','" + student_dict["StudentGender"] + "','" + student_dict["IncomeLevel"] +  "'," + str(student_dict["DaysAbsent"]) + ","
    student_insert += str(student_dict["HoursOfWorkPlaceExp"]) +", '" + student_dict["StudentAthleteFlag"] +"', '"+ student_dict["StudentGraduationTrack"] + "', '" + student_dict["StudentEmploymentFlag"]+"', '"
    student_insert += student_dict["StudentImage"]+ "', " +str(student_dict["SchoolEntityID"]) + ", GETDATE(), '" + student_dict["StudentELLStatus"] + "', '" + student_dict["StudentFirstGeneration"] + "');"



    with open('generatedinserts.txt', 'a') as input_file:
        input_file.write(student_insert + "\n")


    ####student Interest Group Insert
    for i in range (len(student_interest_group_linkages)):
        
        student_interest_insert = "insert into StudentInterestGroups (InterestGroupID, StudentEntityID, LastUpdated)\n"
        student_interest_insert +="values (" + str(student_interest_group_linkages[i]) + "," + str(student_dict["StudentEntityID"]) + ",GETDATE());"

        with open('generatedinserts.txt', 'a') as input_file:
            input_file.write(student_interest_insert + "\n")
        




##### Opportunity Inserts start here #####
def opporunitiy_entity_insert (opp_type):

    opportunity_insert = "insert into OpportunityEntity (OpportunityType,LastUpdated) values ('"+ opp_type+ "',GETDATE())"

    return opportunity_insert

###Static array of organization ID's, and JobListings, must be in this specific order to 
###Have logically sound Opportunities. 
OrganizationID = ["8","4","2","1","7","3","7","7","8","8","8","1","2","3","4","5","6"]
job_listing_id_list = list(range(1,18))

opportunity_id_list = list(range(1,26))


###Seperate file of Opportunity Inserts, going to append this data to the textfile
###Do this so users can just copy and paste one text file into SQL server. 
with open('OpportunityInserts.txt', 'r') as inserts:
    with open('generatedinserts.txt', 'a') as generator:
        for line in inserts:
            generator.write(line)

###Array of possible student comments
student_comments = ["This was a great work experience, it fit with my goals!"]
student_comments.append("I had a great time working with this organization")
student_comments.append("I had a good time with this organization")
student_comments.append("I wish this organization gave me more work so I could learn and do more")
student_comments.append("This was an ok experience. I have done better")
student_comments.append("I did not have a good time with this organization, it was all busy work...")

###Array of possible Organization Comments
organization_comments = ["This student was extraordinary! This student is always welcome back here"]
organization_comments.append("Great student, and they definitely fit in with this organization!")
organization_comments.append("Exemplar student! We need more people like this student")
organization_comments.append("This particular student was on their phone too long.")
organization_comments.append("Average student, did the necessary requirements to complete this task")
organization_comments.append("Good student, and a very quick learner! I can see the potential from this student!")

###Array of "Hours Logged Req"
hours_requested_hours = list(range(1,6))

###list of primary keys from organizations
###Log ID is incremented by 1 everytime it is inserted.
logID = 0
for i in range (0,amount_of_students,5):
    ##studentID of I will be requesting log hours

    ###log id for comment tables
    logID += 1

    ###comments are randomly picked from the array. 
    index = random.randint(0,len(job_listing_id_list) -1) 
    job_id_loghrs = job_listing_id_list[index]

    ###picks student ID's from their PK list, depends on the step of the For loop. 
    student_id_loghrs = student_id_list[i]
    req_hours = hours_requested_hours[random.randint(0,len(hours_requested_hours)-1) ]

    ###orgCommentTable
    student_comment = student_comments[random.randint(0,len(student_comments) -1)]

    ###Org comment table
    organization_comment = organization_comments[random.randint(0,len(organization_comments) -1) ]


    ###Dictionary for organization Purposes. Log Hour inserts get messy
    ### so consolidating these data fields into a dictionary is crucial
    log_dict = {
        "LogID" : logID,
        "JobListingID": job_id_loghrs,
        "StudentEntityID": student_id_loghrs,
        "HoursRequested": req_hours,
        "OrganizationComment": organization_comment,
        "StudentComment": student_comment,
        "OrganizationEntityID": OrganizationID[index]
    }


    ###Log hours insert
    d1 = datetime.datetime.strptime('1/1/2019', '%m/%d/%Y')
    d2 = datetime.datetime.strptime('4/28/2019', '%m/%d/%Y')


    randomDate = random_date(d1, d2)

    log_hours_insert = "insert into LogHours (JobListingID, StudentEntityID, HoursRequested, CounselorApproval, OrganizationApproval, RequestedDate, OrganizationComment, StudentComment, LastUpdated)\n"
    log_hours_insert += "values(" + str(log_dict["JobListingID"]) + ", " + str(log_dict["StudentEntityID"]) + ", " + str(log_dict["HoursRequested"]) + ", "
    log_hours_insert += "'P', 'Y', '"+str(randomDate)+"' " + " '" + log_dict["OrganizationComment"] + "', '" + log_dict["StudentComment"] + "' , GETDATE());"

  
    # ###Student comment insert
    # student_comment_insert = "insert into StudentComment (LogID, StudentEntityID, Comment, LastUpdated)\n"
    # student_comment_insert += "values (" + str(log_dict["LogID"]) + ", " + str(log_dict["StudentEntityID"]) + ",'" + log_dict["StudentComment"] + "',GETDATE());"

    # ###Organization comment insert 
    # organization_comment_insert = "insert into OrganizationComment (LogID, OrganizationEntityID, Comment, LastUpdated)\n"
    # organization_comment_insert += "values (" + str(log_dict["LogID"]) + ", " + str(log_dict["OrganizationEntityID"]) + ",'" + log_dict["OrganizationComment"] + "',GETDATE());"

    ###append these strings in this particular order to our text file.
    with open('generatedinserts.txt', 'a') as input_file:
            input_file.write(log_hours_insert + "\n")
           

opportunity_id_list = list(range(1,26))
###ApplicationREQ INSERTS
###Inserts for student Job Application approvals from faculty
###Step by 20 so not all student's submit an application.
for student in range (0,len(student_id_list),20):
    ###need to calculate dates in a good range

    d1 = datetime.datetime.strptime('1/1/2019', '%m/%d/%Y')
    d2 = datetime.datetime.strptime('4/28/2019', '%m/%d/%Y')


    randomDate = random_date(d1, d2)

    student_app_req_insert = "insert into ApplicationRequest (StudentEntityID, JobListingID, ApprovedFlag, RequestedDate ,LastUpdated)"
    student_app_req_insert += "values(" + str(student_id_list[student]) + ", " + str(job_listing_id_list[random.randint(0,len(job_listing_id_list) -1)]) + ", " + "'P', '" + str(randomDate) +"',GETDATE());"

    ###Append to our text file
    with open('generatedinserts.txt', 'a') as input_file:
            input_file.write(student_app_req_insert + "\n")

for school_cursor in range (len(school_primary_key_list)):
    for opportunity_cursor in range (len(opportunity_id_list)):

        approval_school_flag = " "

        chance = random.randint(1,6)
        if chance == 1 or chance == 3:
            approval_school_flag = 'Y'
        elif chance == 4 or chance == 5:
            approval_school_flag = 'P'
        else:
            approval_school_flag = 'N'


        school_approval_insert_string = "Insert into SchoolApproval (SchoolEntityID, OpportunityEntityID, ApprovedFlag,LastUpdated) \n"
        school_approval_insert_string += "Values (" + str(school_primary_key_list[school_cursor]) + ", " + str(opportunity_id_list[opportunity_cursor]) + ",'"+ approval_school_flag + "',GETDATE());"
        print(school_approval_insert_string)

        with open('generatedinserts.txt', 'a') as input_file:
            input_file.write(school_approval_insert_string + "\n") 