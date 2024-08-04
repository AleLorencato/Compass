CREATE TABLE Cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(255),
    cidadeCliente VARCHAR(255),
    estadoCliente VARCHAR(255),
    paisCliente VARCHAR(255)
);

CREATE TABLE Vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(255),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(255)
);

CREATE TABLE Carro (
    idCarro INT PRIMARY KEY,
    kmCarro INT,
    chassiCarro VARCHAR(255),
    marcaCarro VARCHAR(255),
    modeloCarro VARCHAR(255),
    anoCarro INT,
    idCombustivel INT,
    FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel)
);

CREATE TABLE Combustivel (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(255)
);

CREATE TABLE Locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    idVendedor INT,
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(10, 2),
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
);

INSERT INTO Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;


INSERT OR IGNORE INTO Carro (idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT DISTINCT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
FROM tb_locacao;


INSERT OR IGNORE INTO Combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacao;


INSERT OR IGNORE INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;


INSERT INTO Locacao (idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)
SELECT idLocacao, idCliente, idCarro, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM tb_locacao;