CREATE VIEW dim_cliente AS
SELECT
    cl.idCliente,
    cl.nomeCliente,
    cl.cidadeCliente,
    cl.estadoCliente,
    cl.paisCliente
FROM Cliente cl;

CREATE VIEW dim_carro AS
SELECT
    ca.idCarro,
    ca.kmCarro,
    ca.chassiCarro,
    ca.marcaCarro,
    ca.modeloCarro,
    ca.anoCarro,
    c.idCombustivel,
    c.tipoCombustivel
FROM Carro ca join Combustivel c on c.idCombustivel = ca.idCombustivel

CREATE VIEW dim_vendedor AS
SELECT
    v.idVendedor,
    v.nomeVendedor,
    v.sexoVendedor,
    v.estadoVendedor
FROM Vendedor v;

CREATE VIEW fato_locacao AS
SELECT
    l.idLocacao,
    l.dataLocacao,
    l.horaLocacao,
    l.qtdDiaria,
    l.vlrDiaria,
    l.dataEntrega,
    l.horaEntrega,
    cl.nomeCliente,
    ca.modeloCarro,
    v.nomeVendedor,
    l.idCliente AS fk_idCliente,
    l.idCarro AS fk_idCarro,
    l.idVendedor AS fk_idVendedor
FROM Locacao l
JOIN Cliente cl ON l.idCliente = cl.idCliente
JOIN Carro ca ON l.idCarro = ca.idCarro
JOIN Vendedor v ON l.idVendedor = v.idVendedor;