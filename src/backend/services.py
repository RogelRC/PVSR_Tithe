from backend.models import session
from backend.models import User, Zone, Tithe

### ---------- Territorio ---------- ###

def create_zone(code, name, leader):
    new_zone = Zone(code=code, name=name, leader=leader)
    session.add(new_zone)
    session.commit()

def get_zones():
    return session.query(Zone).all()

def update_zone_leader(code, new_leader):
    zone = session.query(Zone).filter_by(code=code).first()
    if zone:
        zone.leader = new_leader
        session.commit()
        return zone
    return None

def update_zone_name(code, new_name):
    zone = session.query(Zone).filter_by(code=code).first()
    if zone:
        zone.name = new_name
        session.commit()
        return zone
    return None

def update_zone_code(old_code, new_code):
    zone = session.query(Zone).filter_by(code=old_code).first()
    if zone:
        zone.code = new_code
        session.commit()
        return zone
    return None

def delete_zone(code):
    zone = session.query(Zone).filter_by(code=code).first()
    if zone:
        session.delete(zone)
        session.commit()
        return True
    return False

def get_zone_code_by_name(name):
    zone = session.query(Zone).filter_by(name=name).first()
    #print(f"{zone} ][][][][][][]a[sd][as]d[a]sd[a]sd[")
    if zone:
        return zone.code
    return None


### ---------- Usuario ---------- ###

def create_user(name, last_name, sex, type, birth_date, zone_code, address, marital_state, dni, phone, cellphone, notes):
    new_user = User(
        name=name,
        last_name=last_name,
        sex=sex,
        type=type,
        birth_date=birth_date,
        zone_code=zone_code,
        address=address,
        marital_state=marital_state,
        dni=dni,
        phone=phone,
        cellphone=cellphone,
        notes=notes
    )
    session.add(new_user)
    session.commit()
    return new_user

def get_users():
    return session.query(User).all()

def update_user(user_id, **kwargs):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        for key, value in kwargs.items():
            setattr(user, key, value)
        session.commit()
        return user
    return None

def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return True
    return False

def search_users(**kwargs):
    query = session.query(User)
    for key, value in kwargs.items():
        query = query.filter(getattr(User, key) == value)
    return query.all()
