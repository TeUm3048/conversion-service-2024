from pydantic_xml import BaseXmlModel, element
from pydantic import StringConstraints
from datetime import date
from typing import Optional, Annotated, Union


class FieldsXMLSchema(BaseXmlModel, tag='Fields'):
    pass


class PassRusFieldXMLSchema(FieldsXMLSchema):
    subdivision_code: str = element(tag='SubdivisionCode')

    id_oksm: int = element(tag='IdOksm', gt=0)

    surname: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Surname')

    name: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Name')

    patronymic: Optional[Annotated[str, StringConstraints(
        min_length=1, max_length=255)]] = element(tag='Patronymic')


class RusMilitaryCardXMLSchema(FieldsXMLSchema):
    subdivision_code: Optional[str] = element(tag='SubdivisionCode')

    id_oksm: int = element(tag='IdOksm', gt=0)

    surname: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Surname')

    name: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Name')

    patronymic: Optional[Annotated[str, StringConstraints(
        min_length=1, max_length=255)]] = element(tag='Patronymic')


class RusTemporaryIdentityCardXMLSchema(FieldsXMLSchema):
    subdivision_code: Optional[str] = element(tag='SubdivisionCode')

    id_oksm: int = element(tag='IdOksm', gt=0)

    surname: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Surname')

    name: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Name')

    patronymic: Optional[Annotated[str, StringConstraints(
        min_length=1, max_length=255)]] = element(tag='Patronymic')


class RusResidencePermitXMLSchema(FieldsXMLSchema):
    subdivision_code: Optional[str] = element(tag='SubdivisionCode')

    id_oksm: int = element(tag='IdOksm', gt=0)

    surname: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Surname')

    name: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Name')

    patronymic: Optional[Annotated[str, StringConstraints(
        min_length=1, max_length=255)]] = element(tag='Patronymic')


class RusForeignPassportXMLSchema(FieldsXMLSchema):
    subdivision_code: Optional[str] = element(tag='SubdivisionCode')

    id_oksm: int = element(tag='IdOksm', gt=0)

    surname: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Surname')

    name: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Name')

    patronymic: Optional[Annotated[str, StringConstraints(
        min_length=1, max_length=255)]] = element(tag='Patronymic')


class ForeinPassportXMLSchema(FieldsXMLSchema):
    id_oksm: int = element(tag='IdOksm', gt=0)

    surname: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Surname')

    name: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Name')

    patronymic: Optional[Annotated[str, StringConstraints(
        min_length=1, max_length=255)]] = element(tag='Patronymic')


class DiplomaticPassportXMLSchema(FieldsXMLSchema):
    expiration_date: Optional[date] = element(tag='ExpirationDate')

    id_oksm: int = element(tag='IdOksm', gt=0)

    surname: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Surname')

    name: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Name')

    patronymic: Optional[Annotated[str, StringConstraints(
        min_length=1, max_length=255)]] = element(tag='Patronymic')


class ServicePassportXMLSchema(FieldsXMLSchema):
    expiration_date: Optional[date] = element(tag='ExpirationDate')

    id_oksm: int = element(tag='IdOksm', gt=0)

    surname: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Surname')

    name: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Name')

    patronymic: Optional[Annotated[str, StringConstraints(
        min_length=1, max_length=255)]] = element(tag='Patronymic')


class TemporaryResidencePermitXMLSchema(FieldsXMLSchema):
    subdivision_code: Optional[str] = element(tag='SubdivisionCode')

    id_oksm: int = element(tag='IdOksm', gt=0)

    surname: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Surname')

    name: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Name')

    patronymic: Optional[Annotated[str, StringConstraints(
        min_length=1, max_length=255)]] = element(tag='Patronymic')


class RefureeCertificateXMLSchema(FieldsXMLSchema):
    subdivision_code: Optional[str] = element(tag='SubdivisionCode')

    id_oksm: int = element(tag='IdOksm', gt=0)

    surname: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Surname')

    name: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Name')

    patronymic: Optional[Annotated[str, StringConstraints(
        min_length=1, max_length=255)]] = element(tag='Patronymic')


class TemporaryAsylumCertificateXMLSchema(FieldsXMLSchema):
    subdivision_code: Optional[str] = element(tag='SubdivisionCode')

    id_oksm: int = element(tag='IdOksm', gt=0)

    surname: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Surname')

    name: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Name')

    patronymic: Optional[Annotated[str, StringConstraints(
        min_length=1, max_length=255)]] = element(tag='Patronymic')


class MilitaryIDCardXMLSchema(FieldsXMLSchema):
    subdivision_code: Optional[str] = element(tag='SubdivisionCode')

    id_oksm: int = element(tag='IdOksm', gt=0)

    surname: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Surname')

    name: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Name')

    patronymic: Optional[Annotated[str, StringConstraints(
        min_length=1, max_length=255)]] = element(tag='Patronymic')


class SeafarerIDCardXMLSchema(FieldsXMLSchema):
    subdivision_code: Optional[str] = element(tag='SubdivisionCode')

    id_oksm: int = element(tag='IdOksm', gt=0)

    surname: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Surname')

    name: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Name')

    patronymic: Optional[Annotated[str, StringConstraints(
        min_length=1, max_length=255)]] = element(tag='Patronymic')


class TemporaryStatelessPersonCertificateXMLSchema(FieldsXMLSchema):
    subdivision_code: Optional[str] = element(tag='SubdivisionCode')

    id_oksm: int = element(tag='IdOksm', gt=0)

    surname: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Surname')

    name: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Name')

    patronymic: Optional[Annotated[str, StringConstraints(
        min_length=1, max_length=255)]] = element(tag='Patronymic')

    prolongation_date: Optional[date] = element(tag='ProlongationDate')


class RecognizioneCertificateXMLSchema(FieldsXMLSchema):
    subdivision_code: Optional[str] = element(tag='SubdivisionCode')

    id_oksm: int = element(tag='IdOksm', gt=0)

    surname: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Surname')

    name: Annotated[str, StringConstraints(
        min_length=1, max_length=255)] = element(tag='Name')

    patronymic: Optional[Annotated[str, StringConstraints(
        min_length=1, max_length=255)]] = element(tag='Patronymic')



IdentificationCardXMLSchema = Union[PassRusFieldXMLSchema,
                           RusMilitaryCardXMLSchema,
                           RusTemporaryIdentityCardXMLSchema,
                           RusResidencePermitXMLSchema,
                           RusForeignPassportXMLSchema,
                           ForeinPassportXMLSchema,
                           DiplomaticPassportXMLSchema,
                           ServicePassportXMLSchema,
                           TemporaryResidencePermitXMLSchema,
                           RefureeCertificateXMLSchema,
                           TemporaryAsylumCertificateXMLSchema,
                           MilitaryIDCardXMLSchema,
                           SeafarerIDCardXMLSchema,
                           TemporaryStatelessPersonCertificateXMLSchema,
                           RecognizioneCertificateXMLSchema]
