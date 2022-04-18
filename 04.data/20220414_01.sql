-- ������ ����
CREATE SEQUENCE test_seq 
INCREMENT BY 1 
START WITH 1 
MAXVALUE 9999
MINVALUE 1
nocycle
nocache;

-- ������ ����
alter sequence test_seq
maxvalue 99999
INCREMENT BY 10 
;
--������ Ȯ��
select test_seq.currval from dual;

--drop table employees2;
-- ��������ȣ, �����ȣ, �����, job_id, �Ի���, employees2 �Ի��� ��������


create table employees2 (
seqno number(5),
EMPLOYEE_ID NUMBER(6,0),
EMP_NAME VARCHAR2(80 BYTE),
JOB_ID VARCHAR2(10 BYTE),
HIRE_DATE DATE
);

insert into employees2
select test_seq.nextval,EMPLOYEE_ID,EMP_NAME,JOB_ID,HIRE_DATE
from employees;

select * from employees2 order by hire_date desc;
select * from employees2 order by seqno;

commit;

--create table employees2 as select employee_id,emp_name,salary from employees where 1=2;

select * from employees;
select upper(emp_name) from employees;

--���ڱ���

select emp_name, length(emp_name), lengthb(emp_name) from employees;

select stuname, length(stuname),lengthb(stuname) from students;

--���ڿ����� substr
select emp_name, substr(emp_name,0,6) from employees;
select emp_name, substr(emp_name,7) from employees;
select emp_name, substr(emp_name,-1) from employees;

alter table member add juminno char(14);

update member set password='5555', juminno='880505-1105555' where id ='eee';

select name, substr(juminno,1,6) "�ֹι�ȣ���ڸ�", 
substr(juminno,8) "�ֹι�ȣ���ڸ�" from member;

select name, substr(juminno,1,8)||'******' juminno2,
length( substr(juminno,1,8)||'******') jumin_length
from member;


alter table member add filename varchar2(20);
update member set filename='test.doc' where id ='eee';
commit;
select * from member;

select length(id), substr(juminno,1,6), substr(juminno,8), 
substr(filename,-3)
from member;

--Ư�� ���� ��ġ ã�� instr

--insert into member values('fff','6666','ȫ���','010-0000-0000',300,100,'010101-4105555','abc.jason');


select filename,instr(filename,'.'),substr(filename,instr(filename,'.')+1) from member;

-- ���� ��ü : replace ������ ������ ������ ����� �մ�. 
select emp_name from employees;
select replace(emp_name,' ','') from employees;
--trim, ltrim, rtrim



insert into member values('hhh','     7777','ȫ�濵      ','010-   9999-0000',300,100,'000901-4105555','    abc.js');
update member set name=rtrim(name);
update member set phone=replace(phone,' ','');
select length(rtrim(phone)),length(phone) from member;
select * from member;

commit;

-- ���ڿ� ��ġ�� concat
select concat(id,concat('-',password)) from member;
select id||'-'||password from member;

-- Ư������ ä��� lpad, rpad

select rpad(id,10,'*') from member;
select juminno from member;
select rpad(substr(juminno,1,8),14,'*') from member;

-- sysdate : ����ð�(��¥)
select sysdate, sysdate+1, sysdate-1 from dual;

alter table member add create_date date;
select * from member;
insert into member(id,password,create_date)
values('iii','1111',sysdate);

select to_char(create_date,'YYYY/MM/DD hh:mi:ss') from member;

select hire_date from employees; 
select sysdate-hire_date from employees;
-- ���ڸ� ��¥�� �ٲٴ� to_date()
select trunc(sysdate-to_date('22/03/08')) from dual;


select emp_name,sysdate,hire_date,months_between(sysdate,hire_date) from employees;

select sysdate,'22/03/08',months_between(sysdate,to_date('22/03/08')) from dual;
select sysdate,'22/03/08',add_months(sysdate,6) from dual;

--

select sysdate, next_day(sysdate,'�ݿ���') from dual;

create table membership(
id varchar2(30) primary key, --not null, unique
name varchar2(30) not null,
pw varchar2(30),
email varchar2(50),
send_email number(1),
zipcode char(5),
address1 varchar2(50),
address2 varchar2(50),
phone char(11),
tel char(11),
birth date,
newyear number(1),
company number(1),
create_date date,
myip char(15)
);




-- primary key �߰� 
alter table membership add primary key(id);
-- not null ����
alter table membership modify name not null;

