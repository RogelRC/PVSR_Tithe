# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definición de la base
Base = declarative_base()

# Modelos
class Zone(Base):
    __tablename__ = 'zone'
    code = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    leader = Column(String, nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    sex = Column(String, CheckConstraint("sex IN ('M', 'F')"))
    type = Column(String, CheckConstraint("type IN ('Miembro', 'Visitante', 'Anónimo')"), nullable=False)
    birth_date = Column(String)
    zone_code = Column(Integer, ForeignKey('zone.code'))
    address = Column(String)
    marital_state = Column(String, CheckConstraint("marital_state IN ('Casado(a)', 'Soltero(a)', 'Viudo(a)')"))
    dni = Column(String, CheckConstraint("dni GLOB '[0-9]*'"))
    phone = Column(String, CheckConstraint("phone GLOB '[0-9]*'"))
    cellphone = Column(String, CheckConstraint("cellphone GLOB '[0-9]*'"))
    notes = Column(String)

class Tithe(Base):
    __tablename__ = 'tithe'
    folio = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    date = Column(Integer, CheckConstraint("LENGTH(CAST(date AS TEXT)) = 8 AND date GLOB '[0-9]*'"), nullable=False)
    payment = Column(Integer, nullable=False)
    currency = Column(String, CheckConstraint("currency IN ('CUP', 'USD', 'MLC', 'Euro')"), nullable=False)

# Configuración de la base de datos (ejemplo con SQLite)
DATABASE_URL = "sqlite:///database.db"  # Cambia esto según tu base de datos

# Creación del motor y la sesión
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Crear las tablas si no existen
Base.metadata.create_all(engine)

# Crear la zona "Anónimo" si no existe
zone = session.query(Zone).filter_by(code=0).first()
if not zone:
    new_zone = Zone(code=0, name="Anónimo", leader="Anónimo")
    session.add(new_zone)
    session.commit()
    print("Zona 'Anónimo' creada exitosamente.")
else:
    print("La zona 'Anónimo' ya existe.")

print("Base de datos y tablas creadas exitosamente.")
