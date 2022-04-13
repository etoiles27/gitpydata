-- show table 
select * from member;
-- table type
desc member;
-- ora_user table
select * from tab;
-- table의 특정 column을 보여준다
select id, password from member;

select salary from employees;
-- 사칙연산 가능 as 로 별칭선언가능 (as 생략가능) 쌍따옴표를 넣을 경우에는 대소문자를 구별한다.
select salary, salary/5 as salary5 , salary*12 as "Salary12" from employees;
-- 명령어는 대소문자를 구별하지 않는다. 
desc employees;
-- 해당컬럼 역순정렬
select * from employees order by employee_id desc;
-- 해당컬럼 순차정렬
select * from employees order by employee_id;

-- 최대값 최소값
select max(employee_id) from employees;
select min(employee_id) from employees;

select * from students;
select max(stuid)+1 from students;

insert into students values(
(select max(stuid)+1 from students),'을지문덕', 100,100,100,(100+100+100),(100+100+100)/3,0);

-- nvl -> null일때, 
select id, name, nvl(total, 0)+10 from member;
select * from employees;
select emp_name, salary*1230, salary*12*1230 as salary12 ,nvl(commission_pct,0),
salary*12*1230+(salary*12*1230*nvl(commission_pct,0)) as real_salary from employees;

create table triangle(
tno number(5) primary key,
base number(5,1),
height number(5,1),
area number(7,1)
);

insert into triangle values(1,10,5,10*5*0.5);
insert into triangle values(2,15,4,15*4*0.5);
insert into triangle values(3,20,9,20*9*0.5);
insert into triangle values(4,35,12,35*12*0.5);
commit;
select * from triangle;
--사번, 이름. 이메일, 전화번호, 입사일 별칭을 사용해서 출력하세요

select * from employees;
select employee_id as "사번", emp_name as "이름", email as "이메일",
phone_number as "전화번호", hire_date as "입사일" from employees;

select * from departments;

select department_id as "부서번호", department_name as "부서명" from departments;

-- concatenation 연결 
select * from employees;
select emp_name || '의 직급 : '||job_id from employees;

-- distinct 중복제거
select department_id, department_name from departments;
select distinct department_id from employees order by department_id;
select distinct job_id from employees;
select * from jobs;
select * from students;

select * from employees where employee_id>150;
select emp_name, salary from employees where salary>=3000 and salary<=7000 order by salary;
-- 대소문자를 구별한다
select * from employees where lower(emp_name) = 'susan mavris' 
or upper(emp_name)='SUSAN MAVRIS' or initcap(emp_name)='Susan Mavris';

-- 포함된 글자 찾을때 like
select emp_name from employees where lower(emp_name) like '%su%';
select department_id from employees where department_id=20;
select employee_id, emp_name, salary from employees where salary<=4000 
and (department_id=30) order by salary ;

select hire_date from employees where hire_date='07/06/21';
select email from employees where lower(email)='pfay';

select hire_date from employees where hire_date>='07/06/21';
--2000/1/1 이후 입사사원
select employee_id, emp_name, hire_date from employees 
where hire_date>='00/01/01' order by hire_date;

select employee_id, emp_name,to_char(hire_date,'YYYY/MM/DD') from employees where hire_date>='2000/01/01';

-- not 
select * from employees where not department_id=10;
select * from employees where department_id!=20;
select * from employees where department_id <> 20;
select * from employees where department_id ^=20;

-- 3000이상 7000이하
select salary from employees where salary>=3000 and salary<=7000 order by salary;
select salary from employees where salary between 3000 and 7000 order by salary;

-- commission_pct 0.1 or 0.3
select * from employees;
select * from employees 
where commission_pct=0.1 or commission_pct=0.2 or commission_pct=0.3;

create table studata(
stuno number(4),
stuname varchar2(50),
kor number(3),
eng number(3),
math number(3),
total number(5,2),
avg number(5,2),
rank number
);

select * from studata;
commit;

select * from studata where kor>=90 and eng>=90 and math>=90 order by total;

select * from studata where kor between 80 and 90 order by kor;

select * from employees where employee_id=120 or employee_id=130 or employee_id=140;

select * from employees where employee_id>=130 and salary between 3000 and 5000 order by salary;

select * from employees where not
(salary >=3000 and salary<=5000) order by salary;
-- 위아래는 동일한 명령어다
select * from employees where not salary between 3000 and 5000 order by salary;
-- 날짜는 정렬과, 사이. 다 가능하다.
select * from employees where hire_date between '95/01/01' and '02/12/31' order by hire_date;
-- 날짜에서 덧셈뺄셈이 가능하다.
select hire_date, hire_date+10 from employees;

select * from employees 
where employee_id in(120,130,140);

select * from studata
where total in(270,280,290);

select * from studata
where stuname like '__ll%';

select * from employees 
where emp_name like '%n';

select * from employees 
where lower(emp_name) like '%s%';

select * from studata 
where lower(stuname) like '_a%';

select * from studata 
where lower(stuname) not like '_a%';

select * from employees 
where commission_pct is not null;
--where commission_pct is null;

update member set total=null where id='aaa';
commit;
select * from member;

