import pytest

from src.utils import get_pure_operations, get_lst_5_oper_srtd, get_hidden_data

from tests.data.data import tested_operation, operations_zero, tested_result, tested_operation_2, \
    tested_result_2, tested_operation_3, tested_result_3, pure_operations_ts, pure_operations_ts_rst, \
    hidden_test_data_1, hidden_test_result_1, hidden_test_data_2, hidden_test_result_2



def test_get_pure_operation():
    assert get_pure_operations(operations_zero) == []
    assert get_pure_operations(tested_operation) == tested_result
    assert get_pure_operations(tested_operation_2) == tested_result_2
    assert get_pure_operations(tested_operation_3) == tested_result_3


def test_get_lst_5_oper_srtd():
    pure_operations = pure_operations_ts
    assert get_lst_5_oper_srtd(pure_operations) == pure_operations_ts_rst


def test_get_hidden_data():
    assert get_hidden_data(hidden_test_data_1) == hidden_test_result_1
    assert get_hidden_data(hidden_test_data_2) == hidden_test_result_2



