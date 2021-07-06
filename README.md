# exp4
exp4 programacion web
superuser:admin
pass:1234
creacion de user database 18g
create user c##exp4 identified by 1234;
grant connect, resource to c##exp4;
alter user c##exp4 default tablespace users quota unlimited on users;
