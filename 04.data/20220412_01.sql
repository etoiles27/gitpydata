SELECT * FROM employees;
select * from departments;    
select job_id,job_title from jobs;
create table member(
id varchar2(20) primary key,
pw VARCHAR2(20),
name VARCHAR2(20),
phone VARCHAR2(20));
desc member;
select * from tab;
insert into member(id, pw, name, phone) values('aaa','1111','홍길동','010-1111-1111');
select * from member;
commit;
select * from member;
insert into member values('bbb','1111','이순신','010-2222-2222');
select * from member;
commit;
insert into member values('ccc','1111','이순신','010-2222-2222');
commit;
insert into member(id, name) values('dddd','김구');
select * from member;
insert into member values('eee','1111','강감찬','010-3333-3333');
select * from member;
rollback;

select * from employees;
select emp_name, job_id from employees;
desc employees;

--delete from member;
rollback;
select * from member;

--delete from member where id='aaa';
select * from member;
rollback;
select * from member;
--delete from member where id='bbb';
commit;
select * from member;

select employee_id, emp_name, salary from employees
where employee_id>=150 and salary>4000;

select * from member;
insert into member values('bbb','1111','이순신','010-3333-3333');
insert into member values('ddd','1111','김구','010-4444-4444');
insert into member values('eee','1111','강감찬','010-5555-5555');
commit;

update member set phone='010-7777-7777' where id='bbb';
commit;
select * from member;

-- students 테이블 생성, stuid, stuname, kor,eng,math,total,avg,rank
-- 전부 varchar
create table member2(
id varchar2(20),
pw number(4),
kor number(4,1));

insert into member2 values('aaa',1111,99.9);
commit;
select * from member2;

create table students(
stuid varchar2(20),
stuname varchar2(20),
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(4,1),
rank number(3)
);

rollback;
insert into students values('1','홍길동',100,100,100,(100+100+100),(100+100+100)/3,0);
insert into students values('2','이순신',90,100,99,(90+100+99),(90+100+99)/3,0);
insert into students values('3','유관순',95,99,100,(95+99+100),(95+99+100)/3,0);
insert into students values('4','김구',100,100,98,(100+100+98),(100+100+98)/3,0);
insert into students values('5','강감찬',95,98,96,(95+98+96),(95+98+96)/3,0);
commit;
select * from students;


--drop table member2;

--alter table member add create_date date;
select * from member;
update member set create_date=sysdate where id='aaa';

--alter table member drop COLUMN create_date;

--update member set pw='';
--alter table member modify pw number(4);
--commit;
desc member;
--alter table member rename column pw to password;

--alter table member rename to member2;

create table member(
id varchar2(20),
pw VARCHAR2(20),
name VARCHAR2(20),
phone VARCHAR2(20));

create table member as 
select * from member2 where 1=2;

select * from member;
--drop table member;

create table member as 
select * from member2;

select * from member;



--alter table member add total number(3);
--alter table member add avg number(4,1);

select * from students;
update member set total=(select total from students where stuname='홍길동')
where name='홍길동';


--rollback;
commit;


SELECT DISTINCT manager_id FROM employees;
select emp_name from employees where emp_name='Pat Fay';

select emp_name, salary, hire_date from employees; 

create table employees2 as 
select * from employees;
--drop table employees2;

select * from employees;

create table employees2 as 
select employee_id, emp_name, hire_date, salary from employees where 1=2;

insert into employees2 (employee_id, emp_name, hire_date, salary) 
values(198,'Donald OConnell','07/06/21',2600);
insert into employees2 (employee_id, emp_name, hire_date, salary) 
values(199,'Douglas Grant','08/01/13',2600);
insert into employees2 (employee_id, emp_name, hire_date, salary) 
values(200,'Jennifer Whalen','03/09/17',4400);
insert into employees2 (employee_id, emp_name, hire_date, salary) 
values(201,'Michael Hartstein','04/02/17',13000);
insert into employees2 (employee_id, emp_name, hire_date, salary) 
values(202,'Pat Fay','05/08/17',6000);
commit;

insert into employees2 (employee_id, emp_name, hire_date, salary) 
(select employee_id, emp_name, hire_date, salary from employees where employee_id=198);




select employee_id, emp_name, hire_date, salary from employees where employee_id=198;
select * from employees2;
rollback;
--emp1 table, employees_id, emp_name, hire_date

create table emp1 as 
select employee_id, emp_name, hire_date from employees;

alter table emp1 rename to emp0;

