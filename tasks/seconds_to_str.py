__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    """Реализует текстовое представление времени.

    Example:
        >> seconds_to_str(20)
        20s
        >> seconds_to_str(60)
        01m00s
        >> seconds_to_str(65)
        01m05s
        >> seconds_to_str(3700)
        01h01m40s
        >> seconds_to_str(93600)
        01d02h00m00s
    """
    sec_per_day = 86400
    sec_per_hour = 3600
    sec_per_min = 60

    days = seconds // sec_per_day
    seconds %= sec_per_day
    hours = seconds // sec_per_hour
    seconds %= sec_per_hour
    minutes = seconds // sec_per_min
    seconds %= sec_per_min

    fmt = "%02d"

    if days > 0:
        return fmt % days + 'd' + fmt % hours + 'h' + fmt % minutes + 'm' + fmt % seconds + 's'
    if hours > 0:
        return fmt % hours + 'h' + fmt % minutes + 'm' + fmt % seconds + 's'
    if minutes > 0:
        return fmt % minutes + 'm' + fmt % seconds + 's'
    return fmt % seconds + 's'
