--o queries é para guardar as consultas
select usuario from usuarios;

--Pesquisando todas as informações de admin:
select * from usuarios
where usuario = 'Admin';

--Consultar somente a senha do usuario teste:
select usuarios.senha from usuarios
where usuario = 'teste';

--Consultar sobre usuario cujo nome é Admin e senha = senhaerrada
select * from usuarios
where usuario = 'Admin' and senha = 'senhaerrada';

--Trocar a senha do usuário teste:
update usuarios
set senha = 'novaSenha456'
where usuario = 'teste';

--Criando e deletando usuário:
insert into usuarios(usuario, senha)    
values ('temporario', '123');

delete from usuarios
where usuario = 'temporario';

