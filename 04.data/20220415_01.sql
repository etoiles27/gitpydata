select * from tab;

--rename studata2 to sturank;

select * from board;
select * from membership;

insert into board values(
board_seq.nextval, 'ccc','�̺�Ʈ�� �����մϴ�','�̺�Ʈ ��ǰ�� �����մϴ�',sysdate,1);

create table emp02(
empno number(4) primary key,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2) check(deptno between 10 and 19),
gender char(1) check(gender in('M','F'))
);

insert into emp02 values(EMP_SEQ.nextval, 'ȫ�浿','manager',10,'M');
insert into emp02 values(EMP_SEQ.nextval, 'ȫ����','manager',10,'F');
insert into emp02 values(EMP_SEQ.nextval, 'ȫ���','manager',18,'F');


select * from emp02;

-- emp01 �����, 

create table emp01(
EMPLOYEE_ID NUMBER(6) primary key,
EMP_NAME VARCHAR2(80) unique,
SALARY NUMBER(8,2) not null,
MANAGER_ID NUMBER(6),
DEPARTMENT_ID NUMBER(6)
);

insert into emp01 (EMPLOYEE_ID,EMP_NAME,SALARY,MANAGER_ID,DEPARTMENT_ID)
select EMPLOYEE_ID,EMP_NAME,SALARY,MANAGER_ID,DEPARTMENT_ID from employees;

alter table emp01 
add constraint department_fk_id foreign key(department_id)
references departments(department_id); 

alter table emp01 drop primary key;
desc emp01;
alter table emp01 add primary key(employee_id);


select * from students ;
select * from sturank ;

update sturank set stuname='eee' where stuno=5;
select * from membership;

alter table sturank 
add constraint sturank_fk_id foreign key(stuname)
references membership(id); 

alter table sturank rename column stuname to id;

-- 11�� ��
-- decode �� ��ġ�ؾ����� ��Ÿ����. 
select * from employees;

select emp_name, department_id, 
decode(department_id,20,'���������',
                    30,'��������',
                    40,'��������',
                    50,'��������')"����Ȯ��" 
from employees;

select * from students;
select stuid, stuname,avg, decode(avg,100,'����') as "����" from students;

select job_id from employees;

select employee_id, emp_name, salary, job_id,
decode(job_id,'SH_CLERK','2%�λ�',
                'AD_ASST','5%�λ�',
                'IT_PROG','3%�λ�',
                'PU_CLERK','4%�λ�') "�����λ���Ȳ"
from employees;


select employee_id, emp_name, salary, job_id,
decode(job_id,'SH_CLERK',salary*1.02,
                'AD_ASST',salary*1.05,
                'IT_PROG',salary*1.03,
                'PU_CLERK',salary*1.04) "�����λ���Ȳ"
from employees;


select employee_id, emp_name, salary,job_id||': '||
(decode (  substr(job_id,instr(job_id,'_')+1),'CLERK' ,salary*1.05,
                'MAN',salary*1.07,
                'REP',salary*1.04,
                'ACCOUNT',salary*1.06))"�����λ���Ȳ"
from employees;



select emp_name from employees where lower(emp_name) like '%su%';

select substr(job_id,4) from employees;



select employee_id, emp_name, job_id, salary,
case when substr(job_id,4)='CLERK' then salary*1.05
     when substr(job_id,4)='MAN' then salary*1.07
     when substr(job_id,4)='REP' then salary*1.04
     when substr(job_id,4)='ACCOUNT' then salary*1.06
else salary 
end as "�����λ���Ȳ"
from employees;

select * from studata;

select stuno, stuname, avg, 
case when avg>=90 then 'A'
     when avg>=80 then 'B'
     when avg>=70 then 'C'
     when avg>=60 then 'D'
else 'F'
end as "�������"
from studata;

-- 12�� �׷��Լ�

select count(*), count(manager_id), count(commission_pct) from employees;
select commission_pct from employees;
select count(*)-count(commission_pct)"��Ŀ�̼�",count(commission_pct)"Ŀ�̼�" from employees;

select count(*) from employees where commission_pct is null;

select emp_name, sum(salary) from employees
group by emp_name;

select department_id, count(*),sum(salary),
round(avg(salary),2),max(salary),min(salary) from employees
group by department_id;

--60�� �μ� �ִ� ���� 


select employee_id, emp_name, salary , department_id 
from employees where salary =
(select max(salary) from employees where department_id=60 group by department_id) 
and department_id=60;


select employee_id, emp_name, salary , department_id 
from employees where salary =
(select  max(salary) from employees  where department_id=60) and department_id=60;

