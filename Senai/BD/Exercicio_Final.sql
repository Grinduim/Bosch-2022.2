use master ;

go 

if Exists(select * from sys.databases where name =  N'Exercicio')
	BEGIN
		drop DATABASE Exercicio
	END

GO

Create DATABASE Exercicio;

GO

USE Exercicio;

GO

Create SCHEMA Escola;

Go

CREATE TABLE Escola.Aluno 
(
    ID INT NOT NULL PRIMARY KEY IDENTITY(1,1) ,
    Nome VARCHAR(max) not null,
    Cpf VARCHAR(14) not null,
    Data_Nascimento Date NOT NULL,
    Situacao bit NOT NULL
);

GO

CREATE TABLE Escola.Professor
(
    ID INT PRIMARY KEY IDENTITY(1,1),
    Nome VARCHAR(max) not null,
    Cpf VARCHAR(14) not null
);

GO

CREATE TABLE Escola.Curso
(
    ID INT PRIMARY KEY IDENTITY(1,1),
    Nome VARCHAR(max) not null,
    Ativo bit NOT NULL
);

GO

CREATE TABLE Escola.Disciplina
(
    ID INT PRIMARY KEY IDENTITY(1,1),
    Nome VARCHAR(max) not null,
    Ativo bit NOT NULL
);

GO

CREATE TABLE Escola.Disciplina_Curso
(
    ID INT PRIMARY KEY IDENTITY(1,1),
    ID_Curso int FOREIGN KEY REFERENCES Escola.Curso(ID),
    ID_Disciplina int FOREIGN KEY REFERENCES Escola.Disciplina(ID),
    Ativo bit NOT NULL
);

GO

CREATE TABLE Escola.Turma
(
    ID INT PRIMARY KEY IDENTITY(1,1),
    ID_Aluno int FOREIGN KEY REFERENCES Escola.Aluno(ID),
    ID_Profesor INT FOREIGN KEY REFERENCES Escola.Professor(ID),
    ID_Disciplina_Curso INT FOREIGN KEY REFERENCES Escola.Disciplina_Curso(ID),
    Nota1 DECIMAL(19,3) not NULL,
    Nota2 DECIMAL(19,3) not NULL,
    Nota3 DECIMAL(19,3) not NULL,
    Nota4 DECIMAL(19,3) not NULL,
    NotaFinal DECIMAL(19,3) not NULL,
    Ativo bit NOT NULL
);

GO

CREATE SCHEMA Secretaria;

GO

CREATE TABLE Secretaria.Pagamentos
(
    ID INT PRIMARY KEY IDENTITY(1,1),
    ID_Aluno int FOREIGN KEY REFERENCES Escola.Aluno(ID),
    Boleto DATE not NULL,
    Ativo bit
)

GO

CREATE TABLE Secretaria.Inadimplente
(
    ID INT PRIMARY KEY IDENTITY(1,1),
    ID_Aluno int FOREIGN KEY REFERENCES Escola.Aluno(ID),
    Data_Registro DATE not NULL,
)

GO

CREATE SCHEMA ADM;

GO

CREATE TABLE ADM.Logs
(
    ID INT NOT NULL PRIMARY KEY IDENTITY(1,1) ,
    Tabela VARCHAR(max),
    Comando VARCHAR(max),
    Mensagem_Do_Erro VARCHAR(max),
    Data DATEtime
)

GO

create FUNCTION VerificaIdade(@Data date, @Idade int)
RETURNS BIT
BEGIN
    IF((select DATEDIFF(year, @Data, GETDATE())) >= @Idade)
        RETURN 1
    RETURN 0
END

GO

create PROCEDURE NewAluno
    @Nome VARCHAR(max), 
    @Cpf VARCHAR(14), 
    @Data_Nascimento Date, 
    @Situacao bit

AS BEGIN TRY
	DECLARE @Response BIT 
	EXEC @Response = VerificaIdade @Data_Nascimento, 18
    IF ( @Response = 1)
        BEGIN
            INSERT INTO escola.aluno(Nome, Cpf, Data_Nascimento, Situacao)
            VALUES (@Nome, @Cpf, @Data_Nascimento, 1 )
            RETURN
        END
    
    RAISERROR(1500, -1,-1, 'ERRO AO INSERIR ALUNO, IDADE INVALIDA')
