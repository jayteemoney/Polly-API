from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models

def get_poll_or_404(db: Session, poll_id: int, user_id: int = None):
    """
    Fetches a poll by its ID and raises a 404 error if not found.
    Optionally checks for ownership if a user_id is provided.
    """
    query = db.query(models.Poll).filter(models.Poll.id == poll_id)
    
    if user_id:
        query = query.filter(models.Poll.owner_id == user_id)
    
    poll = query.first()
    
    if not poll:
        detail = "Poll not found"
        if user_id:
            detail += " or not authorized"
        raise HTTPException(status_code=404, detail=detail)
    
    return poll