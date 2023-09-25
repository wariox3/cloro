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
        
        ext_UBLExtensions = ET.Element("ext:UBLExtensions")
        invoice.append(ext_UBLExtensions)

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
        ds_SignatureValue = ET.SubElement(ds_SignedInfo, 'ds:SignatureValue', {"Id":"xmldsig-d0322c4f-be87-495a-95d5-9244980495f4-sigvalue"})
        ds_SignatureValue.text = "q4HWeb47oLdDM4D3YiYDOSXE4YfSHkQKxUfSYiEiPuP2XWvD7ELZTC4ENFv6krgDAXczmi0W7OMi LIVvuFz0ohPUc4KNlUEzqSBHVi6sC34sCqoxuRzOmMEoCB9Tr4VICxU1Ue9XhgP7o6X4f8KFAQWW NaeTtA6WaO/yUtq91MKP59aAnFMfYl8lXpaS0kpUwuui3wdCZsGycsl1prEWiwzpaukEUOXyTo7o RBOuNsDIUhP24Fv1alRFnX6/9zEOpRTs4rEQKN3IQnibF757LE/nnkutElZHTXaSV637gpHjXoUN 5JrUwTNOXvmFS98N6DczCQfeNuDIozYwtFVlMw=="
        ds_KeyInfo = ET.SubElement(ds_SignedInfo, 'ds:KeyInfo', {"Id":"xmldsig-87d128b5-aa31-4f0b-8e45-3d9cfa0eec26-keyinfo"})
        ds_X509Data = ET.SubElement(ds_KeyInfo, 'ds:X509Data')
        ds_X509Certificate = ET.SubElement(ds_X509Data, 'ds:X509Certificate')
        ds_X509Certificate.text = "MIIIODCCBiCgAwIBAgIIbAsHYmJtoOIwDQYJKoZIhvcNAQELBQAwgbQxIzAhBgkqhkiG9w0BCQEW FGluZm9AYW5kZXNzY2QuY29tLmNvMSMwIQYDVQQDExpDQSBBTkRFUyBTQ0QgUy5BLiBDbGFzZSBJ STEwMC4GA1UECxMnRGl2aXNpb24gZGUgY2VydGlmaWNhY2lvbiBlbnRpZGFkIGZpbmFsMRMwEQYD VQQKEwpBbmRlcyBTQ0QuMRQwEgYDVQQHEwtCb2dvdGEgRC5DLjELMAkGA1UEBhMCQ08wHhcNMTcw OTE2MTM0ODE5WhcNMjAwOTE1MTM0ODE5WjCCARQxHTAbBgNVBAkTFENhbGxlIEZhbHNhIE5vIDEy IDM0MTgwNgYJKoZIhvcNAQkBFilwZXJzb25hX2p1cmlkaWNhX3BydWViYXMxQGFuZGVzc2NkLmNv bS5jbzEsMCoGA1UEAxMjVXN1YXJpbyBkZSBQcnVlYmFzIFBlcnNvbmEgSnVyaWRpY2ExETAPBgNV BAUTCDExMTExMTExMRkwFwYDVQQMExBQZXJzb25hIEp1cmlkaWNhMSgwJgYDVQQLEx9DZXJ0aWZp Y2FkbyBkZSBQZXJzb25hIEp1cmlkaWNhMQ8wDQYDVQQHEwZCb2dvdGExFTATBgNVBAgTDEN1bmRp bmFtYXJjYTELMAkGA1UEBhMCQ08wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC0Dn8t oZ2CXun+63zwYecJ7vNmEmS+YouH985xDek7ImeE9lMBHXE1M5KDo7iT/tUrcFwKj717PeVL52Nt B6WU4+KBt+nrK+R+OSTpTno5EvpzfIoS9pLI74hHc017rY0wqjl0lw+8m7fyLfi/JO7AtX/dthS+ MKHIcZ1STPlkcHqmbQO6nhhr/CGl+tKkCMrgfEFIm1kv3bdWqk3qHrnFJ6s2GoVNZVCTZW/mOzPC NnnUW12LDd/Kd+MjN6aWbP0D/IJbB42Npqv8+/oIwgCrbt0sS1bysUgdT4im9bBhb00MWVmNRBBe 3pH5knzkBid0T7TZsPCyiMBstiLT3yfpAgMBAAGjggLpMIIC5TAMBgNVHRMBAf8EAjAAMB8GA1Ud IwQYMBaAFKhLtPQLp7Zb1KAohRCdBBMzxKf3MDcGCCsGAQUFBwEBBCswKTAnBggrBgEFBQcwAYYb aHR0cDovL29jc3AuYW5kZXNzY2QuY29tLmNvMIIB4wYDVR0gBIIB2jCCAdYwggHSBg0rBgEEAYH0 SAECCQIFMIIBvzBBBggrBgEFBQcCARY1aHR0cDovL3d3dy5hbmRlc3NjZC5jb20uY28vZG9jcy9E UENfQW5kZXNTQ0RfVjIuNS5wZGYwggF4BggrBgEFBQcCAjCCAWoeggFmAEwAYQAgAHUAdABpAGwA aQB6AGEAYwBpAPMAbgAgAGQAZQAgAGUAcwB0AGUAIABjAGUAcgB0AGkAZgBpAGMAYQBkAG8AIABl AHMAdADhACAAcwB1AGoAZQB0AGEAIABhACAAbABhAHMAIABQAG8AbADtAHQAaQBjAGEAcwAgAGQA ZQAgAEMAZQByAHQAaQBmAGkAYwBhAGQAbwAgAGQAZQAgAFAAZQByAHMAbwBuAGEAIABKAHUAcgDt AGQAaQBjAGEAIAAoAFAAQwApACAAeQAgAEQAZQBjAGwAYQByAGEAYwBpAPMAbgAgAGQAZQAgAFAA cgDhAGMAdABpAGMAYQBzACAAZABlACAAQwBlAHIAdABpAGYAaQBjAGEAYwBpAPMAbgAgACgARABQ AEMAKQAgAGUAcwB0AGEAYgBsAGUAYwBpAGQAYQBzACAAcABvAHIAIABBAG4AZABlAHMAIABTAEMA RDAdBgNVHSUEFjAUBggrBgEFBQcDAgYIKwYBBQUHAwQwRgYDVR0fBD8wPTA7oDmgN4Y1aHR0cDov L3d3dy5hbmRlc3NjZC5jb20uY28vaW5jbHVkZXMvZ2V0Q2VydC5waHA/Y3JsPTEwHQYDVR0OBBYE FL9BXJHmFVE5c5Ai8B1bVBWqXsj7MA4GA1UdDwEB/wQEAwIE8DANBgkqhkiG9w0BAQsFAAOCAgEA b/pa7yerHOu1futRt8QTUVcxCAtK9Q00u7p4a5hp2fVzVrhVQIT7Ey0kcpMbZVPgU9X2mTHGfPdb R0hYJGEKAxiRKsmAwmtSQgWh5smEwFxG0TD1chmeq6y0GcY0lkNA1DpHRhSK368vZlO1p2a6S13Y 1j3tLFLqf5TLHzRgl15cfauVinEHGKU/cMkjLwxNyG1KG/FhCeCCmawATXWLgQn4PGgvKcNrz+y0 cwldDXLGKqriw9dce2Zerc7OCG4/XGjJ2PyZOJK9j1VYIG4pnmoirVmZbKwWaP4/TzLs6LKaJ4b6 6xLxH3hUtoXCzYQ5ehYyrLVwCwTmKcm4alrEht3FVWiWXA/2tj4HZiFoG+I1OHKmgkNv7SwHS7z9 tFEFRaD3W3aD7vwHEVsq2jTeYInE0+7r2/xYFZ9biLBrryl+q22zM5W/EJq6EJPQ6SM/eLqkpzqM EF5OdcJ5kIOxLbrIdOh0+grU2IrmHXr7cWNP6MScSL7KSxhjPJ20F6eqkO1Z/LAxqNslBIKkYS24 VxPbXu0pBXQvu+zAwD4SvQntIG45y/67h884I/tzYOEJi7f6/NFAEuV+lokw/1MoVsEgFESASI9s N0DfUniabyrZ3nX+LG3UFL1VDtDPWrLTNKtb4wkKwGVwqtAdGFcE+/r/1WG0eQ64xCq0NLutCxg="
        ds_Object = ET.SubElement(ds_SignedInfo, 'ds:Object')
        xades_QualifyingProperties = ET.SubElement(ds_Object, 'xades:QualifyingProperties', {"Target":"#xmldsig-d0322c4f-be87-495a-95d5-9244980495f4"})
        xades_SignedProperties = ET.SubElement(xades_QualifyingProperties, 'xades:SignedProperties', {"Id":"xmldsig-d0322c4f-be87-495a-95d5-9244980495f4-signedprops"})
        xades_SignedSignatureProperties = ET.SubElement(xades_SignedProperties, 'xades:SignedSignatureProperties')
        xades_SigningTime = ET.SubElement(xades_SignedSignatureProperties, 'xades:SigningTime')
        xades_SigningTime.text = "2019-06-21T19:09:35.993-05:00"
        xades_SigningCertificate = ET.SubElement(xades_SignedSignatureProperties, 'xades:SigningCertificate')
        xades_Cert = ET.SubElement(xades_SigningCertificate, 'xades:Cert')



        cbc_UBLVersionID = ET.Element("cbc:UBLVersionID")
        cbc_UBLVersionID.text = "UBL 2.1"
        invoice.append(cbc_UBLVersionID)

        cbc_CustomizationID = ET.Element("cbc:CustomizationID")
        cbc_CustomizationID.text = "05"
        invoice.append(cbc_CustomizationID)

        cbc_ProfileID = ET.Element("cbc:ProfileID")
        cbc_ProfileID.text = "DIAN 2.1"
        invoice.append(cbc_ProfileID)
        
        cbc_ProfileExecutionID = ET.Element("cbc:ProfileExecutionID")
        cbc_ProfileExecutionID.text = "2"
        invoice.append(cbc_ProfileExecutionID)

        cbc_ID = ET.Element("cbc:ID")
        cbc_ID.text = "SETP990000002"
        invoice.append(cbc_ID)

        cbc_UUID = ET.Element("cbc:UUID")
        cbc_UUID.text = "941cf36af62dbbc06f105d2a80e9bfe683a90e84960eae4d351cc3afbe8f848c26c39bac4fbc80fa254824c6369ea694"
        cbc_UUID.set("schemeID","2")
        cbc_UUID.set("schemeName","CUFE-SHA384")
        invoice.append(cbc_UUID)           

        cbc_IssueDate = ET.Element("cbc:IssueDate")
        cbc_IssueDate.text = "2019-06-20"
        invoice.append(cbc_IssueDate)

        cbc_IssueTime = ET.Element("cbc:IssueTime")
        cbc_IssueTime.text = "09:15:23-05:00"
        invoice.append(cbc_IssueTime)

        cbc_InvoiceTypeCode = ET.Element("cbc:InvoiceTypeCode")
        cbc_InvoiceTypeCode.text = "01"
        invoice.append(cbc_InvoiceTypeCode)

        cbc_Note = ET.Element("cbc:Note")
        cbc_Note.text = "SETP9900000022019-06-2009:15:23-05:0012600.06012424.01040.00030.0014024.07900508908900108281fc8eac422eba16e22ffd8c6f94b3f40a6e38162c2"
        invoice.append(cbc_Note)

        cbc_DocumentCurrencyCode = ET.Element("cbc:DocumentCurrencyCode")
        cbc_DocumentCurrencyCode.text = "COP"
        cbc_DocumentCurrencyCode.set("listAgencyID","6")
        cbc_DocumentCurrencyCode.set("listAgencyName","United Nations Economic Commission for Europe")
        cbc_DocumentCurrencyCode.set("listID","ISO 4217 Alpha")
        invoice.append(cbc_DocumentCurrencyCode)

        cbc_LineCountNumeric = ET.Element("cbc:LineCountNumeric")
        cbc_IssueTime.text = "2"
        invoice.append(cbc_LineCountNumeric)

        xml_tree = ET.ElementTree(invoice)
        declaration = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
        xml_content = declaration + ET.tostring(invoice, encoding='utf-8').decode('utf-8')
        response = HttpResponse(xml_content, content_type="application/xml")
        return response
        #return Response({"documento:": "hola"}, status=status.HTTP_200_OK)                
