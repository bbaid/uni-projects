use movies;

insert into MOVIESTAR (NAME, GENDER)
values ('Jennifer Aniston', 'F');

select * from MOVIESTAR

use ships;

insert into BATTLES
values ('Denmark Strait', '1941-05-24')

select * from BATTLES

-- deleting 

delete from battles
where name = 'Denmark Strait'

use movies;

delete from MOVIESTAR
where name like 'Jen%'


use pc;

update printer
set price = price * 0.9
where color = 'y';

select * from printer;

--- exercise

use movies;

insert into MOVIESTAR (NAME, GENDER, BIRTHDATE)
values ('Nicole Kidman', 'F', '1967-06-20');

delete from MOVIEEXEC
where NETWORTH < 10000000;

select * from MOVIESTAR where ADDRESS is null

delete from MOVIESTAR where ADDRESS is null

select *
from MOVIEEXEC
where CERT# in (select PRESC# from studio)

update MOVIEEXEC
set name = 'Pres. ' + name
where CERT# in (select presc# from STUDIO);

use pc;

insert into product(model, maker, type)
values ('1100', 'C', 'PC')
insert into pc(model, speed, ram, hd, cd, price)
values ('1100', 2400, 2048, 500, '52x', 299)


delete from pc
where model = '1100'
delete from product
where model = '1100'

insert into product (model, maker, type)
select distinct model, 'Z', 'Laptop' from pc;

insert into laptop (code, model, speed, ram, hd, price, screen)
select code+100, model, speed, ram, hd, price+500, 15 from pc;

select * from laptop

delete from laptop
where model in (select model
				from product
				where type='Laptop' and
				maker not in (select maker
							from product
							where type='printer'))

update product
set maker = 'A'
where maker = 'B';

update pc
set price = price/2, hd = hd+20

update laptop
set screen = screen+1
where model in (select model
				from product
				where maker = 'B')


use ships;

