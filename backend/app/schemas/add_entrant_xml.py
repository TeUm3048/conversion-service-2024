from typing import Union, Annotated, Optional
from pydantic_xml import BaseXmlModel, RootXmlModel, element
from datetime import date
from .identification_xml import IdentificationCardXMLSchema

from pydantic import EmailStr, Field, StringConstraints
from uuid import UUID


class ExistEntrantXMLSchema(BaseXmlModel, tag='Guid'):
    guid: UUID


class IdentificationXMLSchema(BaseXmlModel, tag='Identification'):
    id_document_type: Annotated[int, element(tag='IdDocumentType', gt=0)]

    doc_name: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='DocName')

    doc_series: Optional[Annotated[str, StringConstraints(
        min_length=1, max_length=20)]] = element(tag='DocSeries')

    doc_number: Annotated[str, StringConstraints(
        min_length=1, max_length=50)] = element(tag='DocNumber')

    issue_date: date = element(tag='IssueDate')

    issue_by: Annotated[str, StringConstraints(
        min_length=1, max_length=500)] = element(tag='DocOrganization')

    fields: Optional[IdentificationCardXMLSchema] = element()


class FreeEducationReasonXMLSchema(BaseXmlModel, tag='FreeEducationReason'):
    id_free_education_reason: int = element(tag='IdFreeEducationReason', gt=0)

    id_oksm_free_education_reason: Optional[int] = element(
        tag='IdOksmFreeEducationReason', gt=0, default=None)


class AddressXMLSchema(BaseXmlModel, tag='Address'):
    is_registration: bool = element(tag='IsRegistration')

    full_address: Annotated[str, StringConstraints(
        min_length=1, max_length=1024)] = element(tag='FullAddr')

    id_region: Annotated[int, element(tag='IdRegion', gt=0)]

    city: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='City')


class AddressListXMLSchema(RootXmlModel, tag='AddressList'):
    root: list[AddressXMLSchema] = element(tag='Address')


class AddEntrantXMLSchema(BaseXmlModel, tag='AddEntrant'):
    identification: IdentificationXMLSchema

    snils: Optional[Annotated[str, StringConstraints(
        pattern=r"^\d{11}$")]] = element(tag='Snils')

    id_gender: Annotated[int, element(tag='IdGender', gt=0)]

    birthday: date = element(tag='Birthday')

    birthplace: Annotated[str, StringConstraints(
        min_length=1, max_length=500)] = element(tag='Birthplace')

    phone: Optional[Annotated[str, StringConstraints(
        max_length=120)]] = element(tag='Phone')

    email: Optional[EmailStr] = element(tag='Email')

    id_oksm: int = element(tag='IdOksm', gt=0)

    free_education_reason: Optional[FreeEducationReasonXMLSchema] = element(
        default=None)

    addresses: AddressListXMLSchema


class EntrantChoiceXMLSchema(BaseXmlModel, tag="EntrantChoice"):
    choice: Union[AddEntrantXMLSchema, ExistEntrantXMLSchema] = element()
