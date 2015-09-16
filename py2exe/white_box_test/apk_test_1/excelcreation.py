import os
from xlwt import Workbook, easyxf
from xlrd import open_workbook
from xlutils.copy import copy
import random

path_2_apks = "D:\\tests\\autotest\\WBTA\\BuildsFromTC\\Develop\\195"
files = [x for x in os.listdir(path_2_apks) if x.endswith('.apk')]
array_dir_of_applications = sorted([i.split('-debug')[0] for i in files])

parentdir = os.path.dirname(os.path.abspath(__file__))
test_results = parentdir + "/TestRuns/" + 'WBT_report-SM-G906S-2015-01-22_17-16'

apk_dict={}
mas_of_html_test_files=[]
mas_of_txt_test_files=[]
mas_length_of_apk_names=[]
mas_length_of_apk_values =[]
random_testcount = random.randint(200, 300)
buildID ='195'
devicesname = 'SM-G906S'

header_style = easyxf('pattern: pattern solid, fore_colour light_blue;'+'font: name Arial; '+ 'borders: left thin, right thin, top thin, bottom thin;')
apkname_style = easyxf('pattern: pattern solid, fore_colour yellow;'+'font: name Arial; '+ 'borders: left thin, right thin, top thin, bottom thin;')
pass_style = easyxf('pattern: pattern solid, fore_colour green;'+'font: name Arial;' + 'borders: left thin, right thin, top thin, bottom thin;')
fail_style = easyxf('pattern: pattern solid, fore_colour red;'+'font: name Arial;' + 'borders: left thin, right thin, top thin, bottom thin;')
text_style = easyxf('font: bold 1, color red;')

for i, j in enumerate(array_dir_of_applications):
    path_to_application_dirs = test_results + "/" + array_dir_of_applications[i]
    mas_length_of_apk_names.append(len(j))

    for x in os.listdir(path_to_application_dirs):
        if x.endswith(".html"):
            mas_of_html_test_files.append(x)
        elif x.endswith(".txt"):
            mas_of_txt_test_files.append(x)

    # Creation of dictionary with apk names and results of tests
    if mas_of_html_test_files == []:
        apk_dict[j] = {'result': 'Test results are absent'}
        mas_length_of_apk_values.append(len('Test results are absent'))
    else:
        txt_file_open = open(path_to_application_dirs + "/" + mas_of_txt_test_files[i], "r+")
        str1 = txt_file_open.read()
        count = str1.count('Finished automation testing')
        if count == 0:
            apk_dict[j] = {'result':  'Crashed'}
            mas_length_of_apk_values.append(len('Crashed'))
        else:
            html_file_open = open(path_to_application_dirs + '/' + mas_of_html_test_files[i], "r+")
            str2 = html_file_open.read()
            count1 = str2.count('<td bgcolor="#FF0000">false</td>')
            count2 = str2.count('<td bgcolor="#00CC00">true</td>')
            if (count2 + count1) != int(random_testcount):
                apk_dict[j] = {'result': 'Different number of test count in I/O files (' + str(count2 + count1) + '/' + str(random_testcount) + ')'}
                mas_length_of_apk_values.append(len('Different number of test count in I/O files (' + str(count2 + count1) + '/' + str(random_testcount) + ')'))
            elif count1 == 0:
                apk_dict[j] = {'result': 'Passed'}
                mas_length_of_apk_values.append(len('Passed'))
            else:
                apk_dict[j] = {'result': 'Failed ' + str(count1)}
                mas_length_of_apk_values.append(len('Failed' + str(count1)))

