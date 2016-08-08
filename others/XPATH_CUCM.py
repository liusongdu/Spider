#-*-coding:utf8-*-
from lxml import etree
import os
import re

html = '''
<fieldset>
    <fieldset>
        <table class="content-grid" width="100%" cellspacing="0" cellpadding="0" summary='License Requirements by Type' >
            <tr class="content-grid-stripe-light">
                <td width="20%">CUWL Standard</td>
                <td width="20%">2</td>
                <td width="25%">
                    <a href="/ccmadmin/licenseUserFindList.do?key=fc556022-7ef4-435c-839e-b6ce130fea11" class="content-grid-link">Users(2)</a>
                    <a href="/ccmadmin/licenseDeviceFindList.do?key=fc556022-7ef4-435c-839e-b6ce130fea11" class="content-grid-link">Unassigned Devices(0)</a>
                </td>
                <td width="35%">
            </tr>
            <tr class="content-grid-stripe-dark">
                <td width="20%">Enhanced Plus</b></td>
                <td width="20%">1</b></td>
                <td width="25%">
                    <a href="/ccmadmin/licenseUserFindList.do?key=fc556022-7ef4-435c-839e-b6ce130fea12" class="content-grid-link">Users(1)</a>
                </td>
                <td width="35%">
            </tr>
            <tr class="content-grid-stripe-light">
                <td width="20%">Enhanced</b></td>
                <td width="20%">8859</b></td>
                <td width="25%">
                <a href="/ccmadmin/licenseUserFindList.do?key=fc556022-7ef4-435c-839e-b6ce130fea13" class="content-grid-link">Users(63)</a>
                <a href="/ccmadmin/licenseDeviceFindList.do?key=fc556022-7ef4-435c-839e-b6ce130fea13" class="content-grid-link">Unassigned Devices(8796)</a>
                </td>
                <td width="35%">
            </tr>
            <tr class="content-grid-stripe-dark">
                <td width="20%">Basic</b></td>
                <td width="20%">279</b></td>
                <td width="25%">
                    <a href="/ccmadmin/licenseUserFindList.do?key=fc556022-7ef4-435c-839e-b6ce130fea14" class="content-grid-link">Users(271)</a>
                    <a href="/ccmadmin/licenseDeviceFindList.do?key=fc556022-7ef4-435c-839e-b6ce130fea14" class="content-grid-link">Unassigned Devices(8)</a>
                </td>
                <td width="35%">
            </tr>
            <tr class="content-grid-stripe-light">
                <td width="20%">Essential</b></td>
                <td width="20%">403</b></td>
                <td width="25%">
                    <a href="/ccmadmin/essentialLicenseUserFindList.do" class="content-grid-link">Users(0)</a>
                    <a href="/ccmadmin/licenseDeviceFindList.do?key=fc556022-7ef4-435c-839e-b6ce130fea15" class="content-grid-link">Unassigned Devices(403 )</a>
                </td>
                <td width="35%">
            </tr>
            <tr class="content-grid-stripe-dark">
                <td width="20%">TelePresence Room</b></td>
                <td width="20%">0</b></td>
                <td width="25%"><a href="/ccmadmin/telepresenceLicenseUserFindList.do" class="content-grid-link">Users(0)</a>
                    <a href="/ccmadmin/telepresenceLicenseDeviceFindList.do" class="content-grid-link">Unassigned Devices(0)</a>
                </td>
                <td width="35%">
            </tr>
        </table>
    </fieldset>
</fieldset>
'''

selector = etree.HTML(html)

# GoTo "License Requirements by Type" part
# Use Copy Outer HTML in Firefox to get the element name
urllrbt = '//fieldset/fieldset/table[@summary="License Requirements by Type"]/tr'
urlcell = 'td'
selector1 = selector.xpath(urllrbt)
f = open("D:\\pyRegularExpression\\Results\\license.csv", "w")

for eachselector1 in selector1:
    selector2 = eachselector1.xpath(urlcell)  # list
    j = 0
    for eachselector2 in selector2:
        if j > 1:
            break
        elif j == 0:
            try:
                f.write(eachselector2.text + ',')
            except TypeError:
                f.write('')
        else:
            try:
                f.write(eachselector2.text + '\n')
            except TypeError:
                f.write('')
        j += 1
f.close()