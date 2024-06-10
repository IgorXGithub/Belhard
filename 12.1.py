#Задача репозиторий https://docs.google.com/document/d/14FGggu_6zrSyQvazz_Zo1xlrD6Q4eeQPCt0zqp1fzjw/edit?usp=sharing

from sqlalchemy import Column, INT, VARCHAR, ForeignKey, SMALLINT, create_engine, exc, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import DeclarativeBase, relationship, Session, sessionmaker
from pydantic import BaseModel, PositiveInt, Field
from typing import List, Optional

POSTGRES_DSN = "postgresql://admin:password@127.0.0.1:5432/db"
engine = create_engine(url=POSTGRES_DSN)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Band(Base):
    __tablename__ = 'bands'

    id = Column(SMALLINT, primary_key=True)
    name = Column(VARCHAR(length=128), nullable=False)
    genre = Column(VARCHAR(length=128), nullable=True)
    albums = relationship("Album", back_populates="band")


class Album(Base):
    __tablename__ = 'albums'

    id = Column(SMALLINT, primary_key=True)
    title = Column(VARCHAR(length=128), nullable=False)
    release_year = Column(INT, nullable=True)
    band_id = Column(SMALLINT, ForeignKey('bands.id', ondelete="cascade", onupdate="cascade"), nullable=False)
    band = relationship("Band", back_populates="albums")


class AlbumDTO(BaseModel):
    id: Optional[PositiveInt] = None
    title: str = Field(max_length=128)
    release_year: PositiveInt
    band_id: PositiveInt


class BandDTO(BaseModel):
    id: Optional[PositiveInt] = None
    name: str = Field(max_length=128)
    genre: str = Field(max_length=128)
    albums: List[AlbumDTO] = []


class Repository:
    def __init__(self, session: Session):
        self.session = session

    def save_band(self, schema: BandDTO) -> BandDTO:
        try:
            band = Band(name=schema.name, genre=schema.genre)
            self.session.add(band)
            self.session.commit()
            self.session.refresh(band)
            return BandDTO(
                id=band.id,
                name=band.name,
                genre=band.genre,
                albums=[]
            )
        except exc.IntegrityError as e:
            self.session.rollback()
            print(f"Error saving band: {e}")
            raise

    def save_album(self, schema: AlbumDTO) -> AlbumDTO:
        try:
            album = Album(title=schema.title, release_year=schema.release_year, band_id=schema.band_id)
            self.session.add(album)
            self.session.commit()
            self.session.refresh(album)
            return AlbumDTO(
                id=album.id,
                title=album.title,
                release_year=schema.release_year,
                band_id=schema.band_id
            )
        except exc.IntegrityError as e:
            self.session.rollback()
            print(f"Error saving band: {e}")
            raise

    def get(self, id: int) -> Optional[BandDTO]:
        stmt = select(Band).where(Band.id == id)
        result = self.session.execute(stmt)
        try:
            band = result.scalar_one()
            albums = [
                AlbumDTO(id=album.id, title=album.title, release_year=album.release_year, band_id=album.band_id)
                for album in band.albums
            ]
            return BandDTO(
                id=band.id,
                name=band.name,
                genre=band.genre,
                albums=albums
            )
        except NoResultFound:
            return None

    def update(self, schema: BandDTO) -> Optional[BandDTO]:
        stmt = select(Band).where(Band.id == schema.id)
        result = self.session.execute(stmt)
        band = result.scalar_one()
        band.name = schema.name
        band.genre = schema.genre
        self.session.add(band)
        self.session.commit()
        self.session.refresh(band)
        albums = [
            AlbumDTO(id=album.id, title=album.title, release_year=album.release_year, band_id=album.band_id)
            for album in band.albums
        ]
        return BandDTO(
            id=band.id,
            name=band.name,
            genre=band.genre,
            albums=albums
        )


class AlbumRepository:
    def __init__(self, session: Session):
        self.session = session

    def save(self, schema: AlbumDTO) -> AlbumDTO:
        album = Album(
            title=schema.title,
            release_year=schema.release_year,
            band_id=schema.band_id
        )
        self.session.add(album)
        self.session.commit()
        self.session.refresh(album)
        return AlbumDTO(
            id=album.id,
            title=album.title,
            release_year=album.release_year,
            band_id=album.band_id
        )

    def get(self, id: int) -> Optional[AlbumDTO]:
        stmt = select(Album).where(Album.id == id)
        result = self.session.execute(stmt)
        try:
            album = result.scalar_one()
            return AlbumDTO(
                id=album.id,
                title=album.title,
                release_year=album.release_year,
                band_id=album.band_id
            )
        except NoResultFound:
            return None

    def update(self, schema: AlbumDTO) -> Optional[AlbumDTO]:
        stmt = select(Album).where(Album.id == schema.id)
        result = self.session.execute(stmt)
        album = result.scalar_one()
        album.title = schema.title
        album.release_year = schema.release_year
        self.session.add(album)
        self.session.commit()
        self.session.refresh(album)
        return AlbumDTO(
            id=album.id,
            title=album.title,
            release_year=album.release_year,
            band_id=album.band_id
        )
