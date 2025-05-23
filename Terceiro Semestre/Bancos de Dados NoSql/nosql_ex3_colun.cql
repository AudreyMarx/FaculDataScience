-- exemplo de um comando para criar uma tabela no Cassandra

CREATE COLUMNFAMILY cliente (
codigo varchar primary key,
nome varchar,
cidade varchar )