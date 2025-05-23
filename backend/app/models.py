from sqlalchemy import Column, Integer, String, Enum
from database import Base
import enum

class VoieAcces(enum.Enum):
    formation_initiale_hors_alternance = "formation_initiale_hors_alternance"
    alternance_apprentissage = "alternance_apprentissage"
    alternance_contrat_pro = "alternance_contrat_pro"
    formation_continue = "formation_continue"
    validation_acquis = "validation_acquis"

class Situation(enum.Enum):
    en_formation = "en_formation"
    salarie = "salarie"
    demandeur_emploi = "demandeur_emploi"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    form_type = Column(String, nullable=False)  # Ajout de la colonne form_type

class ASRBD(Base):
    __tablename__ = "asrbd"
    id = Column(Integer, primary_key=True, index=True)
    civilite = Column(String, nullable=False)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    date_naissance = Column(String, nullable=False)
    lieu_naissance = Column(String, nullable=False)
    departement_naissance = Column(String, nullable=False)
    pays = Column(String, nullable=False)
    adresse = Column(String, nullable=False)
    cp = Column(String, nullable=False)
    ville = Column(String, nullable=False)
    tel_fixe = Column(String)
    tel_mobile = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    diplome = Column(String, nullable=False)
    experience = Column(String, nullable=False)
    financement = Column(String, nullable=False)

class EISI(Base):
    __tablename__ = "eisi"
    id = Column(Integer, primary_key=True, index=True)
    id_candidat = Column(String, nullable=False)
    identifiant_candidat = Column(String, nullable=False)
    campus = Column(String, nullable=False)
    civilite = Column(String, nullable=False)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    date_naissance = Column(String, nullable=False)
    code_postal_naissance = Column(String, nullable=False)
    lieu_naissance = Column(String, nullable=False)
    pays_naissance = Column(String, nullable=False)
    nationalite = Column(String, nullable=False)
    dernier_diplome = Column(String, nullable=False)
    niveau_diplome = Column(String, nullable=False)
    annee_diplome = Column(Integer, nullable=False)
    decision_jury = Column(String, nullable=False)
    annee_inscription = Column(Integer, nullable=False)
    voie_acces = Column(Enum(VoieAcces), nullable=False)
    situation_avant_cursus = Column(Enum(Situation), nullable=False)
    dernier_metier = Column(String)
    nom_entreprise = Column(String)
    duree_experience = Column(Integer)
    tel_mobile = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

class DEVIA(Base):
    __tablename__ = "devia"
    id = Column(Integer, primary_key=True, index=True)
    id_candidat = Column(String, nullable=False)
    identifiant_candidat = Column(String, nullable=False)
    campus = Column(String, nullable=False)
    civilite = Column(String, nullable=False)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    date_naissance = Column(String, nullable=False)
    code_postal_naissance = Column(String, nullable=False)
    lieu_naissance = Column(String, nullable=False)
    pays_naissance = Column(String, nullable=False)
    nationalite = Column(String, nullable=False)
    dernier_diplome = Column(String, nullable=False)
    niveau_diplome = Column(String, nullable=False)
    annee_diplome = Column(Integer, nullable=False)
    decision_jury = Column(String, nullable=False)
    annee_inscription = Column(Integer, nullable=False)
    voie_acces = Column(Enum(VoieAcces), nullable=False)
    situation_avant_cursus = Column(Enum(Situation), nullable=False)
    dernier_metier = Column(String)
    nom_entreprise = Column(String)
    duree_experience = Column(Integer)
    tel_mobile = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)