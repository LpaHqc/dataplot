# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 11:21:13 2015

@author: Laure
"""
# --- Imports
import numpy as np
import os
import shutil
from tools.io import read_array_header
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from textwrap import wrap


# --- Variables
FOLDER = r'D:\Users\Laure\Documents\Laure\Mesures\CPSRES32R\NT\To plot'
FILENAME = '20150420_grayscaleDeltaEpsilon_005'
PLOT_SAVE_FOLDER = r'D:\Users\Laure\Documents\Laure\Mesures\CPSRES32R\NT\Plots'
ARCHIVE_FOLDER = r'D:\Users\Laure\Documents\Laure\Mesures\CPSRES32R\NT\Processed'

column_name_x = 'epsilonV'
column_name_y = 'deltaV'

column_list = ['currentpA', 'Gdiff2e2h', 'amplitude', 'phase']

dict_label = {'Vg8V': 'Vg8 (V)', 'VsdmV': '$\mathregular{V_{sd}\,(mV)}$', 'Vg9V': 'Vg9 (V)', 'epsilonV': r'$\mathregular{\epsilon \, (V)}$', 'deltaV': r'$\mathregular{\delta \, (V)}$',
'currentpA': 'I (pA)', 'Gdiff2e2h': r'$\mathregular{G \, (\frac{2e^{2}}{h})}$', 'amplitude': 'Amplitude (V)', 'phase': 'Phase (rad)', 'freqGHz': 'f (GHz)'}


def plot_save_grayscale(FOLDER, FILENAME, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, layout, plot_option, color, header_option, save_option):

    # import data file and return {'array': array, 'header': header}
    path = os.path.join(FOLDER, FILENAME)
    assert os.path.isdir(FOLDER), 'Invalid folder path'
    data = read_array_header(path)
    header = data['header']
    data = data['array']
    MIN_X = data[column_name_x][0]
    MIN_Y = data[column_name_y][0]

    # find size_y which is the sweep length that is the number of points in the sweep
    ind = 0
    while data[column_name_x][ind] == MIN_X:
        ind += 1
    size_y = ind
    MAX_Y = data[column_name_y][size_y-1]
    # find size_x that is the incrementation length : euclidean division enables to
    # find size_x such that measure is complete.
    size_x = data.shape[0]/size_y
    # data troncation to obtain a complete matrix
    data = data[:size_x*size_y]
    MAX_X = data[column_name_x][-1]

    matrix_dic = {c: np.reshape(data[c], (size_y, size_x), order='F') for c in column_list}
    if layout == 'single':
        for c in column_list:
            plt.figure()
            im = plt.imshow(matrix_dic[c], origin='lower', extent=[MIN_X, MAX_X, MIN_Y, MAX_Y], cmap=color, aspect='auto', interpolation='none')
            if header_option == 'yes':
                plt.title(FILENAME +'\n' + "\n".join(wrap(header)) + '\n', fontsize=11)
#                plt.suptitle(, fontsize=11)
            plt.xlabel(dict_label[column_name_x])
            plt.ylabel(dict_label[column_name_y])
            ax = plt.gca()
            ax.xaxis.set_ticks_position('bottom')
            divider = make_axes_locatable(ax)
            cax = divider.append_axes("right", size="5%", pad=0.05)
            cbar = plt.colorbar(im, cax=cax)
            cbar.set_label(dict_label[c])
            plt.tight_layout()

            if save_option == 'yes':
                if header_option == 'yes':
                    SAVE_FOLDER = PLOT_SAVE_FOLDER
                else:
                    SAVE_FOLDER = PLOT_SAVE_FOLDER + '\No_Header'
                if not os.path.isdir(SAVE_FOLDER):
                        os.mkdir(SAVE_FOLDER)
                FILE_RESULT = '{}_grayscale_'.format(FILENAME) + c + '.png'
                save_path = os.path.join(SAVE_FOLDER, FILE_RESULT)
                plt.savefig(save_path)

            if plot_option == 'yes':
                plt.show()
# This part can be optimized by a better use of subplots, share axis functions etc but it is note straightforward ! This solution is a bit too much hand made but gives a reasonable result in my case.
    if layout == 'panel':
        plt.figure()
        if header_option == 'yes':
                #plt.title(FILENAME)
                plt.suptitle(FILENAME + '\n\n' + "\n".join(wrap(header)), fontsize=11)
        for i, c in enumerate(column_list):
            plt.subplot(2, 2, i+1)
            im = plt.imshow(matrix_dic[c], origin='lower', extent=[MIN_X, MAX_X, MIN_Y, MAX_Y], cmap=color, aspect='auto', interpolation='none')
            if i in [2, 3]:
                plt.xlabel(dict_label[column_name_x])
            if i in [0, 2]:
                plt.ylabel(dict_label[column_name_y])
            ax = plt.gca()
            ax.xaxis.set_ticks_position('bottom')
            divider = make_axes_locatable(ax)
            cax = divider.append_axes("right", size="5%", pad=0.05)
            cbar = plt.colorbar(im, cax=cax)
            cbar.set_label(dict_label[c])
        plt.tight_layout(rect =[0, 0, 1, 0.8], h_pad = 0.05)

        if save_option == 'yes':
                if header_option == 'yes':
                    SAVE_FOLDER = PLOT_SAVE_FOLDER
                else:
                    SAVE_FOLDER = PLOT_SAVE_FOLDER + '\No_Header'
                if not os.path.isdir(SAVE_FOLDER):
                        os.mkdir(SAVE_FOLDER)
                FILE_RESULT = '{}_grayscales_'.format(FILENAME) + 'panel' + '.png'
                save_path = os.path.join(SAVE_FOLDER, FILE_RESULT)
                plt.savefig(save_path)

        if plot_option == 'yes':
                plt.show()


if __name__ == '__main__':
    plot_save_grayscale(FOLDER, FILENAME, PLOT_SAVE_FOLDER, column_name_x, column_name_y, column_list, dict_label, 'single', 'yes', 'RdBu', 'yes', 'yes')

