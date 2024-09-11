from typing import Self
from sqlalchemy import Column, Integer, String, Date, Unicode, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as Uuid

from .schemas.add_entrant_xml import AddEntrantXMLSchema
from .schemas.add_entrant_json import AddEntrantSchema


from .database import Base

entrant_address = Table(
    "entrant_to_address",
    Base.metadata,
    Column("add_entrant_id", ForeignKey('add_entrant.id'), primary_key=True),
    Column("add_entrant_address_id", ForeignKey(
        "address.id"), primary_key=True)
)


class AddEntrantModel(Base):
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


class EntrantJson(Base):
    __tablename__ = "entrant_json"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    first_name = Column(Unicode)
    second_name = Column(Unicode)
    middle_name = Column(Unicode)
    dict_sex_id = Column(Integer)
    birthday = Column(Date)
    citizenship_id = Column(Integer)
    motherland = Column(String)
    email = Column(String)
    tel_mobile = Column(String)
    address_txt1 = Column(String)
    address_txt2 = Column(String)
    address_txt3 = Column(String)
    address_txt4 = Column(String)
    has_another_living_address = Column(Boolean)
    second_address_txt1 = Column(String)
    second_address_txt2 = Column(String)
    second_address_txt3 = Column(String)
    second_address_txt4 = Column(String)
    passport_type_id = Column(Integer)
    passport_series = Column(String)
    passport_number = Column(String)
    passport_begda = Column(Date)
    passport_endda = Column(Date)
    passport_org_code = Column(String)
    passport_issued_by = Column(String)
    need_hostel = Column(Boolean)
    special_conditions = Column(Integer)
    is_with_disabilities = Column(Boolean)
    diploma_series = Column(String)
    diploma_number = Column(String)
    diploma_date = Column(Date)
    diploma_registration_number = Column(String)
    graduated_university_text = Column(String)
    edu_diploma_name_text = Column(String)
    snils = Column(String)
    revision = Column(Integer)
    passport_name_text = Column(String)
    has_original_edu_diploma = Column(Boolean)
    passport_uuid = Column(String)
    public_code = Column(String)

    @classmethod
    def from_schema(cls, data: AddEntrantSchema):
        return cls(
            user_id=data.user_id,
            first_name=data.first_name,
            second_name=data.second_name,
            middle_name=data.middle_name,
            dict_sex_id=data.dict_sex_id,
            birthday=data.birthday,
            citizenship_id=data.citizenship_id,
            motherland=data.motherland,
            email=data.email,
            tel_mobile=data.tel_mobile,
            address_txt1=data.address_txt1,
            address_txt2=data.address_txt2,
            address_txt3=data.address_txt3,
            address_txt4=data.address_txt4,
            has_another_living_address=data.has_another_living_address,
            second_address_txt1=data.second_address_txt1,
            second_address_txt2=data.second_address_txt2,
            second_address_txt3=data.second_address_txt3,
            second_address_txt4=data.second_address_txt4,
            passport_type_id=data.passport_type_id,
            passport_series=data.passport_series,
            passport_number=data.passport_number,
            passport_begda=data.passport_begda,
            passport_endda=data.passport_endda,
            passport_org_code=data.passport_org_code,
            passport_issued_by=data.passport_issued_by,
            need_hostel=data.need_hostel,
            special_conditions=data.special_conditions,
            is_with_disabilities=data.is_with_disabilities,
            diploma_series=data.diploma_series,
            diploma_number=data.diploma_number,
            diploma_date=data.diploma_date,
            diploma_registration_number=data.diploma_registration_number,
            graduated_university_text=data.graduated_university_text,
            edu_diploma_name_text=data.edu_diploma_name_text,
            snils=data.snils,
            revision=data.revision,
            passport_name_text=data.passport_name_text,
            has_original_edu_diploma=data.has_original_edu_diploma,
            passport_uuid=data.passport_uuid,
            public_code=data.public_code
        )
