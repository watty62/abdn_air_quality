## work in progress

import requests, json

x = [{'sensordatavalues': [{'id': 6553705054, 'value': '3.80', 'value_type': 'P1'},
                           {'id': 6553705055, 'value': '0.43', 'value_type': 'P2'}], 'id': 3087032227,
      'sensor': {'id': 22549, 'sensor_type': {'id': 14, 'name': 'SDS011', 'manufacturer': 'Nova Fitness'}, 'pin': '1'},
      'timestamp': '2019-03-12 11:36:01',
      'location': {'id': 11441, 'latitude': '57.1640', 'altitude': '49.1', 'longitude': '-2.1200', 'country': 'UK'},
      'sampling_rate': None}, {'sensordatavalues': [{'id': 6553705181, 'value': '79.70', 'value_type': 'humidity'},
                                                    {'id': 6553705180, 'value': '7.20', 'value_type': 'temperature'}],
                               'id': 3087032285, 'sensor': {'id': 22550, 'sensor_type': {'id': 9, 'name': 'DHT22',
                                                                                         'manufacturer': 'various'},
                                                            'pin': '7'}, 'timestamp': '2019-03-12 11:36:01',
                               'location': {'id': 11441, 'latitude': '57.1640', 'altitude': '49.1',
                                            'longitude': '-2.1200', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553707502, 'value': '56.81', 'value_type': 'humidity'},
                              {'id': 6553707503, 'value': '98656.56', 'value_type': 'pressure'},
                              {'id': 6553707501, 'value': '12.40', 'value_type': 'temperature'},
                              {'value': 98924.74, 'value_type': 'pressure_at_sealevel'}], 'id': 3087033386,
         'sensor': {'id': 17204, 'sensor_type': {'id': 17, 'name': 'BME280', 'manufacturer': 'Bosch'}, 'pin': '11'},
         'timestamp': '2019-03-12 11:36:13',
         'location': {'id': 8718, 'latitude': '57.1780', 'altitude': '22.7', 'longitude': '-2.0920', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553708085, 'value': '2.10', 'value_type': 'P1'},
                                                       {'id': 6553708086, 'value': '0.80', 'value_type': 'P2'}],
                                  'id': 3087033662, 'sensor': {'id': 7789, 'sensor_type': {'id': 14, 'name': 'SDS011',
                                                                                           'manufacturer': 'Nova Fitness'},
                                                               'pin': '1'}, 'timestamp': '2019-03-12 11:36:17',
                                  'location': {'id': 3939, 'latitude': '57.1300', 'altitude': '24.3',
                                               'longitude': '-2.0860', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553708239, 'value': '96.20', 'value_type': 'humidity'},
                              {'id': 6553708238, 'value': '14.90', 'value_type': 'temperature'}], 'id': 3087033735,
         'sensor': {'id': 7790, 'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'}, 'pin': '7'},
         'timestamp': '2019-03-12 11:36:18',
         'location': {'id': 3939, 'latitude': '57.1300', 'altitude': '24.3', 'longitude': '-2.0860', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553708917, 'value': '2.60', 'value_type': 'P1'},
                                                       {'id': 6553708921, 'value': '0.93', 'value_type': 'P2'}],
                                  'id': 3087034058, 'sensor': {'id': 15462, 'sensor_type': {'id': 14, 'name': 'SDS011',
                                                                                            'manufacturer': 'Nova Fitness'},
                                                               'pin': '1'}, 'timestamp': '2019-03-12 11:36:22',
                                  'location': {'id': 7832, 'latitude': '57.1240', 'altitude': '33.3',
                                               'longitude': '-2.1020', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553709006, 'value': '5.83', 'value_type': 'P1'},
                              {'id': 6553709007, 'value': '1.17', 'value_type': 'P2'}], 'id': 3087034101,
         'sensor': {'id': 22480, 'sensor_type': {'id': 14, 'name': 'SDS011', 'manufacturer': 'Nova Fitness'},
                    'pin': '1'}, 'timestamp': '2019-03-12 11:36:22',
         'location': {'id': 11407, 'latitude': '56.9640', 'altitude': '11.1', 'longitude': '-2.2120', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553709100, 'value': '91.50', 'value_type': 'humidity'},
                                                       {'id': 6553709098, 'value': '11.00',
                                                        'value_type': 'temperature'}], 'id': 3087034145,
                                  'sensor': {'id': 15463,
                                             'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'},
                                             'pin': '7'}, 'timestamp': '2019-03-12 11:36:23',
                                  'location': {'id': 7832, 'latitude': '57.1240', 'altitude': '33.3',
                                               'longitude': '-2.1020', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553709153, 'value': '81.55', 'value_type': 'humidity'},
                              {'id': 6553709154, 'value': '98889.30', 'value_type': 'pressure'},
                              {'id': 6553709152, 'value': '7.87', 'value_type': 'temperature'},
                              {'value': 99022.79, 'value_type': 'pressure_at_sealevel'}], 'id': 3087034170,
         'sensor': {'id': 22481, 'sensor_type': {'id': 17, 'name': 'BME280', 'manufacturer': 'Bosch'}, 'pin': '11'},
         'timestamp': '2019-03-12 11:36:23',
         'location': {'id': 11407, 'latitude': '56.9640', 'altitude': '11.1', 'longitude': '-2.2120', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553711755, 'value': '2.52', 'value_type': 'P1'},
                                                       {'id': 6553711764, 'value': '0.68', 'value_type': 'P2'}],
                                  'id': 3087035410, 'sensor': {'id': 22691, 'sensor_type': {'id': 14, 'name': 'SDS011',
                                                                                            'manufacturer': 'Nova Fitness'},
                                                               'pin': '1'}, 'timestamp': '2019-03-12 11:36:37',
                                  'location': {'id': 11513, 'latitude': '57.1720', 'altitude': '53.3',
                                               'longitude': '-2.1340', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553711905, 'value': '65.70', 'value_type': 'humidity'},
                              {'id': 6553711904, 'value': '11.50', 'value_type': 'temperature'}], 'id': 3087035483,
         'sensor': {'id': 22692, 'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'}, 'pin': '7'},
         'timestamp': '2019-03-12 11:36:38',
         'location': {'id': 11513, 'latitude': '57.1720', 'altitude': '53.3', 'longitude': '-2.1340', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553713367, 'value': '6.97', 'value_type': 'P1'},
                                                       {'id': 6553713369, 'value': '1.30', 'value_type': 'P2'}],
                                  'id': 3087036178, 'sensor': {'id': 5331, 'sensor_type': {'id': 14, 'name': 'SDS011',
                                                                                           'manufacturer': 'Nova Fitness'},
                                                               'pin': '1'}, 'timestamp': '2019-03-12 11:36:46',
                                  'location': {'id': 3121, 'latitude': '57.1380', 'altitude': '15.9',
                                               'longitude': '-2.0780', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553713523, 'value': '99.90', 'value_type': 'humidity'},
                              {'id': 6553713521, 'value': '13.70', 'value_type': 'temperature'}], 'id': 3087036251,
         'sensor': {'id': 5332, 'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'}, 'pin': '7'},
         'timestamp': '2019-03-12 11:36:46',
         'location': {'id': 3121, 'latitude': '57.1380', 'altitude': '15.9', 'longitude': '-2.0780', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553717294, 'value': '1.97', 'value_type': 'P1'},
                                                       {'id': 6553717297, 'value': '0.67', 'value_type': 'P2'}],
                                  'id': 3087038040, 'sensor': {'id': 22068, 'sensor_type': {'id': 14, 'name': 'SDS011',
                                                                                            'manufacturer': 'Nova Fitness'},
                                                               'pin': '1'}, 'timestamp': '2019-03-12 11:37:07',
                                  'location': {'id': 11199, 'latitude': '57.1500', 'altitude': '103.4',
                                               'longitude': '-2.1660', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553717521, 'value': '0.70', 'value_type': 'P1'},
                              {'id': 6553717522, 'value': '0.70', 'value_type': 'P2'}], 'id': 3087038146,
         'sensor': {'id': 22597, 'sensor_type': {'id': 14, 'name': 'SDS011', 'manufacturer': 'Nova Fitness'},
                    'pin': '1'}, 'timestamp': '2019-03-12 11:37:08',
         'location': {'id': 11466, 'latitude': '57.1900', 'altitude': '86.0', 'longitude': '-2.2780', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553717617, 'value': '83.90', 'value_type': 'humidity'},
                                                       {'id': 6553717616, 'value': '7.30',
                                                        'value_type': 'temperature'}], 'id': 3087038192,
                                  'sensor': {'id': 22598,
                                             'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'},
                                             'pin': '7'}, 'timestamp': '2019-03-12 11:37:09',
                                  'location': {'id': 11466, 'latitude': '57.1900', 'altitude': '86.0',
                                               'longitude': '-2.2780', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553719375, 'value': '1.87', 'value_type': 'P1'},
                              {'id': 6553719376, 'value': '0.53', 'value_type': 'P2'}], 'id': 3087039037,
         'sensor': {'id': 22885, 'sensor_type': {'id': 14, 'name': 'SDS011', 'manufacturer': 'Nova Fitness'},
                    'pin': '1'}, 'timestamp': '2019-03-12 11:37:21',
         'location': {'id': 11610, 'latitude': '57.2680', 'altitude': '103.9', 'longitude': '-2.1880', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553719407, 'value': '77.20', 'value_type': 'humidity'},
                                                       {'id': 6553719406, 'value': '9.40',
                                                        'value_type': 'temperature'}], 'id': 3087039051,
                                  'sensor': {'id': 22886,
                                             'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'},
                                             'pin': '7'}, 'timestamp': '2019-03-12 11:37:21',
                                  'location': {'id': 11610, 'latitude': '57.2680', 'altitude': '103.9',
                                               'longitude': '-2.1880', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553721527, 'value': '39.00', 'value_type': 'P1'},
                              {'id': 6553721529, 'value': '5.67', 'value_type': 'P2'}], 'id': 3087040058,
         'sensor': {'id': 16422, 'sensor_type': {'id': 14, 'name': 'SDS011', 'manufacturer': 'Nova Fitness'},
                    'pin': '1'}, 'timestamp': '2019-03-12 11:37:33',
         'location': {'id': 8320, 'latitude': '57.4560', 'altitude': '59.5', 'longitude': '-2.3780', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553721811, 'value': '79.72', 'value_type': 'humidity'},
                                                       {'id': 6553721813, 'value': '98101.58',
                                                        'value_type': 'pressure'},
                                                       {'id': 6553721809, 'value': '7.53', 'value_type': 'temperature'},
                                                       {'value': 98814.01, 'value_type': 'pressure_at_sealevel'}],
                                  'id': 3087040193, 'sensor': {'id': 16423, 'sensor_type': {'id': 17, 'name': 'BME280',
                                                                                            'manufacturer': 'Bosch'},
                                                               'pin': '11'}, 'timestamp': '2019-03-12 11:37:34',
                                  'location': {'id': 8320, 'latitude': '57.4560', 'altitude': '59.5',
                                               'longitude': '-2.3780', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553723129, 'value': '7.50', 'value_type': 'P1'},
                              {'id': 6553723131, 'value': '1.63', 'value_type': 'P2'}], 'id': 3087040820,
         'sensor': {'id': 17079, 'sensor_type': {'id': 14, 'name': 'SDS011', 'manufacturer': 'Nova Fitness'},
                    'pin': '1'}, 'timestamp': '2019-03-12 11:37:38',
         'location': {'id': 8655, 'latitude': '57.1060', 'altitude': '82.1', 'longitude': '-2.0880', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553723469, 'value': '66.50', 'value_type': 'humidity'},
                                                       {'id': 6553723466, 'value': '11.90',
                                                        'value_type': 'temperature'}], 'id': 3087040984,
                                  'sensor': {'id': 17080,
                                             'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'},
                                             'pin': '7'}, 'timestamp': '2019-03-12 11:37:38',
                                  'location': {'id': 8655, 'latitude': '57.1060', 'altitude': '82.1',
                                               'longitude': '-2.0880', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553724047, 'value': '3.40', 'value_type': 'P1'},
                              {'id': 6553724055, 'value': '1.07', 'value_type': 'P2'}], 'id': 3087041263,
         'sensor': {'id': 15092, 'sensor_type': {'id': 14, 'name': 'SDS011', 'manufacturer': 'Nova Fitness'},
                    'pin': '1'}, 'timestamp': '2019-03-12 11:37:40',
         'location': {'id': 7647, 'latitude': '56.9640', 'altitude': '9.9', 'longitude': '-2.2120', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553724379, 'value': '71.59', 'value_type': 'humidity'},
                                                       {'id': 6553724380, 'value': '98601.63',
                                                        'value_type': 'pressure'}, {'id': 6553724377, 'value': '10.52',
                                                                                    'value_type': 'temperature'},
                                                       {'value': 98719.23, 'value_type': 'pressure_at_sealevel'}],
                                  'id': 3087041420, 'sensor': {'id': 15093, 'sensor_type': {'id': 17, 'name': 'BME280',
                                                                                            'manufacturer': 'Bosch'},
                                                               'pin': '11'}, 'timestamp': '2019-03-12 11:37:40',
                                  'location': {'id': 7647, 'latitude': '56.9640', 'altitude': '9.9',
                                               'longitude': '-2.2120', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553725566, 'value': '0.40', 'value_type': 'P1'},
                              {'id': 6553725567, 'value': '0.00', 'value_type': 'P2'}], 'id': 3087041984,
         'sensor': {'id': 22523, 'sensor_type': {'id': 14, 'name': 'SDS011', 'manufacturer': 'Nova Fitness'},
                    'pin': '1'}, 'timestamp': '2019-03-12 11:37:44',
         'location': {'id': 11428, 'latitude': '57.1100', 'altitude': '99.0', 'longitude': '-2.2400', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553725780, 'value': '58.90', 'value_type': 'humidity'},
                                                       {'id': 6553725779, 'value': '10.80',
                                                        'value_type': 'temperature'}], 'id': 3087042085,
                                  'sensor': {'id': 22524,
                                             'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'},
                                             'pin': '7'}, 'timestamp': '2019-03-12 11:37:45',
                                  'location': {'id': 11428, 'latitude': '57.1100', 'altitude': '99.0',
                                               'longitude': '-2.2400', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553727567, 'value': '1.57', 'value_type': 'P1'},
                              {'id': 6553727569, 'value': '0.40', 'value_type': 'P2'}], 'id': 3087042930,
         'sensor': {'id': 22449, 'sensor_type': {'id': 14, 'name': 'SDS011', 'manufacturer': 'Nova Fitness'},
                    'pin': '1'}, 'timestamp': '2019-03-12 11:37:52',
         'location': {'id': 11392, 'latitude': '57.3900', 'altitude': '144.2', 'longitude': '-2.4680', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553727720, 'value': '53.80', 'value_type': 'humidity'},
                                                       {'id': 6553727719, 'value': '12.30',
                                                        'value_type': 'temperature'}], 'id': 3087043002,
                                  'sensor': {'id': 22450,
                                             'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'},
                                             'pin': '7'}, 'timestamp': '2019-03-12 11:37:53',
                                  'location': {'id': 11392, 'latitude': '57.3900', 'altitude': '144.2',
                                               'longitude': '-2.4680', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553732562, 'value': '3.73', 'value_type': 'P1'},
                              {'id': 6553732564, 'value': '1.20', 'value_type': 'P2'}], 'id': 3087045295,
         'sensor': {'id': 8554, 'sensor_type': {'id': 14, 'name': 'SDS011', 'manufacturer': 'Nova Fitness'},
                    'pin': '1'}, 'timestamp': '2019-03-12 11:38:17',
         'location': {'id': 4315, 'latitude': '57.1460', 'altitude': '35.4', 'longitude': '-2.1140', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553732770, 'value': '84.30', 'value_type': 'humidity'},
                                                       {'id': 6553732769, 'value': '7.90',
                                                        'value_type': 'temperature'}], 'id': 3087045394,
                                  'sensor': {'id': 8555,
                                             'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'},
                                             'pin': '7'}, 'timestamp': '2019-03-12 11:38:18',
                                  'location': {'id': 4315, 'latitude': '57.1460', 'altitude': '35.4',
                                               'longitude': '-2.1140', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553735079, 'value': '1.27', 'value_type': 'P1'},
                              {'id': 6553735080, 'value': '0.43', 'value_type': 'P2'}], 'id': 3087046482,
         'sensor': {'id': 22549, 'sensor_type': {'id': 14, 'name': 'SDS011', 'manufacturer': 'Nova Fitness'},
                    'pin': '1'}, 'timestamp': '2019-03-12 11:38:29',
         'location': {'id': 11441, 'latitude': '57.1640', 'altitude': '49.1', 'longitude': '-2.1200', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553735224, 'value': '80.20', 'value_type': 'humidity'},
                                                       {'id': 6553735223, 'value': '7.20',
                                                        'value_type': 'temperature'}], 'id': 3087046552,
                                  'sensor': {'id': 22550,
                                             'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'},
                                             'pin': '7'}, 'timestamp': '2019-03-12 11:38:30',
                                  'location': {'id': 11441, 'latitude': '57.1640', 'altitude': '49.1',
                                               'longitude': '-2.1200', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553737133, 'value': '56.53', 'value_type': 'humidity'},
                              {'id': 6553737134, 'value': '98650.81', 'value_type': 'pressure'},
                              {'id': 6553737132, 'value': '12.62', 'value_type': 'temperature'},
                              {'value': 98918.77, 'value_type': 'pressure_at_sealevel'}], 'id': 3087047460,
         'sensor': {'id': 17204, 'sensor_type': {'id': 17, 'name': 'BME280', 'manufacturer': 'Bosch'}, 'pin': '11'},
         'timestamp': '2019-03-12 11:38:40',
         'location': {'id': 8718, 'latitude': '57.1780', 'altitude': '22.7', 'longitude': '-2.0920', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553737886, 'value': '1.73', 'value_type': 'P1'},
                                                       {'id': 6553737887, 'value': '0.80', 'value_type': 'P2'}],
                                  'id': 3087047817, 'sensor': {'id': 7789, 'sensor_type': {'id': 14, 'name': 'SDS011',
                                                                                           'manufacturer': 'Nova Fitness'},
                                                               'pin': '1'}, 'timestamp': '2019-03-12 11:38:44',
                                  'location': {'id': 3939, 'latitude': '57.1300', 'altitude': '24.3',
                                               'longitude': '-2.0860', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553738029, 'value': '95.60', 'value_type': 'humidity'},
                              {'id': 6553738028, 'value': '15.10', 'value_type': 'temperature'}], 'id': 3087047884,
         'sensor': {'id': 7790, 'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'}, 'pin': '7'},
         'timestamp': '2019-03-12 11:38:45',
         'location': {'id': 3939, 'latitude': '57.1300', 'altitude': '24.3', 'longitude': '-2.0860', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553738853, 'value': '3.13', 'value_type': 'P1'},
                                                       {'id': 6553738854, 'value': '1.07', 'value_type': 'P2'}],
                                  'id': 3087048274, 'sensor': {'id': 22480, 'sensor_type': {'id': 14, 'name': 'SDS011',
                                                                                            'manufacturer': 'Nova Fitness'},
                                                               'pin': '1'}, 'timestamp': '2019-03-12 11:38:50',
                                  'location': {'id': 11407, 'latitude': '56.9640', 'altitude': '11.1',
                                               'longitude': '-2.2120', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553738910, 'value': '1.87', 'value_type': 'P1'},
                              {'id': 6553738911, 'value': '0.70', 'value_type': 'P2'}], 'id': 3087048302,
         'sensor': {'id': 15462, 'sensor_type': {'id': 14, 'name': 'SDS011', 'manufacturer': 'Nova Fitness'},
                    'pin': '1'}, 'timestamp': '2019-03-12 11:38:50',
         'location': {'id': 7832, 'latitude': '57.1240', 'altitude': '33.3', 'longitude': '-2.1020', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553738976, 'value': '80.90', 'value_type': 'humidity'},
                                                       {'id': 6553738978, 'value': '98896.29',
                                                        'value_type': 'pressure'},
                                                       {'id': 6553738969, 'value': '7.96', 'value_type': 'temperature'},
                                                       {'value': 99029.75, 'value_type': 'pressure_at_sealevel'}],
                                  'id': 3087048331, 'sensor': {'id': 22481, 'sensor_type': {'id': 17, 'name': 'BME280',
                                                                                            'manufacturer': 'Bosch'},
                                                               'pin': '11'}, 'timestamp': '2019-03-12 11:38:51',
                                  'location': {'id': 11407, 'latitude': '56.9640', 'altitude': '11.1',
                                               'longitude': '-2.2120', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553739064, 'value': '92.30', 'value_type': 'humidity'},
                              {'id': 6553739063, 'value': '11.10', 'value_type': 'temperature'}], 'id': 3087048374,
         'sensor': {'id': 15463, 'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'}, 'pin': '7'},
         'timestamp': '2019-03-12 11:38:51',
         'location': {'id': 7832, 'latitude': '57.1240', 'altitude': '33.3', 'longitude': '-2.1020', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553741536, 'value': '1.15', 'value_type': 'P1'},
                                                       {'id': 6553741537, 'value': '0.40', 'value_type': 'P2'}],
                                  'id': 3087049550, 'sensor': {'id': 22691, 'sensor_type': {'id': 14, 'name': 'SDS011',
                                                                                            'manufacturer': 'Nova Fitness'},
                                                               'pin': '1'}, 'timestamp': '2019-03-12 11:39:05',
                                  'location': {'id': 11513, 'latitude': '57.1720', 'altitude': '53.3',
                                               'longitude': '-2.1340', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553741693, 'value': '57.60', 'value_type': 'humidity'},
                              {'id': 6553741691, 'value': '11.50', 'value_type': 'temperature'}], 'id': 3087049633,
         'sensor': {'id': 22692, 'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'}, 'pin': '7'},
         'timestamp': '2019-03-12 11:39:05',
         'location': {'id': 11513, 'latitude': '57.1720', 'altitude': '53.3', 'longitude': '-2.1340', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553743131, 'value': '2.40', 'value_type': 'P1'},
                                                       {'id': 6553743132, 'value': '0.97', 'value_type': 'P2'}],
                                  'id': 3087050314, 'sensor': {'id': 5331, 'sensor_type': {'id': 14, 'name': 'SDS011',
                                                                                           'manufacturer': 'Nova Fitness'},
                                                               'pin': '1'}, 'timestamp': '2019-03-12 11:39:13',
                                  'location': {'id': 3121, 'latitude': '57.1380', 'altitude': '15.9',
                                               'longitude': '-2.0780', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553743250, 'value': '99.90', 'value_type': 'humidity'},
                              {'id': 6553743249, 'value': '13.40', 'value_type': 'temperature'}], 'id': 3087050371,
         'sensor': {'id': 5332, 'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'}, 'pin': '7'},
         'timestamp': '2019-03-12 11:39:14',
         'location': {'id': 3121, 'latitude': '57.1380', 'altitude': '15.9', 'longitude': '-2.0780', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553746728, 'value': '2.60', 'value_type': 'P1'},
                                                       {'id': 6553746729, 'value': '0.50', 'value_type': 'P2'}],
                                  'id': 3087052022, 'sensor': {'id': 22068, 'sensor_type': {'id': 14, 'name': 'SDS011',
                                                                                            'manufacturer': 'Nova Fitness'},
                                                               'pin': '1'}, 'timestamp': '2019-03-12 11:39:33',
                                  'location': {'id': 11199, 'latitude': '57.1500', 'altitude': '103.4',
                                               'longitude': '-2.1660', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553749171, 'value': '3.42', 'value_type': 'P1'},
                              {'id': 6553749172, 'value': '0.90', 'value_type': 'P2'}], 'id': 3087053184,
         'sensor': {'id': 22885, 'sensor_type': {'id': 14, 'name': 'SDS011', 'manufacturer': 'Nova Fitness'},
                    'pin': '1'}, 'timestamp': '2019-03-12 11:39:48',
         'location': {'id': 11610, 'latitude': '57.2680', 'altitude': '103.9', 'longitude': '-2.1880', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553749230, 'value': '73.70', 'value_type': 'humidity'},
                                                       {'id': 6553749227, 'value': '9.30',
                                                        'value_type': 'temperature'}], 'id': 3087053211,
                                  'sensor': {'id': 22886,
                                             'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'},
                                             'pin': '7'}, 'timestamp': '2019-03-12 11:39:49',
                                  'location': {'id': 11610, 'latitude': '57.2680', 'altitude': '103.9',
                                               'longitude': '-2.1880', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553749552, 'value': '1.80', 'value_type': 'P1'},
                              {'id': 6553749555, 'value': '0.70', 'value_type': 'P2'}], 'id': 3087053367,
         'sensor': {'id': 22597, 'sensor_type': {'id': 14, 'name': 'SDS011', 'manufacturer': 'Nova Fitness'},
                    'pin': '1'}, 'timestamp': '2019-03-12 11:39:50',
         'location': {'id': 11466, 'latitude': '57.1900', 'altitude': '86.0', 'longitude': '-2.2780', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553749696, 'value': '83.10', 'value_type': 'humidity'},
                                                       {'id': 6553749694, 'value': '7.30',
                                                        'value_type': 'temperature'}], 'id': 3087053436,
                                  'sensor': {'id': 22598,
                                             'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'},
                                             'pin': '7'}, 'timestamp': '2019-03-12 11:39:51',
                                  'location': {'id': 11466, 'latitude': '57.1900', 'altitude': '86.0',
                                               'longitude': '-2.2780', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553751466, 'value': '11.30', 'value_type': 'P1'},
                              {'id': 6553751471, 'value': '2.03', 'value_type': 'P2'}], 'id': 3087054274,
         'sensor': {'id': 16422, 'sensor_type': {'id': 14, 'name': 'SDS011', 'manufacturer': 'Nova Fitness'},
                    'pin': '1'}, 'timestamp': '2019-03-12 11:40:03',
         'location': {'id': 8320, 'latitude': '57.4560', 'altitude': '59.5', 'longitude': '-2.3780', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553752583, 'value': '3.20', 'value_type': 'P1'},
                                                       {'id': 6553752584, 'value': '1.23', 'value_type': 'P2'}],
                                  'id': 3087054814, 'sensor': {'id': 17079, 'sensor_type': {'id': 14, 'name': 'SDS011',
                                                                                            'manufacturer': 'Nova Fitness'},
                                                               'pin': '1'}, 'timestamp': '2019-03-12 11:40:10',
                                  'location': {'id': 8655, 'latitude': '57.1060', 'altitude': '82.1',
                                               'longitude': '-2.0880', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553754968, 'value': '64.60', 'value_type': 'humidity'},
                              {'id': 6553754926, 'value': '12.10', 'value_type': 'temperature'}], 'id': 3087055936,
         'sensor': {'id': 17080, 'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'}, 'pin': '7'},
         'timestamp': '2019-03-12 11:40:17',
         'location': {'id': 8655, 'latitude': '57.1060', 'altitude': '82.1', 'longitude': '-2.0880', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553755108, 'value': '4.23', 'value_type': 'P1'},
                                                       {'id': 6553755113, 'value': '0.80', 'value_type': 'P2'}],
                                  'id': 3087056023, 'sensor': {'id': 15092, 'sensor_type': {'id': 14, 'name': 'SDS011',
                                                                                            'manufacturer': 'Nova Fitness'},
                                                               'pin': '1'}, 'timestamp': '2019-03-12 11:40:18',
                                  'location': {'id': 7647, 'latitude': '56.9640', 'altitude': '9.9',
                                               'longitude': '-2.2120', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553755946, 'value': '2.62', 'value_type': 'P1'},
                              {'id': 6553755948, 'value': '0.50', 'value_type': 'P2'}], 'id': 3087056414,
         'sensor': {'id': 22523, 'sensor_type': {'id': 14, 'name': 'SDS011', 'manufacturer': 'Nova Fitness'},
                    'pin': '1'}, 'timestamp': '2019-03-12 11:40:20',
         'location': {'id': 11428, 'latitude': '57.1100', 'altitude': '99.0', 'longitude': '-2.2400', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553756559, 'value': '58.90', 'value_type': 'humidity'},
                                                       {'id': 6553756543, 'value': '10.40',
                                                        'value_type': 'temperature'}], 'id': 3087056711,
                                  'sensor': {'id': 22524,
                                             'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'},
                                             'pin': '7'}, 'timestamp': '2019-03-12 11:40:22',
                                  'location': {'id': 11428, 'latitude': '57.1100', 'altitude': '99.0',
                                               'longitude': '-2.2400', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553756670, 'value': '0.68', 'value_type': 'P1'},
                              {'id': 6553756674, 'value': '0.35', 'value_type': 'P2'}], 'id': 3087056756,
         'sensor': {'id': 22449, 'sensor_type': {'id': 14, 'name': 'SDS011', 'manufacturer': 'Nova Fitness'},
                    'pin': '1'}, 'timestamp': '2019-03-12 11:40:22',
         'location': {'id': 11392, 'latitude': '57.3900', 'altitude': '144.2', 'longitude': '-2.4680', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553757231, 'value': '53.80', 'value_type': 'humidity'},
                                                       {'id': 6553757226, 'value': '12.20',
                                                        'value_type': 'temperature'}], 'id': 3087057025,
                                  'sensor': {'id': 22450,
                                             'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'},
                                             'pin': '7'}, 'timestamp': '2019-03-12 11:40:24',
                                  'location': {'id': 11392, 'latitude': '57.3900', 'altitude': '144.2',
                                               'longitude': '-2.4680', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553760481, 'value': '77.68', 'value_type': 'humidity'},
                              {'id': 6553760483, 'value': '98097.34', 'value_type': 'pressure'},
                              {'id': 6553760479, 'value': '7.56', 'value_type': 'temperature'},
                              {'value': 98809.66, 'value_type': 'pressure_at_sealevel'}], 'id': 3087058556,
         'sensor': {'id': 16423, 'sensor_type': {'id': 17, 'name': 'BME280', 'manufacturer': 'Bosch'}, 'pin': '11'},
         'timestamp': '2019-03-12 11:40:37',
         'location': {'id': 8320, 'latitude': '57.4560', 'altitude': '59.5', 'longitude': '-2.3780', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553762396, 'value': '4.30', 'value_type': 'P1'},
                                                       {'id': 6553762397, 'value': '1.50', 'value_type': 'P2'}],
                                  'id': 3087059457, 'sensor': {'id': 8554, 'sensor_type': {'id': 14, 'name': 'SDS011',
                                                                                           'manufacturer': 'Nova Fitness'},
                                                               'pin': '1'}, 'timestamp': '2019-03-12 11:40:46',
                                  'location': {'id': 4315, 'latitude': '57.1460', 'altitude': '35.4',
                                               'longitude': '-2.1140', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553762624, 'value': '84.70', 'value_type': 'humidity'},
                              {'id': 6553762623, 'value': '8.00', 'value_type': 'temperature'}], 'id': 3087059567,
         'sensor': {'id': 8555, 'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'}, 'pin': '7'},
         'timestamp': '2019-03-12 11:40:47',
         'location': {'id': 4315, 'latitude': '57.1460', 'altitude': '35.4', 'longitude': '-2.1140', 'country': 'UK'},
         'sampling_rate': None}, {'sensordatavalues': [{'id': 6553764859, 'value': '2.33', 'value_type': 'P1'},
                                                       {'id': 6553764862, 'value': '0.50', 'value_type': 'P2'}],
                                  'id': 3087060628, 'sensor': {'id': 22549, 'sensor_type': {'id': 14, 'name': 'SDS011',
                                                                                            'manufacturer': 'Nova Fitness'},
                                                               'pin': '1'}, 'timestamp': '2019-03-12 11:40:58',
                                  'location': {'id': 11441, 'latitude': '57.1640', 'altitude': '49.1',
                                               'longitude': '-2.1200', 'country': 'UK'}, 'sampling_rate': None}, {
         'sensordatavalues': [{'id': 6553764997, 'value': '79.70', 'value_type': 'humidity'},
                              {'id': 6553764996, 'value': '7.30', 'value_type': 'temperature'}], 'id': 3087060690,
         'sensor': {'id': 22550, 'sensor_type': {'id': 9, 'name': 'DHT22', 'manufacturer': 'various'}, 'pin': '7'},
         'timestamp': '2019-03-12 11:40:59',
         'location': {'id': 11441, 'latitude': '57.1640', 'altitude': '49.1', 'longitude': '-2.1200', 'country': 'UK'},
         'sampling_rate': None}]

