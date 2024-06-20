create table teacher(tid int primary key,tpass varchar(10),tname varchar(30),class_teacher varchar(10) , handling_classes varchar(30));
create table studentbio(sid int primary key,spass varchar(10),sname varchar(30),sclass varchar(5),dob date, fname varchar(30),mname varchar(30));
create table studentmark(sid int primary key,sclass varchar(5),ut1 float,ut2 float,ut3 float, quarterly float,ut4 float, half-yearly float, ut5 float);
