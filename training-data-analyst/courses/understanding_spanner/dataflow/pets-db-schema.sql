CREATE TABLE Pets (
     PetID INT64 NOT NULL, 
     OwnerID INT64 NOT NULL, 
     PetType STRING(MAX) NOT NULL,
     PetName STRING(MAX) NOT NULL,
     Breed STRING(MAX) NOT NULL,
) PRIMARY KEY (PetID);