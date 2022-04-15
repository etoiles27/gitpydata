-- 시퀀스 생성
CREATE SEQUENCE test_seq 
INCREMENT BY 1 
START WITH 1 
MAXVALUE 9999
MINVALUE 1
nocycle
nocache;

-- 시퀀스 수정
alter sequence test_seq
maxvalue 99999
INCREMENT BY 10 
;
--시퀀스 확인
select test_seq.currval from dual;

--drop table employees2;
-- 시퀀스번호, 사원번호, 사원명, job_id, 입사일, employees2 입사일 오름차순


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

--문자길이

select emp_name, length(emp_name), lengthb(emp_name) from employees;

select stuname, length(stuname),lengthb(stuname) from students;

--문자열추출 substr
select emp_name, substr(emp_name,0,6) from employees;
select emp_name, substr(emp_name,7) from employees;
select emp_name, substr(emp_name,-1) from employees;

alter table member add juminno char(14);

update member set password='5555', juminno='880505-1105555' where id ='eee';

select name, substr(juminno,1,6) "주민번호앞자리", 
substr(juminno,8) "주민번호뒷자리" from member;

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

--특정 문자 위치 찾기 instr

--insert into member values('fff','6666','홍길순','010-0000-0000',300,100,'010101-4105555','abc.jason');


select filename,instr(filename,'.'),substr(filename,instr(filename,'.')+1) from member;

-- 문자 대체 : replace 공백이 있으면 공백을 지울수 잇다. 
select emp_name from employees;
select replace(emp_name,' ','') from employees;
--trim, ltrim, rtrim



insert into member values('hhh','     7777','홍길영      ','010-   9999-0000',300,100,'000901-4105555','    abc.js');
update member set name=rtrim(name);
update member set phone=replace(phone,' ','');
select length(rtrim(phone)),length(phone) from member;
select * from member;

commit;

-- 문자열 합치기 concat
select concat(id,concat('-',password)) from member;
select id||'-'||password from member;

-- 특정문자 채우기 lpad, rpad

select rpad(id,10,'*') from member;
select juminno from member;
select rpad(substr(juminno,1,8),14,'*') from member;

-- sysdate : 현재시간(날짜)
select sysdate, sysdate+1, sysdate-1 from dual;

alter table member add create_date date;
select * from member;
insert into member(id,password,create_date)
values('iii','1111',sysdate);

select to_char(create_date,'YYYY/MM/DD hh:mi:ss') from member;

select hire_date from employees; 
select sysdate-hire_date from employees;
-- 문자를 날짜로 바꾸는 to_date()
select trunc(sysdate-to_date('22/03/08')) from dual;


select emp_name,sysdate,hire_date,months_between(sysdate,hire_date) from employees;

select sysdate,'22/03/08',months_between(sysdate,to_date('22/03/08')) from dual;
select sysdate,'22/03/08',add_months(sysdate,6) from dual;

--

select sysdate, next_day(sysdate,'금요일') from dual;

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




-- primary key 추가 
alter table membership add primary key(id);
-- not null 수정
alter table membership modify name not null;

desc membership;
insert into membership values(
'aaa','홍길동','1111','aaa@naver.com',1,'01222','서울 금천구 금천동','101-1',
'01011111111','0211111111','1999/01/01',0,0,sysdate,'101.101.101.100'
);
insert into membership values(
'bbb','홍길자','1111','bbb@naver.com',1,'01222','서울 양천구 금천동','101-1',
'01022222222','0222222222','1980/01/01',0,0,sysdate,'101.101.101.92'
);
insert into membership values(
'ccc','홍길순','1111','ccc@naver.com',1,'01333','서울 강남구 강남동','101-1',
'01033333333','0233333333','1988/01/01',0,0,sysdate,'101.101.101.1'
);
insert into membership values(
'ddd','이순신','1111','ddd@naver.com',1,'01333','서울 송파구 송파동','101-1',
'01044444444','0244444444','2012/01/01',0,0,sysdate,'101.101.101.21'
);
insert into membership values(
'eee','유관순','5555','eee@naver.com',1,'01333','서울 종로구 종로동','101-1',
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
-- 선언: idex명 mem_fk_id,  외래키(컬럼) 위치 membership 테이블 id
constraint mem_fk_id foreign key(id) references membership(id)

);



insert into board values(board_seq.nextval, 'eee','게시판제목3','게시판에들어가는 내용을 입력합니다.',sysdate,1);
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

--manager_id == null -> 999로 ceo로 표시하세요

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
'aaa','많은 글자가 들어갈 수 있습니다. 정말인가요??'
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