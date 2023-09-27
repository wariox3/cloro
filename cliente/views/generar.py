from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from pymongo import MongoClient
from decouple import config
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import xml.etree.ElementTree as ET
from django.http import HttpResponse
import json
import datetime



class GenerarView(APIView):
    def post(self, request):  
        raw = request.data        
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
        sts_QRCode.text = "NroFactura=SETP990000002 NitFacturador=800197268 NitAdquiriente=900108281 FechaFactura=2019-06-20 ValorTotalFactura=14024.07 CUFE=941cf36af62dbbc06f105d2a80e9bfe683a90e84960eae4d351cc3afbe8f848c26c39bac4fbc80fa254824c6369ea694 URL=https://catalogo-vpfe-hab.dian.gov.co/Document/FindDocument?documentKey=941cf36af62dbbc06f105d2a80e9bfe683a90e84960eae4d351cc3afbe8f848c26c39bac4fbc80fa254824c6369ea694&partitionKey=co|06|94&emissionDate=20190620"
        
        ext_UBLExtension = ET.SubElement(ext_UBLExtensions, 'ext:UBLExtension')
        ext_ExtensionContent = ET.SubElement(ext_UBLExtension, 'ext:ExtensionContent')
        ds_Signature = ET.SubElement(ext_ExtensionContent, 'ds:Signature', {"Id":"xmldsig-d0322c4f-be87-495a-95d5-9244980495f4"})
        
        ds_SignedInfo = ET.SubElement(ds_Signature, 'ds:SignedInfo')
        ds_CanonicalizationMethod = ET.SubElement(ds_SignedInfo, 'ds:CanonicalizationMethod', {"Algorithm":"http://www.w3.org/TR/2001/REC-xml-c14n-20010315"})
        ds_SignatureMethod = ET.SubElement(ds_SignedInfo, 'ds:SignatureMethod', {"Algorithm":"http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"})
        ds_Reference = ET.SubElement(ds_SignedInfo, 'ds:Reference', {"id":"xmldsig-d0322c4f-be87-495a-95d5-9244980495f4-ref0", "URI":""})
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
        ds_SignatureValue.text = "q4HWeb47oLdDM4D3YiYDOSXE4YfSHkQKxUfSYiEiPuP2XWvD7ELZTC4ENFv6krgDAXczmi0W7OMi LIVvuFz0ohPUc4KNlUEzqSBHVi6sC34sCqoxuRzOmMEoCB9Tr4VICxU1Ue9XhgP7o6X4f8KFAQWW NaeTtA6WaO/yUtq91MKP59aAnFMfYl8lXpaS0kpUwuui3wdCZsGycsl1prEWiwzpaukEUOXyTo7o RBOuNsDIUhP24Fv1alRFnX6/9zEOpRTs4rEQKN3IQnibF757LE/nnkutElZHTXaSV637gpHjXoUN 5JrUwTNOXvmFS98N6DczCQfeNuDIozYwtFVlMw=="
        
        ds_KeyInfo = ET.SubElement(ds_Signature, 'ds:KeyInfo', {"Id":"xmldsig-87d128b5-aa31-4f0b-8e45-3d9cfa0eec26-keyinfo"})
        ds_X509Data = ET.SubElement(ds_KeyInfo, 'ds:X509Data')
        ds_X509Certificate = ET.SubElement(ds_X509Data, 'ds:X509Certificate')
        ds_X509Certificate.text = "MIIIODCCBiCgAwIBAgIIbAsHYmJtoOIwDQYJKoZIhvcNAQELBQAwgbQxIzAhBgkqhkiG9w0BCQEW FGluZm9AYW5kZXNzY2QuY29tLmNvMSMwIQYDVQQDExpDQSBBTkRFUyBTQ0QgUy5BLiBDbGFzZSBJ STEwMC4GA1UECxMnRGl2aXNpb24gZGUgY2VydGlmaWNhY2lvbiBlbnRpZGFkIGZpbmFsMRMwEQYD VQQKEwpBbmRlcyBTQ0QuMRQwEgYDVQQHEwtCb2dvdGEgRC5DLjELMAkGA1UEBhMCQ08wHhcNMTcw OTE2MTM0ODE5WhcNMjAwOTE1MTM0ODE5WjCCARQxHTAbBgNVBAkTFENhbGxlIEZhbHNhIE5vIDEy IDM0MTgwNgYJKoZIhvcNAQkBFilwZXJzb25hX2p1cmlkaWNhX3BydWViYXMxQGFuZGVzc2NkLmNv bS5jbzEsMCoGA1UEAxMjVXN1YXJpbyBkZSBQcnVlYmFzIFBlcnNvbmEgSnVyaWRpY2ExETAPBgNV BAUTCDExMTExMTExMRkwFwYDVQQMExBQZXJzb25hIEp1cmlkaWNhMSgwJgYDVQQLEx9DZXJ0aWZp Y2FkbyBkZSBQZXJzb25hIEp1cmlkaWNhMQ8wDQYDVQQHEwZCb2dvdGExFTATBgNVBAgTDEN1bmRp bmFtYXJjYTELMAkGA1UEBhMCQ08wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC0Dn8t oZ2CXun+63zwYecJ7vNmEmS+YouH985xDek7ImeE9lMBHXE1M5KDo7iT/tUrcFwKj717PeVL52Nt B6WU4+KBt+nrK+R+OSTpTno5EvpzfIoS9pLI74hHc017rY0wqjl0lw+8m7fyLfi/JO7AtX/dthS+ MKHIcZ1STPlkcHqmbQO6nhhr/CGl+tKkCMrgfEFIm1kv3bdWqk3qHrnFJ6s2GoVNZVCTZW/mOzPC NnnUW12LDd/Kd+MjN6aWbP0D/IJbB42Npqv8+/oIwgCrbt0sS1bysUgdT4im9bBhb00MWVmNRBBe 3pH5knzkBid0T7TZsPCyiMBstiLT3yfpAgMBAAGjggLpMIIC5TAMBgNVHRMBAf8EAjAAMB8GA1Ud IwQYMBaAFKhLtPQLp7Zb1KAohRCdBBMzxKf3MDcGCCsGAQUFBwEBBCswKTAnBggrBgEFBQcwAYYb aHR0cDovL29jc3AuYW5kZXNzY2QuY29tLmNvMIIB4wYDVR0gBIIB2jCCAdYwggHSBg0rBgEEAYH0 SAECCQIFMIIBvzBBBggrBgEFBQcCARY1aHR0cDovL3d3dy5hbmRlc3NjZC5jb20uY28vZG9jcy9E UENfQW5kZXNTQ0RfVjIuNS5wZGYwggF4BggrBgEFBQcCAjCCAWoeggFmAEwAYQAgAHUAdABpAGwA aQB6AGEAYwBpAPMAbgAgAGQAZQAgAGUAcwB0AGUAIABjAGUAcgB0AGkAZgBpAGMAYQBkAG8AIABl AHMAdADhACAAcwB1AGoAZQB0AGEAIABhACAAbABhAHMAIABQAG8AbADtAHQAaQBjAGEAcwAgAGQA ZQAgAEMAZQByAHQAaQBmAGkAYwBhAGQAbwAgAGQAZQAgAFAAZQByAHMAbwBuAGEAIABKAHUAcgDt AGQAaQBjAGEAIAAoAFAAQwApACAAeQAgAEQAZQBjAGwAYQByAGEAYwBpAPMAbgAgAGQAZQAgAFAA cgDhAGMAdABpAGMAYQBzACAAZABlACAAQwBlAHIAdABpAGYAaQBjAGEAYwBpAPMAbgAgACgARABQ AEMAKQAgAGUAcwB0AGEAYgBsAGUAYwBpAGQAYQBzACAAcABvAHIAIABBAG4AZABlAHMAIABTAEMA RDAdBgNVHSUEFjAUBggrBgEFBQcDAgYIKwYBBQUHAwQwRgYDVR0fBD8wPTA7oDmgN4Y1aHR0cDov L3d3dy5hbmRlc3NjZC5jb20uY28vaW5jbHVkZXMvZ2V0Q2VydC5waHA/Y3JsPTEwHQYDVR0OBBYE FL9BXJHmFVE5c5Ai8B1bVBWqXsj7MA4GA1UdDwEB/wQEAwIE8DANBgkqhkiG9w0BAQsFAAOCAgEA b/pa7yerHOu1futRt8QTUVcxCAtK9Q00u7p4a5hp2fVzVrhVQIT7Ey0kcpMbZVPgU9X2mTHGfPdb R0hYJGEKAxiRKsmAwmtSQgWh5smEwFxG0TD1chmeq6y0GcY0lkNA1DpHRhSK368vZlO1p2a6S13Y 1j3tLFLqf5TLHzRgl15cfauVinEHGKU/cMkjLwxNyG1KG/FhCeCCmawATXWLgQn4PGgvKcNrz+y0 cwldDXLGKqriw9dce2Zerc7OCG4/XGjJ2PyZOJK9j1VYIG4pnmoirVmZbKwWaP4/TzLs6LKaJ4b6 6xLxH3hUtoXCzYQ5ehYyrLVwCwTmKcm4alrEht3FVWiWXA/2tj4HZiFoG+I1OHKmgkNv7SwHS7z9 tFEFRaD3W3aD7vwHEVsq2jTeYInE0+7r2/xYFZ9biLBrryl+q22zM5W/EJq6EJPQ6SM/eLqkpzqM EF5OdcJ5kIOxLbrIdOh0+grU2IrmHXr7cWNP6MScSL7KSxhjPJ20F6eqkO1Z/LAxqNslBIKkYS24 VxPbXu0pBXQvu+zAwD4SvQntIG45y/67h884I/tzYOEJi7f6/NFAEuV+lokw/1MoVsEgFESASI9s N0DfUniabyrZ3nX+LG3UFL1VDtDPWrLTNKtb4wkKwGVwqtAdGFcE+/r/1WG0eQ64xCq0NLutCxg="
        
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
        cbc_EndDate = ET.SubElement(cac_InvoicePeriod, "cbc:EndDate")
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
        cac_PartyLegalEntity = ET.SubElement(cac_Party, "cac:PartyLegalEntity")
        cac_Contact = ET.SubElement(cac_Party, "cac:Contact")


        cac_AccountingCustomerParty = ET.SubElement(invoice, "cac:AccountingCustomerParty")
        cac_TaxRepresentativeParty = ET.SubElement(invoice, "cac:TaxRepresentativeParty")
        cac_Delivery = ET.SubElement(invoice, "cac:Delivery")
        cac_DeliveryTerms = ET.SubElement(invoice, "cac:DeliveryTerms")
        cac_PaymentMeans = ET.SubElement(invoice, "cac:PaymentMeans")
        cac_PrepaidPayment = ET.SubElement(invoice, "cac:PrepaidPayment")
        cac_TaxTotal = ET.SubElement(invoice, "cac:TaxTotal")
        cac_TaxTotal = ET.SubElement(invoice, "cac:TaxTotal")
        cac_TaxTotal = ET.SubElement(invoice, "cac:TaxTotal")
        cac_LegalMonetaryTotal = ET.SubElement(invoice, "cac:LegalMonetaryTotal")
        cac_InvoiceLine = ET.SubElement(invoice, "cac:InvoiceLine")
        cac_InvoiceLine = ET.SubElement(invoice, "cac:InvoiceLine")

        xml_tree = ET.ElementTree(invoice)
        declaration = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
        xml_content = declaration + ET.tostring(invoice, encoding='utf-8').decode('utf-8')
        response = HttpResponse(xml_content, content_type="application/xml")
        return response
        #return Response({"documento:": "hola"}, status=status.HTTP_200_OK)                
