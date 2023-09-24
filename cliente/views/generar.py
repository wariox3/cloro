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
        ext_UBLExtensions.text = "12345"
        invoice.append(ext_UBLExtensions)

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
