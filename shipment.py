# pip install openpyxl
# pip install shippo

import pandas as pd
import shippo

shippo.api_key = "shippo_test_86066b7641bf8b97b552699400271f6f4bf01eed"

class Address:
    def __init__(self):
        self._city = ''
        self._state = ''
        self._zip = ''
        self._country = ''

    def get_city(self):
        return self._city

    def get_state(self):
        return self._state

    def get_zip(self):
        return self._zip

    def get_country(self):
        return self._country

    def set_city(self, city):
        self._city = city

    def set_state(self, state):
        self._state = state

    def set_zip(self, zip):
        self._zip = zip

    def set_country(self, country):
        self._country = country

    def to_dict(self):
        return {
            'city': self._city,
            'zip': self._zip,
            'country': self._country
        }

    def is_valid_address(self):
        return len(self._city) != 0 and len(self._state) != 0 and len(self._country) != 0 and self._zip.isnumeric()

class Parcel:
    def __init__(self):
        self._length = ''
        self._width = ''
        self._height = ''
        self._weight = ''
        self._distance_unit = 'in'
        self._mass_unit = 'lb'

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_weight(self):
        return self._weight

    def set_length(self, length):
        self._length = length

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def set_weight(self, weight):
        self._weight = weight

    def to_dict(self):
        return {
            'length': self._length,
            'width': self._width,
            'height': self._height,
            'distance_unit': self._distance_unit,
            'weight': self._weight,
            'mass_unit': self._mass_unit
        }

    def is_valid_parcel(self):
        return self._length.isnumeric() and self._width.isnumeric() and self._height.isnumeric() and self._weight.isnumeric()

class Shipment:
    def __init__(self):
        self._from_address = Address()
        self._to_address = Address()
        self._parcel = Parcel()
        self._df = None

    def get_from_address(self):
        return self._from_address

    def get_to_addresss(self):
        return self._to_address

    def get_parcel(self):
        return self._parcel

    def set_address(self, to_address=False):
        city = input('Please enter the city name:')
        state = input('Please enter the state:')
        zip = input('Please enter the zip:')
        country = input('Please enter the country:')

        if to_address:
            self._to_address.set_city(city)
            self._to_address.set_state(state)
            self._to_address.set_zip(zip)
            self._to_address.set_country(country)
            print("The To Address is saved")
        else:
            self._from_address.set_city(city)
            self._from_address.set_state(state)
            self._from_address.set_zip(zip)
            self._from_address.set_country(country)
            print("The From Address is saved")


    def set_parcel(self):
        length = input('Please give the dimension of length (unit: in): ')
        width = input('Please give the dimension of width (unit: in): ')
        height = input('Please give the dimension of height (unit: in): ')
        weight = input('Please give the estimate weight (unit: lb): ')

        self._parcel.set_width(width)
        self._parcel.set_length(length)
        self._parcel.set_height(height)
        self._parcel.set_weight(weight)

        print("The box dimension is saved")

    def display_sub_menu(self):
        f = open('./static/shipping_sub_menu.txt')
        output = ""
        for line in f:
            output += line
        f.close()
        return output

    def create_shipment(self):
        if not self._parcel.is_valid_parcel():
            raise AttributeError('Please set the box dimension appropriately')
        if not self._from_address.is_valid_address():
            raise AttributeError('Please set the From Address appropriately')
        if not self._to_address.is_valid_address():
            raise AttributeError('Please set the To Address appropriately')


        shipment = shippo.Shipment.create(api_key=shippo.api_key,
                                          address_from=self._from_address.to_dict(),
                                          address_to=self._to_address.to_dict(),
                                          parcels=[self._parcel.to_dict()])
        l = []
        for rate in shipment.rates:
            l.append(((shipment.address_from.city + "," + shipment.address_from.state), shipment.address_from.zip,
                      (shipment.address_to.city + "," + shipment.address_to.state), shipment.address_to.zip,
                      rate.attributes, rate.provider, rate.currency, rate.amount, rate.estimated_days,
                      rate.duration_terms))

        pd.set_option('display.max_columns', None)
        self._df = pd.DataFrame(l, columns=["Ship From", "Ship From Zipcode", "Ship To", "Ship To Zipcode", "Arrtibutes",
                                        "Provider", "Currency", "Amount", "estiamate deliver days", "notes"])

        print(self._df)

    def export(self):
        self._df.to_excel("shipping_cost.xlsx", sheet_name="clean_data")
        print('The file is exported as shipping_cost.xlsx')

