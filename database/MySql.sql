-- criar no mysql
CREATE DATABASE Ingresso;

CREATE TABLE User (
    Id CHAR(36) NOT NULL,
    Name NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) NOT NULL, 
    Cpf NVARCHAR(85) NULL,
    PasswordHash NVARCHAR(255) NOT NULL,
    ConfirmEmail INT NULL,
    CONSTRAINT PK_User PRIMARY KEY(Id),
    CONSTRAINT UQ_User_Email UNIQUE(Email),
    CONSTRAINT UQ_User_Cpf UNIQUE(Cpf)
);

CREATE INDEX IX_User_Email ON User(Email);
CREATE INDEX IX_User_Cpf ON User(Cpf);

CREATE TABLE AdditionalInfoUser (
    Id INT NOT NULL AUTO_INCREMENT,
    UserId CHAR(36) NOT NULL,
    BirthDate DATETIME NULL,
    Gender NVARCHAR(50) NULL,
    Phone NVARCHAR(88) NULL,
    Cep NVARCHAR(40) NULL,
    Logradouro NVARCHAR(60) NULL,
    Numero NVARCHAR(30) NULL,
    Complemento NVARCHAR(40) NULL,
    Referencia NVARCHAR(40) NULL,
    Bairro NVARCHAR(50) NULL,
    Estado NVARCHAR(20) NULL,
    Cidade NVARCHAR(60) NULL,
    CONSTRAINT PK_AdditionalInfoUser PRIMARY KEY(Id),
    CONSTRAINT FK_IdUser FOREIGN KEY(UserId) REFERENCES User(Id)
);

CREATE TABLE Permission (
    Id INT NOT NULL AUTO_INCREMENT,
    VisualName NVARCHAR(70) NOT NULL,
    PermissionName NVARCHAR(70) NOT NULL, 
    CONSTRAINT PK_Permission PRIMARY KEY(Id)
);

CREATE TABLE UserPermission (
    Id INT NOT NULL AUTO_INCREMENT,
    UserId CHAR(36) NOT NULL,
    PermissionId INT NOT NULL, 
    CONSTRAINT PK_UserPermission PRIMARY KEY(Id),
    CONSTRAINT FK_UserPermission_User FOREIGN KEY (UserId) REFERENCES User(Id),
    CONSTRAINT FK_UserPermission_Permission FOREIGN KEY (PermissionId) REFERENCES Permission(Id)
);

CREATE TABLE Movie (
    Id CHAR(36) NOT NULL,
    Title NVARCHAR(100) NOT NULL,
    Description NVARCHAR(1000) NOT NULL,
    Gender NVARCHAR(50) NOT NULL,
    Duration NVARCHAR(30) NOT NULL,
    MovieRating INT NOT NULL,
    ImgUrl NVARCHAR(100) NOT NULL,
    PublicId NVARCHAR(70) NOT NULL,
    ImgUrlBackground NVARCHAR(100) NULL,
    PublicIdImgBackgound NVARCHAR(70) NULL,
    StatusMovie NVARCHAR(30) NOT NULL,
    CONSTRAINT PK_Movie PRIMARY KEY(Id)
);

CREATE TABLE Region (
    Id CHAR(36) NOT NULL,
    State NVARCHAR(70) NOT NULL,
    City NVARCHAR(70) NOT NULL,
    CONSTRAINT PK_Region PRIMARY KEY(Id)
);

CREATE TABLE MovieTheater (
    Id CHAR(36) NOT NULL,
    MovieId CHAR(36) NOT NULL,
    RegionId CHAR(36) NOT NULL,
    CONSTRAINT PK_MovieTheater PRIMARY KEY(Id),
    CONSTRAINT FK_MovieTheater_Movie FOREIGN KEY(MovieId) REFERENCES Movie(Id),
    CONSTRAINT FK_MovieTheater_Region FOREIGN KEY(RegionId) REFERENCES Region(Id)
);