--drop table member2;
create table studata2
as select * from studata;

select * from studata2;

update studata2 set total=0;
update studata2 set avg=0;
commit;

update studata2 set total = kor+eng+math;
update studata2 set avg = total/3;

select stuno,stuname, total, rank from studata
order by total desc;

update studata set rank = 1 order by total desc;

select * from studata order by total desc;

--update (select * from studata order by total desc)
--set rank=(select rank() over (order by total desc) rank from studata order by total desc);

select rank() over (order by total desc) rank from studata order by total desc;

delete studata2;
select * from studata2 order by stuno;

insert into studata2 (select * from studata);

insert into studata2(stuno, stuname, kor, eng, math, total, avg,rank) 
select stuno, stuname, kor, eng, math, total, avg,
rank() over(order by total desc) rank 
from studata order by total desc; 

select * from studata2 order by rank;

--drop table studata2

--테이블 타입만 복제생성 
create table studata2 as select * from studata where 1=2;
desc studata2;
select * from studata2;

--모든테이블 복제생성
--create table studata2 as select * from studata;

insert into studata2 
select * from studata;
delete studata2;
commit;

insert into studata2(stuno, stuname, kor, eng, math, total, avg, rank) 
select stuno, stuname, kor, eng, math, total, avg,
rank() over (order by total desc) rank 
from studata;
select * from studata2 order by rank ;
select * from studata2 order by stuno;
commit;

select employee_id from employees;
--순차정렬
select salary from employees order by salary;
--역순정렬
select salary from employees order by salary desc;


--employees2: employee_id, emp_name, salary, rank 
--employees의 모든데이터를 employees2에 넣을것, salary 로 rank


create table employees3 as select * from employees where 1=2;
alter table employees3 add rank number;

insert into employees3 (EMPLOYEE_ID,EMP_NAME,EMAIL,PHONE_NUMBER,HIRE_DATE,SALARY,MANAGER_ID,COMMISSION_PCT,RETIRE_DATE,DEPARTMENT_ID,JOB_ID,CREATE_DATE,UPDATE_DATE,rank)
select EMPLOYEE_ID,EMP_NAME,EMAIL,PHONE_NUMBER,HIRE_DATE,SALARY,MANAGER_ID,COMMISSION_PCT,RETIRE_DATE,DEPARTMENT_ID,JOB_ID,CREATE_DATE,UPDATE_DATE,
rank() over (order by salary desc) rank 
from employees;

select EMPLOYEE_ID,EMP_NAME,salary,rank from employees3 order by rank ;
select EMPLOYEE_ID,EMP_NAME,salary,rank from employees3 order by EMPLOYEE_ID ;


select * from employees2;
--alter table employees2 rename to employees4;
--alter table employees2 rename to employees3;
create table employees2 as 
select EMPLOYEE_ID,EMP_NAME,salary from employees where 1=2;

alter table employees2 add rank number(4);

insert into employees2 (EMPLOYEE_ID,EMP_NAME,salary,rank)
select EMPLOYEE_ID,EMP_NAME,salary,
rank() over (order by salary desc) rank 
from employees;
select * from employees2;


-- 부서번호- 순차정렬, 부서번호가 같을경우 , 샐러리-역순정렬
select DEPARTMENT_ID, salary from employees order by DEPARTMENT_ID, salary desc;
select * from employees order by EMPLOYEE_ID, HIRE_DATE desc;


select -10, abs(-10) from dual;
select floor(10.3245) from dual;
select round(10.3245,3) from dual;
-- 정수 첫째자리에서 반올림
select round(277.4567,-1) from dual;

select * from studata;
select * from studata
where mod(stuno,2)=1;

--사원번호가 짝수만 출력
select * from employees 
where mod(employee_id,2)=0;


--drop table employees2;
create table employees2 as 
select employee_id,emp_name,salary from employees where 1=2;
alter table employees2 add rank number(4);


insert into employees2( employee_id,emp_name,salary, rank )
select EMPLOYEE_ID,EMP_NAME,salary,
rank() over (order by salary desc) rank 
from employees where  mod(employee_id,2)=1;

select * from employees2 order by employee_id;

-- 시퀀스 생성
CREATE SEQUENCE emp_seq 
INCREMENT BY 1 
START WITH 1 
MAXVALUE 100000
MINVALUE 1;


--nextval 시퀀스다음번호를 가져옴, currval 현재번호를 가져옴
create table students2 as 
select * from students where 1=2;
insert into students2 values(
board_seq.nextval,'나비',100,100,100,(100+100+100),(100+100+100)/3,0);

select * from students2;

select board_seq.currval from dual;
select board_seq.nextval from dual;



create table emp01 (
empno number(5),
EMPLOYEE_ID NUMBER(6,0),
EMP_NAME VARCHAR2(80 BYTE),
SALARY NUMBER(8,2)
);

insert into emp01
select emp_seq.nextval,EMPLOYEE_ID,EMP_NAME,SALARY from employees;

--delete emp01;

--insert into emp01(empno) values(emp_seq.nextval);


select * from emp01 order by empno;

select emp_seq.currval from dual;
