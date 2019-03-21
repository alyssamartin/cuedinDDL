import random
import names 
import faker
import string



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

#No password for these guys. just here for associations
#only the schoolemployees should have thier own passwords
userEntityID = 0

for i in range (6): 
    #primary keys are 1,2,3 for userentity
    school_entity_insert = "insert into userEntity (UserName, EmailAddress, EntityType) values  ('"+ school_list[i].replace(" ","") +"', '"+school_email_list[i] + "'" + "SCHL" + "')"
    print (school_entity_insert)

    userEntityID = userEntityID + 1

    school_insert = "insert into school (schoolEntityID, schoolName, StreetAddress, Country, City, State, SchoolCounty, ZipCode) values (" + str(userEntityID)+ ", '" + school_list[i] + "','" + school_street_address_list[i] + "','" + school_country+ "','"+ school_city_list[i] + "','"+ school_state + "','" +  school_county_list[i] + "'," + school_zipcode_list[i] + ")"

    print(school_insert)


    with open('generatedinserts.txt', 'a') as input_file:
        input_file.write(school_entity_insert + "\n")
        input_file.write(school_insert + "\n")

#Whatever the amount of userEntity ID's there are
#this is the amount of schools there are 
amount_of_schools = userEntityID 





#Student Inserts 
amount_of_students = 20
for i in range (amount_of_students):
    ###Determining Gender over here
    ###Determining names based off of genders
    ###kids will have boy or girl names. but 10% chance someone is a third party gender
    gender_flag = random.randint(0,1) 
    third_party_gender_flag = random.randint(1,100)

    ###0 means female 
    if gender_flag = 0:

        ##The if block that determines if they want to be a third gender (no choice, it's python's choice)
        if third_party_gender_flag <= 10:
            student_gender = "third party"
        else:
        ##Female
            student_gender = "female"
        student_first_name = names.get_first_name(gender='female')
        student_last_name = names.get_last_name()

    ###1 means male
    elif gender_flag = 1:

        ##The if block that determines if they want to be a third gender
        if third_party_gender_flag <= 10:
            student_gender "third party"
        else:
            student_gender  = "male"

        student_first_name = names.get_first_name(gender='male')
        student_last_name = names.get_last_name()

    student_middle_initial = random.choice(string.ascii_uppercase)
    
    student_full_name = student_first_name + student_last_name
    ##Generate student username
    student_user_name = student_full_name + student_middle_initial + str(random.randint(0,1000))

    print(student_user_name)
    #Generate student's school for email and further use...
    school_list_id = list(range(0,amount_of_schools + 1)) ##foreign key
    student_school_id = random.randint(0,amount_of_schools -1)
    student_school = school_list[student_school_id]
    
    ##generate student emailAddress
    student_email_domain = school_email_list[student_school_id].split("@")[1]
    student_email = student_user_name + "@" + student_email_domain

    ###Generate student Address
    student_street_address = fake.StreetAddress
    student_country = USA 
    student_
    






# Create table Student (
# StudentEntityID int not null, done
# FirstName varchar (50) not null, done
# LastName varchar (50) not null, done 
# MiddleInitial varchar (1) not null,done 
# StreetAddress varchar (50) not null,
# Country varchar (50) not null,
# City varchar (50) not null,
# State varchar (50) not null,
# ZipCode int not null,
# StudentGradeLevel varchar (25) not null,
# StudentGPA decimal not null,
# StudentACTScore int null,
# StudentSATScore int null,
# StudentEthnicity varchar (30) null, --PC datafield
# StudentGender varchar (30) null, --PC datafield
# IncomeLevel varchar (50) null, --PC datafield 
# DaysAbsent int not null,
# ParentEntityID int null, --parent might not be associated with anything
# SchoolEntityID int not null, --student needs to be associated with a school 
# primary key (StudentEntityID),
# Foreign key (StudentEntityID) references UserEntity (UserEntityID),
# Foreign key (ParentEntityID) references Parent (ParentEntityID),
# Foreign key (SchoolEntityID) references School (SchoolEntityID)
# );












