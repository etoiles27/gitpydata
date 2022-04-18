bno --일련번호 - 답글기능이 없을때 정렬기준
btitle --제목
bcontent --내용
bdate --등록날짜
bgroup --답글그룹 - 정렬기준
bstep --답글에 대한 순서
bindent --들여쓰기
bhit --조회수
bimg --등록이미지 파일 
;

select * from board order by bno desc;

--insert into board values(board_seq.nextval, 'aaa','게시판제목5','게시판내용5',sysdate,1);
--insert into board values(board_seq.nextval, 'aaa','[답글]게시판제목2','게시판2에 답글입니다',sysdate,1);
--commit;


create table tboard(
bno number(4) primary key,--일련번호 - 답글기능이 없을때 정렬기준
id varchar2(20) not null,
btitle varchar2(200) not null, --제목
bcontent varchar2(3000),--내용
bdate date default sysdate, --등록날짜
bgroup number(4) not null, --답글그룹 - 정렬기준
bstep number(4),--답글에 대한 순서
bindent number(4),--들여쓰기
bhit number(4),--조회수
bimg varchar2(200),--등록이미지 파일 
constraint membership_fk_id foreign key(id) references membership(id)
);


delete from tboard;
desc tboard;

--insert into tboard values(b_seq.nextval, 'aaa', '첫번째 게시글','첫번째 게시글입니다',sysdate, b_seq.currval,0,0,1, '1.jpg');

select * from tboard;
--insert into tboard values(b_seq.nextval, 'bbb', '두번째 게시글','두번째 게시글입니다',sysdate, b_seq.currval,0,0,1, '1.jpg');

--insert into tboard values(b_seq.nextval, 'ccc', '3번째 게시글','3번째 게시글입니다',sysdate, b_seq.currval,0,0,1, '1.jpg');

--insert into tboard values(b_seq.nextval, 'ddd', '4번째 게시글','4번째 게시글입니다',sysdate, b_seq.currval,0,0,1, '1.jpg');

--insert into tboard values(b_seq.nextval, 'eee', '5번째 게시글','5번째 게시글입니다',sysdate, b_seq.currval,0,0,1, '1.jpg');

--insert into tboard values(b_seq.nextval, 'aaa', '6번째 게시글','6번째 게시글입니다',sysdate, b_seq.currval,0,0,1, '1.jpg');
--insert into tboard values(b_seq.nextval, 'bbb', '7번째 게시글','6번째 게시글입니다',sysdate, b_seq.currval,0,0,1, '1.jpg');
--insert into tboard values(b_seq.nextval, 'ccc', '8번째 게시글','8번째 게시글입니다',sysdate, b_seq.currval,0,0,1, '1.jpg');

--insert into tboard values(b_seq.nextval, 'ddd', '9번째 게시글','9번째 게시글입니다',sysdate, b_seq.currval,0,0,1, '1.jpg');
--insert into tboard values(b_seq.nextval, 'eee', '10번째 게시글','10번째 게시글입니다',sysdate, b_seq.currval,0,0,1, '1.jpg');

--insert into tboard values(b_seq.nextval, 'aaa', '[답글]5번째 게시글','[답글]5번째 게시글입니다',sysdate,5,1,1,1, '1.jpg');
--insert into tboard values(b_seq.nextval, 'aaa', '[답글]7번째 게시글','[답글]7번째 게시글입니다',sysdate,7,1,1,1, '1.jpg');
--insert into tboard values(b_seq.nextval, 'aaa', '[답글답글]7번째 게시글','[답글답글]7번째 게시글입니다',sysdate,7,2,2,1, '1.jpg');
--insert into tboard values(b_seq.nextval, 'aaa', '[답글]3번째 게시글','[답글]3번째 게시글입니다',sysdate,3,1,1,1, '1.jpg');
--insert into tboard values(b_seq.nextval, 'aaa', '[답글답글]5번째 게시글','[답글답글]5번째 게시글입니다',sysdate,5,2,2,1, '1.jpg');

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
-- null 값이 있으면 출력을 안해준다. self join의 경우
select employee_id, emp_name, manager_id from employees where manager_id is null;
select e1.employee_id, e1.emp_name, e1.manager_id ,e2.emp_name
from employees e1, employees e2
where e1.manager_id=e2.employee_id(+)
order by e1.employee_id;

--eq join & outer join
-- null 같이 조인
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


insert into studata values(stu_seq.nextval, '홍길동',100,100,90,(100+100+90),(100+100+90)/3,1);

update studata set kor=90, eng=98 where stuname='홍길동';

select * from studata order by stuno desc;
rollback;
-- alter sequence stu_seq increment by 1;

select * from studata where lower(stuname)='홍길동';

select * from studata where lower(stuname) like '%홍%';

delete studata where stuname=':1'