desc membership;
insert into membership values(
'aaa','ȫ�浿','1111','aaa@naver.com',1,'01222','���� ��õ�� ��õ��','101-1',
'01011111111','0211111111','1999/01/01',0,0,sysdate,'101.101.101.100'
);
insert into membership values(
'bbb','ȫ����','1111','bbb@naver.com',1,'01222','���� ��õ�� ��õ��','101-1',
'01022222222','0222222222','1980/01/01',0,0,sysdate,'101.101.101.92'
);
insert into membership values(
'ccc','ȫ���','1111','ccc@naver.com',1,'01333','���� ������ ������','101-1',
'01033333333','0233333333','1988/01/01',0,0,sysdate,'101.101.101.1'
);
insert into membership values(
'ddd','�̼���','1111','ddd@naver.com',1,'01333','���� ���ı� ���ĵ�','101-1',
'01044444444','0244444444','2012/01/01',0,0,sysdate,'101.101.101.21'
);
insert into membership values(
'eee','������','5555','eee@naver.com',1,'01333','���� ���α� ���ε�','101-1',
'01055555555','0255555555','2002/01/01',0,0,sysdate,'101.101.101.11'
);


select * from membership;
commit;

select * from membership where birth>to_date('2004/01/01');


select * from membership where months_between(sysdate,birth)<216;

create table board(
bno number(4) primary key,
id varchar2(30) not null,
title varchar2(100),
content varchar2(3000),
create_date date,
hit number(4) default 0,
-- ����: idex�� mem_fk_id,  �ܷ�Ű(�÷�) ��ġ membership ���̺� id
constraint mem_fk_id foreign key(id) references membership(id)

);



insert into board values(board_seq.nextval, 'eee','�Խ�������3','�Խ��ǿ����� ������ �Է��մϴ�.',sysdate,1);
commit;
select * from board;

delete membership where id = 'eee';


select sysdate-to_date('22/03/08') from dual;
select to_date('22/03/08')-sysdate from dual;

select hire_date, to_char(hire_date,'yyyy/mm/dd day')from employees;
update member set create_date=sysdate 
where id ='aaa';
commit;
select * from member;

select to_char(sysdate,'hh') hour,to_char(sysdate,'mi') minute from dual;

select * from studata;

select to_char(avg,'99.00')from studata;

select to_char(to_date('22/03/08'),'yyyy-mm-dd')from dual;

select * from employees where hire_date='20080113';
select * from employees where hire_date=to_date(20080113,'yyyy/mm/dd');

select '20,000'-'19,000' from dual;
select to_number('20,000','99,999')-to_number('19,000','99,999') from dual;
select to_number(replace('20,000',',','')) from dual;

--manager_id == null -> 999�� ceo�� ǥ���ϼ���

select manager_id, nvl( manager_id,999) from employees;

select manager_id, nvl( to_char(manager_id),'ceo') from employees;


select * from students;
select min(kor) from students;
select min(salary) from employees; 
select count(*) from employees;
select count(*), count(employee_id),count(manager_id),min(salary) from employees;
select round(avg(salary),2) from employees;

select emp_name, salary from employees
where salary<(select avg(salary) from employees);
select count(*) from employees
where salary<(select avg(salary) from employees);

select department_id from employees;
select department_id, department_name from departments;

select sum(salary) from employees; 

select sum(salary) from employees
where department_id=60; 

select department_id,sum(salary),count(*) from employees
group by department_id order by department_id; 


select * from employees
where mod(employee_id,2)=1
order by employee_id;

select abs(months_between(hire_date,sysdate)) from employees;
select months_between(sysdate,hire_date) from employees;

select sysdate-to_date('20180101','yyyymmdd') from dual;

create table emp02(
id varchar2(20),
content clob
);

insert into emp02 values(
'aaa','���� ���ڰ� �� �� �ֽ��ϴ�. �����ΰ���??'
);
select * from emp02;

commit;


select * from emp01;
alter table emp01 add(job varchar2(9));

alter table emp01 modify(job varchar2(30));

desc emp01;

update emp01 
set job=null 
where empno<10;

alter table emp01 modify(job number(10));
alter table emp01 drop column job;

commit;


select * from studata2;
update studata2 
set kor=0, total=0+eng+math, avg=(0+eng+math)/3
where stuno=8;

select * from studata2 order by stuno;

rollback;