# Check existence of excel_report.xls
def check_existence_of_file(file_name='excel_report.xls'):
    if os.path.isfile(file_name):
        book1 = open_workbook(file_name, formatting_info=True)
        mas_of_sheet_names = book1.sheet_names()

        # Write sheets depending on device name
        if devicesname in mas_of_sheet_names:
            i = mas_of_sheet_names.index(devicesname)
            sheet = book1.sheet_by_index(i)
            col_index = sheet.ncols
            book2=copy(book1)
            book2.get_sheet(i).write(0, col_index, "Result / build #"+buildID, header_style)
            mas_length_of_apk_values.append(len("Result / build #"+buildID))
            book2.get_sheet(i).col(col_index).width = 5000
            col = sheet.col(0)
            number_of_passed=0
            NUMBER_OF_APK = len(apk_dict)
            for row_index, key in enumerate(sorted(apk_dict)):
                list_apk_excel = col[1:]
                test_result = apk_dict[key]['result']

            # Compare names of apk with content in cells
                for name in list_apk_excel:
                    if key == name.value:
                        element_index = list_apk_excel.index(name)+1
                        if test_result == 'Passed':
                            book2.get_sheet(i).write(element_index,col_index,test_result, pass_style)
                            number_of_passed+=1
                        else:
                            book2.get_sheet(i).write(element_index,col_index,test_result, fail_style)
                        del apk_dict[key]
                        break
            # Check the existence of new apk
            if len(apk_dict) > 0:
                count =1
                for row_index, key in enumerate(sorted(apk_dict)):
                    test_result = apk_dict[key]['result']
                    book2.get_sheet(i).write(len(col[1:])+count, 0, key, apkname_style)
                    if test_result == 'Passed':
                        book2.get_sheet(i).write(len(col[1:])+count, col_index,test_result, pass_style)
                        number_of_passed+=1
                    else:
                        book2.get_sheet(i).write(len(col[1:])+count, col_index,test_result, fail_style)
                    count+=1
            rate = 100*number_of_passed/NUMBER_OF_APK
            book2.get_sheet(i).write(NUMBER_OF_APK +1, col_index, "Rate = " + str(rate) + " %", text_style)
            book2.get_sheet(i).col(col_index).width = 257*max(mas_length_of_apk_values)
            book2.get_sheet(i).col(0).width = 257*max(mas_length_of_apk_names)
            book2.save('excel_report.xls')
        else:
            book2=copy(book1)
            sheet2 = book2.add_sheet(devicesname)
            col_index = 0
            sheet2.write(0, 0, "Apk name", header_style)
            sheet2.write(0, 1, "Result / build #"+ buildID, header_style)
            mas_length_of_apk_values.append(len("Result / build #"+buildID))
            sheet2.col(1).width = 5000
            number_of_passed = 0
            for row_index, key in enumerate(sorted(apk_dict)):
                row_index += 1
                test_result = apk_dict[key]['result']
                sheet2.col(col_index).width = 257*max(mas_length_of_apk_names)
                sheet2.col(col_index+1).width = 257*max(mas_length_of_apk_values)
                sheet2.write(row_index, col_index, key, apkname_style)
                if test_result == 'Passed':
                    number_of_passed +=1
                    sheet2.write(row_index, col_index+1, test_result, pass_style)
                else:
                    sheet2.write(row_index, col_index+1, test_result, fail_style)
            rate = 100*number_of_passed/len(apk_dict)
            sheet2.write(len(apk_dict)+1, col_index+1, "Rate = " + str(rate) + " %", text_style)
            sheet2.set_panes_frozen(True)
            sheet2.set_vert_split_pos(1)
            book2.save('excel_report.xls')
    else:
        # First creation of excel file
        print "Creation of excel_report.xls"
        col_index = 0
        book = Workbook()
        sheet1 = book.add_sheet(devicesname)
        sheet1.write(0, 0, "Apk name", header_style)
        sheet1.write(0, 1, "Result / build #"+ buildID, header_style)
        mas_length_of_apk_values.append(len("Result / build #"+buildID))
        sheet1.col(1).width = 5000
        number_of_passed = 0
        for row_index, key in enumerate(sorted(apk_dict)):
            row_index += 1
            test_result = apk_dict[key]['result']
            sheet1.col(col_index).width = 257*max(mas_length_of_apk_names)
            sheet1.col(col_index+1).width = 257*max(mas_length_of_apk_values)
            sheet1.write(row_index, col_index, key, apkname_style)
            if test_result == 'Passed':
                number_of_passed +=1
                sheet1.write(row_index, col_index+1, test_result, pass_style)
            else:
                sheet1.write(row_index, col_index+1, test_result, fail_style)
        rate = 100*number_of_passed/len(apk_dict)
        sheet1.write(len(apk_dict)+1, col_index+1, "Rate = " + str(rate) + " %", text_style)
        sheet1.set_panes_frozen(True)
        sheet1.set_vert_split_pos(1)
        book.save('excel_report.xls')
check_existence_of_file()

#Line chart creation of rate of passed tests in new xls file
import xlsxwriter
workbook = open_workbook('excel_report.xls')
number_of_sheets = workbook.nsheets
mas_of_sheet_names = workbook.sheet_names()
dict = {}

for i in range(number_of_sheets):
    rate_digits = []
    sheet_names = mas_of_sheet_names[i]
    sheet = workbook.sheet_by_index(i)

    for j in range(sheet.ncols):
        particular_cell_value = sheet.cell(21, j).value
        rate_digit = ''.join(x for x in particular_cell_value if x.isdigit())
        if rate_digit == '':
            continue
        else:
            rate_digits.append(int(rate_digit))
            dict[sheet_names] = rate_digits

workbook = xlsxwriter.Workbook('chart of rate of passed tests.xlsx')
worksheet = workbook.add_worksheet()
chart = workbook.add_chart({'type': 'line'})
colors = ['blue', 'red', 'green']

for i,j in enumerate(dict):
    worksheet.write(0, i, j)
    for x,y in enumerate(dict[j]):
        worksheet.write(x+1, i, y)

    chart.add_series({
        'values': ['Sheet1',1,i,len(dict[j]),i],
        'line':{'color': colors[i]},
        'name':j,
        'marker': {
        'type': 'circle',
        'size': 6,
        'border': {'color': 'black'},
        'fill':   {'color': 'red'},},})
    chart.set_x_axis({'min': 0, 'max': len(dict[j])})

chart.set_y_axis({'min': -10, 'max': 100})
chart.set_title({'name': 'Rate of passed tests',})
chart.set_size({'width': 720, 'height': 576})
worksheet.insert_chart('A1', chart)

workbook.close()