END TRY
BEGIN CATCH
    INSERT INTO ADM.Logs(Tabela, Comando, Mensagem_Do_Erro, Data)
    VALUES ('Aluno', 'Insert - Via Procedure', ERROR_MESSAGE(), GETDATE())


END CATCH

GO

CREATE PROCEDURE UpdateAluno
    @Nome VARCHAR(max), 
    @Cpf VARCHAR(14), 
    @Data_Nascimento Date, 
    @Situacao bit,
    @ID int

AS BEGIN TRY

    DECLARE @Response BIT 
	EXEC @Response = VerificaIdade @Data_Nascimento, 18

    IF ( @Response = 1)
        BEGIN
            UPDATE Escola.Aluno
            set Nome = @Nome, Cpf = @Cpf, Data_Nascimento = @Data_Nascimento, Situacao = @Situacao
            where ID = @ID
        END

    RAISERROR(1500, -1,-1, 'ERRO AO INSERIR ALUNO, IDADE INVALIDA')

END TRY

BEGIN CATCH

    INSERT INTO ADM.Logs(Tabela, Comando, Mensagem_Do_Erro, Data)
    VALUES ('Aluno', 'Update - Via Procedure', ERROR_MESSAGE(), GETDATE())

END CATCH

GO

CREATE PROCEDURE DeleteAluno
    @ID INT

AS BEGIN TRY
    DELETE FROM  Escola.Aluno WHERE ID = @ID
END TRY
BEGIN CATCH
    INSERT INTO ADM.Logs(Tabela, Comando, Mensagem_Do_Erro, Data)
    VALUES ('Aluno', 'DELETE - Via Procedure', ERROR_MESSAGE(), GETDATE())
END CATCH

GO

exec NewAluno 'Vinicius', '1233.331', '2002-11-07', 1
SELECT * FROM Escola.Aluno

EXEC UpdateAluno 'Vinicius2', '1233.331', '2002-11-07', 1,1
SELECT * FROM Escola.Aluno

-- exec DeleteAluno 1
-- SELECT * FROM Escola.Aluno

GO

CREATE PROCEDURE NewPagamento
    @ID_Aluno int,
    @Boleto DATE

AS BEGIN TRY

    INSERT INTO Secretaria.Pagamentos(ID_Aluno, Boleto, Ativo)
    VALUES (@ID_Aluno, @Boleto, 0)

END TRY

BEGIN CATCH

    INSERT INTO ADM.Logs(Tabela, Comando, Mensagem_Do_Erro, Data)
    VALUES ('Secretaria.Pagamento', 'Insert - Via Procedure', ERROR_MESSAGE(), GETDATE())

END CATCH

GO

CREATE PROCEDURE UpdadePagamento
    @ID INT,
    @ID_Aluno int,
    @Boleto Date,
    @Ativo bit
AS BEGIN TRY
    UPDATE Secretaria.Pagamentos
    set ID_Aluno = @ID_Aluno, Ativo =  @Ativo, Boleto = @Boleto where ID = @ID

END TRY

BEGIN CATCH

    INSERT INTO ADM.Logs(Tabela, Comando, Mensagem_Do_Erro, Data)
    VALUES ('Secretaria.Pagamento', 'Update - Via Procedure', ERROR_MESSAGE(), GETDATE())

END CATCH

GO


CREATE PROCEDURE DeletePagamento
    @ID INT
AS BEGIN TRY
    DELETE FROM  Secretaria.Pagamentos WHERE ID = @ID
END TRY
BEGIN CATCH
    INSERT INTO ADM.Logs(Tabela, Comando, Mensagem_Do_Erro, Data)
    VALUES ('Secretaria.Pagamento', 'DELETE - Via Procedure', ERROR_MESSAGE(), GETDATE())
END CATCH

GO

Exec NewPagamentO 1, '2022-12-24'
SELECT * FROM Secretaria.Pagamentos

EXEC UpdadePagamento 1,1,'2022-12-24', null
SELECT * FROM Secretaria.Pagamentos

EXEC DeletePagamento 1
SELECT * FROM Secretaria.Pagamentos