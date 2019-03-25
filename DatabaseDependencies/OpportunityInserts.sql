--1
insert into OpportunityEntity (OpportunityType) values ('JOB');

insert into JobListing (JobListingID, JobTitle, JobDescription, JobType, Location, Deadline, postingDate, LastUpdated, Approved, NumOfApplicants, OrganizationID)
values (1,'Athletic Trainer Intern', 'Assist head athletic trainer in day-to-day tasks', 'Internship', 'Harrisonburg VA', '6/30/2019', '3/3/2019' ,  getDate(),'Y',5, 8)

insert into OpportunityInterestGroups (InterestID, OpportunityID) VALUES
(3,1),
(4,1),
(8,1);


--2
insert into OpportunityEntity (OpportunityType) values ('JOB');

insert into JobListing (JobListingID, JobTitle, JobDescription, JobType, Location, Deadline, postingDate, LastUpdated, Approved, NumOfApplicants, OrganizationID)
values (2,'Administrative Assisant', 'Handling office tasks', 'Job Shadowing', 'Harrisonburg VA', '9/3/2019', '1/3/2019', getDate(),'P',17,4);

insert into OpportunityInterestGroups (InterestID, OpportunityID) VALUES
(3,2),
(2,2);

--3

insert into OpportunityEntity (OpportunityType) values ('JOB');

insert into JobListing (JobListingID, JobTitle, JobDescription, JobType, Location, Deadline, postingDate, LastUpdated, Approved, NumOfApplicants, OrganizationID)
values (3,'Assistant Baker', 'Assisting head baker with day-to-day baking', 'Apprenticeship', 'Harrisonburg VA', '4/5/2019', '2/14/2019', getDate(),'P',7, 2);

insert into OpportunityInterestGroups (InterestID, OpportunityID) VALUES
(1,3);

--4
insert into OpportunityEntity (OpportunityType) values ('JOB');

insert into JobListing (JobListingID, JobTitle, JobDescription, JobType, Location, Deadline, postingDate, LastUpdated, Approved, NumOfApplicants, OrganizationID)
values (4,'Store Manager (Shadow)', 'Oversee daily operations including training staff and working with vendors', 'Job Shadowing', 'Harrisonburg VA', '6/7/2019', '1/5/2019', getDate(),'Y',15, 1);

insert into OpportunityInterestGroups (InterestID, OpportunityID) VALUES
(1,4);

--5
insert into OpportunityEntity (OpportunityType) values ('JOB');

insert into JobListing (JobListingID, JobTitle, JobDescription, JobType, Location, Deadline, postingDate, LastUpdated, Approved, NumOfApplicants, OrganizationID)
values (5,'Automation Engineer Shadow', 'Shadow lead engineer to design, program, simulate, and test automated machinery', 'Job Shadowing', 'Elkton, VA', '5/6/2019', '3/4/2019', getDate(),'Y',30, 7);


insert into OpportunityInterestGroups (InterestID, OpportunityID) VALUES
(7,5),
(8,5),
(9,5);

--6
insert into OpportunityEntity (OpportunityType) values ('JOB');

insert into JobListing (JobListingID, JobTitle, JobDescription, JobType, Location, Deadline, postingDate, LastUpdated, Approved, NumOfApplicants, OrganizationID)
values (6,'Lab Tech', 'Collect samples, study, and perform tests', 'Internship', 'Elkton, VA', '7/6/2019', '1/4/2019', getDate(),'P',25, 3);

insert into OpportunityInterestGroups (InterestID, OpportunityID) VALUES
(8,6),
(9,6);

--7
insert into OpportunityEntity (OpportunityType) values ('JOB');

insert into JobListing (JobListingID, JobTitle, JobDescription, JobType, Location, Deadline, postingDate, LastUpdated, Approved, NumOfApplicants, OrganizationID)
values (7,'Help Desk Associate', 'Provide customer support and help customers solve problems', 'Apprenticeship', 'Harrisonburg, VA', '8/4/2019', '2/2/2019', getDate(),'Y',27, 7);

insert into OpportunityInterestGroups (InterestID, OpportunityID) VALUES
(3,7),
(4,7),
(5,7);

--8
insert into OpportunityEntity (OpportunityType) values ('JOB');

insert into JobListing (JobListingID, JobTitle, JobDescription, JobType, Location, Deadline, postingDate, LastUpdated, Approved, NumOfApplicants, OrganizationID)
values (8,'Software Engineer', 'Perform analysis and problem definition and propose solutions', 'Job Shadowing', 'Harrisonburg, VA', '7/11/2019', '3/20/2019', getDate(),'Y',30, 7);

insert into OpportunityInterestGroups (InterestID, OpportunityID) VALUES
(7,8),
(8,8),
(9,8);


--9
insert into OpportunityEntity (OpportunityType) values ('JOB');

insert into JobListing (JobListingID, JobTitle, JobDescription, JobType, Location, Deadline, postingDate, LastUpdated, Approved, NumOfApplicants, OrganizationID)
values (9,'ED Technician', 'Assist doctors in treating patients', 'Clinical', 'Harrisonburg, VA', '6/4/2019', '3/22/2019', getDate(),'P',21, 8);

insert into OpportunityInterestGroups (InterestID, OpportunityID) VALUES
(3,9),
(4,9),
(10,9);


--10
insert into OpportunityEntity (OpportunityType) values ('JOB');

insert into JobListing (JobListingID, JobTitle, JobDescription, JobType, Location, Deadline, postingDate, LastUpdated, Approved, NumOfApplicants, OrganizationID)
values (10,'Psych Technician', 'Performs treatment following instructions', 'Clinical', 'Harrisonburg, VA', '5/4/2019', '3/25/2019', getDate(),'P',10, 8);

insert into OpportunityInterestGroups (InterestID, OpportunityID) VALUES
(3,10),
(4,10),
(10,10);

insert into OpportunityEntity (OpportunityType) values ('JOB');

--11
insert into JobListing (JobListingID, JobTitle, JobDescription, JobType, Location, Deadline, postingDate, LastUpdated, Approved, NumOfApplicants, OrganizationID)
values (11,'Cardiology Department Shadow', 'Shadow head of cardiology', 'Job Shadowing', 'Harrisonburg, VA', '7/11/2019', '3/22/2019', getDate(),'P',15, 8);

insert into OpportunityInterestGroups (InterestID, OpportunityID) VALUES
(3,11),
(4,11),
(10,11);

