"""
 * Author: Christopher Gedler <cgedler@gmail.com>
 * Version: 1.0
 * Last Change: 28.05.2020 
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
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
