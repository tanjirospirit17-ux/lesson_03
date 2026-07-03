from address import Address
from mailing import Mailing

to_address = Address("101000", "Москва", "ул. Тверская", "10", "5")
from_address = Address("190000", "Санкт-Петербург", "Невский проспект", "25", "12")

my_mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500,
    track="AB123456789RU"
)

print(
    f"Отправление {my_mailing.track} из "
    f"{my_mailing.from_address.zip_code}, "
    f"{my_mailing.from_address.city}, "
    f"{my_mailing.from_address.street}, "
    f"{my_mailing.from_address.house} - "
    f"{my_mailing.from_address.apartment} в "
    f"{my_mailing.to_address.zip_code}, "
    f"{my_mailing.to_address.city}, "
    f"{my_mailing.to_address.street}, "
    f"{my_mailing.to_address.house} - "
    f"{my_mailing.to_address.apartment}. "
    f"Стоимость {my_mailing.cost} рублей."
)