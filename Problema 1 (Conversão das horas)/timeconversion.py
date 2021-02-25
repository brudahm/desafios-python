#!/usr/bin/python
def to_24(am_pm):
    meridian = am_pm[-2:]
    hours = am_pm[:2]
    minutes = am_pm[3:5]
    seconds = am_pm[6:8]

    if hours > '12' or minutes > '59' or seconds > '59':
        raise ValueError("Nao e um horario valido")

    if meridian == 'PM' and hours != '12':
        am_pm = str(12 + int(hours)) + am_pm[2:]

    if meridian == 'AM' and hours == '12':
        am_pm = '00' + am_pm[2:]

    return am_pm[:-2]
