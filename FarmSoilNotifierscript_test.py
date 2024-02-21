import unittest
from unittest.mock import patch
from your_script_name import read_sensor_data, send_email

class TestSoilSensorScript(unittest.TestCase):

    @patch('builtins.input', return_value='Soil Moisture: 50%')
    def test_read_sensor_data(self, mock_input):
        result = read_sensor_data()
        self.assertEqual(result, 'Soil Moisture: 50%')

    @patch('smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        message = "Test email message"
        send_email(message)
        mock_smtp.return_value.starttls.assert_called_once()
        mock_smtp.return_value.login.assert_called_once()
        mock_smtp.return_value.sendmail.assert_called_once()

if __name__ == '__main__':
    unittest.main()
