drop table OpportunityInterestGroups
drop table TechnicalSchool
drop table University
drop table EducationInstitution
drop table Scholarship
drop table JobListing
drop table UserInterest
drop table OpportunityEntity
drop table Organization
drop table Student
drop table StudentInterestGroups
drop table InterestGroups
drop table Parent
drop table SchoolEmployee
drop table School
drop table Password
drop table UserEntity


create table UserEntity (
UserEntityID int identity(1,1) not null,
UserName varchar(50) not null,
EmailAddress varchar (255) not null,
EntityType varchar (10) not null,
Primary Key (UserEntityID)
);

--PasswordTable
create table Password (
PasswordID int not null,
PasswordHash varchar(100) not null,
PasswordSalt varchar(75) not null,
UserEntityID int not null,
LastUpdated datetime,
Primary Key (PasswordID),
Foreign Key (UserEntityID) references UserEntity (UserEntityID)
); 

--SchoolTable Inherits from the UserEntity Table
--This table will not be randomly generated, but 
--Hardcoded with good information on 3 schools cuedIn uses
Create table School(
SchoolEntityID int not null,
SchoolName varchar (50) not null,
StreetAddress varchar (50) not null,
Country varchar (50) not null,
City varchar (50) not null,
State varchar (50) not null,
ZipCode int not null,
--insert a school image here possibly!
primary key (SchoolEntityID),
Foreign key (SchoolEntityID) references UserEntity (UserEntityID)
);

--References the SchoolTable. 
Create table SchoolEmployee(
SchoolEmployeeEntityID int identity (1,1) not null,
FirstName varchar (50),
LastName varchar (50) not null,
MiddleName varchar (50) not null,
StreetAddress varchar (50) not null,
Country varchar (50) not null,
City varchar (50) not null,
State varchar (50) not null,
ZipCode int not null,
SchoolEmployeeEntityType varchar (5) not null, --CON, ADMIN, TEACHER
SchoolEntityID int not null,
UserEntityID int not null,
primary key (SchoolEmployeeEntityID),
Foreign key (SchoolEntityID) references School (SchoolEntityID),
Foreign key (UserEntityID) references UserEntity (UserEntityID)
);

Create table Parent (
ParentEntityID int not null,
FirstName varchar (50),
LastName varchar (50) not null,
MiddleName varchar (50) not null,
StreetAddress varchar (50) not null,
Country varchar (50) not null,
City varchar (50) not null,
State varchar (50) not null,
ZipCode int not null,
primary key (ParentEntityID)
);

--References the userEntity, and 
Create table Student (
StudentEntityID int not null,
FirstName varchar (50) not null,
LastName varchar (50) not null,
MiddleName varchar (50) not null,
StreetAddress varchar (50) not null,
Country varchar (50) not null,
City varchar (50) not null,
State varchar (50) not null,
ZipCode int not null,
StudentGradeLevel varchar (25) not null,
StudentGPA decimal not null,
StudentACTScore int null,
StudentSATScore int null,
StudentEthnicity varchar (30) null, --PC datafield
StudentGender varchar (30) null, --PC datafield
IncomeLevel varchar (50) null, --PC datafield 
DaysAbsent int not null,
ParentEntityID int null, --parent might not be associated with anything
SchoolEntityID int not null, --student needs to be associated with a school 
primary key (StudentEntityID),
Foreign key (StudentEntityID) references UserEntity (UserEntityID),
Foreign key (ParentEntityID) references Parent (ParentEntityID),
Foreign key (SchoolEntityID) references School (SchoolEntityID)
);

--InterestGroup Table
Create table InterestGroups(
InterestGroupID int identity(1,1),
InterestGroupName varchar (90),
primary key (InterestGroupID)
);

--Interest Groups where it links students and interest groups 
create table StudentInterestGroups(
InterestGroupID int,
StudentEntityID int,
primary key (InterestGroupID),
primary key (StudentEntityID),
Foreign key (InterestID) references InterestGroups,
Foreign key (StudentEntityID) references Student
)

--Creates a org/business
Create table Organization (
OrganizationEntityID int not null,
OrganizationName varchar (50) not null,
OrganizationDescription varchar(255) not null,
StreetAddress varchar (50) not null,
Country varchar (50) not null,
City varchar (50) not null,
State varchar (50) not null,
ZipCode int not null,
primary key (OrganizationEntityID),
Foreign key (OrganizationEntityID) references UserEntity (UserEntityID)
);

--
Create table UserChecklist (
UserEntityID int not null,
OpportunityEntityID int not null,
Primary Key (UserEntityID),
Primary Key (OpportunityEntityID),
Foreign Key (UserEntityID) references UserEntity (UserEntityID),
Foreign Key (OpportunityEntityID) references OpportunityEntity (OpportunityEntityID),
);

Create table OpportunityEntity (
OpportunityEntityID int identity(1,1) not null,
OpportunityType varchar(6) not null, --JOB HE SCHOL
Primary Key (OpportunityEntityID),
);

Create Table JobListing (
JobListingID int not null,
JobTitle varchar(255) not null,
JobDescription varchar(255) not null,
JobType varchar(255) not null,
Location varchar(255) not null,
Deadline datetime not null,
LastUpdated datetime not null,
Approved varchar(3) not null,
NumOfApplicants int not null,
OrganizationID int not null,
Primary Key (JobListingID),
Foreign Key (JobListingID) references OpportunityEntity (OpportunityEntityID),
Foreign Key (OrganizationID) references Organization (OrganizationEntityID)
);

Create Table Scholarship (
ScholarshipID int not null,
ScholarshipName varchar(50) not null,
ScholarshipDescription varchar(255) not null,
ScholarshipMin money not null,
ScholarshipMax money not null,
ScholarshipQuantity int not null,
ScholarshipDueDate datetime not null,
OrganizationID int not null,
Approved varchar(3) not null,
LastUpdated datetime not null,
Primary key (ScholarshipID),
foreign Key (ScholarshipID) references OpportunityEntity(OpportunityEntityID),
Foreign Key (OrganizationID) references Organization (OrganizationEntityID)
) ;

Create table EducationInstitution (
HigherEducationID int not null,
EducationInsitutionName varchar(50) not null,
ApplicationDueDate datetime not null,
StreetAddress varchar (50) not null,
Country varchar (50) not null,
City varchar (50) not null,
State varchar (50) not null,
ZipCode int not null,
InstateTutition money not null,
OutOfStateTutition money not null,
UnversityType varchar(10), --This will be a subtype discriminator TS or UNIV
Primary Key (HigherEducationID),
Foreign Key (HigherEducationID) references OpportunityEntity (OpportunityEntityID)
);

Create Table University (
UnversityID int not null,
GPARequirement decimal not null,
SATRequirement int not null,
ACTRequirement int not null,
Primary Key (UnversityID),
Foreign Key (UnversityID) references EducationInstitution (HigherEducationID),
) ;
 

Create Table TechnicalSchool (
TechnicalSchoolID int not null,
TechnicalSchoolSkill varchar(50) not null,
Description varchar(50) not null,
Primary Key (TechnicalSchoolID),
Foreign Key (TechnicalSchoolID) references EducationInstitution (HigherEducationID),
);

Create table OpportunityInterestGroups (
InterestGroupsID int,
OpportunityEntityID int,
primary key (InterestID),
primary key (OpportunityEntityID),
Foreign key (InterestGroupsID) references InterestGroups,
Foreign key (OpportunityEntityID) references OpportunityEntity
);


