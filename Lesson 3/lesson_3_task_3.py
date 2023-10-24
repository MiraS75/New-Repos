from address import Address
from mailing import Mailing


to_address = Address("123456", "Moscow", "Lenin Street", "10", "20")
from_address = Address("654321", "Saint Petersburg", "Pushkin Street", "5", "15")


mailing = Mailing(to_address, from_address, 100, "123456789")


print(f"Отправление {mailing.track} из {mailing.from_address.index}, 
      {mailing.from_address.city}, {mailing.from_address.street}, 
      {mailing.from_address.house} - {mailing.from_address.apartment} 
      в {mailing.to_address.index}, {mailing.to_address.city}, 
      {mailing.to_address.street}, {mailing.to_address.house} - 
      {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")