# -*- coding: utf-8 -*-
import ttk
import xlwt
import xlrd
import tkFileDialog
import tkMessageBox
import unicodedata
import Tkinter
from tempfile import TemporaryFile
from datetime import datetime

import collections

class Persons:
    def __init__(self, full_name, num_tab, struct_name, value):
        self.full_name = full_name
        self.struct_name = struct_name
        self.value = value
        self.num_tab = num_tab

    def sort(self):
        res = []
        for k, v in collections.OrderedDict(sorted(self.value.items())).items():
            # v.insert(0, datetime.strftime(k, '%d-%m-%Y'))
            res.append(v)
        return res

def center_window(w, h, window):
    # Получение ширины и высоты экрана
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # Расчет позиций x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.resizable(False, False)

def Quit(event):
    main_window.destroy()

def person_id_window_destroy(event):
    person_id_window.destroy()

def SaveFile():
    fn = tkFileDialog.SaveAs(main_window, filetypes=[('Microsoft Office Excel', '.xls')]).show()

    if isinstance(fn, unicode):
        fn = unicodedata.normalize('NFKD', fn).encode('ascii', 'ignore')

    if isinstance(fn, str):
        if not fn.endswith('.xls'):
            fn += '.xls'
    else:
        return False
    return fn

def Draw_window(event):
    global person_id_window, person_id_text
    person_id_window = Tkinter.Toplevel(main_window)
    center_window(200, 150, person_id_window)
    person_id_window.title('Parser')

    label = Tkinter.Label(person_id_window, text='Введите табельный\n номер сотрудника', font='Arial 12')
    label.place(x=20, y=15)
    person_id_text = Tkinter.Text(person_id_window, font='Arial 12', height=1, width=15, wrap='word')
    person_id_text.place(x=30, y=65)

    okBtn = ttk.Button(person_id_window, text='Ок')
    cancelBtn = ttk.Button(person_id_window, text='Отмена')
    okBtn.bind('<Button-1>', Reportperson)
    cancelBtn.bind('<Button-1>', person_id_window_destroy)
    okBtn.place(x=15, y=100)
    cancelBtn.place(x=110, y=100)

    person_id_window.mainloop()

def Write_to_file(data, first_row, report_type=None, person_id=None):
    book = xlwt.Workbook()
    sheet_query = book.add_sheet('Query')
    position_y = 0

    # Первая строка в xsl документе
    for position_x, word in enumerate(first_row):
                sheet_query.write(position_y, position_x, word)
    position_y += 1

    if report_type == 'person':
        data = {person_id: data[person_id]}

    for num in sorted(data):
        position_x = 0
        sheet_query.write(position_y, position_x, data[num].full_name)
        sheet_query.write(position_y, position_x + 1, data[num].num_tab)
        sheet_query.write(position_y, position_x + 2, data[num].struct_name)
        for item in data[num].sort():
            position_x = 3
            for i in item:
                sheet_query.write(position_y, position_x, i)
                position_x += 1
            position_y += 1

    fn = SaveFile()
    if isinstance(fn, str) and fn != '.xls':
        book.save(fn)
        book.save(TemporaryFile())
        tkMessageBox.showinfo('Info', 'Отчет создан!')

def Reportall(event):
    data, first_row = Makedatabase()
    if data and first_row:
        Write_to_file(data, first_row)

def Reportperson(event):
    person_id = None
    person = person_id_text.get('0.0', Tkinter.END).strip().encode('utf-8')

    if person != '':
        try:
            person_id = int(person.encode('utf-8'))
        except Exception:
            tkMessageBox.showwarning('Ошибка!', 'Не правильный табельный номер сотрудника!')
    else:
        tkMessageBox.showwarning('Ошибка!', 'Введите табельный номер сотрудника!')

    person_id_window.destroy()
    data, first_row = Makedatabase()
    if data and first_row and person_id:
            Write_to_file(data, first_row, 'person', person_id)

