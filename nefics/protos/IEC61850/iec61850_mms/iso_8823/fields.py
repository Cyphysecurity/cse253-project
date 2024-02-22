"""
ISO 8823 ASN1 field definitions
"""
from scapy.asn1fields import *
from .tags import ASN1_Tags_ISO_8823


class ASN1F_MODE_SELECTOR(ASN1F_SET):
    ASN1_tag = ASN1_Tags_ISO_8823.MODE_SELECTOR_TAG


class ASN1F_NORMAL_MODE_PARAMETERS(ASN1F_SEQUENCE):
    ASN1_tag = ASN1_Tags_ISO_8823.NORMAL_MODE_PARAMETERS_TAG


class ASN1F_MODE_VALUE(ASN1F_INTEGER):
    ASN1_tag = ASN1_Tags_ISO_8823.MODE_VALUE_TAG


class ASN1F_CP_TYPE(ASN1F_SET):
    ASN1_tag = ASN1_Tags_ISO_8823.CP_TYPE_TAG


class ASN1F_CALLING_PRESENTATION_SELECTOR(ASN1F_STRING):
    ASN1_tag = ASN1_Tags_ISO_8823.CALLING_PRESENTATION_SELECTOR_TAG


class ASN1F_RESPONDING_PRESENTATION_SELECTOR(ASN1F_STRING):
    ASN1_tag = ASN1_Tags_ISO_8823.RESPONDING_PRESENTATION_SELECTOR_TAG


class ASN1F_CALLED_PRESENTATION_SELECTOR(ASN1F_STRING):
    ASN1_tag = ASN1_Tags_ISO_8823.CALLED_PRESENTATION_SELECTOR_TAG


class ASN1F_PRESENTATION_CONTEXT_DEFINITION_LIST(ASN1F_SEQUENCE_OF):
    ASN1_tag = ASN1_Tags_ISO_8823.PRESENTATION_CONTEXT_DEFINITION_LIST_TAG


class ASN1F_PRESENTATION_CONTEXT_DEFINITION_RESULT_LIST(ASN1F_SEQUENCE_OF):
    ASN1_tag = ASN1_Tags_ISO_8823.PRESENTATION_CONTEXT_DEFINITION_RESULT_LIST_TAG


class ASN1F_PRESENTATION_CONTEXT_IDENTIFIER(ASN1F_INTEGER):
    ASN1_tag = ASN1_Tags_ISO_8823.PRESENTATION_CONTEXT_IDENTIFIER_TAG


class ASN1F_ABSTRACT_SYNTAX_NAME(ASN1F_OID):
    ASN1_tag = ASN1_Tags_ISO_8823.ABSTRACT_SYNTAX_NAME_TAG


class ASN1F_TRANSFER_SYNTAX_NAME(ASN1F_OID):
    ASN1_tag = ASN1_Tags_ISO_8823.TRANSFER_SYNTAX_NAME_TAG


class ASN1F_USER_DATA(ASN1F_CHOICE):
    ASN1_tag = ASN1_Tags_ISO_8823.USER_DATA_TAG


class ASN1F_FULLY_ENCODED_DATA(ASN1F_SEQUENCE):
    ASN1_tag = ASN1_Tags_ISO_8823.FULLY_ENCODED_DATA_TAG


class ASN1F_PDV_LIST(ASN1F_SEQUENCE):
    ASN1_tag = ASN1_Tags_ISO_8823.PDV_LIST_TAG


class ASN1F_CONTENT(ASN1F_SEQUENCE):
    ASN1_tag = ASN1_Tags_ISO_8823.CONTENT_TAG


class ASN1F_RESULT(ASN1F_INTEGER):
    ASN1_tag = ASN1_Tags_ISO_8823.RESULT_TAG


class ASN1F_RESULT_LIST_TRANSFER_SYNTAX(ASN1F_OID):
    ASN1_tag = ASN1_Tags_ISO_8823.RESULT_LIST_TRANSFER_SYNTAX_TAG
