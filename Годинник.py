your_data = int(input('Enter a number from 0 to 8639999: '))

if 0 <= your_data < 8640000:
    days = your_data // 86400
    your_data = your_data % 86400
    hours = your_data // 3600
    your_data = your_data % 3600
    minutes = your_data // 60
    seconds = your_data % 60

    if days == 1:
        day_meaning = "день"
    elif 2 <= days <= 4:
        day_meaning = "дні"
    else:
        day_meaning = "днів"

    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)
    seconds = str(seconds).zfill(2)

    print(f"{days} {day_meaning}, {hours}:{minutes}:{seconds}")
else:
    print("Enter a number from 0 to 8639999:.")