select department_id,count(*),count(commission_pct), count(*)-count(commission_pct)
from employees group by department_id;


select department_id, round(avg(salary),2) from employees 
where department_id>40
group by department_id
having avg(salary)>=4000
order by department_id;

--�μ��� �ִ���� ���, 5000�޷� �̻��� �ִ밪��
select department_id, max(salary) from employees 
group by department_id
having avg(salary)>=5000
order by max(salary);

-- 13�� join
select department_id from employees;
select department_id , department_name from departments;

select * from employees,departments;

create table employees2 as 
select department_id , department_name from departments;

select * from employees2;

update employees2 set department_name='��ȹ��'
where department_id=10;

select * from employees2,departments;

-- eq join ��Ī�� �� �� �ִ�. 
select employee_id, emp_name, e.department_id,department_name
from employees e, departments d
where e.department_id = d.department_id;

--eq join job_id, job_name

select employee_id, emp_name, e.job_id, job_title
from employees e, jobs j
where e.job_id = j.job_id;


select * from board;
select * from membership;

select bno, name  ,title, content, b.create_date, hit
from board b, membership m
where b.id =  m.id;


select employee_id,emp_name, e.job_id, job_title, e.department_id, department_name
from employees e, jobs j, departments d
where e.job_id = j.job_id and e.department_id = d.department_id
and e.employee_id >= 150 
and lower(e.emp_name) like '%s%';



select employee_id,emp_name, e.job_id, job_title, e.department_id, department_name
from employees e, jobs j, departments d
where e.job_id = j.job_id and e.department_id = d.department_id(+) 
order by employee_id;

select * from employees order by employee_id;
select * from employees where department_id is null;
select * from countries;



-- �̺�Ʈ �Խ���, ���̺� ����. 
create table eventboard(
eb_idx number(20), -- �Խù� ������ȣ
eb_code number(20), -- ������, ����, ��÷�� �˷��ִ� �ڵ� 
eb_title varchar2(30), -- �Խù� ����
eb_contents varchar2(10000), -- �Խù�����
eb_img varchar2(50), -- �Խù��� ���Ǵ� �̹��� ���� �ּ�
eb_winner varchar2(50), -- ��÷��
eb_startday date, -- �̺�Ʈ���۳�
eb_endday date, -- �̺�Ʈ ���ᳯ
eb_write_time date, --�Խù� �ۼ���
eb_hit number(20), -- ��ȸ��
u_id varchar2(20), -- ����� ���̵�
u_ip char(20) --������� ������
);




select * from kor_loan_status;

select region, sum(loan_jan_amt) from kor_loan_status
group by region;


select substr(period,1,4),region, sum(loan_jan_amt) from kor_loan_status
group by substr(period,1,4) , region
order by substr(period,1,4);


select substr(period,1,4) newp,region, sum(loan_jan_amt) from kor_loan_status
group by substr(period,1,4), region
order by sum(loan_jan_amt) desc;



create table test1(
ind number generated always as identity primary key,
content varchar2(3000)
);

insert into test1 (content) values('aaaaaaaaaaaaaaaaaa');
insert into test1 (content) values('bbbbbbbbbbbbbbbbbbbb');
select * from test1;



create table salary_grade(
grade number(1),
low_salary number(5),
high_salary number(5)
);
insert into salary_grade values(1,2000,3000);
insert into salary_grade values(2,3001,5000);
insert into salary_grade values(3,5001,8000);
insert into salary_grade values(4,8001,10000);
insert into salary_grade values(5,10001,30000);

commit;

select * from salary_grade;

-- non eq join



select employee_id, emp_name, salary, grade
from employees, salary_grade
where salary between low_salary and high_salary
order by employee_id
;

select employee_id,emp_name,
case when salary>=10001 then 5
     when salary>=8001 then 4
     when salary>=5001 then 3
     when salary>=3001 then 2
     when salary>=2000 then 1
end as "grade"
from employees order by employee_id;


-- 

create table stu_grade(
grade char(2),
low_score number(5),
high_score number(5)
);

insert into stu_grade values('A+',95,100);
insert into stu_grade values('A',90,94);
insert into stu_grade values('B+',85,89);
insert into stu_grade values('B',80,84);
insert into stu_grade values('C',0,79);


commit;
select * from stu_grade;


select stuno, stuname, grade
from studata, stu_grade
where avg between low_score and high_score
order by stuno
;

--selfjoin �ڱ��ڽ����̺�2���� ����

select e1.employee_id, e1.emp_name, e1.manager_id ,e2.emp_name
from employees e1, employees e2
where e1.manager_id=e2.employee_id(+)
order by e1.employee_id;


