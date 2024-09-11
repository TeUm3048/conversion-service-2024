from typing import Self
from sqlalchemy import Column, Integer, String, Date, Unicode, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table, ForeignKey

from .schemas.add_entrant_xml import AddEntrantXMLSchema

from .database import Base

entrant_address = Table(
    "entrant_to_address",
    Base.metadata,
    Column("add_entrant_id", ForeignKey('add_entrant.id'), primary_key=True),
    Column("add_entrant_address_id", ForeignKey(
        "address.id"), primary_key=True)
)


class AddEntrant(Base):
    __tablename__ = "add_entrant"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(Unicode)
    second_name = Column(Unicode)
    middle_name = Column(Unicode)

    passport_type_id = Column(Integer)
    passport_org_code = Column(String)
    passport_series = Column(String)
    passport_number = Column(String)

    # issue date
    passport_begda = Column(Date)
    passport_issued_by = Column(String)
    snils = Column(String(length=11))
    dict_sex_id = Column(Integer)

    birthday = Column(Date)
    motherland = Column(String)

    tel_mobile = Column(String)
    email = Column(String)

    citizenship_id = Column(Integer)
    adresses = relationship("AddEntrantAddress",
                            secondary=entrant_address)

    id_free_education_reason = Column(Integer)
    id_oksm_free_education_reason = Column(Integer)

    @classmethod
    def from_xml_schema(cls, data: AddEntrantXMLSchema) -> Self:
        if data.identification.fields is None:
            raise ValueError('Missing required field: identification.fields')
        try:

            entrant = cls(
                first_name=data.identification.fields.name,
                second_name=data.identification.fields.surname,
                middle_name=data.identification.fields.patronymic,
                passport_type_id=data.identification.id_document_type,
                passport_org_code=data.identification.doc_name,
                passport_series=data.identification.doc_series,
                passport_number=data.identification.doc_number,
                passport_begda=data.identification.issue_date,
                passport_issued_by=data.identification.issue_by,
                snils=data.snils,
                dict_sex_id=data.id_gender,
                birthday=data.birthday,
                motherland=data.birthplace,
                tel_mobile=data.phone,
                email=data.email,
                citizenship_id=data.id_oksm,
                id_free_education_reason=data.free_education_reason.id_free_education_reason or data.free_education_reason,
                id_oksm_free_education_reason=data.free_education_reason.id_oksm_free_education_reason or data.free_education_reason,
                adresses=[]
            )

            for address in data.addresses.root:
                entrant.adresses.append(AddEntrantAddress(
                    city=address.city,
                    full_address=address.full_address,
                    id_region=address.id_region,
                    is_registration=address.is_registration
                ))

        except (KeyError, AttributeError) as e:
            raise ValueError(f'Missing required field: {e}')

        return entrant


class AddEntrantAddress(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    full_address = Column(String)
    id_region = Column(Integer)
    is_registration = Column(Boolean)
