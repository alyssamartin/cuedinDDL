drop table SchoolApproval
drop table ApplicationRequest
drop table OrganizationComment
drop table StudentComment
drop table LogHours
drop table OpportunityInterestGroups
drop table TechnicalSchool
drop table University
drop table HigherEducation
drop table Scholarship
drop table JobListing
drop table UserChecklist
drop table OpportunityEntity
drop table Organization
drop table StudentInterestGroups
drop table Student
drop table InterestGroups
drop table SchoolEmployee
drop table School
drop table Parent
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
PasswordHash varchar(255) not null,
PasswordSalt varchar(100) not null,
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
SchoolCounty varchar (50) not null,
ZipCode int not null,
--insert a school image here possibly!
primary key (SchoolEntityID),
Foreign key (SchoolEntityID) references UserEntity (UserEntityID)
);

--References the SchoolTable. 
Create table SchoolEmployee(
SchoolEmployeeEntityID int identity (1,1) not null,
FirstName varchar (50) not null,
LastName varchar (50) not null,
MiddleName varchar (50) null,
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

--References the UserEntity Table
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
primary key (ParentEntityID),
Foreign key (ParentEntityID) references UserEntity (UserEntityID)
);

--References the userEntity, and 
Create table Student (
StudentEntityID int not null,
FirstName varchar (50) not null,
LastName varchar (50) not null,
MiddleInitial varchar (1) not null,
StreetAddress varchar (50) not null,
Country varchar (50) not null,
City varchar (50) not null,
State varchar (50) not null,
ZipCode int not null,
StudentGradeLevel varchar (25) not null,
StudentGPA float not null,
StudentACTScore int null,
StudentSATScore int null,
StudentEthnicity varchar (30) null, --PC datafield
StudentGender varchar (30) null, --PC datafield
IncomeLevel varchar (50) null, --PC datafield 
DaysAbsent int not null,
HoursOfWorkPlaceExp int not null, --possible stored trigger on update of our new tables
StudentEmploymentFlag varchar (1) not null,
StudentAthleteFlag varchar (1) not null,
StudentGraduationTrack varchar (1) not null,
ParentEntityID int null, --parent might not be associated with anything
StudentImage varchar (100),
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
primary key (InterestGroupID, StudentEntityID),
Foreign key (InterestGroupID) references InterestGroups (InterestGroupID),
Foreign key (StudentEntityID) references Student (StudentEntityID)
);

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
Image varchar(50),
ExternalLink varchar (100),
primary key (OrganizationEntityID),
Foreign key (OrganizationEntityID) references UserEntity (UserEntityID)
);

Create table OpportunityEntity (
OpportunityEntityID int identity(1,1) not null,
OpportunityType varchar(6) not null, --JOB HE SCHOL
Primary Key (OpportunityEntityID),
);


--
Create table UserChecklist (
UserEntityID int not null,
OpportunityEntityID int not null,
Primary Key (UserEntityID, OpportunityEntityID),
Foreign Key (UserEntityID) references UserEntity (UserEntityID),
Foreign Key (OpportunityEntityID) references OpportunityEntity (OpportunityEntityID),
);



--JobListing Table references the OpportunityEntity Table
Create Table JobListing (
JobListingID int not null,
JobTitle varchar(255) not null,
JobDescription varchar(255) not null,
JobType varchar(255) not null,
Location varchar(255) not null,
Deadline datetime not null,
PostingDate datetime not null,
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
PostingDate datetime not null,
ScholarshipDueDate datetime not null,
OrganizationID int not null,
Approved varchar(3) not null,
LastUpdated datetime not null,
Primary key (ScholarshipID),
foreign Key (ScholarshipID) references OpportunityEntity(OpportunityEntityID),
Foreign Key (OrganizationID) references Organization (OrganizationEntityID)
) ;

--References the OpportunityEntity Table
Create table HigherEducation (
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
Image varchar (100),
ExternalLink varchar (100),
Primary Key (HigherEducationID),
Foreign Key (HigherEducationID) references OpportunityEntity (OpportunityEntityID)
);

Create Table University (
UnversityID int not null,
GPARequirement decimal not null,
SATRequirement int not null,
ACTRequirement int not null,
Primary Key (UnversityID),
Foreign Key (UnversityID) references HigherEducation (HigherEducationID),
) ;
 
--Technical school table references the HigherEducation Table
Create Table TechnicalSchool (
TechnicalSchoolID int not null,
TechnicalSchoolSkill varchar(50) not null,
Description varchar(50) not null,
Primary Key (TechnicalSchoolID),
Foreign Key (TechnicalSchoolID) references HigherEducation (HigherEducationID),
);

Create table OpportunityInterestGroups (
InterestGroupID int,
OpportunityEntityID int,
primary key (InterestGroupID, OpportunityEntityID),
Foreign key (InterestGroupID) references InterestGroups,
Foreign key (OpportunityEntityID) references OpportunityEntity
);

Create Table StudentComment (
LogID int,
StudentEntityID int,
Comment varchar (255),
primary Key(LogID, StudentEntityID),
Foreign Key (StudentEntityID) references student (StudentEntityID)
);

Create Table OrganizationComment (
LogID int,
OrganizationEntityID int,
Comment varchar (255),
primary Key(LogID, OrganizationEntityID),
Foreign Key (OrganizationEntityID) references Organization (OrganizationEntityID)
);

Create Table LogHours (
LogID int identity(1,1),
JobListingID int, 
HoursRequested int,
CounselorApproval varchar (10),
OrganizationApproval varchar(10),
StudentEntityID int,
Primary key (LogID),
Foreign key (JobListingID) references JobListing (JobListingID),
Foreign key (StudentEntityID) references Student (StudentEntityID)
);


Create table ApplicationRequest (
ApplicationID int Identity (1,1),
StudentEntityID int,
JobListingID int,
ApprovedFlag varchar (1),
primary key (ApplicationID),
Foreign key (StudentEntityID) references Student (StudentEntityID),
Foreign key (JobListingID) references JobListing (JobListingID)
);

Create table SchoolApproval (
SchoolEntityID int,
OpportunityEntityID int,
ApprovedFlag varchar(1)
primary key (SchoolEntityID, OpportunityEntityID),
Foreign key (SchoolEntityID) references school (SchoolEntityID),
Foreign key (OpportunityEntityID) references opportunityEntity(OpportunityEntityID)

);