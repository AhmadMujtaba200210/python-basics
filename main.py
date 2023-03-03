def convert_seconds(seconds):
    hours=seconds//3600
    minutes=(seconds-hours*3600)//60
    remaining_seconds=(seconds-minutes*60-hours*3600)

    return hours,minutes,remaining_seconds

print(convert_seconds(40000))

# this code is written by Ahmad!