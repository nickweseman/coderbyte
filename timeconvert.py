def TimeConvert(num):
    hours = num // 60
    minutes = num % 60

    time = [str(hours), str(minutes)]

    return ":".join(time)


# keep this function call here
print(TimeConvert(126))
print(TimeConvert(45))