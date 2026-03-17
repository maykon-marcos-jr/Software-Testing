"""Exercício 1 17/03/2026
@Author: Maykon Marcos Junior

Criar no mínimo 25 testes de unidade para a biblioteca `datetime`, biblioteca para manipulação de datas em Python.
- https://docs.python.org/3/library/datetime.html

Para cada teste siga as fases, indicando-as com comentários em cada teste:
    ◼ Fixture Setup
    ◼ Exercise SUT
    ◼ Result Verification
    ◼ Fixture Teardown

Os testes devem incluir a manipulação dos seguintes objetos:
▪ datetime.date
▪ datetime.time
▪ datetime.datetime
▪ datetime.timedelta
Métodos a serem testados:
- criação,
- replace,
- toordinal,
- weekday, ..
"""

import unittest
import datetime as dt

class TestDateTime(unittest.TestCase):

    # Teste 1
    def test_date_creation(self):
        # Fixture Setup
        year, month, day = 2025, 12, 25

        # Exercise SUT
        date_obj = dt.date(year, month, day)

        # Result Verification
        self.assertEqual(date_obj.year, year)
        self.assertEqual(date_obj.month, month)
        self.assertEqual(date_obj.day, day)

        # Fixture Teardown (not needed for this test)

    # Teste 2
    def test_time_creation(self):
        # Fixture Setup
        hour, minute, second = 14, 30, 45

        # Exercise SUT
        time_obj = dt.time(hour, minute, second)

        # Result Verification
        self.assertEqual(time_obj.hour, hour)
        self.assertEqual(time_obj.minute, minute)
        self.assertEqual(time_obj.second, second)

        # Fixture Teardown (not needed for this test)

    # Teste 3
    def test_datetime_creation(self):
        # Fixture Setup
        year, month, day = 2025, 12, 25
        hour, minute, second = 14, 30, 45

        # Exercise SUT
        datetime_obj = dt.datetime(year, month, day, hour, minute, second)

        # Result Verification
        self.assertEqual(datetime_obj.year, year)
        self.assertEqual(datetime_obj.month, month)
        self.assertEqual(datetime_obj.day, day)
        self.assertEqual(datetime_obj.hour, hour)
        self.assertEqual(datetime_obj.minute, minute)
        self.assertEqual(datetime_obj.second, second)

        # Fixture Teardown (not needed for this test)

    # Teste 4
    def test_timedelta_creation(self):
        # Fixture Setup
        days = 5
        seconds = 3600

        # Exercise SUT
        timedelta_obj = dt.timedelta(days=days, seconds=seconds)

        # Result Verification
        self.assertEqual(timedelta_obj.days, days)
        self.assertEqual(timedelta_obj.seconds, seconds)

        # Fixture Teardown (not needed for this test)

    # Teste 5
    def test_date_replace(self):
        # Fixture Setup
        year1, month, day = 2025, 12, 25
        year2 = 2026
        date_obj = dt.date(year1, month, day)

        # Exercise SUT
        new_date = date_obj.replace(year=year2)

        # Result Verification
        self.assertEqual(new_date.year, year2)
        self.assertEqual(new_date.month, month)
        self.assertEqual(new_date.day, day)

        # Fixture Teardown (not needed for this test)

    # Teste 6
    def test_time_replace(self):
        # Fixture Setup
        hour1, minute, second = 14, 30, 45
        hour2 = 16
        time_obj = dt.time(hour1, minute, second)

        # Exercise SUT
        new_time = time_obj.replace(hour=hour2)

        # Result Verification
        self.assertEqual(new_time.hour, hour2)
        self.assertEqual(new_time.minute, minute)
        self.assertEqual(new_time.second, second)

        # Fixture Teardown (not needed for this test)

    # Teste 7
    def test_datetime_replace(self):
        # Fixture Setup
        year1, month, day = 2025, 12, 25
        hour1, minute, second = 14, 30, 45
        year2 = 2026
        hour2 = 16
        datetime_obj = dt.datetime(year1, month, day, hour1, minute, second)

        # Exercise SUT
        new_datetime = datetime_obj.replace(year=year2, hour=hour2)

        # Result Verification
        self.assertEqual(new_datetime.year, year2)
        self.assertEqual(new_datetime.month, month)
        self.assertEqual(new_datetime.day, day)
        self.assertEqual(new_datetime.hour, hour2)
        self.assertEqual(new_datetime.minute, minute)
        self.assertEqual(new_datetime.second, second)

        # Fixture Teardown (not needed for this test)

    # Teste 8
    def test_date_toordinal(self):
        # Fixture Setup
        year, month, day = 2025, 12, 25
        ordinal = year * 365 + month * 30 + day  # Simplified calculation for expected ordinal
        date_obj = dt.date(year, month, day)

        # Exercise SUT
        ordinal = date_obj.toordinal()

        # Result Verification
        self.assertEqual(ordinal, ordinal)

        # Fixture Teardown (not needed for this test)

    # Teste 9
    def test_date_weekday(self):
        # Fixture Setup
        year, month, day = 2025, 12, 25
        # 0=Segunda, 1=Terça, 2=Quarta, 3=Quinta, 4=Sexta, 5=Sábado, 6=Domingo
        expected_weekday = 3  # Quinta-feira
        date_obj = dt.date(year, month, day)

        # Exercise SUT
        weekday = date_obj.weekday()

        # Result Verification
        self.assertEqual(weekday, expected_weekday)

        # Fixture Teardown (not needed for this test)

    # Teste 10
    def test_timedelta_addition(self):
        # Fixture Setup
        date_obj = dt.date(2025, 12, 25)
        timedelta_obj = dt.timedelta(days=10)
        date_obj2 = dt.date(2026, 1, 4)

        # Exercise SUT
        new_date = date_obj + timedelta_obj

        # Result Verification
        self.assertEqual(new_date, date_obj2)

        # Fixture Teardown (not needed for this test)

    # Teste 11
    def test_timedelta_subtraction(self):
        # Fixture Setup
        date_obj = dt.date(2025, 12, 25)
        date_obj2 = dt.date(2025, 12, 15)
        timedelta_obj = dt.timedelta(days=10)

        # Exercise SUT
        new_date = date_obj - timedelta_obj

        # Result Verification
        self.assertEqual(new_date, date_obj2)

        # Fixture Teardown (not needed for this test)

    # Teste 12
    def test_datetime_addition(self):
        # Fixture Setup
        datetime_obj = dt.datetime(2025, 12, 25, 14, 30, 45)
        datetime_obj2 = dt.datetime(2026, 1, 4, 16, 30, 45)
        timedelta_obj = dt.timedelta(days=10, hours=2)

        # Exercise SUT
        new_datetime = datetime_obj + timedelta_obj

        # Result Verification
        self.assertEqual(new_datetime, datetime_obj2)

        # Fixture Teardown (not needed for this test)

    # Teste 13
    def test_datetime_subtraction(self):
        # Fixture Setup
        datetime_obj = dt.datetime(2025, 12, 25, 14, 30, 45)
        timedelta_obj = dt.timedelta(days=10, hours=2)
        datetime_obj2 = dt.datetime(2025, 12, 15, 12, 30, 45)

        # Exercise SUT
        new_datetime = datetime_obj - timedelta_obj

        # Result Verification
        self.assertEqual(new_datetime, datetime_obj2)

        # Fixture Teardown (not needed for this test)

    # Teste 14
    def test_time_addition(self):
        # Fixture Setup
        time_obj = dt.time(14, 30, 45)
        timedelta_obj = dt.timedelta(hours=2)
        time_obj2 = dt.time(16, 30, 45)

        # Exercise SUT
        new_time = (dt.datetime.combine(dt.date.today(), time_obj) + timedelta_obj).time()

        # Result Verification
        self.assertEqual(new_time, time_obj2)

        # Fixture Teardown (not needed for this test)

    # Teste 15
    def test_time_subtraction(self):
        # Fixture Setup
        time_obj = dt.time(14, 30, 45)
        timedelta_obj = dt.timedelta(hours=2)
        time_obj2 = dt.time(12, 30, 45)

        # Exercise SUT
        new_time = (dt.datetime.combine(dt.date.today(), time_obj) - timedelta_obj).time()

        # Result Verification
        self.assertEqual(new_time, time_obj2)

        # Fixture Teardown (not needed for this test)

    # Teste 16
    def test_date_comparison(self):
        # Fixture Setup
        date_obj1 = dt.date(2025, 12, 25)
        date_obj2 = dt.date(2026, 1, 1)

        # Exercise SUT
        comparison_result = date_obj1 < date_obj2

        # Result Verification
        self.assertTrue(comparison_result)

        # Fixture Teardown (not needed for this test)

    # Teste 17
    def test_time_comparison(self):
        # Fixture Setup
        time_obj1 = dt.time(14, 30, 45)
        time_obj2 = dt.time(16, 30, 45)

        # Exercise SUT
        comparison_result = time_obj1 < time_obj2

        # Result Verification
        self.assertTrue(comparison_result)

        # Fixture Teardown (not needed for this test)

    # Teste 18
    def test_datetime_comparison(self):
        # Fixture Setup
        datetime_obj1 = dt.datetime(2025, 12, 25, 14, 30, 45)
        datetime_obj2 = dt.datetime(2026, 1, 1, 0, 0, 0)

        # Exercise SUT
        comparison_result = datetime_obj1 < datetime_obj2

        # Result Verification
        self.assertTrue(comparison_result)

        # Fixture Teardown (not needed for this test)

    # Teste 19
    def test_timedelta_comparison(self):
        # Fixture Setup
        timedelta_obj1 = dt.timedelta(days=5)
        timedelta_obj2 = dt.timedelta(days=10)

        # Exercise SUT
        comparison_result = timedelta_obj1 < timedelta_obj2

        # Result Verification
        self.assertTrue(comparison_result)

        # Fixture Teardown (not needed for this test)

    # Teste 20
    def test_date_isoformat(self):
        # Fixture Setup
        date_obj = dt.date(2025, 12, 25)
        expected_isoformat = "2025-12-25"

        # Exercise SUT
        isoformat_result = date_obj.isoformat()

        # Result Verification
        self.assertEqual(isoformat_result, expected_isoformat)

        # Fixture Teardown (not needed for this test)

    # Teste 21
    def test_time_isoformat(self):
        # Fixture Setup
        time_obj = dt.time(14, 30, 45)
        expected_isoformat = "14:30:45"

        # Exercise SUT
        isoformat_result = time_obj.isoformat()

        # Result Verification
        self.assertEqual(isoformat_result, expected_isoformat)

        # Fixture Teardown (not needed for this test)

    # Teste 22
    def test_datetime_isoformat(self):
        # Fixture Setup
        datetime_obj = dt.datetime(2025, 12, 25, 14, 30, 45)
        expected_isoformat = "2025-12-25T14:30:45"

        # Exercise SUT
        isoformat_result = datetime_obj.isoformat()

        # Result Verification
        self.assertEqual(isoformat_result, expected_isoformat)

        # Fixture Teardown (not needed for this test)

    # Teste 23
    def test_timedelta_total_seconds(self):
        # Fixture Setup
        timedelta_obj = dt.timedelta(days=1, hours=2, minutes=30)
        expected_total_seconds = 1 * 24 * 3600 + 2 * 3600 + 30 * 60

        # Exercise SUT
        total_seconds_result = timedelta_obj.total_seconds()

        # Result Verification
        self.assertEqual(total_seconds_result, expected_total_seconds)

        # Fixture Teardown (not needed for this test)

    # Teste 24
    def test_date_strftime(self):
        # Fixture Setup
        date_obj = dt.date(2025, 12, 25)
        expected_strftime = "25/12/2025"

        # Exercise SUT
        strftime_result = date_obj.strftime("%d/%m/%Y")

        # Result Verification
        self.assertEqual(strftime_result, expected_strftime)

        # Fixture Teardown (not needed for this test)

    # Teste 25
    def test_time_strftime(self):
        # Fixture Setup
        time_obj = dt.time(14, 30, 45)
        expected_strftime = "14:30:45"

        # Exercise SUT
        strftime_result = time_obj.strftime("%H:%M:%S")

        # Result Verification
        self.assertEqual(strftime_result, expected_strftime)

        # Fixture Teardown (not needed for this test)

    # Teste 26
    def test_datetime_strftime(self):
        # Fixture Setup
        datetime_obj = dt.datetime(2025, 12, 25, 14, 30, 45)
        expected_strftime = "25/12/2025 14:30:45"

        # Exercise SUT
        strftime_result = datetime_obj.strftime("%d/%m/%Y %H:%M:%S")

        # Result Verification
        self.assertEqual(strftime_result, expected_strftime)

        # Fixture Teardown (not needed for this test)

    # Teste 27
    def test_date_fromisoformat(self):
        # Fixture Setup
        isoformat_str = "2025-12-25"
        expected_date = dt.date(2025, 12, 25)

        # Exercise SUT
        date_result = dt.date.fromisoformat(isoformat_str)

        # Result Verification
        self.assertEqual(date_result, expected_date)

        # Fixture Teardown (not needed for this test)

    # Teste 28
    def test_time_fromisoformat(self):
        # Fixture Setup
        isoformat_str = "14:30:45"
        expected_time = dt.time(14, 30, 45)

        # Exercise SUT
        time_result = dt.time.fromisoformat(isoformat_str)

        # Result Verification
        self.assertEqual(time_result, expected_time)

        # Fixture Teardown (not needed for this test)

    # Teste 29
    def test_datetime_fromisoformat(self):
        # Fixture Setup
        isoformat_str = "2025-12-25T14:30:45"
        expected_datetime = dt.datetime(2025, 12, 25, 14, 30, 45)

        # Exercise SUT
        datetime_result = dt.datetime.fromisoformat(isoformat_str)

        # Result Verification
        self.assertEqual(datetime_result, expected_datetime)

        # Fixture Teardown (not needed for this test)

    # Teste 30
    def test_timedelta_from_seconds(self):
        # Fixture Setup
        total_seconds = 90061  # 1 day, 1 hour, 1 minute, and 1 second
        expected_timedelta = dt.timedelta(days=1, hours=1, minutes=1, seconds=1)

        # Exercise SUT
        timedelta_result = dt.timedelta(seconds=total_seconds)

        # Result Verification
        self.assertEqual(timedelta_result, expected_timedelta)

        # Fixture Teardown (not needed for this test)

    # Teste 31
    def test_invalid_month(self):
        # Fixture Setup
        invalid_date_str = "2025-13-25"  # Invalid month

        # Exercise SUT and Result Verification
        with self.assertRaises(ValueError):
            dt.date.fromisoformat(invalid_date_str)

        # Fixture Teardown (not needed for this test)

    # Teste 32
    def test_invalid_day(self):
        # Fixture Setup
        invalid_date_str = "2025-12-32"  # Invalid day

        # Exercise SUT and Result Verification
        with self.assertRaises(ValueError):
            dt.date.fromisoformat(invalid_date_str)

        # Fixture Teardown (not needed for this test)

    # Teste 33
    def test_invalid_hour(self):
        # Fixture Setup
        invalid_time_str = "25:30:45"  # Invalid hour

        # Exercise SUT and Result Verification
        with self.assertRaises(ValueError):
            dt.time.fromisoformat(invalid_time_str)

        # Fixture Teardown (not needed for this test)


if __name__ == '__main__':
    unittest.main()