def Makedatabase():
    files_list = textbox.get('0.0', Tkinter.END).strip().encode('utf-8').split('\n')
    sheet_name = sheet_text.get('0.0', Tkinter.END).strip().encode('utf-8')
    data = {}
    first_row = []
    if files_list[0] != '':
        for file_number, fl in enumerate(files_list):
            fl = fl.strip().replace('/', '//')
            try:
                workbook = xlrd.open_workbook(fl, encoding_override='utf-8', on_demand=True)
            except Exception:
                tkMessageBox.showwarning('Ошибка!', 'Не правильный путь к файлу: \n%s' % fl)
                continue

            sheets = workbook.sheet_names()
            if sheet_name in sheets:
                for n_sh, sheet in enumerate(sheets):
                    sheet = sheet.encode('utf-8')
                    if sheet == sheet_name:
                        for row_number, row in enumerate(range(workbook.sheet_by_name(sheet).nrows)):
                            values = []
                            for col in range(workbook.sheet_by_name(sheet).ncols):
                                values.append(workbook.sheet_by_name(sheet).cell(row, col).value.strip())

                            if row_number == 0:
                                first_row = values
                                continue
                            num_tab = int(values[1].encode('utf-8'))
                            if file_number == 0:
                                if row != 0:
                                    data[num_tab] = Persons(full_name=values[0], num_tab=values[1],
                                                                                 struct_name=values[2],
                                                                                 value={datetime.strptime(values[3], '%d-%m-%Y'): values[3:]})
                            else:
                                if num_tab in data.keys():
                                    data[num_tab].value[datetime.strptime(values[3], '%d-%m-%Y')] = values[3:]
                                else:
                                    data[num_tab] = Persons(full_name=values[0], num_tab=values[1], struct_name=values[2],
                                                            value={datetime.strptime(values[3], '%d-%m-%Y'): values[3:]})
            else:
                tkMessageBox.showwarning('Ошибка!', 'В документе\n%s\nнет станицы с именем %s' % (fl, sheet_name))
        return data, first_row
    else:
        tkMessageBox.showwarning('Ошибка!', 'Файлы не выбраны!')
        return None, None

def LoadFiles(event):
    fn = tkFileDialog.askopenfilenames(filetypes=[('Microsoft Office Excel', '.xls')])
    if isinstance(fn, tuple):
        for line in fn:
            if line == '':
                return
            textbox.insert('1.0', '%s\n' % line.replace(' ', '\n'))
    else:
        if fn == '':
                return
        textbox.insert('1.0', '%s\n' % fn.strip().replace(' ', '\n'))

# Создание главного не изменяемого окна в центре экрана
main_window = Tkinter.Tk()
main_window.title('Parser')
center_window(800, 400, main_window)
# Создание панели для кнопок и панели для текстового поля
panelFrame = Tkinter.Frame(main_window, height=60, bg='gray')
textFrame = Tkinter.Frame(main_window)
panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)
# Добавление прокрутки на текстовую панель
scrollbar = Tkinter.Scrollbar(textFrame)
scrollbar.pack(side='right', fill='y')
# Создание текстового окна
textbox = Tkinter.Text(textFrame, font='Arial 14', wrap='word', yscrollcommand=scrollbar.set)
textbox.pack(side='left', fill='both', expand=1)
scrollbar['command'] = textbox.yview
# Создание кнопок на верхней панеле с вызовом соответствующих функций
loadBtn = ttk.Button(panelFrame, text='Выбрать файлы')
quitBtn = ttk.Button(panelFrame, text='Выход')
makeallBtn = ttk.Button(panelFrame, text='Отчет по всем\n сотрудникам')
makepersonBtn = ttk.Button(panelFrame, text='  Отчет по\nсотруднику')

loadBtn.bind('<Button-1>', LoadFiles)
quitBtn.bind('<Button-1>', Quit)
makeallBtn.bind('<Button-1>', Reportall)
makepersonBtn.bind('<Button-1>', Draw_window)
# Расположение кнопок на панеле
loadBtn.place(x=10, y=10, width=110, height=40)
makeallBtn.place(x=150, y=10, width=110, height=40)
makepersonBtn.place(x=290, y=10, width=110, height=40)
quitBtn.place(x=740, y=10, width=50, height=40)
# Создание и размещение на верхней панеле лейбла и текстового поля
label = Tkinter.Label(panelFrame, text='Имя страницы:', font='Arial 12', bg='gray')
label.place(x=450, y=15)
sheet_text = Tkinter.Text(panelFrame, font='Arial 12', height=1, width=15, wrap='word', bg='gray')
sheet_text.insert(1.0, 'Query')
sheet_text.place(x=565, y=15)

main_window.mainloop()