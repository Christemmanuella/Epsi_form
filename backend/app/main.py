from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import Optional
from database import engine, get_db
from models import User, ASRBD, EISI, DEVIA
from sqlalchemy.orm import Session

app = FastAPI()

# Ajout du middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Création des tables au démarrage
User.__table__.create(engine, checkfirst=True)
ASRBD.__table__.create(engine, checkfirst=True)
EISI.__table__.create(engine, checkfirst=True)
DEVIA.__table__.create(engine, checkfirst=True)

class FormSubmission(BaseModel):
    email: EmailStr
    form_type: str

class EISICreate(BaseModel):
    id_candidat: str
    identifiant_candidat: str
    campus: str
    civilite: str
    nom: str
    prenom: str
    date_naissance: str
    code_postal_naissance: str
    lieu_naissance: str
    pays_naissance: str
    nationalite: str
    dernier_diplome: str
    niveau_diplome: str
    annee_diplome: int
    decision_jury: str
    annee_inscription: int
    voie_acces: str
    situation_avant_cursus: str
    dernier_metier: Optional[str] = None
    nom_entreprise: Optional[str] = None
    duree_experience: Optional[int] = None
    tel_mobile: str
    email: EmailStr

class DEVIACreate(BaseModel):
    id_candidat: str
    identifiant_candidat: str
    campus: str
    civilite: str
    nom: str
    prenom: str
    date_naissance: str
    code_postal_naissance: str
    lieu_naissance: str
    pays_naissance: str
    nationalite: str
    dernier_diplome: str
    niveau_diplome: str
    annee_diplome: int
    decision_jury: str
    annee_inscription: int
    voie_acces: str
    situation_avant_cursus: str
    dernier_metier: Optional[str] = None
    nom_entreprise: Optional[str] = None
    duree_experience: Optional[int] = None
    tel_mobile: str
    email: EmailStr

class ASRBDCreate(BaseModel):
    civilite: str
    nom: str
    prenom: str
    date_naissance: str
    lieu_naissance: str
    departement_naissance: str
    pays: str
    adresse: str
    cp: str
    ville: str
    tel_fixe: Optional[str] = None
    tel_mobile: str
    email: EmailStr
    diplome: str
    experience: str
    financement: str

class EmailCheck(BaseModel):
    email: EmailStr

def validate_email_domain(email: str):
    allowed_domains = ['@ecoles-epsi.net', '@wis-ecoles.net', '@ecoles-wis.net']
    if not any(email.lower().endswith(domain.lower()) for domain in allowed_domains):
        raise HTTPException(status_code=400, detail="L'email doit appartenir au domaine @ecoles-epsi.net, @wis-ecoles.net ou @ecoles-wis.net")

@app.post("/submit-form")
async def submit_form(submission: FormSubmission, db: Session = Depends(get_db)):
    validate_email_domain(submission.email)
    
    if submission.form_type not in ["EISI", "DEVIA", "ASRBD"]:
        raise HTTPException(status_code=400, detail="Type de formulaire invalide")
    
    # Ne pas insérer dans la table users ici
    return {"message": f"Formulaire {submission.form_type} sélectionné avec succès", 
            "redirect": f"/form-{submission.form_type.lower()}.html"}

@app.post("/submit-eisi")
async def submit_eisi(eisi: EISICreate, db: Session = Depends(get_db)):
    # Vérifier si l'email existe déjà dans la table eisi
    existing_email = db.query(EISI).filter(EISI.email == eisi.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Cet email est déjà utilisé dans la formation EISI")
    
    db_eisi = EISI(**eisi.dict())
    try:
        db.add(db_eisi)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'insertion dans la table eisi : {str(e)}")
    
    return {"message": "Formulaire soumis avec succès", "redirect": "/login.html"}

@app.post("/submit-devia")
async def submit_devia(devia: DEVIACreate, db: Session = Depends(get_db)):
    # Vérifier si l'email existe déjà dans la table devia
    existing_email = db.query(DEVIA).filter(DEVIA.email == devia.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Cet email est déjà utilisé dans la formation DEVIA")
    
    db_devia = DEVIA(**devia.dict())
    try:
        db.add(db_devia)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'insertion dans la table devia : {str(e)}")
    
    return {"message": "Formulaire soumis avec succès", "redirect": "/login.html"}

@app.post("/submit-asrbd")
async def submit_asrbd(asrbd: ASRBDCreate, db: Session = Depends(get_db)):
    # Vérifier si l'email existe déjà dans la table asrbd
    existing_email = db.query(ASRBD).filter(ASRBD.email == asrbd.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Cet email est déjà utilisé dans la formation ASRBD")
    
    db_asrbd = ASRBD(**asrbd.dict())
    try:
        db.add(db_asrbd)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'insertion dans la table asrbd : {str(e)}")
    
    return {"message": "Formulaire soumis avec succès", "redirect": "/login.html"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.post("/check-email")
async def check_email(email_check: EmailCheck, db: Session = Depends(get_db)):
    validate_email_domain(email_check.email)
    
    # Vérifier l'email dans toutes les tables finales
    existing_eisi = db.query(EISI).filter(EISI.email == email_check.email).first()
    existing_devia = db.query(DEVIA).filter(DEVIA.email == email_check.email).first()
    existing_asrbd = db.query(ASRBD).filter(ASRBD.email == email_check.email).first()
    
    if existing_eisi or existing_devia or existing_asrbd:
        raise HTTPException(status_code=400, detail="Cet email est déjà utilisé")
    
    return {"message": "Email valide et disponible"}