'''

from datetime import datetime
import pprint
import get_weather
import math


def get_data(box):
    # gets luftdaten data for all sensors within a given lat/log box
    # box = 'lat_0,long_0,lat_1,long_1'
    r = requests.get('https://api.luftdaten.info/v1/filter/box=' + box)
    my_json = r.json()
    return my_json


def tidy_values(our_list):
    # organises ourlist as a dictionary of dictionaries follows:

    new_dict = {}
    for sensor in our_list:
        location_id = str(sensor['location']['id'])
        if (new_dict.get(location_id, None) == None):
            new_dict[location_id] = {}
            new_dict[location_id]['location'] = sensor['location']
        for sensordata in sensor['sensordatavalues']:
            new_dict[location_id][sensordata['value_type']] = {
                'value': float(sensordata['value']),
                'timestamp': sensor['timestamp'],
                'id': sensor['id'],
                'sensor_type': sensor['sensor']['sensor_type']}
    return (new_dict)


def test_values(sensor_list, weather_data):
    # test that:
    # 1. timestamps are fairly recent (within the last X minutes)
    # 2. check if humidity is >80% flag PM readings as invalid
    # 3. flag high P1/P2 readings (based on hard limits)
    # 4. flag high P1/P2 readings based on group medium/std

    # timestamps test
    current_time = datetime.now()
    for location_id in sensor_list:
        for param in sensor_list[location_id]:
            try:
                sense_time = sensor_list[location_id][param]['timestamp']
                delta_time = current_time - datetime.strptime(sense_time, "%Y-%m-%d %H:%M:%S")
                delta_time = divmod(delta_time.days * 86400 + delta_time.seconds, 60)
                if (delta_time[0] > 15):  # check >15min since last report
                    print ('timestamp fail!, id = ' + str(sensor_list[location_id][param]['id']) + ', ' + param)
            except:
                # no timestamp on this paramater
                False

    # PM test
    for location_id in sensor_list:
        # first find nearest weather city from weather_data
        min_dist = 1000000
        for city in weather_data['list']:
            dist = math.sqrt(
                math.pow(city['coord']['Lat'] - float(sensor_list[location_id]['location']['latitude']), 2) +
                math.pow(city['coord']['Lon'] - float(sensor_list[location_id]['location']['longitude']), 2)
            )
            if (dist < min_dist):
                min_dist = dist
                local_city = city
        # check local humidity level is within range based on weather
        # NB sensor humidity not used as not all sensors have this.
        if (local_city['main']['humidity'] > 70):
            # humidity is too high, PM readings should be ignored
            False
        else:
            try:
                # ref: http://ec.europa.eu/environment/air/quality/standards.htm
                sense_P1 = sensor_list[location_id]['P1']['value']
                if (sense_P1 > 40):  # check PM10 >40 ug/m^3
                    print ('PM1 high reading!, id = ' + str(
                        sensor_list[location_id]['P1']['id']) + ', ' + 'PM1 = ' + str(sense_P1))
                sense_P2 = sensor_list[location_id]['P2']['value']
                if (sense_P2 > 20):  # check PM2.5 >20 ug/m^3
                    print ('PM2 high reading!, id = ' + str(
                        sensor_list[location_id]['P2']['id']) + ', ' + 'PM2 = ' + str(sense_P2))
            except:
                # no PM1 or PM2 readings
                False


def main():
    box = [57.5476, -1.9113, 56.9630, -2.4682]
    bigbox = [100, -1, 20, -50]
    # box = bigbox #test
    strbox = (str(box)[1:-1]).replace(" ", "")
    our_list = get_data(strbox)
    # our_list is a list of dictionaries

    tidy_list = tidy_values(our_list)
    # tidy_list is a list of dictionaries that is easier to work with.
    print(tidy_list)
    weather_data = get_weather.main(box)
    # adds weather data to each sensor

    # pp = pprint.PrettyPrinter(indent=1)
    # pp.pprint (tidy_list)
    # pp.pprint (weather_data)
    test_values(tidy_list, weather_data)

    return ()
'''


