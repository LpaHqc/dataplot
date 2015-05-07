# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 17:07:39 2014

@author: Laure
"""

# --- Variables
FOLDER = r'D:\Users\Laure\Documents\Laure\Mesures\CPSRES32R\NT'

FILE_TEMPLATE = '20150422_grayscale_freqEpsilon_002_5av'
FILE_RESULT = '{}_averaged'.format(FILE_TEMPLATE)

# --- File contents infos

AV = 'average'
L = ['currentpA', 'Gdiff2e2h', 'amplitude', 'phase']
N_AV = 5
SWEEP_LENGTH = 201


# --- Imports
import numpy as np
import os
from tools.io import read_array


def sweep_averaging(FOLDER, FILENAME, COLUMNS_TO_AVERAGE, AVERAGE_COLUMN, N_AV, SWEEP_LENGTH):
    """
    This function transforms an array with averages of sweeps in an averaged array.
    It works for grayscales.
    data is an array with colum Names
    COLUMNS_TO_AVERAGE is a list (of strings) containing the column's names to average
    AVERAGE_COLUMN is a string = the column where the average index is stored
    N_AV is the number of averages
    SWEEP_LENGTH is the sweep length
    """
# import data file and remove header to obtain array
    path = os.path.join(FOLDER, FILENAME)
    assert os.path.isdir(FOLDER), 'Invalid folder path'
    data = read_array(path)

#    la division euclidienne permet d'avoir le nombre de points de la valeur
#    incrementale du grayscale pour lesquels la mesure est complète
    INCREMENTATION_LENGTH = data.shape[0]/SWEEP_LENGTH/N_AV
    print INCREMENTATION_LENGTH
    average_indexes = list(set(data[AVERAGE_COLUMN]))

# --- Averaged array infos
    avg_array = []
    avg_array_LENGTH = INCREMENTATION_LENGTH*SWEEP_LENGTH
    columns_names = list(data.dtype.names)
    columns_names.remove(AVERAGE_COLUMN)
    print columns_names

# --- main
    for column in columns_names:
        if column not in COLUMNS_TO_AVERAGE:
            # construction of columns that do not need to be averaged
            # filter by last average index enables to select only complete data
            avg_column = data[column][data[AVERAGE_COLUMN] == average_indexes[-1]]

        else:
            # average
            avg_column = np.zeros(avg_array_LENGTH)
            for i in range(INCREMENTATION_LENGTH):
                # filter data array by incremental value of grayscale (consecutive blocks)
                filter_by_incr_value = data[column][i*N_AV*SWEEP_LENGTH:(i+1)*N_AV*SWEEP_LENGTH]
                # create SWEEP_LENGTH*N_AV matrix from filtered array
                # 'F' order means that values are written by columns
                matrix = np.reshape(filter_by_incr_value, (-1, N_AV), order='F')
                avg_column[i*SWEEP_LENGTH:(i+1)*SWEEP_LENGTH] = np.mean(matrix, axis=1)

        avg_array.append(avg_column)

    result = np.rec.fromarrays(avg_array, names=columns_names)

# --- save averaged array
    save_path = os.path.join(FOLDER, FILE_RESULT)
    with open(save_path, 'wb') as f:
        f.write('\t'.join(result.dtype.names) + '\n')
        np.savetxt(f, result, delimiter='\t', fmt='%g')


if __name__ == '__main__':
    sweep_averaging(FOLDER, FILE_TEMPLATE, L, AV, N_AV, SWEEP_LENGTH)
