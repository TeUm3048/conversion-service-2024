from warnings import warn
from pydantic_xml import BaseXmlModel, RootXmlModel, element
from typing import List, Optional, Annotated
from datetime import date, datetime
from .add_entrant_json import AddEntrantSchema


class PhotoXMLSchema(BaseXmlModel, tag='Photo'):
    file_hash: Annotated[str, element(
        tag='FileHash', min_length=1, max_length=32)]

    fui: Annotated[str, element(tag='Fui', min_length=1, max_length=32)]


class DocumentXMLSchema(BaseXmlModel, tag='Document'):
    GUID: Annotated[str, element(tag='Guid', min_length=36, max_length=36)]

    file_hash: Annotated[str, element(
        tag='FileHash', min_length=1, max_length=32)]

    id_document_type: Annotated[int, element(tag='IdDocumentType', gt=0)]

    doc_name: Optional[Annotated[str, element(
        tag='DocName', min_length=1, max_length=255)]]

    doc_series: Optional[Annotated[str, element(
        tag='DocSeries', min_length=1, max_length=20)]]

    doc_number: Optional[Annotated[str, element(
        tag='DocNumber', min_length=1, max_length=50)]]

    issue_date: Optional[date] = element(tag='IssueDate')

    issue_by: Optional[Annotated[str, element(
        tag='DocOrganization', min_length=1, max_length=500)]]

    id_check_status: Annotated[int, element(tag='IdCheckStatus', gt=0)]

    id_achievement: Optional[Annotated[int,
                                       element(tag='IdAchievement', gt=0)]]


class DocumentListXMLSchema(RootXmlModel, tag='Document'):
    root: DocumentXMLSchema = element(tag='Document')


class AddressXMLSchema(BaseXmlModel, tag='Address'):
    is_registration: bool = element(tag='IsRegistration')

    full_address: Annotated[str, element(
        tag='FullAddress', min_length=1, max_length=1024)]

    id_region: Annotated[int, element(tag='IdRegion', gt=0)]

    city: Annotated[str, element(tag='City', min_length=1, max_length=255)]


class AddressListXMLSchema(RootXmlModel, tag='AddressList'):
    root: List[AddressXMLSchema] = element(tag='Address')


class FreeEducationReasonXMLSchema(BaseXmlModel, tag='FreeEducationReason'):
    id_free_education_reason: Annotated[int, element(
        tag='IdFreeEducationReason', gt=0)]

    id_oksm_free_education_reason: Optional[Annotated[int, element(
        tag='IdOksmFreeEducationReason', gt=0, default=None)]]


class EntrantXMLSchema(BaseXmlModel, tag='Entrant'):
    id_object: Annotated[int, element(tag='IdObject', gt=0)]

    GUID: Annotated[str, element(tag='Guid', min_length=36, max_length=36)]

    snils: Optional[Annotated[str, element(
        tag='Snils', min_length=11, max_length=11)]]

    id_gender: Annotated[int, element(tag='IdGender', gt=0)]

    birthday: date = element(tag='Birthday')

    birthplace: Annotated[str, element(
        tag='Birthplace', min_length=1, max_length=500)]

    phone: Optional[Annotated[str, element(tag='Phone', max_length=120)]]

    email: Optional[Annotated[str, element(tag='Email')]]

    availability_edu_doc: bool = element(tag='AvailabilityEduDoc')

    date_availability_edu_doc: Optional[datetime] = element(
        tag='DateAvailabilityEduDoc')

    surname: Annotated[str, element(
        tag='Surname', min_length=1, max_length=255)]

    name: Annotated[str, element(tag='Name', min_length=1, max_length=255)]

    patronymic: Optional[Annotated[str, element(
        tag='Patronymic', min_length=1, max_length=255)]]

    id_oksm: Annotated[int, element(tag='IdOksm', gt=0)]

    free_education_reason: Optional[FreeEducationReasonXMLSchema]

    address_list: Optional[AddressListXMLSchema] = element(tag='AddressList')

    photo: Optional[PhotoXMLSchema]


class SuccessResultListXMLSchema(RootXmlModel, tag='SuccessResultList'):
    root: list[EntrantXMLSchema] = element(tag='Entrant')


class PackageDataXMLSchema(BaseXmlModel, tag='PackageData'):
    id_jwt: Annotated[int, element(tag='ID_JWT', gt=0)]

    entity_action: Annotated[str, element(
        tag='EntityAction', min_length=1, max_length=50)]

    SuccessResultList: Optional[SuccessResultListXMLSchema] = element(
        tag='SuccestResultList')


def create_get_entrant_xml_response(data: AddEntrantSchema) -> PackageDataXMLSchema:
    addresses = [
        AddressXMLSchema(is_registration=warn('Change it!') or data.has_another_living_address,
                         full_address=data.address_txt1,
                         id_region=warn('Change it!') or 1,
                         city=warn('Change it!') or data.address_txt2 or "132")
    ]

    entrant = EntrantXMLSchema(id_object=243,
                               GUID=warn("Change it!") or "12345678-1234-1234-1234-123456789012",
                               snils=data.snils,
                               id_gender=data.dict_sex_id,
                               birthday=data.birthday,
                               birthplace=data.motherland,
                               phone=data.tel_mobile,
                               email=data.email,
                               availability_edu_doc=warn("Change it!") or True,
                               date_availability_edu_doc=warn(
                                   "Change it!") or date(1970, 1, 1),
                               surname=data.second_name,
                               name=data.first_name,
                               patronymic=data.middle_name,
                               id_oksm=data.citizenship_id,
                               free_education_reason=warn(
                                   "Change it!") or None,
                               address_list=AddressListXMLSchema(
                                   root=addresses),
                               photo=warn("Change it!") or None
                               )

    return PackageDataXMLSchema(id_jwt=23,
                                entity_action="sfs",
                                SuccessResultList=SuccessResultListXMLSchema(root=[entrant]))
