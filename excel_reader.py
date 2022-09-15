import pandas as pd
from actions_logger import Logger
import tkinter
from tkinter import filedialog

tkinter.Tk().withdraw()
logger = Logger()


class ExcelReader:
    def __init__(self):
        self.hosts = []
        self.ip = []
        self.site = []
        self.country = []
        self.bu = []

    def data_reader(self):
        try:
            excel_data_df = pd.read_excel(filedialog.askopenfile().name)
            logger.file_was_found()
        except FileNotFoundError as e:
            logger.no_file_error(e)
            print("The excel file was not found.")

        self.hosts = excel_data_df['host'].values.tolist()
        self.ip = excel_data_df['ip'].values.tolist()
        self.site = excel_data_df['Site'].values.tolist()
        self.country = excel_data_df['Country'].values.tolist()
        self.bu = excel_data_df['BU'].values.tolist()
