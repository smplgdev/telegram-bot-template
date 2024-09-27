from pytz import timezone
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, func
from sqlalchemy.orm import declared_attr

from config_reader import config
from db.base import Base

timezone = timezone(config.timezone)


class TimeStampedMixin:
    @declared_attr
    def created_at(cls):
        return Column(DateTime(timezone=True), server_default=func.now())

    @declared_attr
    def updated_at(cls):
        return Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class User(TimeStampedMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger, unique=True)
    tg_username = Column(String(length=32), unique=True)
    tg_first_name = Column(String(length=64))
    tg_language_code = Column(String(length=6))
