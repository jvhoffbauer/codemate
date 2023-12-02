from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import ENUM

from app.db.base_class import Base, same_as


STATUS = ('UNAPPROVED', 'APPROVED')


class Series(Base):
    id = Column(Integer, primary_key=True, index=True)
    novel_id = Column(Integer, ForeignKey('novel.id'))
    writer_id = Column(Integer, ForeignKey('writer.id'))
    order_number = Column(Integer, nullable=False)
    status = Column(ENUM(*STATUS), default=STATUS[0])
    is_free = Column(Boolean, default=True)
    published_at = Column(DateTime, default=same_as('created_at'))
    approved_at = Column(DateTime)
    is_deleted = Column(Boolean, default=False)
    is_impressing = Column(Boolean, default=True)
    is_completed = Column(Boolean, default=False)

    # One to One relation
    series_statistic = relationship('SeriesStatistic', uselist=False, cascade="all, delete-orphan")

    # One to Many relation
    paragraph = relationship('Paragraph', back_populates='series', uselist=True, join_depth=1, cascade="all, delete")
    series_status = relationship('SeriesStatus', back_populates='series', join_depth=1, uselist=True, cascade="all, delete")
    series_meta = relationship('SeriesMeta', back_populates='series', uselist=True, cascade="all, delete")

    # Many to One relation
    novel = relationship('Novel', back_populates='series', join_depth=1)
    writer = relationship('Writer', back_populates='series', join_depth=1)

    # Many to Many relation
    user_read = relationship('UserRead', back_populates='series')
    user_rating = relationship('UserRating', back_populates='series')
    comment = relationship('Comment', back_populates='series')
    coupon_series = relationship('CouponSeries', back_populates='series', join_depth=1)
    cash_series = relationship('CashSeries', back_populates='series', join_depth=1)


# 회차 상태 변경 관리 (상태 자체는 series 테이블에서 관리)
class SeriesStatus(Base):
    id = Column(Integer, primary_key=True, index=True)
    series_id = Column(Integer, ForeignKey('series.id'), index=True)
    manager_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    status = Column(ENUM(*STATUS))
    reason = Column(String(100), default=None)

    # One to One relation
    manager = relationship('User', back_populates='series_status', join_depth=1)

    # Many to One relation
    series = relationship('Series', back_populates='series_status', join_depth=2, cascade="all, delete")


class SeriesStatistic(Base):
    id = Column(Integer, primary_key=True, index=True)
    series_id = Column(Integer, ForeignKey('series.id'), index=True)
    view_count = Column(Integer, default=0)
    rating = Column(Float, default=0)
    rating_count = Column(Integer, default=0)
    total_rating = Column(Float, default=0)
    like_count = Column(Integer, default=0)
    payment_count = Column(Integer, default=0)
    language_code = Column(String(30), ForeignKey('language.code'), default='kr')

    # Many to One relation
    series = relationship('Series', back_populates='series_statistic', cascade="all, delete")


class SeriesMeta(Base):
    id = Column(Integer, primary_key=True, index=True)
    series_id = Column(Integer, ForeignKey('series.id'), index=True)
    is_origin = Column(Boolean, default=False)
    title = Column(String(100), nullable=False, index=True)
    description = Column(String(1000), default="")
    language_code = Column(String(30), ForeignKey('language.code'), default='kr')

    # Many to One relation
    series = relationship('Series', back_populates='series_meta', cascade="all, delete")
