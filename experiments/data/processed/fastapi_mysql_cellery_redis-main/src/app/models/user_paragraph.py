from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class UserParagraph(Base):
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True, index=True)
    paragraph_id = Column(Integer, ForeignKey('paragraph.id'), primary_key=True, index=True)

    # Many to Many relation
    user = relationship('User', back_populates='user_paragraph')
    paragraph = relationship('Paragraph', back_populates='user_paragraph')