CREATE TABLE Theatre (
    Id CHAR(36) NOT NULL,
    Title NVARCHAR(100) NOT NULL,
    Description NVARCHAR(1000) NOT NULL,
    Data DATETIME NOT NULL,
    Location NVARCHAR(100) NOT NULL,
    TypeOfAttraction NVARCHAR(70) NOT NULL,
    Category NVARCHAR(70) NOT NULL,
    PublicId NVARCHAR(70) NOT NULL,
    ImgUrl NVARCHAR(100) NOT NULL,
    CONSTRAINT PK_Theatre PRIMARY KEY(Id)
);

CREATE TABLE RegionTheatre (
    Id CHAR(36) NOT NULL,
    TheatreId CHAR(36) NOT NULL,
    RegionId CHAR(36) NOT NULL,
    CONSTRAINT PK_RegionTheatre PRIMARY KEY(Id),
    CONSTRAINT FK_RegionTheatre_Theatre FOREIGN KEY(TheatreId) REFERENCES Theatre(Id),
    CONSTRAINT FK_RegionTheatre_Region FOREIGN KEY(RegionId) REFERENCES Region(Id)
);

CREATE TABLE Cinema (
    Id CHAR(36) NOT NULL,
    NameCinema NVARCHAR(120) NOT NULL,
    District NVARCHAR(120) NOT NULL,
    Ranking NVARCHAR(100) NOT NULL,
    CONSTRAINT PK_Cinema PRIMARY KEY(Id)
);

CREATE TABLE MovieRegionTicketsPurchased (
    Id CHAR(36) NOT NULL,
    TicketsSeats NVARCHAR(200) NULL,
    MovieId CHAR(36) NOT NULL,
    CinemaId CHAR(36) NOT NULL,
    CONSTRAINT PK_MovieRegionTicketsPurchased PRIMARY KEY(Id),
    CONSTRAINT FK_MovieRegionTicketsPurchased_Movie FOREIGN KEY(MovieId) REFERENCES Movie(Id),
    CONSTRAINT FK_MovieRegionTicketsPurchased_Cinema FOREIGN KEY(CinemaId) REFERENCES Cinema(Id)
);

CREATE TABLE CinemaMovie (
    Id CHAR(36) NOT NULL,
    CinemaId CHAR(36) NOT NULL,
    MovieId CHAR(36) NOT NULL,
    RegionId CHAR(36) NOT NULL,
    ScreeningSchedule NVARCHAR(150) NOT NULL,
    CONSTRAINT PK_CinemaMovie PRIMARY KEY(Id),
    CONSTRAINT FK_CinemaMovie_Cinema FOREIGN KEY(CinemaId) REFERENCES Cinema(Id),
    CONSTRAINT FK_CinemaMovie_Region FOREIGN KEY(RegionId) REFERENCES Region(Id),
    CONSTRAINT FK_CinemaMovie_Movie FOREIGN KEY(MovieId) REFERENCES Movie(Id)
);

CREATE TABLE FormOfPayment (
    Id CHAR(36) NOT NULL,
    FormName NVARCHAR(60) NOT NULL,
    Price NVARCHAR(60) NOT NULL,
    MovieId CHAR(36) NOT NULL,
    CONSTRAINT PK_FormOfPayment PRIMARY KEY(Id),
    CONSTRAINT FK_FormOfPayment_Movie FOREIGN KEY(MovieId) REFERENCES Movie(Id)
);

CREATE TABLE AdditionalFoodMovie (
    Id CHAR(36) NOT NULL,
    Title NVARCHAR(100) NOT NULL,
    Price NVARCHAR(60) NOT NULL,
    Fee NVARCHAR(60) NOT NULL,
    ImgUrl NVARCHAR(140) NOT NULL,
    PublicId NVARCHAR(70) NOT NULL,
    MovieId CHAR(36) NOT NULL,
    CONSTRAINT PK_AdditionalFoodMovie PRIMARY KEY(Id),
    CONSTRAINT FK_AdditionalFoodMovie_Movie FOREIGN KEY(MovieId) REFERENCES Movie(Id)
);
