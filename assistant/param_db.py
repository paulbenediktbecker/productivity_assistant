class NotionSynthavoParamDB():


    PRIO_TODAY = {'id': 'T%60%5Bg', 'type': 'select', 'select': {'id': 'M]M{', 'name': 'Today', 'color': 'blue'}}
    PRIO_HIGH = {'id': 'T%60%5Bg', 'type': 'select', 'select': {'id': '`imy', 'name': 'High', 'color': 'red'}}
    PRIO_MID = {'id': 'T%60%5Bg', 'type': 'select', 'select': {'id': '}Jc<', 'name': 'Mid', 'color': 'yellow'}}
    PRIO_LOW = {'id': 'T%60%5Bg', 'type': 'select', 'select': {'id': 'NJVq', 'name': 'Low', 'color': 'green'}}

    PRIO_DEFAULT = PRIO_TODAY

    status_general = {
        'id':'%5EOE%40',
        'type':'select',
        'select': {
            'id':'1',
            'name':'General',
            'color':'red'
        }
    }
    status_HR = {
        'id':'%5EOE%40',
        'type':'select',
        'select': {
            'id':'3',
            'name':'HR',
            'color':'green'
        }
    }
    status_Sales = {
        'id':'%5EOE%40',
        'type':'select',
        'select': {
            'id':'2',
            'name':'Sales',
            'color':'yellow'
        }
    }
    status_Dev = {
        'id':'%5EOE%40',
        'type':'select',
        'select': {
            'id':'2ee71963-e2e1-45b4-b093-d6b59109e4d5',
            'name':'Dev',
            'color':'purple'
        }
    }

    STATUS_DEFAULT = status_general


class NotionTorrParamDB():
    PRIO_TODAY = {'id': 'kxUR', 'type': 'select', 'select': {'id': 'Wu;[', 'name': 'Today', 'color': 'gray'}}
    PRIO_HIGH = {'id': 'kxUR', 'type': 'select', 'select': {'id': 'JrDp', 'name': 'High', 'color': 'pink'}}
    PRIO_MID = {'id': 'kxUR', 'type': 'select', 'select': {'id': 'bz{X', 'name': 'Mid', 'color': 'yellow'}}
    PRIO_FAST = {'id': 'kxUR', 'type': 'select', 'select': {'id': 'S>A]', 'name': 'Fast', 'color': 'purple'}}
    PRIO_NOW = {'id': 'kxUR', 'type': 'select', 'select': {'id': 'Z|JL', 'name': 'Now', 'color': 'blue'}}
    PRIO_LOW = {'id': 'kxUR', 'type': 'select', 'select': {'id': '@`ku', 'name': 'Low', 'color': 'green'}}

    PRIO_DEFAULT = PRIO_TODAY

class NotionPrivateParamDB():
    status_today = {
        "id": "^OE@",
        "type": "select",
        "select": {
            "id": "9b329245-fc7d-4257-97d4-0cda03c24dda",
            "name": "TODAY",
            "color": "blue"
        }
    }
    
    STATUS_DEFAULT = {
        'id': '%5EOE%40', 
        'type': 'select', 
        'select': {
            'id': '1',
            'name': 'To Do', 
            'color': 'green'
		}
	}

    
    
    