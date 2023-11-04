from decouple import config 
import xml.etree.ElementTree as ET

class Xml():
    def __init__(self):
        pass

    def generar(self):              
        invoice = ET.Element("Invoice")
        invoice.set("xmlns", "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2")
        invoice.set("xmlns:cac", "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2")
        invoice.set("xmlns:cbc", "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2")
        invoice.set("xmlns:ds", "http://www.w3.org/2000/09/xmldsig#")
        invoice.set("xmlns:ext", "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2")
        invoice.set("xmlns:sts", "dian:gov:co:facturaelectronica:Structures-2-1")
        invoice.set("xmlns:xades", "http://uri.etsi.org/01903/v1.3.2#")
        invoice.set("xmlns:xades141", "http://uri.etsi.org/01903/v1.4.1#")
        invoice.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        invoice.set("xsi:schemaLocation", "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2     http://docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd")
        
        ext_UBLExtensions = ET.SubElement(invoice,"ext:UBLExtensions")
        ext_UBLExtension = ET.SubElement(ext_UBLExtensions, 'ext:UBLExtension')
        ext_ExtensionContent = ET.SubElement(ext_UBLExtension, 'ext:ExtensionContent')
        sts_DianExtensions = ET.SubElement(ext_ExtensionContent, 'sts:DianExtensions')
        sts_InvoiceControl = ET.SubElement(sts_DianExtensions, 'sts:InvoiceControl')
        sts_InvoiceAuthorization = ET.SubElement(sts_InvoiceControl, 'sts:InvoiceAuthorization')
        sts_InvoiceAuthorization.text = "18760000001"
        sts_AuthorizationPeriod = ET.SubElement(sts_InvoiceControl, 'sts:AuthorizationPeriod')
        cbc_StartDate = ET.SubElement(sts_AuthorizationPeriod, 'cbc:StartDate')
        cbc_StartDate.text = "2019-01-19"
        cbc_EndDate = ET.SubElement(sts_AuthorizationPeriod, 'cbc:EndDate')
        cbc_EndDate.text = "2030-01-19"
        sts_AuthorizedInvoices = ET.SubElement(sts_InvoiceControl, 'sts:AuthorizedInvoices')
        sts_Prefix = ET.SubElement(sts_AuthorizedInvoices, 'sts:Prefix')
        sts_Prefix.text = "SETP"
        sts_From = ET.SubElement(sts_AuthorizedInvoices, 'sts:From')
        sts_From.text = "990000000"
        sts_To = ET.SubElement(sts_AuthorizedInvoices, 'sts:To')
        sts_To.text = "995000000"
        sts_InvoiceSource = ET.SubElement(sts_DianExtensions, 'sts:InvoiceSource')
        cbc_IdentificationCode = ET.SubElement(sts_InvoiceSource, 'cbc:IdentificationCode', {"listAgencyID":"6", "listAgencyName":"United Nations Economic Commission for Europe", "listSchemeURI":"urn:oasis:names:specification:ubl:codelist:gc:CountryIdentificationCode-2.1"})
        cbc_IdentificationCode.text = "CO"
        sts_SoftwareProvider = ET.SubElement(sts_DianExtensions, 'sts:SoftwareProvider')
        sts_ProviderID = ET.SubElement(sts_SoftwareProvider, 'sts:ProviderID', {"schemeAgencyID":"195", "schemeAgencyName":"CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)", "schemeID":"4", "schemeName":"31"})
        sts_ProviderID.text = "800197268"
        sts_SoftwareID = ET.SubElement(sts_SoftwareProvider, 'sts:SoftwareID', {"schemeAgencyID":"195", "schemeAgencyName":"CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)"})
        sts_SoftwareID.text = "56f2ae4e-9812-4fad-9255-08fcfcd5ccb0"
        sts_SoftwareSecurityCode = ET.SubElement(sts_DianExtensions, 'sts:SoftwareSecurityCode', {"schemeAgencyID": "195", "schemeAgencyName":"CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)"})        
        sts_SoftwareSecurityCode.text = "a8d18e4e5aa00b44a0b1f9ef413ad8215116bd3ce91730d580eaed795c83b5a32fe6f0823abc71400b3d59eb542b7de8"
        sts_AuthorizationProvider = ET.SubElement(sts_DianExtensions, 'sts:AuthorizationProvider')
        sts_AuthorizationProviderID = ET.SubElement(sts_AuthorizationProvider, 'sts:AuthorizationProviderID', {"schemeAgencyID":"195", "schemeAgencyName":"CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)", "schemeID":"4", "schemeName":"31"})
        sts_AuthorizationProviderID.text = "800197268"
        sts_QRCode = ET.SubElement(sts_DianExtensions, 'sts:QRCode')
        sts_QRCode.text = """NroFactura=SETP990000002
								NitFacturador=800197268
								NitAdquiriente=900108281
								FechaFactura=2019-06-20
								ValorTotalFactura=14024.07
								CUFE=941cf36af62dbbc06f105d2a80e9bfe683a90e84960eae4d351cc3afbe8f848c26c39bac4fbc80fa254824c6369ea694
								URL=https://catalogo-vpfe-hab.dian.gov.co/Document/FindDocument?documentKey=941cf36af62dbbc06f105d2a80e9bfe683a90e84960eae4d351cc3afbe8f848c26c39bac4fbc80fa254824c6369ea694&amp;partitionKey=co|06|94&amp;emissionDate=20190620"""
        
        ext_UBLExtension = ET.SubElement(ext_UBLExtensions, 'ext:UBLExtension')
        ext_ExtensionContent = ET.SubElement(ext_UBLExtension, 'ext:ExtensionContent')
        ds_Signature = ET.SubElement(ext_ExtensionContent, 'ds:Signature', {"Id":"xmldsig-d0322c4f-be87-495a-95d5-9244980495f4"})
        
        ds_SignedInfo = ET.SubElement(ds_Signature, 'ds:SignedInfo')
        ds_CanonicalizationMethod = ET.SubElement(ds_SignedInfo, 'ds:CanonicalizationMethod', {"Algorithm":"http://www.w3.org/TR/2001/REC-xml-c14n-20010315"})
        ds_SignatureMethod = ET.SubElement(ds_SignedInfo, 'ds:SignatureMethod', {"Algorithm":"http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"})
        ds_Reference = ET.SubElement(ds_SignedInfo, 'ds:Reference', {"Id":"xmldsig-d0322c4f-be87-495a-95d5-9244980495f4-ref0", "URI":""})
        ds_Transforms = ET.SubElement(ds_Reference, 'ds:Transforms')
        ds_Transform = ET.SubElement(ds_Transforms, 'ds:Transform', {"Algorithm":"http://www.w3.org/2000/09/xmldsig#enveloped-signature"})
        ds_DigestMethod = ET.SubElement(ds_Reference, 'ds:DigestMethod', {"Algorithm":"http://www.w3.org/2001/04/xmlenc#sha256"})
        ds_DigestValue = ET.SubElement(ds_Reference, 'ds:DigestValue')
        ds_DigestValue.text = "akcOQ5qEh4dkMwt0d5BoXRR8Bo4vdy9DBZtfF5O0SsA="
        ds_Reference = ET.SubElement(ds_SignedInfo, 'ds:Reference', {"URI":"#xmldsig-87d128b5-aa31-4f0b-8e45-3d9cfa0eec26-keyinfo"})
        ds_DigestMethod = ET.SubElement(ds_Reference, 'ds:DigestMethod', {"Algorithm":"http://www.w3.org/2001/04/xmlenc#sha256"})
        ds_DigestValue = ET.SubElement(ds_Reference, 'ds:DigestValue')
        ds_DigestValue.text = "troRYR2fcmJLV6gYibVM6XlArbddSCkjYkACZJP47/4="
        ds_Reference = ET.SubElement(ds_SignedInfo, 'ds:Reference', {"Type":"http://uri.etsi.org/01903#SignedProperties", "URI":"#xmldsig-d0322c4f-be87-495a-95d5-9244980495f4-signedprops"})
        ds_DigestMethod = ET.SubElement(ds_Reference, 'ds:DigestMethod', {"Algorithm":"http://www.w3.org/2001/04/xmlenc#sha256"})
        ds_DigestValue = ET.SubElement(ds_Reference, 'ds:DigestValue')
        ds_DigestValue.text = "hpIsyD/08hVUc1exnfEyhGyKX5s3pUPbpMKmPhkPPqU="
        
        ds_SignatureValue = ET.SubElement(ds_Signature, 'ds:SignatureValue', {"Id":"xmldsig-d0322c4f-be87-495a-95d5-9244980495f4-sigvalue"})
        ds_SignatureValue.text = """
q4HWeb47oLdDM4D3YiYDOSXE4YfSHkQKxUfSYiEiPuP2XWvD7ELZTC4ENFv6krgDAXczmi0W7OMi
LIVvuFz0ohPUc4KNlUEzqSBHVi6sC34sCqoxuRzOmMEoCB9Tr4VICxU1Ue9XhgP7o6X4f8KFAQWW
NaeTtA6WaO/yUtq91MKP59aAnFMfYl8lXpaS0kpUwuui3wdCZsGycsl1prEWiwzpaukEUOXyTo7o
RBOuNsDIUhP24Fv1alRFnX6/9zEOpRTs4rEQKN3IQnibF757LE/nnkutElZHTXaSV637gpHjXoUN
5JrUwTNOXvmFS98N6DczCQfeNuDIozYwtFVlMw==
"""        
        ds_KeyInfo = ET.SubElement(ds_Signature, 'ds:KeyInfo', {"Id":"xmldsig-87d128b5-aa31-4f0b-8e45-3d9cfa0eec26-keyinfo"})
        ds_X509Data = ET.SubElement(ds_KeyInfo, 'ds:X509Data')
        ds_X509Certificate = ET.SubElement(ds_X509Data, 'ds:X509Certificate')
        ds_X509Certificate.text = """
MIIIODCCBiCgAwIBAgIIbAsHYmJtoOIwDQYJKoZIhvcNAQELBQAwgbQxIzAhBgkqhkiG9w0BCQEW
FGluZm9AYW5kZXNzY2QuY29tLmNvMSMwIQYDVQQDExpDQSBBTkRFUyBTQ0QgUy5BLiBDbGFzZSBJ
STEwMC4GA1UECxMnRGl2aXNpb24gZGUgY2VydGlmaWNhY2lvbiBlbnRpZGFkIGZpbmFsMRMwEQYD
VQQKEwpBbmRlcyBTQ0QuMRQwEgYDVQQHEwtCb2dvdGEgRC5DLjELMAkGA1UEBhMCQ08wHhcNMTcw
OTE2MTM0ODE5WhcNMjAwOTE1MTM0ODE5WjCCARQxHTAbBgNVBAkTFENhbGxlIEZhbHNhIE5vIDEy
IDM0MTgwNgYJKoZIhvcNAQkBFilwZXJzb25hX2p1cmlkaWNhX3BydWViYXMxQGFuZGVzc2NkLmNv
bS5jbzEsMCoGA1UEAxMjVXN1YXJpbyBkZSBQcnVlYmFzIFBlcnNvbmEgSnVyaWRpY2ExETAPBgNV
BAUTCDExMTExMTExMRkwFwYDVQQMExBQZXJzb25hIEp1cmlkaWNhMSgwJgYDVQQLEx9DZXJ0aWZp
Y2FkbyBkZSBQZXJzb25hIEp1cmlkaWNhMQ8wDQYDVQQHEwZCb2dvdGExFTATBgNVBAgTDEN1bmRp
bmFtYXJjYTELMAkGA1UEBhMCQ08wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC0Dn8t
oZ2CXun+63zwYecJ7vNmEmS+YouH985xDek7ImeE9lMBHXE1M5KDo7iT/tUrcFwKj717PeVL52Nt
B6WU4+KBt+nrK+R+OSTpTno5EvpzfIoS9pLI74hHc017rY0wqjl0lw+8m7fyLfi/JO7AtX/dthS+
MKHIcZ1STPlkcHqmbQO6nhhr/CGl+tKkCMrgfEFIm1kv3bdWqk3qHrnFJ6s2GoVNZVCTZW/mOzPC
NnnUW12LDd/Kd+MjN6aWbP0D/IJbB42Npqv8+/oIwgCrbt0sS1bysUgdT4im9bBhb00MWVmNRBBe
3pH5knzkBid0T7TZsPCyiMBstiLT3yfpAgMBAAGjggLpMIIC5TAMBgNVHRMBAf8EAjAAMB8GA1Ud
IwQYMBaAFKhLtPQLp7Zb1KAohRCdBBMzxKf3MDcGCCsGAQUFBwEBBCswKTAnBggrBgEFBQcwAYYb
aHR0cDovL29jc3AuYW5kZXNzY2QuY29tLmNvMIIB4wYDVR0gBIIB2jCCAdYwggHSBg0rBgEEAYH0
SAECCQIFMIIBvzBBBggrBgEFBQcCARY1aHR0cDovL3d3dy5hbmRlc3NjZC5jb20uY28vZG9jcy9E
UENfQW5kZXNTQ0RfVjIuNS5wZGYwggF4BggrBgEFBQcCAjCCAWoeggFmAEwAYQAgAHUAdABpAGwA
aQB6AGEAYwBpAPMAbgAgAGQAZQAgAGUAcwB0AGUAIABjAGUAcgB0AGkAZgBpAGMAYQBkAG8AIABl
AHMAdADhACAAcwB1AGoAZQB0AGEAIABhACAAbABhAHMAIABQAG8AbADtAHQAaQBjAGEAcwAgAGQA
ZQAgAEMAZQByAHQAaQBmAGkAYwBhAGQAbwAgAGQAZQAgAFAAZQByAHMAbwBuAGEAIABKAHUAcgDt
AGQAaQBjAGEAIAAoAFAAQwApACAAeQAgAEQAZQBjAGwAYQByAGEAYwBpAPMAbgAgAGQAZQAgAFAA
cgDhAGMAdABpAGMAYQBzACAAZABlACAAQwBlAHIAdABpAGYAaQBjAGEAYwBpAPMAbgAgACgARABQ
AEMAKQAgAGUAcwB0AGEAYgBsAGUAYwBpAGQAYQBzACAAcABvAHIAIABBAG4AZABlAHMAIABTAEMA
RDAdBgNVHSUEFjAUBggrBgEFBQcDAgYIKwYBBQUHAwQwRgYDVR0fBD8wPTA7oDmgN4Y1aHR0cDov
L3d3dy5hbmRlc3NjZC5jb20uY28vaW5jbHVkZXMvZ2V0Q2VydC5waHA/Y3JsPTEwHQYDVR0OBBYE
FL9BXJHmFVE5c5Ai8B1bVBWqXsj7MA4GA1UdDwEB/wQEAwIE8DANBgkqhkiG9w0BAQsFAAOCAgEA
b/pa7yerHOu1futRt8QTUVcxCAtK9Q00u7p4a5hp2fVzVrhVQIT7Ey0kcpMbZVPgU9X2mTHGfPdb
R0hYJGEKAxiRKsmAwmtSQgWh5smEwFxG0TD1chmeq6y0GcY0lkNA1DpHRhSK368vZlO1p2a6S13Y
1j3tLFLqf5TLHzRgl15cfauVinEHGKU/cMkjLwxNyG1KG/FhCeCCmawATXWLgQn4PGgvKcNrz+y0
cwldDXLGKqriw9dce2Zerc7OCG4/XGjJ2PyZOJK9j1VYIG4pnmoirVmZbKwWaP4/TzLs6LKaJ4b6
6xLxH3hUtoXCzYQ5ehYyrLVwCwTmKcm4alrEht3FVWiWXA/2tj4HZiFoG+I1OHKmgkNv7SwHS7z9
tFEFRaD3W3aD7vwHEVsq2jTeYInE0+7r2/xYFZ9biLBrryl+q22zM5W/EJq6EJPQ6SM/eLqkpzqM
EF5OdcJ5kIOxLbrIdOh0+grU2IrmHXr7cWNP6MScSL7KSxhjPJ20F6eqkO1Z/LAxqNslBIKkYS24
VxPbXu0pBXQvu+zAwD4SvQntIG45y/67h884I/tzYOEJi7f6/NFAEuV+lokw/1MoVsEgFESASI9s
N0DfUniabyrZ3nX+LG3UFL1VDtDPWrLTNKtb4wkKwGVwqtAdGFcE+/r/1WG0eQ64xCq0NLutCxg=
"""        
        ds_Object = ET.SubElement(ds_Signature, 'ds:Object')
        xades_QualifyingProperties = ET.SubElement(ds_Object, 'xades:QualifyingProperties', {"Target":"#xmldsig-d0322c4f-be87-495a-95d5-9244980495f4"})
        xades_SignedProperties = ET.SubElement(xades_QualifyingProperties, 'xades:SignedProperties', {"Id":"xmldsig-d0322c4f-be87-495a-95d5-9244980495f4-signedprops"})
        xades_SignedSignatureProperties = ET.SubElement(xades_SignedProperties, 'xades:SignedSignatureProperties')
        xades_SigningTime = ET.SubElement(xades_SignedSignatureProperties, 'xades:SigningTime')
        xades_SigningTime.text = "2019-06-21T19:09:35.993-05:00"
        
        xades_SigningCertificate = ET.SubElement(xades_SignedSignatureProperties, 'xades:SigningCertificate')
        xades_Cert = ET.SubElement(xades_SigningCertificate, 'xades:Cert')
        xades_CertDigest = ET.SubElement(xades_Cert, 'xades:CertDigest')
        ds_DigestMethod = ET.SubElement(xades_CertDigest, 'ds:DigestMethod', {"Algorithm":"http://www.w3.org/2001/04/xmlenc#sha256"})
        ds_DigestValue = ET.SubElement(xades_CertDigest, 'ds:DigestValue')
        ds_DigestValue.text = "nem6KXhqlV0A0FK5o+MwJZ3Y1aHgmL1hDs/RMJu7HYw="
        xades_IssuerSerial = ET.SubElement(xades_Cert, 'xades:IssuerSerial')
        ds_X509IssuerName = ET.SubElement(xades_IssuerSerial, 'ds:X509IssuerName')
        ds_X509IssuerName.text = "C=CO,L=Bogota D.C.,O=Andes SCD.,OU=Division de certificacion entidad final,CN=CA ANDES SCD S.A. Clase II,1.2.840.113549.1.9.1=#1614696e666f40616e6465737363642e636f6d2e636f"
        ds_X509SerialNumber = ET.SubElement(xades_IssuerSerial, 'ds:X509SerialNumber')
        ds_X509SerialNumber.text = "7785324499979575522"
        xades_Cert = ET.SubElement(xades_SigningCertificate, 'xades:Cert')
        xades_CertDigest = ET.SubElement(xades_Cert, 'xades:CertDigest')
        ds_DigestMethod = ET.SubElement(xades_CertDigest, 'ds:DigestMethod', {"Algorithm":"http://www.w3.org/2001/04/xmlenc#sha256"})
        ds_DigestValue = ET.SubElement(xades_CertDigest, 'ds:DigestValue')
        ds_DigestValue.text = "oEsyOEeUGTXr45Jr0jHJx3l/9CxcsxPMOTarEiXOclY="
        xades_IssuerSerial = ET.SubElement(xades_Cert, 'xades:IssuerSerial')
        ds_X509IssuerName = ET.SubElement(xades_IssuerSerial, 'ds:X509IssuerName')
        ds_X509IssuerName.text = "C=CO,L=Bogota D.C.,O=Andes SCD,OU=Division de certificacion,CN=ROOT CA ANDES SCD S.A.,1.2.840.113549.1.9.1=#1614696e666f40616e6465737363642e636f6d2e636f"
        ds_X509SerialNumber = ET.SubElement(xades_IssuerSerial, 'ds:X509SerialNumber')
        ds_X509SerialNumber.text = "8136867327090815624"        
        xades_Cert = ET.SubElement(xades_SigningCertificate, 'xades:Cert')
        xades_CertDigest = ET.SubElement(xades_Cert, 'xades:CertDigest')
        ds_DigestMethod = ET.SubElement(xades_CertDigest, 'ds:DigestMethod', {"Algorithm":"http://www.w3.org/2001/04/xmlenc#sha256"})
        ds_DigestValue = ET.SubElement(xades_CertDigest, 'ds:DigestValue')
        ds_DigestValue.text = "Cs7emRwtXWVYHJrqS9eXEXfUcFyJJBqFhDFOetHu8ts="
        xades_IssuerSerial = ET.SubElement(xades_Cert, 'xades:IssuerSerial')
        ds_X509IssuerName = ET.SubElement(xades_IssuerSerial, 'ds:X509IssuerName')
        ds_X509IssuerName.text = "C=CO,L=Bogota D.C.,O=Andes SCD,OU=Division de certificacion,CN=ROOT CA ANDES SCD S.A.,1.2.840.113549.1.9.1=#1614696e666f40616e6465737363642e636f6d2e636f"
        ds_X509SerialNumber = ET.SubElement(xades_IssuerSerial, 'ds:X509SerialNumber')
        ds_X509SerialNumber.text = "3184328748892787122"        

        xades_SignaturePolicyIdentifier = ET.SubElement(xades_SignedSignatureProperties, 'xades:SignaturePolicyIdentifier')
        xades_SignaturePolicyId = ET.SubElement(xades_SignaturePolicyIdentifier, 'xades:SignaturePolicyId')
        xades_SigPolicyId = ET.SubElement(xades_SignaturePolicyId, 'xades:SigPolicyId')
        xades_Identifier = ET.SubElement(xades_SigPolicyId, 'xades:Identifier')
        xades_Identifier.text = "https://facturaelectronica.dian.gov.co/politicadefirma/v1/politicadefirmav2.pdf"
        xades_SigPolicyHash = ET.SubElement(xades_SignaturePolicyId, 'xades:SigPolicyHash')
        ds_DigestMethod = ET.SubElement(xades_SigPolicyHash, 'ds:DigestMethod', {"Algorithm":"http://www.w3.org/2001/04/xmlenc#sha256"})
        ds_DigestValue = ET.SubElement(xades_SigPolicyHash, 'ds:DigestValue')
        ds_DigestValue.text = "dMoMvtcG5aIzgYo0tIsSQeVJBDnUnfSOfBpxXrmor0Y="

        xades_SignerRole = ET.SubElement(xades_SignedSignatureProperties, 'xades:SignerRole')
        xades_ClaimedRoles = ET.SubElement(xades_SignerRole, 'xades:ClaimedRoles')
        xades_ClaimedRole = ET.SubElement(xades_ClaimedRoles, 'xades:ClaimedRole')
        xades_ClaimedRole.text = "supplier"

        cbc_UBLVersionID = ET.SubElement(invoice,"cbc:UBLVersionID")
        cbc_UBLVersionID.text = "UBL 2.1"    
        
        cbc_CustomizationID = ET.SubElement(invoice,"cbc:CustomizationID")
        cbc_CustomizationID.text = "05"

        cbc_ProfileID = ET.SubElement(invoice,"cbc:ProfileID")
        cbc_ProfileID.text = "DIAN 2.1"

        cbc_ProfileExecutionID = ET.SubElement(invoice, "cbc:ProfileExecutionID")
        cbc_ProfileExecutionID.text = "2"
        
        cbc_ID = ET.SubElement(invoice, "cbc:ID")
        cbc_ID.text = "SETP990000002"

        cbc_UUID = ET.SubElement(invoice, "cbc:UUID", {"schemeID":"2", "schemeName":"CUFE-SHA384"})
        cbc_UUID.text = "941cf36af62dbbc06f105d2a80e9bfe683a90e84960eae4d351cc3afbe8f848c26c39bac4fbc80fa254824c6369ea694"
        
        cbc_IssueDate = ET.SubElement(invoice, "cbc:IssueDate")
        cbc_IssueDate.text = "2019-06-20"

        cbc_IssueTime = ET.SubElement(invoice, "cbc:IssueTime")
        cbc_IssueTime.text = "09:15:23-05:00"

        cbc_InvoiceTypeCode = ET.SubElement(invoice, "cbc:InvoiceTypeCode")
        cbc_InvoiceTypeCode.text = "01"

        cbc_Note = ET.SubElement(invoice, "cbc:Note")
        cbc_Note.text = "SETP9900000022019-06-2009:15:23-05:0012600.06012424.01040.00030.0014024.07900508908900108281fc8eac422eba16e22ffd8c6f94b3f40a6e38162c2"

        cbc_DocumentCurrencyCode = ET.SubElement(invoice, "cbc:DocumentCurrencyCode", {"listAgencyID":"6","listAgencyName":"United Nations Economic Commission for Europe","listID":"ISO 4217 Alpha"})
        cbc_DocumentCurrencyCode.text = "COP"

        cbc_LineCountNumeric = ET.SubElement(invoice, "cbc:LineCountNumeric")
        cbc_LineCountNumeric.text = "2"

        cac_InvoicePeriod = ET.SubElement(invoice, "cac:InvoicePeriod")
        cbc_StartDate = ET.SubElement(cac_InvoicePeriod, "cbc:StartDate")
        cbc_StartDate.text = "2019-05-01"
        cbc_EndDate = ET.SubElement(cac_InvoicePeriod, "cbc:EndDate")
        cbc_EndDate.text = "2019-05-30"
        cac_BillingReference = ET.SubElement(invoice, "cac:BillingReference")
        cac_InvoiceDocumentReference = ET.SubElement(cac_BillingReference, "cac:InvoiceDocumentReference")
        cbc_ID = ET.SubElement(cac_InvoiceDocumentReference, "cbc:ID")
        cbc_ID.text = "SFR3123856"
        cbc_UUID = ET.SubElement(cac_InvoiceDocumentReference, "cbc:UUID", {"schemeName":"CUFE-SHA1"})
        cbc_UUID.text = "a675432fecc1d537361dcdbdfbd08d6e5283f2bc"
        cbc_IssueDate = ET.SubElement(cac_InvoiceDocumentReference, "cbc:IssueDate")
        cbc_IssueDate.text = "2018-09-29"
        cbc_DocumentDescription = ET.SubElement(cac_InvoiceDocumentReference, "cbc:DocumentDescription")
        cbc_DocumentDescription.text = "Prepago recibido"

        cac_BillingReference = ET.SubElement(invoice, "cac:BillingReference")
        cac_InvoiceDocumentReference = ET.SubElement(cac_BillingReference, "cac:InvoiceDocumentReference")
        cbc_ID = ET.SubElement(cac_InvoiceDocumentReference, "cbc:ID")
        cbc_ID.text = "SETP990000101"
        cbc_UUID = ET.SubElement(cac_InvoiceDocumentReference, "cbc:UUID", {"schemeName":"CUFE-SHA384"})
        cbc_UUID.text = "1dc661228f152332d876e1f1cd2042ecdea1804ed0da78f84dc9ee0938d69f17037dc53f97778ed2721d65c1fc3c73ac"
        cbc_IssueDate = ET.SubElement(cac_InvoiceDocumentReference, "cbc:IssueDate")
        cbc_IssueDate.text = "2018-09-29"
        cbc_DocumentDescription = ET.SubElement(cac_InvoiceDocumentReference, "cbc:DocumentDescription")
        cbc_DocumentDescription.text = "Factura anterior"
        cac_AccountingSupplierParty = ET.SubElement(invoice, "cac:AccountingSupplierParty")
        cbc_AdditionalAccountID = ET.SubElement(cac_AccountingSupplierParty, "cbc:AdditionalAccountID")
        cbc_AdditionalAccountID.text = "1"
        
        cac_Party = ET.SubElement(cac_AccountingSupplierParty, "cac:Party")
        cac_PartyName = ET.SubElement(cac_Party, "cac:PartyName")
        cbc_Name = ET.SubElement(cac_PartyName, "cbc:Name")
        cbc_Name.text = "Nombre Tienda"
        cac_PartyName = ET.SubElement(cac_Party, "cac:PartyName")
        cbc_Name = ET.SubElement(cac_PartyName, "cbc:Name")
        cbc_Name.text = "Establecimiento Principal"
        cac_PartyName = ET.SubElement(cac_Party, "cac:PartyName")
        cbc_Name = ET.SubElement(cac_PartyName, "cbc:Name")
        cbc_Name.text = "DIAN"
        cac_PhysicalLocation = ET.SubElement(cac_Party, "cac:PhysicalLocation")
        cac_Address = ET.SubElement(cac_PhysicalLocation, "cac:Address")
        cbc_ID = ET.SubElement(cac_Address, "cbc:ID")
        cbc_ID.text = "11001"
        cbc_CityName = ET.SubElement(cac_Address, "cbc:CityName")
        cbc_CityName.text = "Bogotá, D.c. "
        cbc_CountrySubentity = ET.SubElement(cac_Address, "cbc:CountrySubentity")
        cbc_CountrySubentity.text = "Bogotá"
        cbc_CountrySubentityCode = ET.SubElement(cac_Address, "cbc:CountrySubentityCode")
        cbc_CountrySubentityCode.text = "11"
        cac_AddressLine = ET.SubElement(cac_Address, "cac:AddressLine")
        cbc_Line = ET.SubElement(cac_AddressLine, "cbc:Line")
        cbc_Line.text = "Av. #97 - 13"
        cac_Country = ET.SubElement(cac_Address, "cac:Country")
        cbc_IdentificationCode = ET.SubElement(cac_Country, "cbc:IdentificationCode")
        cbc_IdentificationCode.text = "CO"        
        cbc_Name = ET.SubElement(cac_Country, "cbc:Name", {"languageID":"es"})
        cbc_Name.text = "Colombia"
        
        cac_PartyTaxScheme = ET.SubElement(cac_Party, "cac:PartyTaxScheme")
        cbc_RegistrationName = ET.SubElement(cac_PartyTaxScheme, "cbc:RegistrationName")
        cbc_RegistrationName.text = "DIAN"
        cbc_CompanyID = ET.SubElement(cac_PartyTaxScheme, "cbc:CompanyID", {"schemeAgencyID":"195", "schemeAgencyName":"CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)", "schemeID":"4", "schemeName":"31"})
        cbc_CompanyID.text = "800197268"
        cbc_TaxLevelCode = ET.SubElement(cac_PartyTaxScheme, "cbc:TaxLevelCode", {"listName":"05"})
        cbc_TaxLevelCode.text = "O-99"
        cac_RegistrationAddress = ET.SubElement(cac_PartyTaxScheme, "cac:RegistrationAddress")
        cbc_ID = ET.SubElement(cac_RegistrationAddress, "cbc:ID")
        cbc_ID.text = "11001"
        cbc_CityName = ET.SubElement(cac_RegistrationAddress, "cbc:CityName")
        cbc_CityName.text = "Bogotá, D.c. "
        cbc_CountrySubentity = ET.SubElement(cac_RegistrationAddress, "cbc:CountrySubentity")
        cbc_CountrySubentity.text = "Bogotá"
        cbc_CountrySubentityCode = ET.SubElement(cac_RegistrationAddress, "cbc:CountrySubentityCode")
        cbc_CountrySubentityCode.text = "11"
        cac_AddressLine = ET.SubElement(cac_RegistrationAddress, "cac:AddressLine")
        cbc_Line = ET.SubElement(cac_AddressLine, "cbc:Line")
        cbc_Line.text = "Av. Jiménez #7 - 13"
        cac_Country = ET.SubElement(cac_RegistrationAddress, "cac:Country")
        cbc_IdentificationCode = ET.SubElement(cac_Country, "cbc:IdentificationCode")
        cbc_IdentificationCode.text = "CO"
        cbc_Name = ET.SubElement(cac_Country, "cbc:Name", {"languageID":"es"})
        cbc_Name.text = "Colombia"        
        cac_TaxScheme = ET.SubElement(cac_PartyTaxScheme, "cac:TaxScheme")
        cbc_ID = ET.SubElement(cac_TaxScheme, "cbc:ID")
        cbc_ID.text = "01"
        cbc_Name = ET.SubElement(cac_TaxScheme, "cbc:Name")
        cbc_Name.text = "IVA"

        cac_PartyLegalEntity = ET.SubElement(cac_Party, "cac:PartyLegalEntity")
        cbc_RegistrationName = ET.SubElement(cac_PartyLegalEntity, "cbc:RegistrationName")
        cbc_RegistrationName.text = "DIAN"
        cbc_CompanyID = ET.SubElement(cac_PartyLegalEntity, "cbc:CompanyID", {"schemeAgencyID":"195", "schemeAgencyName":"CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)", "schemeID":"9", "schemeName":"31"})
        cbc_CompanyID.text = "800197268"
        cac_CorporateRegistrationScheme = ET.SubElement(cac_PartyLegalEntity, "cac:CorporateRegistrationScheme")
        cbc_ID = ET.SubElement(cac_CorporateRegistrationScheme, "cbc:ID")
        cbc_ID.text = "SETP"
        cbc_Name = ET.SubElement(cac_CorporateRegistrationScheme, "cbc:Name")
        cbc_Name.text = "10181"
        
        cac_Contact = ET.SubElement(cac_Party, "cac:Contact")
        cbc_Name = ET.SubElement(cac_Contact, "cbc:Name")
        cbc_Name.text = "Eric Valencia"
        cbc_Telephone = ET.SubElement(cac_Contact, "cbc:Telephone")
        cbc_Telephone.text = "6111111"
        cbc_ElectronicMail = ET.SubElement(cac_Contact, "cbc:ElectronicMail")
        cbc_ElectronicMail.text = "eric.valencia@ket.co"
        cbc_Note = ET.SubElement(cac_Contact, "cbc:Note")
        cbc_Note.text = "Test descripcion contacto"

        cac_AccountingCustomerParty = ET.SubElement(invoice, "cac:AccountingCustomerParty")
        cbc_AdditionalAccountID = ET.SubElement(cac_AccountingCustomerParty, "cbc:AdditionalAccountID")
        cbc_AdditionalAccountID.text = "1"
        cac_Party = ET.SubElement(cac_AccountingCustomerParty, "cac:Party")
        cac_PartyName = ET.SubElement(cac_Party, "cac:PartyName")
        cbc_Name = ET.SubElement(cac_PartyName, "cbc:Name")
        cbc_Name.text = "OPTICAS GMO COLOMBIA S A S"
        cac_PhysicalLocation = ET.SubElement(cac_Party, "cac:PhysicalLocation")
        cac_Address = ET.SubElement(cac_PhysicalLocation, "cac:Address")
        cbc_ID = ET.SubElement(cac_Address, "cbc:ID")
        cbc_ID.text = "11001"
        cbc_CityName = ET.SubElement(cac_Address, "cbc:CityName")
        cbc_CityName.text = "Bogotá, D.c. "
        cbc_CountrySubentity = ET.SubElement(cac_Address, "cbc:CountrySubentity")
        cbc_CountrySubentity.text = "Bogotá"
        cbc_CountrySubentityCode = ET.SubElement(cac_Address, "cbc:CountrySubentityCode")
        cbc_CountrySubentityCode.text = "11"
        cac_AddressLine = ET.SubElement(cac_Address, "cac:AddressLine")
        cbc_Line = ET.SubElement(cac_AddressLine, "cbc:Line")
        cbc_Line.text = "CARRERA 8 No 20-14/40"
        cac_Country = ET.SubElement(cac_Address, "cac:Country")
        cbc_IdentificationCode = ET.SubElement(cac_Country, "cbc:IdentificationCode")
        cbc_IdentificationCode.text = "CO"
        cbc_Name = ET.SubElement(cac_Country, "cbc:Name", {"languageID":"es"})
        cbc_Name.text = "Colombia"
        cac_PartyTaxScheme = ET.SubElement(cac_Party, "cac:PartyTaxScheme")
        cbc_RegistrationName = ET.SubElement(cac_PartyTaxScheme, "cbc:RegistrationName")
        cbc_RegistrationName.text = "OPTICAS GMO COLOMBIA S A S"
        cbc_CompanyID = ET.SubElement(cac_PartyTaxScheme, "cbc:CompanyID", {"schemeAgencyID":"195", "schemeAgencyName":"CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)", "schemeID":"3", "schemeName":"31"})
        cbc_CompanyID.text = "900108281"
        cbc_TaxLevelCode = ET.SubElement(cac_PartyTaxScheme, "cbc:TaxLevelCode", {"listName":"04"})
        cbc_TaxLevelCode.text = "O-99"
        cac_RegistrationAddress = ET.SubElement(cac_PartyTaxScheme, "cac:RegistrationAddress")
        cbc_ID = ET.SubElement(cac_RegistrationAddress, "cbc:ID")
        cbc_ID.text = "11001"
        cbc_CityName = ET.SubElement(cac_RegistrationAddress, "cbc:CityName")
        cbc_CityName.text = "Bogotá, D.c. "
        cbc_CountrySubentity = ET.SubElement(cac_RegistrationAddress, "cbc:CountrySubentity")
        cbc_CountrySubentity.text = "Bogotá"
        cbc_CountrySubentityCode = ET.SubElement(cac_RegistrationAddress, "cbc:CountrySubentityCode")
        cbc_CountrySubentityCode.text = "11"
        cac_AddressLine = ET.SubElement(cac_RegistrationAddress, "cac:AddressLine")
        cbc_Line = ET.SubElement(cac_AddressLine, "cbc:Line")
        cbc_Line.text = "CR 9 A N0 99 - 07 OF 802"
        cac_Country = ET.SubElement(cac_RegistrationAddress, "cac:Country")
        cbc_IdentificationCode = ET.SubElement(cac_Country, "cbc:IdentificationCode")
        cbc_IdentificationCode.text = "CO"
        cbc_Name = ET.SubElement(cac_Country, "cbc:Name", {"languageID":"es"})
        cbc_Name.text = "Colombia"
        cac_TaxScheme = ET.SubElement(cac_PartyTaxScheme, "cac:TaxScheme")
        cbc_ID = ET.SubElement(cac_TaxScheme, "cbc:ID")
        cbc_ID.text = "01"
        cbc_Name = ET.SubElement(cac_TaxScheme, "cbc:Name")
        cbc_Name.text = "IVA"

        cac_PartyLegalEntity = ET.SubElement(cac_Party, "cac:PartyLegalEntity")
        cbc_RegistrationName = ET.SubElement(cac_PartyLegalEntity, "cbc:RegistrationName")
        cbc_RegistrationName.text = "OPTICAS GMO COLOMBIA S A S"
        cbc_CompanyID = ET.SubElement(cac_PartyLegalEntity, "cbc:CompanyID", {"schemeAgencyID":"195", "schemeAgencyName":"CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)", "schemeID":"3", "schemeName":"31"})
        cbc_CompanyID.text = "900108281"
        cac_CorporateRegistrationScheme = ET.SubElement(cac_PartyLegalEntity, "cac:CorporateRegistrationScheme")
        cbc_Name = ET.SubElement(cac_CorporateRegistrationScheme, "cbc:Name")
        cbc_Name.text = "90518"
        cac_Contact = ET.SubElement(cac_Party, "cac:Contact")
        cbc_Name = ET.SubElement(cac_Contact, "cbc:Name")
        cbc_Name.text = "Diana Cruz"
        cbc_Telephone = ET.SubElement(cac_Contact, "cbc:Telephone")
        cbc_Telephone.text = "31031031089"
        cbc_ElectronicMail = ET.SubElement(cac_Contact, "cbc:ElectronicMail")
        cbc_ElectronicMail.text = "dcruz@empresa.org"

        cac_TaxRepresentativeParty = ET.SubElement(invoice, "cac:TaxRepresentativeParty")
        cac_PartyIdentification = ET.SubElement(cac_TaxRepresentativeParty, "cac:PartyIdentification")
        cbc_ID = ET.SubElement(cac_PartyIdentification, "cbc:ID", {"schemeAgencyID":"195", "schemeAgencyName":"CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)", "schemeID":"4", "schemeName":"31"})
        cbc_ID.text = "989123123"

        cac_Delivery = ET.SubElement(invoice, "cac:Delivery")
        cac_DeliveryAddress = ET.SubElement(cac_Delivery, "cac:DeliveryAddress")
        cbc_ID = ET.SubElement(cac_DeliveryAddress, "cbc:ID")
        cbc_ID.text = "11001"
        cbc_CityName = ET.SubElement(cac_DeliveryAddress, "cbc:CityName")
        cbc_CityName.text = "Bogotá, D.c. "
        cbc_CountrySubentity = ET.SubElement(cac_DeliveryAddress, "cbc:CountrySubentity")
        cbc_CountrySubentity.text = "Bogotá, D.c. 11"
        cbc_CountrySubentityCode = ET.SubElement(cac_DeliveryAddress, "cbc:CountrySubentityCode")
        cbc_CountrySubentityCode.text = "11"
        cac_AddressLine = ET.SubElement(cac_DeliveryAddress, "cac:AddressLine")    
        cbc_Line = ET.SubElement(cac_AddressLine, "cbc:Line")  
        cbc_Line.text = "CARRERA 8 No 20-14/40"
        cac_Country = ET.SubElement(cac_DeliveryAddress, "cac:Country")
        cbc_IdentificationCode = ET.SubElement(cac_Country, "cbc:IdentificationCode")
        cbc_IdentificationCode.text = "CO"
        cbc_Name = ET.SubElement(cac_Country, "cbc:Name", {"languageID":"es"})
        cbc_Name.text = "Colombia"
        
        cac_DeliveryParty = ET.SubElement(cac_Delivery, "cac:DeliveryParty")
        cac_PartyName = ET.SubElement(cac_DeliveryParty, "cac:PartyName")
        cbc_Name = ET.SubElement(cac_PartyName, "cbc:Name")     
        cbc_Name.text = "Empresa de transporte"
        cac_PhysicalLocation = ET.SubElement(cac_DeliveryParty, "cac:PhysicalLocation")
        cac_Address = ET.SubElement(cac_PhysicalLocation, "cac:Address")
        cbc_ID = ET.SubElement(cac_Address, "cbc:ID")
        cbc_ID.text = "11001"
        cbc_CityName = ET.SubElement(cac_Address, "cbc:CityName")
        cbc_CityName.text = "Bogotá, D.c. "
        cbc_CountrySubentity = ET.SubElement(cac_Address, "cbc:CountrySubentity")
        cbc_CountrySubentity.text = "Bogotá"
        cbc_CountrySubentityCode = ET.SubElement(cac_Address, "cbc:CountrySubentityCode")
        cbc_CountrySubentityCode.text = "11"
        cac_AddressLine = ET.SubElement(cac_Address, "cac:AddressLine")
        cbc_Line = ET.SubElement(cac_AddressLine, "cbc:Line")
        cbc_Line.text = "Av.  #17 - 193"
        cac_Country = ET.SubElement(cac_Address, "cac:Country")
        cbc_IdentificationCode = ET.SubElement(cac_Country, "cbc:IdentificationCode")
        cbc_IdentificationCode.text = "CO"
        cbc_Name = ET.SubElement(cac_Country, "cbc:Name", {"languageID":"es"})
        cbc_Name.text = "Colombia"

        cac_PartyTaxScheme = ET.SubElement(cac_DeliveryParty, "cac:PartyTaxScheme")
        cbc_RegistrationName = ET.SubElement(cac_PartyTaxScheme, "cbc:RegistrationName")
        cbc_RegistrationName.text = "Empresa de transporte"
        cbc_CompanyID = ET.SubElement(cac_PartyTaxScheme, "cbc:CompanyID", {"schemeAgencyID":"195", "schemeAgencyName":"CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)", "schemeID":"1", "schemeName":"31"})
        cbc_CompanyID.text = "981223983"
        cbc_TaxLevelCode = ET.SubElement(cac_PartyTaxScheme, "cbc:TaxLevelCode", {"listName":"04"})
        cbc_TaxLevelCode.text = "O-99"
        cac_TaxScheme = ET.SubElement(cac_PartyTaxScheme, "cac:TaxScheme")
        cbc_ID = ET.SubElement(cac_TaxScheme, "cbc:ID")
        cbc_ID.text = "01"
        cbc_Name = ET.SubElement(cac_TaxScheme, "cbc:Name")
        cbc_Name.text = "IVA"

        cac_PartyLegalEntity = ET.SubElement(cac_DeliveryParty, "cac:PartyLegalEntity")
        cbc_RegistrationName = ET.SubElement(cac_PartyLegalEntity, "cbc:RegistrationName")
        cbc_RegistrationName.text = "Empresa de transporte"
        cbc_CompanyID = ET.SubElement(cac_PartyLegalEntity, "cbc:CompanyID", {"schemeAgencyID":"195", "schemeAgencyName":"CO, DIAN (Dirección de Impuestos y Aduanas Nacionales)", "schemeID":"1", "schemeName":"31"})
        cbc_CompanyID.text = "981223983"
        cac_CorporateRegistrationScheme = ET.SubElement(cac_PartyLegalEntity, "cac:CorporateRegistrationScheme")
        cbc_Name = ET.SubElement(cac_CorporateRegistrationScheme, "cbc:Name")
        cbc_Name.text = "75433"

        cac_Contact = ET.SubElement(cac_DeliveryParty, "cac:Contact")
        cbc_Name = ET.SubElement(cac_Contact, "cbc:Name")
        cbc_Name.text = "Eric Van Boxsom"
        cbc_Telephone = ET.SubElement(cac_Contact, "cbc:Telephone")
        cbc_Telephone.text = "9712311"
        cbc_Telefax = ET.SubElement(cac_Contact, "cbc:Telefax")
        cbc_Telefax.text = "12431241"
        cbc_ElectronicMail = ET.SubElement(cac_Contact, "cbc:ElectronicMail")
        cbc_ElectronicMail.text = "eric.vanboxsom@gosocket.net"
        cbc_Note = ET.SubElement(cac_Contact, "cbc:Note")
        cbc_Note.text = "Test descripcion contacto"

        cac_DeliveryTerms = ET.SubElement(invoice, "cac:DeliveryTerms")
        cbc_SpecialTerms = ET.SubElement(cac_DeliveryTerms, "cbc:SpecialTerms")
        cbc_SpecialTerms.text = "Portes Pagados"
        cbc_LossRiskResponsibilityCode = ET.SubElement(cac_DeliveryTerms, "cbc:LossRiskResponsibilityCode")
        cbc_LossRiskResponsibilityCode.text = "CFR"
        cbc_LossRisk = ET.SubElement(cac_DeliveryTerms, "cbc:LossRisk")
        cbc_LossRisk.text = "Costo y Flete"

        cac_PaymentMeans = ET.SubElement(invoice, "cac:PaymentMeans")
        cbc_ID = ET.SubElement(cac_PaymentMeans, "cbc:ID")
        cbc_ID.text = "2"
        cbc_PaymentMeansCode = ET.SubElement(cac_PaymentMeans, "cbc:PaymentMeansCode")
        cbc_PaymentMeansCode.text = "41"
        cbc_PaymentDueDate = ET.SubElement(cac_PaymentMeans, "cbc:PaymentDueDate")
        cbc_PaymentDueDate.text = "2019-06-30"
        cbc_PaymentID = ET.SubElement(cac_PaymentMeans, "cbc:PaymentID")
        cbc_PaymentID.text = "1234"

        cac_PrepaidPayment = ET.SubElement(invoice, "cac:PrepaidPayment")
        cbc_ID = ET.SubElement(cac_PrepaidPayment, "cbc:ID")
        cbc_ID.text = "SFR3123856"
        cbc_PaidAmount = ET.SubElement(cac_PrepaidPayment, "cbc:PaidAmount", {"currencyID":"COP"})
        cbc_PaidAmount.text = "1000.00"
        cbc_ReceivedDate = ET.SubElement(cac_PrepaidPayment, "cbc:ReceivedDate")
        cbc_ReceivedDate.text = "2018-09-29"
        cbc_PaidDate = ET.SubElement(cac_PrepaidPayment, "cbc:PaidDate")
        cbc_PaidDate.text = "2018-09-29"
        cbc_InstructionID = ET.SubElement(cac_PrepaidPayment, "cbc:InstructionID")
        cbc_InstructionID.text = "Prepago recibido"

        cac_TaxTotal = ET.SubElement(invoice, "cac:TaxTotal")
        cbc_TaxAmount = ET.SubElement(cac_TaxTotal, "cbc:TaxAmount", {"currencyID":"COP"})
        cbc_TaxAmount.text = "2424.01"
        cac_TaxSubtotal = ET.SubElement(cac_TaxTotal, "cac:TaxSubtotal")
        cbc_TaxableAmount = ET.SubElement(cac_TaxSubtotal, "cbc:TaxableAmount", {"currencyID":"COP"})
        cbc_TaxableAmount.text = "12600.06"
        cbc_TaxAmount = ET.SubElement(cac_TaxSubtotal, "cbc:TaxAmount", {"currencyID":"COP"})
        cbc_TaxAmount.text = "2394.01"
        cac_TaxCategory = ET.SubElement(cac_TaxSubtotal, "cac:TaxCategory")
        cbc_Percent = ET.SubElement(cac_TaxCategory, "cbc:Percent")
        cbc_Percent.text = "19.00"
        cac_TaxScheme = ET.SubElement(cac_TaxCategory, "cac:TaxScheme")
        cbc_ID = ET.SubElement(cac_TaxScheme, "cbc:ID")
        cbc_ID.text = "01"
        cbc_Name = ET.SubElement(cac_TaxScheme, "cbc:Name")
        cbc_Name.text = "IVA"

        cac_TaxSubtotal = ET.SubElement(cac_TaxTotal, "cac:TaxSubtotal")
        cbc_TaxableAmount = ET.SubElement(cac_TaxSubtotal, "cbc:TaxableAmount", {"currencyID":"COP"})
        cbc_TaxableAmount.text = "187.50"
        cbc_TaxAmount = ET.SubElement(cac_TaxSubtotal, "cbc:TaxAmount", {"currencyID":"COP"})
        cbc_TaxAmount.text = "30.00"
        cac_TaxCategory = ET.SubElement(cac_TaxSubtotal, "cac:TaxCategory")
        cbc_Percent = ET.SubElement(cac_TaxCategory, "cbc:Percent")
        cbc_Percent.text = "16.00"
        cac_TaxScheme = ET.SubElement(cac_TaxCategory, "cac:TaxScheme")
        cbc_ID = ET.SubElement(cac_TaxScheme, "cbc:ID")
        cbc_ID.text = "01"
        cbc_Name = ET.SubElement(cac_TaxScheme, "cbc:Name")
        cbc_Name.text = "IVA"

        cac_TaxTotal = ET.SubElement(invoice, "cac:TaxTotal")
        cbc_TaxAmount = ET.SubElement(cac_TaxTotal, "cbc:TaxAmount", {"currencyID":"COP"})
        cbc_TaxAmount.text = "0.00"
        cac_TaxSubtotal = ET.SubElement(cac_TaxTotal, "cac:TaxSubtotal")
        cbc_TaxableAmount = ET.SubElement(cac_TaxSubtotal, "cbc:TaxableAmount", {"currencyID":"COP"})
        cbc_TaxableAmount.text = "0.00"
        cbc_TaxAmount = ET.SubElement(cac_TaxSubtotal, "cbc:TaxAmount", {"currencyID":"COP"})
        cbc_TaxAmount.text = "0.00"
        cac_TaxCategory = ET.SubElement(cac_TaxSubtotal, "cac:TaxCategory")
        cbc_Percent = ET.SubElement(cac_TaxCategory, "cbc:Percent")
        cbc_Percent.text = "0.00"
        cac_TaxScheme = ET.SubElement(cac_TaxCategory, "cac:TaxScheme")
        cbc_ID = ET.SubElement(cac_TaxScheme, "cbc:ID")
        cbc_ID.text = "03"
        cbc_Name = ET.SubElement(cac_TaxScheme, "cbc:Name")
        cbc_Name.text = "ICA"

        cac_TaxTotal = ET.SubElement(invoice, "cac:TaxTotal")
        cbc_TaxAmount = ET.SubElement(cac_TaxTotal, "cbc:TaxAmount", {"currencyID":"COP"})
        cbc_TaxAmount.text = "0.00"
        cac_TaxSubtotal = ET.SubElement(cac_TaxTotal, "cac:TaxSubtotal")
        cbc_TaxableAmount = ET.SubElement(cac_TaxSubtotal, "cbc:TaxableAmount", {"currencyID":"COP"})
        cbc_TaxableAmount.text = "0.00"
        cbc_TaxAmount = ET.SubElement(cac_TaxSubtotal, "cbc:TaxAmount", {"currencyID":"COP"})
        cbc_TaxAmount.text = "0.00"
        cac_TaxCategory = ET.SubElement(cac_TaxSubtotal, "cac:TaxCategory")
        cbc_Percent = ET.SubElement(cac_TaxCategory, "cbc:Percent")
        cbc_Percent.text = "0.00"
        cac_TaxScheme = ET.SubElement(cac_TaxCategory, "cac:TaxScheme")
        cbc_ID = ET.SubElement(cac_TaxScheme, "cbc:ID")
        cbc_ID.text = "04"
        cbc_Name = ET.SubElement(cac_TaxScheme, "cbc:Name")
        cbc_Name.text = "INC"

        cac_LegalMonetaryTotal = ET.SubElement(invoice, "cac:LegalMonetaryTotal")
        cbc_LineExtensionAmount = ET.SubElement(cac_LegalMonetaryTotal, "cbc:LineExtensionAmount", {"currencyID":"COP"})
        cbc_LineExtensionAmount.text = "12600.06"
        cbc_TaxExclusiveAmount = ET.SubElement(cac_LegalMonetaryTotal, "cbc:TaxExclusiveAmount", {"currencyID":"COP"})
        cbc_TaxExclusiveAmount.text = "12787.56"
        cbc_TaxInclusiveAmount = ET.SubElement(cac_LegalMonetaryTotal, "cbc:TaxInclusiveAmount", {"currencyID":"COP"})
        cbc_TaxInclusiveAmount.text = "15024.07"
        cbc_PrepaidAmount = ET.SubElement(cac_LegalMonetaryTotal, "cbc:PrepaidAmount", {"currencyID":"COP"})
        cbc_PrepaidAmount.text = "1000.00"
        cbc_PayableAmount = ET.SubElement(cac_LegalMonetaryTotal, "cbc:PayableAmount", {"currencyID":"COP"})
        cbc_PayableAmount.text = "14024.07"

        cac_InvoiceLine = ET.SubElement(invoice, "cac:InvoiceLine")
        cbc_ID = ET.SubElement(cac_InvoiceLine, "cbc:ID")
        cbc_ID.text = "1"
        cbc_InvoicedQuantity = ET.SubElement(cac_InvoiceLine, "cbc:InvoicedQuantity", {"unitCode":"EA"})
        cbc_InvoicedQuantity.text = "1.000000"
        cbc_LineExtensionAmount = ET.SubElement(cac_InvoiceLine, "cbc:LineExtensionAmount", {"currencyID":"COP"})
        cbc_LineExtensionAmount.text = "12600.06"
        cbc_FreeOfChargeIndicator = ET.SubElement(cac_InvoiceLine, "cbc:FreeOfChargeIndicator")
        cbc_FreeOfChargeIndicator.text = "false"
        cac_Delivery = ET.SubElement(cac_InvoiceLine, "cac:Delivery")
        cac_DeliveryLocation = ET.SubElement(cac_Delivery, "cac:DeliveryLocation")
        cbc_ID = ET.SubElement(cac_DeliveryLocation, "cbc:ID", {"schemeID":"999", "schemeName":"EAN"})
        cbc_ID.text = "613124312412"
        cac_AllowanceCharge = ET.SubElement(cac_InvoiceLine, "cac:AllowanceCharge")
        cbc_ID = ET.SubElement(cac_AllowanceCharge, "cbc:ID")
        cbc_ID.text = "1"
        cbc_ChargeIndicator = ET.SubElement(cac_AllowanceCharge, "cbc:ChargeIndicator")
        cbc_ChargeIndicator.text = "false"
        cbc_AllowanceChargeReason = ET.SubElement(cac_AllowanceCharge, "cbc:AllowanceChargeReason")
        cbc_AllowanceChargeReason.text = "Descuento por cliente frecuente"
        cbc_MultiplierFactorNumeric = ET.SubElement(cac_AllowanceCharge, "cbc:MultiplierFactorNumeric")
        cbc_MultiplierFactorNumeric.text = "33.33"
        cbc_Amount = ET.SubElement(cac_AllowanceCharge, "cbc:Amount", {"currencyID":"COP"})
        cbc_Amount.text = "6299.94"
        cbc_BaseAmount = ET.SubElement(cac_AllowanceCharge, "cbc:BaseAmount", {"currencyID":"COP"})
        cbc_BaseAmount.text = "18900.00"
        cac_TaxTotal = ET.SubElement(cac_InvoiceLine, "cac:TaxTotal")
        cbc_TaxAmount = ET.SubElement(cac_TaxTotal, "cbc:TaxAmount", {"currencyID":"COP"})
        cbc_TaxAmount.text = "2394.01"
        cac_TaxSubtotal = ET.SubElement(cac_TaxTotal, "cac:TaxSubtotal")
        cbc_TaxableAmount = ET.SubElement(cac_TaxSubtotal, "cbc:TaxableAmount", {"currencyID":"COP"})
        cbc_TaxableAmount.text = "12600.06"
        cbc_TaxAmount = ET.SubElement(cac_TaxSubtotal, "cbc:TaxAmount", {"currencyID":"COP"})
        cbc_TaxAmount.text = "2394.01"
        cac_TaxCategory = ET.SubElement(cac_TaxSubtotal, "cac:TaxCategory")
        cbc_Percent = ET.SubElement(cac_TaxCategory, "cbc:Percent")
        cbc_Percent.text = "19.00"
        cac_TaxScheme = ET.SubElement(cac_TaxCategory, "cac:TaxScheme")
        cbc_ID = ET.SubElement(cac_TaxScheme, "cbc:ID")
        cbc_ID.text = "01"
        cbc_Name = ET.SubElement(cac_TaxScheme, "cbc:Name")
        cbc_Name.text = "IVA"
        cac_Item = ET.SubElement(cac_InvoiceLine, "cac:Item")
        cbc_Description = ET.SubElement(cac_Item, "cbc:Description")
        cbc_Description.text = "AV OASYS -2.25 (8.4) LENTE DE CONTATO"
        cac_SellersItemIdentification = ET.SubElement(cac_Item, "cac:SellersItemIdentification")
        cbc_ID = ET.SubElement(cac_SellersItemIdentification, "cbc:ID")
        cbc_ID.text = "AOHV84-225"
        cac_AdditionalItemIdentification = ET.SubElement(cac_Item, "cac:AdditionalItemIdentification")
        cbc_ID = ET.SubElement(cac_AdditionalItemIdentification, "cbc:ID", {"schemeID":"999", "schemeName":"EAN13"})
        cbc_ID.text = "6543542313534"
        cac_Price = ET.SubElement(cac_InvoiceLine, "cac:Price")
        cbc_PriceAmount = ET.SubElement(cac_Price, "cbc:PriceAmount", {"currencyID":"COP"})
        cbc_PriceAmount.text = "18900.00"
        cbc_BaseQuantity = ET.SubElement(cac_Price, "cbc:BaseQuantity", {"unitCode":"EA"})
        cbc_BaseQuantity.text = "1.000000"

        cac_InvoiceLine = ET.SubElement(invoice, "cac:InvoiceLine")
        cbc_ID = ET.SubElement(cac_InvoiceLine, "cbc:ID")
        cbc_ID.text = "2"
        cbc_InvoicedQuantity = ET.SubElement(cac_InvoiceLine, "cbc:InvoicedQuantity", {"unitCode":"NIU"})
        cbc_InvoicedQuantity.text = "1.000000"
        cbc_LineExtensionAmount = ET.SubElement(cac_InvoiceLine, "cbc:LineExtensionAmount", {"currencyID":"COP"})
        cbc_LineExtensionAmount.text = "0.00"
        cbc_FreeOfChargeIndicator = ET.SubElement(cac_InvoiceLine, "cbc:FreeOfChargeIndicator")
        cbc_FreeOfChargeIndicator.text = "true"
        cac_DocumentReference = ET.SubElement(cac_InvoiceLine, "cac:DocumentReference")
        cbc_ID = ET.SubElement(cac_DocumentReference, "cbc:ID")
        cbc_ID.text = "TST1543623"
        cbc_IssueDate = ET.SubElement(cac_DocumentReference, "cbc:IssueDate")
        cbc_IssueDate.text = "2019-03-02"
        cbc_DocumentTypeCode = ET.SubElement(cac_DocumentReference, "cbc:DocumentTypeCode")
        cbc_DocumentTypeCode.text = "1001-A"
        cbc_DocumentType = ET.SubElement(cac_DocumentReference, "cbc:DocumentType")
        cbc_DocumentType.text = "Bienes Propios"
        cac_DocumentReference = ET.SubElement(cac_InvoiceLine, "cac:DocumentReference")
        cbc_ID = ET.SubElement(cac_DocumentReference, "cbc:ID")
        cbc_ID.text = "GR8713461"
        cbc_IssueDate = ET.SubElement(cac_DocumentReference, "cbc:IssueDate")
        cbc_IssueDate.text = "2019-03-02"
        cbc_DocumentTypeCode = ET.SubElement(cac_DocumentReference, "cbc:DocumentTypeCode")
        cbc_DocumentTypeCode.text = "AR"
        cac_PricingReference = ET.SubElement(cac_InvoiceLine, "cac:PricingReference")
        cac_AlternativeConditionPrice = ET.SubElement(cac_PricingReference, "cac:AlternativeConditionPrice")
        cbc_PriceAmount = ET.SubElement(cac_AlternativeConditionPrice, "cbc:PriceAmount", {"currencyID":"COP"})
        cbc_PriceAmount.text = "100.00"
        cbc_PriceTypeCode = ET.SubElement(cac_AlternativeConditionPrice, "cbc:PriceTypeCode")
        cbc_PriceTypeCode.text = "03"
        cbc_PriceType = ET.SubElement(cac_AlternativeConditionPrice, "cbc:PriceType")
        cbc_PriceType.text = "Otro valor"

        cac_Delivery = ET.SubElement(cac_InvoiceLine, "cac:Delivery")
        cac_DeliveryLocation = ET.SubElement(cac_Delivery, "cac:DeliveryLocation")
        cbc_ID = ET.SubElement(cac_DeliveryLocation, "cbc:ID", {"schemeID":"999", "schemeName":"EAN"})
        cbc_ID.text = "613124312412"
        cac_TaxTotal = ET.SubElement(cac_InvoiceLine, "cac:TaxTotal")
        cbc_TaxAmount = ET.SubElement(cac_TaxTotal, "cbc:TaxAmount", {"currencyID":"COP"})
        cbc_TaxAmount.text = "30.00"
        cac_TaxSubtotal = ET.SubElement(cac_TaxTotal, "cac:TaxSubtotal")
        cbc_TaxableAmount = ET.SubElement(cac_TaxSubtotal, "cbc:TaxableAmount", {"currencyID":"COP"})
        cbc_TaxableAmount.text = "187.50"
        cbc_TaxAmount = ET.SubElement(cac_TaxSubtotal, "cbc:TaxAmount", {"currencyID":"COP"})
        cbc_TaxAmount.text = "30.00"
        cac_TaxCategory = ET.SubElement(cac_TaxSubtotal, "cac:TaxCategory")
        cbc_Percent = ET.SubElement(cac_TaxCategory, "cbc:Percent")
        cbc_Percent.text = "16.00"
        cac_TaxScheme = ET.SubElement(cac_TaxCategory, "cac:TaxScheme")
        cbc_ID = ET.SubElement(cac_TaxScheme, "cbc:ID")
        cbc_ID.text = "01"
        cbc_Name = ET.SubElement(cac_TaxScheme, "cbc:Name")
        cbc_Name.text = "IVA"
        cac_Item = ET.SubElement(cac_InvoiceLine, "cac:Item")
        cbc_Description = ET.SubElement(cac_Item, "cbc:Description")
        cbc_Description.text = "Bolsa"
        cac_SellersItemIdentification = ET.SubElement(cac_Item, "cac:SellersItemIdentification")
        cbc_ID = ET.SubElement(cac_SellersItemIdentification, "cbc:ID")
        cbc_ID.text = "91412012412"        
        cac_StandardItemIdentification = ET.SubElement(cac_Item, "cac:StandardItemIdentification")
        cbc_ID = ET.SubElement(cac_StandardItemIdentification, "cbc:ID", {"schemeAgencyID":"10", "schemeID":"001", "schemeName":"UNSPSC"})
        cbc_ID.text = "18937100-7"
        cac_Price = ET.SubElement(cac_InvoiceLine, "cac:Price")
        cbc_PriceAmount = ET.SubElement(cac_Price, "cbc:PriceAmount", {"currencyID":"COP"})
        cbc_PriceAmount.text = "0.00"
        cbc_BaseQuantity = ET.SubElement(cac_Price, "cbc:BaseQuantity", {"unitCode":"NIU"})
        cbc_BaseQuantity.text = "1.000000"

        xml_tree = ET.ElementTree(invoice)
        declaration = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
        xml_content = declaration + ET.tostring(invoice, encoding='utf-8').decode('utf-8')
        #response = HttpResponse(xml_content, content_type="application/xml")
        return xml_content
        #return Response({"documento:": "hola"}, status=status.HTTP_200_OK)
