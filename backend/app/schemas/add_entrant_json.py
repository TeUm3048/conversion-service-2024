from pydantic import BaseModel, EmailStr
from .add_entrant_xml import AddEntrantXMLSchema
from typing import Optional
from datetime import date
from uuid import UUID
from warnings import warn


class AddEntrantSchema(BaseModel):
    id: int
    user_id: int
    first_name: str
    second_name: str
    middle_name: Optional[str] = None
    dict_sex_id: int
    birthday: date
    citizenship_id: int
    motherland: str
    email: EmailStr
    tel_mobile: str
    address_txt1: str
    address_txt2: Optional[str] = None
    address_txt3: Optional[str] = None
    address_txt4: Optional[str] = None
    has_another_living_address: bool
    second_address_txt1: Optional[str] = None
    second_address_txt2: Optional[str] = None
    second_address_txt3: Optional[str] = None
    second_address_txt4: Optional[str] = None
    passport_type_id: int
    passport_series: str
    passport_number: str
    passport_begda: date
    passport_endda: Optional[date] = None
    passport_org_code: str
    passport_issued_by: str
    need_hostel: Optional[bool]
    special_conditions: Optional[int] = None
    is_with_disabilities: Optional[bool] = None
    diploma_series: str
    diploma_number: str
    diploma_date: date
    diploma_registration_number: str
    graduated_university_text: str
    edu_diploma_name_text: Optional[str]
    snils: Optional[str] = None
    revision: int
    passport_name_text: Optional[str] = None
    has_original_edu_diploma: bool
    passport_uuid: UUID
    public_code: str

    @classmethod
    def from_xml_schema(cls, data: AddEntrantXMLSchema):
        try:
            ent = cls(
                id=warn("\033[91m\033[1mChange it!\033[0m") or 1,
                user_id=warn("\033[91m\033[1mChange it!\033[0m") or 1,
                first_name=data.identification.fields.name,
                second_name=data.identification.fields.surname,
                middle_name=data.identification.fields.patronymic,
                dict_sex_id=data.id_gender,
                birthday=data.birthday,
                citizenship_id=data.id_oksm,
                motherland=data.birthplace,
                email=data.email,
                tel_mobile=data.phone,
                address_txt1=data.addresses.root[0].full_address if data.addresses.root else None,
                address_txt2=data.addresses.root[0].city if data.addresses.root else None,
                has_another_living_address=data.addresses.root[0].is_registration,
                passport_type_id=data.identification.id_document_type,
                passport_series=data.identification.doc_series,
                passport_number=data.identification.doc_number,
                passport_begda=data.identification.issue_date,
                passport_org_code=data.identification.doc_name,
                passport_issued_by=data.identification.issue_by,
                need_hostel=warn("\033[91m\033[1mChange it!\033[0m") or 1,
                diploma_series=warn("\033[91m\033[1mChange it!\033[0m") or 'Ты снова куришь, снова слёзы на твоих щеках',
                diploma_number=warn("\033[91m\033[1mChange it!\033[0m") or 'Опять ждала меня бухого до семи утра',
                diploma_date=warn("\033[91m\033[1mChange it!\033[0m") or date(1970, 1, 1),
                diploma_registration_number=warn("\033[91m\033[1mChange it!\033[0m") or 'Пообещал, что я всю жизнь буду любить тебя',
                graduated_university_text=warn("\033[91m\033[1mChange it!\033[0m") or 'Я рэпер, зай, мои слова не стоят нихуя',
                edu_diploma_name_text=warn("\033[91m\033[1mChange it!\033[0m") or 'И я подонок, я изменщик, я gaslighter и абьюзер',
                snils=data.snils,
                revision=warn("\033[91m\033[1mChange it!\033[0m") or 1,
                has_original_edu_diploma=warn("\033[91m\033[1mChange it!\033[0m") or 1,
                passport_uuid=warn("\033[91m\033[1mChange it!\033[0m") or UUID('12345678123456781234567812345678'),
                public_code=warn("\033[91m\033[1mChange it!\033[0m") or 'Я не нравлюсь твоей маме, да и хуй с ней',
                # id_free_education_reason=data.free_education_reason.id_free_education_reason or data.free_education_reason,
                # id_oksm_free_education_reason=data.free_education_reason.id_oksm_free_education_reason or data.free_education_reason,
                # adresses=[]
                passport_name_text=data.identification.doc_name
            )
            return ent
        except (KeyError, AttributeError) as e:
            raise ValueError(f'Missing required field: {e}')


warn("\033[91m\033[1m Development fields are used. Delete them! \033[0m")
