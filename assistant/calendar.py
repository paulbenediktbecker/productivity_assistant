

class Calendar(object):

    def __init__(self) -> None:
        pass

class GoogleCalendar(Calendar):

    def __init__(self) -> None:
        super().__init__()


class OutlookCalendar(Calendar):

    def __init__(self) -> None:
        super().__init__()


class PrivateCalendar(GoogleCalendar):

    def __init__(self) -> None:
        super().__init__()
        
        self.day_ids = {
            0:"Monday",
            1:"Tuesday",
            2:"Wednesday",
            3:"Thursday",
            4:"Friday",
            5:"Saturday",
            6:"Sunday"
        }

        self.lates = [
            0,1,2,3,4,5,6
        ]
        self.earlies = [
            5,6
        ]

        

    def book_slot():
        pass

    def book_late():
        pass

    def book_early():

        pass
