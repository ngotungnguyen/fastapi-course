from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Job(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    company_url = Column(String)
    location = Column(String, nullable=False)
    description = Column(String)
    date_posted = Column(Date)
    is_active = Column(Boolean(), default=True)
    owner_id = Column(Integer, ForeignKey('user.id'))
    # id trong Job này sẽ có ForeignKey với bảng User là trường user.id
    owner = relationship("User", back_populates="jobs")
    # tạo quan hệ ngược Job với User và backup quan hệ này bằng jobs
