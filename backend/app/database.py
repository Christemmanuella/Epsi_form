from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Utilisation du chemin monté via le volume
DATABASE_URL = "sqlite:////app/db/students.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Ajouter cette ligne pour créer les tables au démarrage (déplacer dans main.py si nécessaire)
# Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        print(f"Erreur lors de la création de la session de base de données : {str(e)}")
        raise
    finally:
        db.close()