--cria a tabela com um campo JSON

CREATE TABLE pedidos (
nrped serial PRIMARY KEY,
detalhes json NOT NULL);

INSERT INTO pedidos(detalhes) VALUES
('{"cliente":"Nei","produto":"Smartphone Xiaomi","qtd":8}'),
('{"cliente":"Rui","produto":"Tablet Samsung","qtd":9}'),
('{"cliente":"Lia","produto":"Smartphone iPhone","qtd":5,"peso":194 }');


INSERT INTO pedidos (detalhes) VALUES('{"cliente":"Ana", "itens":{"produto":"tablet", "qtd":2}}')

SELECT detalhes->'cliente' AS cliente FROM pedidos