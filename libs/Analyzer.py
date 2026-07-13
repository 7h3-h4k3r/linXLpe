from . import get_groups_id_str

class Analyzer:
    '''
        future Update
    '''

    @staticmethod
    def analyze_groups(groups_data):
        groups_list = [
            ('sudo','HIGH'),
            ('docker','HIGH'),
            ('lxd','HIGH'),
            ('disk','HIGH'),
            ('adm','MEDIAM'),
            ('shadow','HIGH'),
            ('root','CRITICAL'),
            ('www-data','INFO'),
            ('users','INFO')
        ]

        print(get_groups_id_str(groups_data))



        



