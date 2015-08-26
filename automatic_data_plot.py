# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:22:38 2015

@author: Laure
"""
import os
import shutil
from make_grayscale import plot_save_grayscale

FOLDER_TO_PLOT = r'D:\Users\Laure\Documents\Laure\Mesures\CPSRES32R\NT\To plot'
ARCHIVE_FOLDER = r'D:\Users\Laure\Documents\Laure\Mesures\CPSRES32R\NT\Processed'
PLOT_SAVE_FOLDER = r'D:\Users\Laure\Documents\Laure\Mesures\CPSRES32R\NT\Plots'

move_option = 'yes'

column_list_1 = ['currentpA', 'Gdiff2e2h', 'amplitude', 'phase']

column_list_2 = ['I1pA', 'G12e2h', 'I2pA', 'G22e2h', 'amplitude', 'phase']

dict_label = {'Vg8V': 'Vg8 (V)', 'VsdmV': '$\mathregular{V_{sd}\,(mV)}$',
              'Vg9V': 'Vg9 (V)', 'epsilonV': r'$\mathregular{\epsilon \, (V)}$',
              'deltaV': r'$\mathregular{\delta \, (V)}$',
              'currentpA': 'I (pA)', 'I1pA': '$\mathregular{I_{1}\, (pA)}$',
              'I2pA': '$\mathregular{I_{2}\, (pA)}$',
              'Gdiff2e2h': r'$\mathregular{G \, (\frac{2e^{2}}{h})}$',
              'G12e2h': r'$\mathregular{G_{1} \, (\frac{2e^{2}}{h})}$',
              'G22e2h': r'$\mathregular{G_{2} \, (\frac{2e^{2}}{h})}$',
              'amplitude': 'Amplitude (V)',
              'phase': 'Phase (rad)',
              'freqGHz': 'f (GHz)'}

for filename in os.listdir(FOLDER_TO_PLOT):
    # Select column_list depending on date : after April 22nd simultaneous left and right measurement, before this date we measure through the superconducting finger.
    if (int(filename[5:6])>=4) and (int(filename[6:8])>=22):
        print (filename, int(filename[5:6])<=4)
        column_list = column_list_2
    else:
        column_list = column_list_1
    #print column_list

        if (('grayscaleDeltaEpsilon' in filename or 'DeltaEps' in filename or 'Delta_Eps' in filename) and ('multi' not in filename)):
            print filename
            column_name_x = 'epsilonV'
            column_name_y = 'deltaV'

            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'single', 'no', 'RdBu', 'yes', 'yes')
            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'single', 'no', 'RdBu', 'no', 'yes')
            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'panel', 'no', 'RdBu', 'yes', 'yes')
            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'panel', 'no', 'RdBu', 'no', 'yes')

            if move_option =='yes':
                path = os.path.join(FOLDER_TO_PLOT, filename)
                shutil.move(path, ARCHIVE_FOLDER)

        if 'grayscale_freqEpsilon' in filename:
            print filename
            column_name_x = 'epsilonV'
            column_name_y = 'freqGHz'

            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'single', 'no', 'RdBu', 'yes', 'yes')
            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'single', 'no', 'RdBu', 'no', 'yes')
            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'panel', 'no', 'RdBu', 'yes', 'yes')
            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'panel', 'no', 'RdBu', 'no', 'yes')

            if move_option =='yes':
                path = os.path.join(FOLDER_TO_PLOT, filename)
                shutil.move(path, ARCHIVE_FOLDER)

        if ('Vg8Vg9' in filename and 'multi' not in filename):
            print filename
            column_name_x = 'Vg9V'
            column_name_y = 'Vg8V'

            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'single', 'no', 'RdBu', 'yes', 'yes')
            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'single', 'no', 'RdBu', 'no', 'yes')
            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'panel', 'no', 'RdBu', 'yes', 'yes')
            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'panel', 'no', 'RdBu', 'no', 'yes')

            if move_option =='yes':
                path = os.path.join(FOLDER_TO_PLOT, filename)
                shutil.move(path, ARCHIVE_FOLDER)

        if ('VsdVg8' in filename and 'multi' not in filename):
            print filename
            column_name_x = 'Vg8V'
            column_name_y = 'VsdmV'

            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'single', 'no', 'RdBu', 'yes', 'yes')
            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'single', 'no', 'RdBu', 'no', 'yes')
            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'panel', 'no', 'RdBu', 'yes', 'yes')
            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'panel', 'no', 'RdBu', 'no', 'yes')

            if move_option =='yes':
                path = os.path.join(FOLDER_TO_PLOT, filename)
                shutil.move(path, ARCHIVE_FOLDER)

        if ('VsdDelta' in filename or 'Vsd_Delta' in filename):
            print filename
            column_name_x = 'deltaV'
            column_name_y = 'VsdmV'

            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'single', 'no', 'RdBu', 'yes', 'yes')
            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'single', 'no', 'RdBu', 'no', 'yes')
            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'panel', 'no', 'RdBu', 'yes', 'yes')
            plot_save_grayscale(FOLDER_TO_PLOT, filename, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'panel', 'no', 'RdBu', 'no', 'yes')

            if move_option =='yes':
                path = os.path.join(FOLDER_TO_PLOT, filename)
                shutil.move(path, ARCHIVE_FOLDER)
                
