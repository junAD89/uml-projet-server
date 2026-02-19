pour se connecter a la base de donne on utilise

# USE bibliotheque;

CREATE TABLE Adherent (  
 id_adherent INT AUTO_INCREMENT PRIMARY KEY,
nom VARCHAR(50) NOT NULL,
prenom VARCHAR(50) NOT NULL,
email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Bibliotheque (
id_bibliotheque INT AUTO_INCREMENT PRIMARY KEY,
nom_bibliotheque VARCHAR(100) NOT NULL,
adresse VARCHAR(150) NOT NULL
);

CREATE TABLE Categorie (
id_categorie INT AUTO_INCREMENT PRIMARY KEY,
nom_categorie VARCHAR(100) NOT NULL,
description TEXT
);

CREATE TABLE Livre (
id_livre INT AUTO_INCREMENT PRIMARY KEY,
titre VARCHAR(150) NOT NULL,
auteur VARCHAR(100) NOT NULL,
editeur VARCHAR(100),
annee_publication INT,
statut VARCHAR(30) NOT NULL,
id_categorie INT NOT NULL,
id_bibliotheque INT NOT NULL,
FOREIGN KEY (id_categorie) REFERENCES Categorie(id_categorie),
FOREIGN KEY (id_bibliotheque) REFERENCES Bibliotheque(id_bibliotheque)
);

CREATE TABLE Bibliothecaire (
id_bibliothecaire INT AUTO_INCREMENT PRIMARY KEY,
nom VARCHAR(50) NOT NULL,
prenom VARCHAR(90) NOT NULL,
login VARCHAR(50) NOT NULL UNIQUE,
role VARCHAR(40) NOT NULL
);

CREATE TABLE Reservation (
id_reservation INT AUTO_INCREMENT PRIMARY KEY,
date_reservation DATE NOT NULL,
statut VARCHAR(30) NOT NULL,
id_adherent INT NOT NULL,
id_livre INT NOT NULL,
FOREIGN KEY (id_adherent) REFERENCES Adherent(id_adherent),
FOREIGN KEY (id_livre) REFERENCES Livre(id_livre)
);

CREATE TABLE Emprunt (
id_emprunt INT AUTO_INCREMENT PRIMARY KEY,
date_emprunt DATE NOT NULL,
date_retour_prevue DATE NOT NULL,
date_retour_effective DATE,
statut VARCHAR(30) NOT NULL,
id_livre INT NOT NULL,
id_adherent INT NOT NULL,
id_bibliothecaire INT NOT NULL,
FOREIGN KEY (id_livre) REFERENCES Livre(id_livre),
FOREIGN KEY (id_adherent) REFERENCES Adherent(id_adherent),
FOREIGN KEY (id_bibliothecaire) REFERENCES Bibliothecaire(id_bibliothecaire)
);

CREATE TABLE Penalite (
id_penalite INT AUTO_INCREMENT PRIMARY KEY,
montant DECIMAL(10,2) NOT NULL,
motif VARCHAR(150) NOT NULL,
dateCreation DATE NOT NULL,
statut VARCHAR(50) NOT NULL,
id_emprunt INT NOT NULL,
FOREIGN KEY (id_emprunt) REFERENCES Emprunt(id_emprunt)
);
