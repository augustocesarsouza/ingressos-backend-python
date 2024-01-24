create database Ingresso;

use Ingresso;
create table User (
	Id CHAR(36) NOT NULL,
    Name NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) NOT NULL,
    Cpf NVARCHAR(85) NULL,
    PasswordHash NVARCHAR(255) NOT NULL,
    ConfirmEmail INT NULL,

	PRIMARY KEY (Id),
    UNIQUE KEY UQ_User_Email (Email),
    UNIQUE KEY UQ_User_Cpf (Cpf)
);
CREATE INDEX IX_User_Email ON User (Email);
CREATE INDEX IX_User_Cpf ON User (Cpf);

use Ingresso;
create table Permission (
	Id INT NOT NULL auto_increment,
    VisualName NVARCHAR(70) NOT NULL,
    PermissionName NVARCHAR(70) NOT NULL,
    
    PRIMARY KEY (Id)
);

INSERT INTO Permission(VisualName, PermissionName) VALUES ('moderator', 'mod');
SELECT * FROM Permission;

use Ingresso;
create table UserPermission (
	Id INT NOT NULL auto_increment,
    UserId CHAR(36) NOT NULL,
    PermissionId INT NOT NULL,
    
    PRIMARY KEY (Id),
    FOREIGN KEY (UserId) REFERENCES User(Id),
    FOREIGN KEY (PermissionId) REFERENCES Permission(Id)
);