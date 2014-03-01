##
## Test math functions
##
import os
import sys
import time
import unittest

import numpy as np

import scipy
import scipy.misc 
from scipy.special import gammaln

import misopy
import misopy.pyx
import misopy.pyx.matrix_utils as matrix_utils


class TestMath(unittest.TestCase):
    """
    Test mathematics functions.
    """
    def setUp(self):
        pass

    
    def test_mat_trans(self):
        """
        Test matrix transpose.
        """
        A = np.array([[1,2],
                      [3,4],
                      [5,6]], dtype=float)
        A_trans_pyx = matrix_utils.py_mat_trans(A, A.shape[0], A.shape[1])
        A_trans_numpy = A.T
        assert (np.array_equal(A_trans_pyx, A_trans_numpy)), \
          "Matrix transpose failed (1)."
          
        B = np.array([[1,2,3,4,5],
                      [10,20,30,40,50]], dtype=float)
        B_trans_pyx = matrix_utils.py_mat_trans(B, B.shape[0], B.shape[1])
        B_trans_numpy = B.T
        assert (np.array_equal(B_trans_pyx, B_trans_numpy)), \
          "Matrix transpose failed (2)."

          
    def test_mat_times_mat(self):
        A = np.array([[1, 2, 3],
                      [4, 5, 6]], dtype=float)
        B = np.array([[10, 20],
                      [40, 50],
                      [0, 1]], dtype=float)
        pyx_A_times_B = \
          matrix_utils.py_mat_times_mat(A, 
                                        A.shape[0],
                                        A.shape[1],
                                        B.shape[1],
                                        B)
        numpy_A_times_B = np.matrix(A) * np.matrix(B)
        assert (pyx_A_times_B, numpy_A_times_B), \
          "Matrix multiplication failed."


def main():
    unittest.main()


if __name__ == "__main__":
    main()
