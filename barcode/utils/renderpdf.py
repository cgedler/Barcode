"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author:     Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date:    23.01.2020
--  Description:    utils.py
--
--  module file that using to make PDF
======================================================================================
"""
# Imports
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  
#
#  name: function render_to_pdf
#
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    #This part will create the pdf.
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding='UTF-8')
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
#
#  name: function PdfResponseMixin
#
class PdfResponseMixin(object, ):
    def write_pdf(self, file_object, ):
        context = self.get_context_data()
        template = self.get_template_names()[0]
        generate_pdf(template, file_object=file_object, context=context)
    def render_to_response(self, context, **response_kwargs):
        resp = HttpResponse(content_type='application/pdf')
        self.write_pdf(resp)
        return resp
#
#  name: function CoverPdfResponseMixin
#
class CoverPdfResponseMixin(PdfResponseMixin, ):
    cover_pdf = None
    def render_to_response(self, context, **response_kwargs):
        merger = PdfFileMerger()
        merger.append(open(self.cover_pdf, "rb"))
        pdf_fo = StringIO.StringIO()
        self.write_pdf(pdf_fo)
        merger.append(pdf_fo)
        resp = HttpResponse(content_type='application/pdf')
        merger.write(resp)
        return resp