"""
BER codec en-/decoders for ISO 8650-1 / ACSE
"""
from scapy.asn1.ber import *
from .tags import ASN1_Tags_ACSE


class BER_Codec_AARQ_TYPE(BERcodec_SEQUENCE):
    tag = ASN1_Tags_ACSE.AARQ_TYPE_TAG


class BER_Codec_APPLICATION_CONTEXT_NAME(BERcodec_OID):
    tag = ASN1_Tags_ACSE.APPLICATION_CONTEXT_NAME_TAG


class BER_Codec_CALLED_AP_TITLE_FORM_2(BERcodec_OID):
    tag = ASN1_Tags_ACSE.CALLED_AP_TITLE_FORM_2_TAG


class BER_Codec_CALLED_AE_QUALIFIER_FORM_2(BERcodec_INTEGER):
    tag = ASN1_Tags_ACSE.CALLED_AE_QUALIFIER_FORM_2_TAG


class BER_Codec_CALLING_AP_TITLE_FORM_2(BERcodec_OID):
    tag = ASN1_Tags_ACSE.CALLING_AP_TITLE_FORM_2_TAG


class BER_Codec_CALLING_AE_QUALIFIER_FORM_2(BERcodec_INTEGER):
    tag = ASN1_Tags_ACSE.CALLING_AE_QUALIFIER_FORM_2_TAG


class BER_Codec_USER_INFORMATION(BERcodec_SEQUENCE):
    tag = ASN1_Tags_ACSE.USER_INFORMATION_TAG


class BER_Codec_EXTERNAL_T(BERcodec_SEQUENCE):
    tag = ASN1_Tags_ACSE.EXTERNAL_T_TAG


class BER_Codec_INDIRECT_REFERENCE(BERcodec_INTEGER):
    tag = ASN1_Tags_ACSE.INDIRECT_REFERENCE_TAG


class BER_Codec_ACSE_MMS_DATA(BERcodec_SEQUENCE):
    tag = ASN1_Tags_ACSE.MMS_DATA_TAG


class BER_Codec_AARE_TYPE(BERcodec_SEQUENCE):
    tag = ASN1_Tags_ACSE.AARE_TYPE_TAG


class BER_Codec_AARE_RESULT_TYPE(BERcodec_INTEGER):
    tag = ASN1_Tags_ACSE.AARE_RESULT_TYPE_TAG



class BER_Codec_ACSE_SERVICE_USER(BERcodec_INTEGER):
    tag = ASN1_Tags_ACSE.ACSE_SERVICE_USER_TAG
