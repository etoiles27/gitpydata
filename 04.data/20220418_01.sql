bno --�Ϸù�ȣ - ��۱���� ������ ���ı���
btitle --����
bcontent --����
bdate --��ϳ�¥
bgroup --��۱׷� - ���ı���
bstep --��ۿ� ���� ����
bindent --�鿩����
bhit --��ȸ��
bimg --����̹��� ���� 
;

select * from board order by bno desc;

--insert into board values(board_seq.nextval, 'aaa','�Խ�������5','�Խ��ǳ���5',sysdate,1);
--insert into board values(board_seq.nextval, 'aaa','[���]�Խ�������2','�Խ���2�� ����Դϴ�',sysdate,1);
--commit;


create table tboard(
bno number(4) primary key,--�Ϸù�ȣ - ��۱���� ������ ���ı���
id varchar2(20) not null,
btitle varchar2(200) not null, --����
bcontent varchar2(3000),--����
bdate date default sysdate, --��ϳ�¥
bgroup number(4) not null, --��۱׷� - ���ı���
bstep number(4),--��ۿ� ���� ����
bindent number(4),--�鿩����
bhit number(4),--��ȸ��
bimg varchar2(200),--����̹��� ���� 
constraint membership_fk_id foreign key(id) references membership(id)
);


delete from tboard;
desc tboard;

--insert into tboard values(b_seq.nextval, 'aaa', 'ù��° �Խñ�','ù��° �Խñ��Դϴ�',sysdate, b_seq.currval,0,0,1, '1.jpg');

select * from tboard;
--insert into tboard values(b_seq.nextval, 'bbb', '�ι�° �Խñ�','�ι�° �Խñ��Դϴ�',sysdate, b_seq.currval,0,0,1, '1.jpg');

--insert into tboard values(b_seq.nextval, 'ccc', '3��° �Խñ�','3��° �Խñ��Դϴ�',sysdate, b_seq.currval,0,0,1, '1.jpg');

--insert into tboard values(b_seq.nextval, 'ddd', '4��° �Խñ�','4��° �Խñ��Դϴ�',sysdate, b_seq.currval,0,0,1, '1.jpg');

--insert into tboard values(b_seq.nextval, 'eee', '5��° �Խñ�','5��° �Խñ��Դϴ�',sysdate, b_seq.currval,0,0,1, '1.jpg');

--insert into tboard values(b_seq.nextval, 'aaa', '6��° �Խñ�','6��° �Խñ��Դϴ�',sysdate, b_seq.currval,0,0,1, '1.jpg');
--insert into tboard values(b_seq.nextval, 'bbb', '7��° �Խñ�','6��° �Խñ��Դϴ�',sysdate, b_seq.currval,0,0,1, '1.jpg');
--insert into tboard values(b_seq.nextval, 'ccc', '8��° �Խñ�','8��° �Խñ��Դϴ�',sysdate, b_seq.currval,0,0,1, '1.jpg');

--insert into tboard values(b_seq.nextval, 'ddd', '9��° �Խñ�','9��° �Խñ��Դϴ�',sysdate, b_seq.currval,0,0,1, '1.jpg');
--insert into tboard values(b_seq.nextval, 'eee', '10��° �Խñ�','10��° �Խñ��Դϴ�',sysdate, b_seq.currval,0,0,1, '1.jpg');

--insert into tboard values(b_seq.nextval, 'aaa', '[���]5��° �Խñ�','[���]5��° �Խñ��Դϴ�',sysdate,5,1,1,1, '1.jpg');
--insert into tboard values(b_seq.nextval, 'aaa', '[���]7��° �Խñ�','[���]7��° �Խñ��Դϴ�',sysdate,7,1,1,1, '1.jpg');
--insert into tboard values(b_seq.nextval, 'aaa', '[��۴��]7��° �Խñ�','[��۴��]7��° �Խñ��Դϴ�',sysdate,7,2,2,1, '1.jpg');
--insert into tboard values(b_seq.nextval, 'aaa', '[���]3��° �Խñ�','[���]3��° �Խñ��Դϴ�',sysdate,3,1,1,1, '1.jpg');
--insert into tboard values(b_seq.nextval, 'aaa', '[��۴��]5��° �Խñ�','[��۴��]5��° �Խñ��Դϴ�',sysdate,5,2,2,1, '1.jpg');

select * from tboard order by bgroup desc, bstep asc;
commit;



select employee_id, emp_name, manager_id from employees;

--eq join inner join
select employee_id, emp_name, employees.department_id, department_name 
from employees, departments
where employees.department_id = departments.department_id;

--self join
select e1.employee_id, e1.emp_name, e1.manager_id ,e2.emp_name
from employees e1, employees e2
where e1.manager_id=e2.employee_id
order by e1.employee_id;


--self join & outer join
-- null ���� ������ ����� �����ش�. self join�� ���
select employee_id, emp_name, manager_id from employees where manager_id is null;
select e1.employee_id, e1.emp_name, e1.manager_id ,e2.emp_name
from employees e1, employees e2
where e1.manager_id=e2.employee_id(+)
order by e1.employee_id;

--eq join & outer join
-- null ���� ����
select emp_name, department_id from employees where department_id is null;
select employee_id, emp_name, e.department_id, department_name 
from employees e, departments d
where e.department_id = d.department_id(+)
order by employee_id;

--ansi join
    -- original eq join ver
select employee_id, emp_name, e.department_id, department_name 
from employees e, departments d
where e.department_id = d.department_id;
    -- ansi  eq join ver
select employee_id, emp_name, e.department_id, department_name 
from employees e inner join departments d 
on e.department_id = d.department_id;
    -- ansi using ver
select e.employee_id, e.emp_name, d.department_name 
from employees e inner join departments d 
using (department_id);
    -- ansi natural ver
select * from employees natural join departments;
    -- ansi outer join ver
select e.employee_id, e.emp_name, d.department_name 
from employees e left outer join departments d 
using (department_id);


desc departments;


insert into studata values(stu_seq.nextval, 'ȫ�浿',100,100,90,(100+100+90),(100+100+90)/3,1);

update studata set kor=90, eng=98 where stuname='ȫ�浿';

select * from studata order by stuno desc;
rollback;
-- alter sequence stu_seq increment by 1;

select * from studata where lower(stuname)='ȫ�浿';

select * from studata where lower(stuname) like '%ȫ%';

delete studata where stuname=':1'
