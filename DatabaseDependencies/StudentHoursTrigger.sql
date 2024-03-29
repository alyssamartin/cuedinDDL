Create Trigger UpdateHoursApproved on [dbo].[LogHours]
After Update
as
if(Update([CounselorApproval]))
begin
Set NoCount on

Declare @CounselorApproval varchar,
@HoursWorked int,
@StudentEntityID int,
@StudentEmploymentFlag varchar

--set variables

select @CounselorApproval=(select [CounselorApproval] from inserted)
select @HoursWorked=(select [HoursRequested] from inserted)
select @StudentEntityID=(select StudentEntityID from inserted)
select @StudentEmploymentFlag=(Select [StudentEmploymentFlag] from student where StudentEntityID = @StudentEntityID)

if @CounselorApproval = 'Y'
begin
update Student set [HoursOfWorkPlaceExp] = [HoursOfWorkPlaceExp] + @HoursWorked where studentEntityID =  @StudentEntityID
end

if @CounselorApproval = 'Y' and @StudentEmploymentFlag = 'N'
begin 
update Student set [StudentEmploymentFlag] = 'Y' where StudentEntityID = @StudentEntityID
end
end
