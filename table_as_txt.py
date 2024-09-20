from itertools import count

from tabulate import tabulate


# class ReportTable:
#     HEADER = ['Source', 'File', 'Parameter']
#     table_data = []
#
#     def add_cell(self, value, column, new_row=False):
#         if new_row:
#             self.add_empty_row()
#         col_id = self._get_column_id(column)
#         self.table_data[len(self.table_data) - 1][col_id] = value
#
#     def log_table(self):
#         print(tabulate(self.table_data, headers=self.HEADER))
#
#     def clear_table(self):
#         self.table_data = []
#
#     def add_empty_row(self, count_new_lines=1):
#         for i in range(count_new_lines):
#             self.table_data.append([None] * len(self.HEADER))
#
#     def _get_column_id(self, column):
#         if isinstance(column, int):
#             return int(column)
#         else:
#             return self.HEADER.index(column)
#
#
# tt = ReportTable()
# tt.add_cell("FILE1", "File", True)
# tt.add_cell("FILE2", "File", True)
# tt.add_cell("PARAMETER", "Parameter")
# tt.add_cell("SOURCE", "Source")
# tt.log_table()
#
# h = ['Source', 'File', 'Parameter']
# print(h.index("File"))
# print(h.index(1))
#
# table = [['John', 'Smith', 39],
#          ['Mary', 'Jane', 25],
#          ['Jennifer', 'Doe', 28]]
# headers = ['First Name', 'Last Name', 'Age']
# print(len(table))
# table.append(['John', 'Smith', 28])
# table.append(['Prokop'] * 3)
# table.append([None] * 3)
# table.append(['John', 'Smith'])
#
# rows, cols = (5, 5)
# arr = [None] * 5
# print(arr)
# print(tabulate(table, headers=headers))
headers = ["Roll Number","Student name","Marks"]
dt =        [[1,"Sasha",34],
            [2,"Richard",36],
            [3,"Judy",20],
            [4,"Lori",39],
            [5,"Maggie",40]]

all_data = [headers] + dt



table1 = tabulate(all_data)
table2 = tabulate(all_data, headers='firstrow')

print(table1)
print(table2)