def get_sensor_list():
    pass


def query_the_api():
    box = [57.5476, -1.9113, 56.9630, -2.4682]
    strbox = (str(box)[1:-1]).replace(" ", "")
    r = requests.get('https://api.luftdaten.info/v1/filter/box=' + strbox)
    my_json = r.json()
    return my_json


def filter_json(in_list):
    found_list = []
    print(len(in_list))
    for device in in_list:
        for key, val in device.items():
            # print (key, val)
            if key == "sensor":
                for k,v in val.items():
                    if k == "id":
                        found_list.append(int(v))
    return sorted(found_list)

''' 
    short_list = []

    for city in city_list:
        GB = False
        NS = False
        EW = False
        no_walton = False
        for key, val in city.items():  # outer dictionary
            if key == "country" and val == "GB":
                GB = True  # we are only interested in GB places (no point testing lat long of whole world)

            if key == "name" and val != "Walton":
                no_walton = True  # needed because there is a fictional town "Walton" in the data

            if key == "coord":
                for k, v in val.items():  # inner dictionary
                    # equivalent of our bounding box
                    if k == "lon" and float(v) > -2.78633 and float(v) < 1.9112:
                        EW = True
                    if k == "lat" and float(v) > 56.955 and float(v) < 57.6875:
                        NS = True
            if GB and NS and EW and no_walton:
                short_list.append(city)
    return short_list
'''


def check_against_stored():
    pass


def add_new_to_list():
    pass


def send_alerts_if_down():
    pass


def main():
    get_sensor_list()
    # whats_up = query_the_api()
    whats_up = x
    # print (whats_up)
    found = filter_json(whats_up)
    check_against_stored()
    add_new_to_list()
    send_alerts_if_down()


if __name__ == '__main__':
    main()
