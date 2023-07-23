from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class Menu(Base):
    __tablename__ = "menus"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)

    submenus = relationship("SubMenu", back_populates="menu", cascade="all, delete-orphan")


class SubMenu(Base):
    __tablename__ = "submenus"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    menu_id = Column(String, ForeignKey("menus.id"))

    menu = relationship("Menu", back_populates="submenus")
    dishes = relationship("Dish", back_populates="submenu", cascade="all, delete-orphan")


class Dish(Base):
    __tablename__ = "dishes"
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    submenu_id = Column(String, ForeignKey("submenus.id"))

    submenu = relationship("SubMenu", back_populates="dishes")
